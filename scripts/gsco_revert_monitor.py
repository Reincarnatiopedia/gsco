#!/usr/bin/env python3
"""
GSCO Revert Monitor — отслеживает реверты правок бота ReNeuralAgent.
Запуск: cron каждые 10 минут.
При обнаружении реверта — останавливает бота и логирует.

Cron: */10 * * * * cd /opt/reincarnatiopedia/data && python3 gsco_revert_monitor.py >> /var/log/gsco_revert_monitor.log 2>&1
"""
import requests, sqlite3, json, time, os, sys
from pathlib import Path
from datetime import datetime, timedelta

DB_PATH = Path(__file__).parent / "gsco_wikidata.db"
STOP_FILE = Path(__file__).parent / "BOT_EMERGENCY_STOP"
BOT_USER = "ReNeuralAgent"
UA = "GSCO-RevertMonitor/1.0 (wikidata@marisdreshmanis.com) python-requests"
API = "https://www.wikidata.org/w/api.php"

# Thresholds
REVERT_THRESHOLD_24H = 1   # любой реверт = стоп
REVERT_THRESHOLD_7D = 3    # 3 за неделю = серьёзная проблема


def init_db(db):
    db.executescript("""
        CREATE TABLE IF NOT EXISTS revert_log (
            revid INTEGER PRIMARY KEY,
            qid TEXT,
            timestamp TEXT,
            comment TEXT,
            reverted_by TEXT,
            detected_at TEXT
        );
        CREATE TABLE IF NOT EXISTS bot_stats (
            date TEXT PRIMARY KEY,
            edits_count INTEGER DEFAULT 0,
            reverts_count INTEGER DEFAULT 0,
            warnings_count INTEGER DEFAULT 0
        );
    """)


def get_recent_contributions(limit=500, hours=24):
    """Получает последние правки бота через API."""
    end = datetime.utcnow()
    start = end - timedelta(hours=hours)

    params = {
        "action": "query",
        "list": "usercontribs",
        "ucuser": BOT_USER,
        "uclimit": str(limit),
        "ucstart": end.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "ucend": start.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "ucprop": "ids|title|timestamp|comment|tags",
        "format": "json",
    }

    try:
        r = requests.get(API, params=params,
                        headers={"User-Agent": UA}, timeout=30)
        r.raise_for_status()
        return r.json().get("query", {}).get("usercontribs", [])
    except Exception as e:
        print(f"[{datetime.now().isoformat()}] ERROR fetching contribs: {e}")
        return []


def check_if_reverted(revid):
    """Проверяет, была ли конкретная правка откачена."""
    params = {
        "action": "query",
        "prop": "revisions",
        "revids": str(revid),
        "rvprop": "ids|user|comment|tags",
        "rvlimit": "5",
        "format": "json",
    }

    try:
        r = requests.get(API, params=params,
                        headers={"User-Agent": UA}, timeout=30)
        data = r.json()
        pages = data.get("query", {}).get("pages", {})
        for page_id, page in pages.items():
            revisions = page.get("revisions", [])
            for rev in revisions:
                tags = rev.get("tags", [])
                comment = rev.get("comment", "").lower()
                # Проверяем теги и комментарии на признаки реверта
                if any(t in tags for t in ["mw-undo", "mw-rollback", "mw-manual-revert"]):
                    return True, rev.get("user", "unknown"), rev.get("comment", "")
                if "revert" in comment or "undo" in comment or "rv " in comment:
                    return True, rev.get("user", "unknown"), rev.get("comment", "")
    except Exception as e:
        print(f"[{datetime.now().isoformat()}] ERROR checking revert for {revid}: {e}")

    return False, None, None


def check_reverts_via_recentchanges(hours=1):
    """Альтернативный метод: ищем реверты через RecentChanges."""
    end = datetime.utcnow()
    start = end - timedelta(hours=hours)

    params = {
        "action": "query",
        "list": "recentchanges",
        "rctag": "mw-undo|mw-rollback|mw-manual-revert",
        "rclimit": "50",
        "rcstart": end.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "rcend": start.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "rcprop": "user|comment|title|ids|tags|timestamp",
        "format": "json",
    }

    reverts = []
    try:
        r = requests.get(API, params=params,
                        headers={"User-Agent": UA}, timeout=30)
        changes = r.json().get("query", {}).get("recentchanges", [])
        for change in changes:
            comment = change.get("comment", "").lower()
            # Ищем упоминание нашего бота в комментарии реверта
            if BOT_USER.lower() in comment or "reneuralagent" in comment:
                reverts.append(change)
    except Exception as e:
        print(f"[{datetime.now().isoformat()}] ERROR checking recentchanges: {e}")

    return reverts


def emergency_stop(reason):
    """Создаёт файл-флаг для остановки бота."""
    STOP_FILE.write_text(json.dumps({
        "reason": reason,
        "timestamp": datetime.now().isoformat(),
        "action": "BOT STOPPED — manual review required"
    }, indent=2))
    print(f"[{datetime.now().isoformat()}] EMERGENCY STOP: {reason}")
    print(f"  Stop file created: {STOP_FILE}")
    print(f"  To resume: rm {STOP_FILE}")


def main():
    now = datetime.now()
    db = sqlite3.connect(str(DB_PATH))
    init_db(db)

    # Check if bot is already stopped
    if STOP_FILE.exists():
        print(f"[{now.isoformat()}] Bot already stopped. Remove {STOP_FILE} to resume.")
        db.close()
        return

    print(f"[{now.isoformat()}] Checking for reverts...")

    # Method 1: Check our recent contributions
    contribs = get_recent_contributions(limit=100, hours=24)
    new_reverts = 0

    for contrib in contribs:
        revid = contrib.get("revid")
        if not revid:
            continue

        # Skip if already checked
        existing = db.execute("SELECT 1 FROM revert_log WHERE revid = ?", (revid,)).fetchone()
        if existing:
            continue

        # Check via tags on the contribution itself
        tags = contrib.get("tags", [])
        if any(t in tags for t in ["mw-reverted"]):
            qid = contrib.get("title", "").replace("Property:", "")
            comment = contrib.get("comment", "")
            db.execute(
                "INSERT OR IGNORE INTO revert_log VALUES (?,?,?,?,?,?)",
                (revid, qid, contrib.get("timestamp", ""), comment,
                 "unknown", now.isoformat())
            )
            new_reverts += 1
            print(f"  REVERT DETECTED: {qid} (revid={revid})")

    # Method 2: Check RecentChanges for reverts mentioning us
    rc_reverts = check_reverts_via_recentchanges(hours=1)
    for rv in rc_reverts:
        revid = rv.get("revid", 0)
        qid = rv.get("title", "")
        db.execute(
            "INSERT OR IGNORE INTO revert_log VALUES (?,?,?,?,?,?)",
            (revid, qid, rv.get("timestamp", ""), rv.get("comment", ""),
             rv.get("user", "unknown"), now.isoformat())
        )
        new_reverts += 1
        print(f"  REVERT via RC: {qid} by {rv.get('user', '?')}")

    db.commit()

    # Count reverts in last 24h and 7d
    reverts_24h = db.execute(
        "SELECT COUNT(*) FROM revert_log WHERE detected_at > ?",
        ((now - timedelta(hours=24)).isoformat(),)
    ).fetchone()[0]

    reverts_7d = db.execute(
        "SELECT COUNT(*) FROM revert_log WHERE detected_at > ?",
        ((now - timedelta(days=7)).isoformat(),)
    ).fetchone()[0]

    # Update daily stats
    today = now.strftime("%Y-%m-%d")
    db.execute("""
        INSERT INTO bot_stats (date, reverts_count)
        VALUES (?, ?)
        ON CONFLICT(date) DO UPDATE SET reverts_count = reverts_count + ?
    """, (today, new_reverts, new_reverts))
    db.commit()

    # Emergency stop check
    if reverts_24h >= REVERT_THRESHOLD_24H:
        emergency_stop(f"{reverts_24h} revert(s) in last 24h (threshold: {REVERT_THRESHOLD_24H})")
    elif reverts_7d >= REVERT_THRESHOLD_7D:
        emergency_stop(f"{reverts_7d} reverts in last 7d (threshold: {REVERT_THRESHOLD_7D})")
    else:
        print(f"  OK: 0 reverts in 24h, {reverts_7d} in 7d")
        # Update edit count for today
        edit_count = len(contribs)
        db.execute("""
            INSERT INTO bot_stats (date, edits_count)
            VALUES (?, ?)
            ON CONFLICT(date) DO UPDATE SET edits_count = ?
        """, (today, edit_count, edit_count))
        db.commit()

    db.close()


if __name__ == "__main__":
    main()
