#!/usr/bin/env python3
"""
GSCO Edit Daemon — выполняет правки из edit_queue в Wikidata.
Один поток. Dynamic throttle. Emergency stop check.

Запуск: python3 gsco_edit_daemon.py [--dry-run] [--limit 500]
Остановка: touch /opt/reincarnatiopedia/data/BOT_EMERGENCY_STOP

Cron (рекомендуется): nohup python3 -u gsco_edit_daemon.py --limit 500 >> /var/log/gsco_edit_daemon.log 2>&1 &
"""
import sqlite3, requests, json, time, sys, argparse, random
from pathlib import Path
from datetime import datetime, timedelta

DB_PATH = Path(__file__).parent / "gsco_wikidata.db"
STOP_FILE = Path(__file__).parent / "BOT_EMERGENCY_STOP"
CREDENTIALS_FILE = Path(__file__).parent / ".wikidata_credentials.json"

API = "https://www.wikidata.org/w/api.php"
UA = "GSCO-EditDaemon/1.0 (wikidata@marisdreshmanis.com) python-requests"

# Wikidata bot policy constants
MAXLAG = 5
MIN_SLEEP = 1.5
MAX_SLEEP = 3.0
PROBATION_THRESHOLD = 50  # правок до "approved" для нового языка


class WikidataSession:
    """Авторизованная сессия для Wikidata API."""

    def __init__(self, credentials_file):
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": UA})
        self.csrf_token = None

        if credentials_file.exists():
            creds = json.loads(credentials_file.read_text())
            self.username = creds["username"]
            self.password = creds["password"]
        else:
            print(f"ERROR: No credentials file at {credentials_file}")
            print(f"Create it with: {{\"username\": \"ReNeuralAgent\", \"password\": \"...\"}}")
            sys.exit(1)

    def login(self):
        """Login через bot password."""
        # Step 1: Get login token
        r = self.session.get(API, params={
            "action": "query", "meta": "tokens",
            "type": "login", "format": "json"
        }, timeout=30)
        login_token = r.json()["query"]["tokens"]["logintoken"]

        # Step 2: Login
        r = self.session.post(API, data={
            "action": "login",
            "lgname": self.username,
            "lgpassword": self.password,
            "lgtoken": login_token,
            "format": "json"
        }, timeout=30)

        result = r.json().get("login", {})
        if result.get("result") != "Success":
            print(f"LOGIN FAILED: {result}")
            sys.exit(1)
        print(f"Logged in as {self.username}")

        # Step 3: Get CSRF token
        r = self.session.get(API, params={
            "action": "query", "meta": "tokens",
            "format": "json"
        }, timeout=30)
        self.csrf_token = r.json()["query"]["tokens"]["csrftoken"]

    def wbsetlabel(self, qid, language, value, summary=""):
        return self._edit("wbsetlabel", qid, language, value, summary)

    def wbsetdescription(self, qid, language, value, summary=""):
        return self._edit("wbsetdescription", qid, language, value, summary)

    def wbsetaliases(self, qid, language, aliases, summary=""):
        """Добавляет aliases (не заменяет)."""
        data = {
            "action": "wbsetaliases",
            "id": qid,
            "language": language,
            "add": "|".join(aliases) if isinstance(aliases, list) else aliases,
            "summary": summary or "Adding aliases from GSCO database",
            "bot": "1",
            "token": self.csrf_token,
            "maxlag": str(MAXLAG),
            "format": "json",
        }
        return self._post(data)

    def _edit(self, action, qid, language, value, summary=""):
        data = {
            "action": action,
            "id": qid,
            "language": language,
            "value": value,
            "summary": summary or f"Adding {action.replace('wbset', '')} from GSCO database",
            "bot": "1",
            "token": self.csrf_token,
            "maxlag": str(MAXLAG),
            "format": "json",
        }
        return self._post(data)

    def _post(self, data):
        try:
            r = self.session.post(API, data=data, timeout=30)
            resp = r.json()

            if "error" in resp:
                code = resp["error"].get("code", "")
                if code == "maxlag":
                    retry_after = int(resp["error"].get("info", "").split()[-2]
                                     if "seconds" in resp["error"].get("info", "")
                                     else "5")
                    return {"status": "maxlag", "retry_after": retry_after}
                return {"status": "error", "code": code, "info": resp["error"].get("info")}

            if "success" in resp:
                return {"status": "ok", "response": resp}

            return {"status": "unknown", "response": resp}

        except requests.exceptions.Timeout:
            return {"status": "timeout"}
        except Exception as e:
            return {"status": "exception", "error": str(e)}


def get_throttle(db, key):
    row = db.execute("SELECT value FROM throttle_config WHERE key=?", (key,)).fetchone()
    return row[0] if row else None


def set_throttle(db, key, value):
    db.execute("INSERT OR REPLACE INTO throttle_config VALUES (?,?)", (key, str(value)))
    db.commit()


def dynamic_sleep():
    """Случайная задержка для антипаттерн-детектора."""
    return random.uniform(MIN_SLEEP, MAX_SLEEP)


def check_probation(db, language):
    """Проверяет статус языка в probation."""
    row = db.execute(
        "SELECT edits_done, status FROM language_probation WHERE language=?",
        (language,)
    ).fetchone()

    if not row:
        # New language — start probation
        db.execute(
            "INSERT INTO language_probation (language, first_edit) VALUES (?, ?)",
            (language, datetime.now().isoformat())
        )
        db.commit()
        return "probation"

    edits_done, status = row
    if status == "blocked":
        return "blocked"
    if status == "probation" and edits_done >= PROBATION_THRESHOLD:
        db.execute(
            "UPDATE language_probation SET status='approved', approved_at=? WHERE language=?",
            (datetime.now().isoformat(), language)
        )
        db.commit()
        return "approved"

    return status


def update_probation_count(db, language):
    db.execute(
        "UPDATE language_probation SET edits_done = edits_done + 1 WHERE language=?",
        (language,)
    )
    db.commit()


def adjust_daily_limit(db):
    """Dynamic throttle: увеличивает лимит если 0 ревертов за 7 дней."""
    reverts_7d = db.execute("""
        SELECT COALESCE(SUM(reverts_count), 0)
        FROM bot_stats
        WHERE date > date('now', '-7 days')
    """).fetchone()[0]

    current_limit = int(get_throttle(db, "max_edits_per_day") or "500")

    if reverts_7d == 0:
        # +20% каждую неделю, cap at 20000
        new_limit = min(int(current_limit * 1.2), 20000)
        if new_limit != current_limit:
            set_throttle(db, "max_edits_per_day", new_limit)
            print(f"  Throttle increased: {current_limit} → {new_limit} (0 reverts in 7d)")
    elif reverts_7d > 0:
        # Any reverts — halve the limit
        new_limit = max(current_limit // 2, 100)
        set_throttle(db, "max_edits_per_day", new_limit)
        print(f"  Throttle DECREASED: {current_limit} → {new_limit} ({reverts_7d} reverts in 7d)")


def main():
    parser = argparse.ArgumentParser(description="GSCO Edit Daemon")
    parser.add_argument("--dry-run", action="store_true", help="Don't actually edit")
    parser.add_argument("--limit", type=int, default=500, help="Max edits this run")
    args = parser.parse_args()

    print(f"=== GSCO Edit Daemon ===")
    print(f"Date: {datetime.now().isoformat()}")
    print(f"Mode: {'DRY RUN' if args.dry_run else 'LIVE'}")
    print(f"Limit: {args.limit}")
    print()

    # Check emergency stop
    if STOP_FILE.exists():
        print(f"STOPPED: {STOP_FILE} exists. Remove to resume.")
        sys.exit(0)

    db = sqlite3.connect(str(DB_PATH))

    # Check daily limit
    today = datetime.now().strftime("%Y-%m-%d")
    last_date = get_throttle(db, "last_edit_date")
    if last_date != today:
        set_throttle(db, "edits_today", "0")
        set_throttle(db, "last_edit_date", today)
        # Adjust throttle weekly check
        adjust_daily_limit(db)

    max_daily = int(get_throttle(db, "max_edits_per_day") or "500")
    edits_today = int(get_throttle(db, "edits_today") or "0")
    remaining = min(args.limit, max_daily - edits_today)

    if remaining <= 0:
        print(f"Daily limit reached: {edits_today}/{max_daily}")
        db.close()
        return

    print(f"Daily limit: {max_daily} | Done today: {edits_today} | This run: {remaining}")

    # Login to Wikidata
    ws = None
    if not args.dry_run:
        ws = WikidataSession(CREDENTIALS_FILE)
        ws.login()

    # Get pending edits ordered by priority
    edits = db.execute("""
        SELECT id, qid, edit_type, language, value, confidence, source
        FROM edit_queue
        WHERE status = 'pending'
        ORDER BY priority ASC, id ASC
        LIMIT ?
    """, (remaining,)).fetchall()

    print(f"Pending edits: {len(edits)}")
    print()

    success = 0
    failed = 0
    skipped = 0

    for edit_id, qid, edit_type, language, value, confidence, source in edits:
        # Check emergency stop between edits
        if STOP_FILE.exists():
            print("EMERGENCY STOP detected mid-run")
            break

        # Probation check
        prob_status = check_probation(db, language)
        if prob_status == "blocked":
            db.execute("UPDATE edit_queue SET status='skipped' WHERE id=?", (edit_id,))
            skipped += 1
            continue

        # Only low-priority QIDs during probation
        if prob_status == "probation":
            qid_num = int(qid[1:]) if qid[1:].isdigit() else 0
            if qid_num < 10000000:
                # Skip high-profile during probation
                continue

        if args.dry_run:
            print(f"  DRY: {edit_type} {qid} {language} = {value[:60]}")
            db.execute("UPDATE edit_queue SET status='sent', sent_at=? WHERE id=?",
                       (datetime.now().isoformat(), edit_id))
            success += 1
        else:
            # Real edit
            summary = f"Adding {edit_type} from GSCO occupation database (I: GSCO, S: {source})"

            if edit_type == "label":
                result = ws.wbsetlabel(qid, language, value, summary)
            elif edit_type == "description":
                result = ws.wbsetdescription(qid, language, value, summary)
            elif edit_type == "alias":
                result = ws.wbsetaliases(qid, language, value, summary)
            else:
                result = {"status": "error", "info": f"Unknown edit_type: {edit_type}"}

            if result["status"] == "ok":
                db.execute("UPDATE edit_queue SET status='confirmed', sent_at=? WHERE id=?",
                           (datetime.now().isoformat(), edit_id))
                update_probation_count(db, language)
                success += 1
                if success % 50 == 0:
                    print(f"  Progress: {success}/{len(edits)} sent")
            elif result["status"] == "maxlag":
                retry = result.get("retry_after", 5)
                print(f"  maxlag — waiting {retry}s")
                time.sleep(retry)
                continue  # retry this edit
            else:
                print(f"  FAILED {qid}: {result}")
                db.execute("UPDATE edit_queue SET status='failed' WHERE id=?", (edit_id,))
                failed += 1

        db.commit()

        # Dynamic sleep
        time.sleep(dynamic_sleep())

    # Update daily counter
    edits_today = int(get_throttle(db, "edits_today") or "0")
    set_throttle(db, "edits_today", edits_today + success)

    # Update bot_stats
    today = datetime.now().strftime("%Y-%m-%d")
    db.execute("""
        INSERT INTO bot_stats (date, edits_count)
        VALUES (?, ?)
        ON CONFLICT(date) DO UPDATE SET edits_count = edits_count + ?
    """, (today, success, success))
    db.commit()

    print(f"\n=== Results ===")
    print(f"Success: {success} | Failed: {failed} | Skipped: {skipped}")
    print(f"Daily total: {edits_today + success}/{max_daily}")

    db.close()


if __name__ == "__main__":
    main()
