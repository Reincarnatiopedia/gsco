#!/usr/bin/env python3
"""
GSCO Edit Queue — наполняет очередь правок из SQLite кэша.
Проверяет что поле пустое в Wikidata перед добавлением в очередь.

Запуск: python3 gsco_edit_queue.py --type descriptions --lang en --limit 1000
"""
import sqlite3, requests, json, time, sys, argparse
from pathlib import Path
from datetime import datetime

DB_PATH = Path(__file__).parent / "gsco_wikidata.db"
UA = "GSCO-EditQueue/1.0 (wikidata@marisdreshmanis.com) python-requests"
API = "https://www.wikidata.org/w/api.php"
WDQS = "https://query.wikidata.org/sparql"

BATCH_SIZE = 50  # wbgetentities limit


def init_queue_tables(db):
    """Создаёт таблицы очереди и валидации."""
    db.executescript("""
        CREATE TABLE IF NOT EXISTS edit_queue (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            qid TEXT NOT NULL,
            edit_type TEXT NOT NULL CHECK(edit_type IN ('label', 'description', 'alias')),
            language TEXT NOT NULL,
            value TEXT NOT NULL,
            confidence REAL NOT NULL DEFAULT 1.0,
            source TEXT NOT NULL,
            priority INTEGER DEFAULT 2,
            status TEXT DEFAULT 'pending'
                CHECK(status IN ('pending', 'sent', 'confirmed', 'failed', 'skipped')),
            created_at TEXT DEFAULT (datetime('now')),
            sent_at TEXT,
            UNIQUE(qid, edit_type, language)
        );

        CREATE TABLE IF NOT EXISTS validation_cache (
            qid TEXT NOT NULL,
            language TEXT NOT NULL,
            field_type TEXT NOT NULL,
            current_value TEXT,
            last_checked TEXT DEFAULT (datetime('now')),
            ttl_seconds INTEGER DEFAULT 3600,
            PRIMARY KEY (qid, language, field_type)
        );

        CREATE TABLE IF NOT EXISTS language_probation (
            language TEXT PRIMARY KEY,
            edits_done INTEGER DEFAULT 0,
            reverts INTEGER DEFAULT 0,
            status TEXT DEFAULT 'probation'
                CHECK(status IN ('probation', 'approved', 'blocked')),
            first_edit TEXT,
            approved_at TEXT
        );

        CREATE TABLE IF NOT EXISTS throttle_config (
            key TEXT PRIMARY KEY,
            value TEXT
        );

        CREATE INDEX IF NOT EXISTS idx_eq_status ON edit_queue(status);
        CREATE INDEX IF NOT EXISTS idx_eq_priority ON edit_queue(priority, status);
        CREATE INDEX IF NOT EXISTS idx_eq_lang ON edit_queue(language, status);
        CREATE INDEX IF NOT EXISTS idx_vc_ttl ON validation_cache(last_checked);
    """)

    # Default throttle config
    defaults = {
        "max_edits_per_day": "500",
        "sleep_between_edits": "2.0",
        "edits_today": "0",
        "last_edit_date": "",
        "warmup_multiplier": "1.0",
    }
    for k, v in defaults.items():
        db.execute(
            "INSERT OR IGNORE INTO throttle_config VALUES (?, ?)", (k, v)
        )
    db.commit()


def get_throttle(db, key):
    row = db.execute("SELECT value FROM throttle_config WHERE key=?", (key,)).fetchone()
    return row[0] if row else None


def set_throttle(db, key, value):
    db.execute("INSERT OR REPLACE INTO throttle_config VALUES (?,?)", (key, str(value)))
    db.commit()


def is_field_empty(db, qid, language, field_type):
    """Проверяет кэш валидации — пусто ли поле. Если кэш устарел, перепроверяет."""
    row = db.execute("""
        SELECT current_value, last_checked, ttl_seconds
        FROM validation_cache
        WHERE qid=? AND language=? AND field_type=?
    """, (qid, language, field_type)).fetchone()

    if row:
        current_value, last_checked, ttl = row
        age = (datetime.utcnow() - datetime.fromisoformat(last_checked)).total_seconds()
        if age < ttl:
            return current_value is None or current_value == ""

    # Cache miss or expired — need to check live
    return None  # Caller must check via API


def check_fields_batch(qids, language, field_type, db):
    """Проверяет пакет QID через Wikidata API и обновляет validation_cache."""
    prop_map = {"label": "labels", "description": "descriptions", "alias": "aliases"}
    prop = prop_map.get(field_type, "labels")

    results = {}
    for i in range(0, len(qids), BATCH_SIZE):
        batch = qids[i:i+BATCH_SIZE]
        try:
            r = requests.get(API, params={
                "action": "wbgetentities",
                "ids": "|".join(batch),
                "props": prop,
                "languages": language,
                "format": "json",
            }, headers={"User-Agent": UA}, timeout=30)

            resp = r.json()
            if "error" in resp:
                print(f"  API error: {resp['error'].get('info')}")
                continue

            for qid, entity in resp.get("entities", {}).items():
                if "missing" in entity:
                    continue
                if field_type == "alias":
                    aliases = entity.get("aliases", {}).get(language, [])
                    current = "|".join(a["value"] for a in aliases) if aliases else ""
                else:
                    current = entity.get(prop, {}).get(language, {}).get("value", "")

                results[qid] = current
                db.execute("""
                    INSERT OR REPLACE INTO validation_cache
                    VALUES (?, ?, ?, ?, datetime('now'), 3600)
                """, (qid, language, field_type, current or None))

        except Exception as e:
            print(f"  Batch check error: {e}")

        time.sleep(0.5)

    db.commit()
    return results


def build_description_queue(db, language, limit=1000):
    """Строит очередь descriptions для людей на основе GSCO данных.
    Шаблон: '{occupation}' (на целевом языке).
    Только для occupation items, не для людей (Q5) — людей будем делать отдельно.
    """
    print(f"Building description queue for occupation items, lang={language}...")

    # Берём профессии из кэша у которых есть label на нужном языке но нет description
    rows = db.execute("""
        SELECT o.qid, l.label
        FROM occupations o
        JOIN labels l ON o.qid = l.qid AND l.lang = ?
        LEFT JOIN descriptions d ON o.qid = d.qid AND d.lang = ?
        WHERE d.description IS NULL
        AND o.qid LIKE 'Q%'
        LIMIT ?
    """, (language, language, limit)).fetchall()

    if not rows:
        print(f"  No occupation items without descriptions in {language}")
        return 0

    print(f"  Found {len(rows)} candidates from cache")

    # Verify against live Wikidata in batches
    qids = [r[0] for r in rows]
    label_map = {r[0]: r[1] for r in rows}
    live_status = check_fields_batch(qids, language, "description", db)

    queued = 0
    for qid in qids:
        live_value = live_status.get(qid, "")
        if live_value:  # Already has description — skip
            continue

        label = label_map[qid]
        # Simple description template for occupations
        if language == "en":
            desc = f"type of occupation"
        elif language == "ru":
            desc = f"профессия"
        elif language == "de":
            desc = f"Beruf"
        elif language == "fr":
            desc = f"métier"
        elif language == "es":
            desc = f"profesión"
        elif language == "lv":
            desc = f"profesija"
        else:
            desc = label  # fallback — use label as description basis

        # Don't add if description would be same as label
        if desc.lower() == label.lower():
            continue

        db.execute("""
            INSERT OR IGNORE INTO edit_queue
            (qid, edit_type, language, value, confidence, source, priority)
            VALUES (?, 'description', ?, ?, 1.0, 'GSCO', 2)
        """, (qid, language, desc))
        queued += 1

    db.commit()
    print(f"  Queued {queued} descriptions")
    return queued


def build_label_queue(db, language, limit=1000):
    """Строит очередь labels для профессий из GSCO данных.
    Добавляет label только если поле пустое в Wikidata.
    """
    print(f"Building label queue for lang={language}...")

    # Берём профессии из GSCO у которых есть label на нужном языке
    # но проверим через API что в Wikidata поле пустое
    rows = db.execute("""
        SELECT o.qid, l.label
        FROM occupations o
        JOIN labels l ON o.qid = l.qid AND l.lang = ?
        WHERE o.qid LIKE 'Q%'
        LIMIT ?
    """, (language, limit)).fetchall()

    if not rows:
        print(f"  No labels available for {language}")
        return 0

    print(f"  Found {len(rows)} candidates with labels in cache")

    # Check which ones are empty in Wikidata
    qids = [r[0] for r in rows]
    label_map = {r[0]: r[1] for r in rows}
    live_status = check_fields_batch(qids, language, "label", db)

    queued = 0
    for qid in qids:
        live_value = live_status.get(qid, "")
        if live_value:  # Already has label — skip
            continue

        label = label_map[qid]
        if len(label) < 2 or len(label) > 250:
            continue

        db.execute("""
            INSERT OR IGNORE INTO edit_queue
            (qid, edit_type, language, value, confidence, source, priority)
            VALUES (?, 'label', ?, ?, 1.0, 'GSCO', 1)
        """, (qid, language, label))
        queued += 1

    db.commit()
    print(f"  Queued {queued} labels")
    return queued


def queue_stats(db):
    """Показывает статистику очереди."""
    stats = db.execute("""
        SELECT edit_type, language, status, COUNT(*)
        FROM edit_queue
        GROUP BY edit_type, language, status
        ORDER BY edit_type, language
    """).fetchall()

    total = db.execute("SELECT COUNT(*) FROM edit_queue").fetchone()[0]
    pending = db.execute("SELECT COUNT(*) FROM edit_queue WHERE status='pending'").fetchone()[0]
    sent = db.execute("SELECT COUNT(*) FROM edit_queue WHERE status='sent'").fetchone()[0]

    print(f"\n=== Edit Queue Stats ===")
    print(f"Total: {total} | Pending: {pending} | Sent: {sent}")
    for edit_type, lang, status, count in stats:
        print(f"  {edit_type:12s} {lang:5s} {status:10s} {count:6d}")


def main():
    parser = argparse.ArgumentParser(description="GSCO Edit Queue Builder")
    parser.add_argument("--type", choices=["labels", "descriptions"], default="labels")
    parser.add_argument("--lang", default="en")
    parser.add_argument("--limit", type=int, default=1000)
    parser.add_argument("--stats", action="store_true")
    parser.add_argument("--init", action="store_true", help="Initialize tables only")
    args = parser.parse_args()

    db = sqlite3.connect(str(DB_PATH))
    init_queue_tables(db)

    if args.init:
        print("Tables initialized.")
        db.close()
        return

    if args.stats:
        queue_stats(db)
        db.close()
        return

    if args.type == "labels":
        build_label_queue(db, args.lang, args.limit)
    elif args.type == "descriptions":
        build_description_queue(db, args.lang, args.limit)

    queue_stats(db)
    db.close()


if __name__ == "__main__":
    main()
