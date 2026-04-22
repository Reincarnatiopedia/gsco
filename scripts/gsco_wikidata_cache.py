#!/usr/bin/env python3
"""
GSCO Wikidata Cache — еженедельный дамп всех профессий из Wikidata в SQLite.
Убивает таймауты SPARQL: все маппинги работают с локальной базой за миллисекунды.

Запуск: python3 gsco_wikidata_cache.py
Cron:   0 3 * * 0 cd /opt/reincarnatiopedia/data && python3 gsco_wikidata_cache.py >> /var/log/gsco_cache.log 2>&1

Схема БД:
  occupations(qid TEXT PK, isco08 TEXT, isco88 TEXT)
  labels(qid TEXT, lang TEXT, label TEXT, PK(qid,lang))
  aliases(qid TEXT, lang TEXT, alias TEXT)
  descriptions(qid TEXT, lang TEXT, description TEXT, PK(qid,lang))
"""
import sqlite3, requests, json, time, sys, os
from pathlib import Path
from datetime import datetime

DB_PATH = Path(__file__).parent / "gsco_wikidata.db"
WDQS = "https://query.wikidata.org/sparql"
UA = "GSCO-Cache/1.0 (wikidata@marisdreshmanis.com) python-requests"
BATCH_SIZE = 50  # items per API call (500 x 53 langs = too large, API truncates)

# Languages we care about (ESCO 28 + major world languages)
LANGS = [
    "en", "de", "fr", "es", "it", "pt", "nl", "pl", "cs", "sk", "hu", "ro",
    "bg", "hr", "sl", "et", "lv", "lt", "fi", "sv", "da", "el", "ga", "mt",
    "no", "is", "ar", "ru", "uk", "be", "kk", "uz", "az", "ka", "hy",
    "tr", "fa", "he", "hi", "bn", "ta", "te", "th", "vi", "id", "ms",
    "ja", "ko", "zh", "sw", "ha", "yo", "tl",
]


def init_db(db):
    """Создаёт таблицы если не существуют."""
    db.executescript("""
        CREATE TABLE IF NOT EXISTS occupations (
            qid TEXT PRIMARY KEY,
            isco08 TEXT,
            isco88 TEXT,
            en_label TEXT
        );
        CREATE TABLE IF NOT EXISTS labels (
            qid TEXT,
            lang TEXT,
            label TEXT,
            PRIMARY KEY (qid, lang)
        );
        CREATE TABLE IF NOT EXISTS aliases (
            qid TEXT,
            lang TEXT,
            alias TEXT
        );
        CREATE TABLE IF NOT EXISTS descriptions (
            qid TEXT,
            lang TEXT,
            description TEXT,
            PRIMARY KEY (qid, lang)
        );
        CREATE TABLE IF NOT EXISTS meta (
            key TEXT PRIMARY KEY,
            value TEXT
        );
        CREATE INDEX IF NOT EXISTS idx_labels_lang ON labels(lang);
        CREATE INDEX IF NOT EXISTS idx_occ_isco08 ON occupations(isco08);
        CREATE INDEX IF NOT EXISTS idx_occ_en ON occupations(en_label);
    """)


def sparql_query(query, retries=3):
    """Выполняет SPARQL запрос к Wikidata с ретраями."""
    for attempt in range(retries):
        try:
            r = requests.get(WDQS, params={"query": query, "format": "json"},
                           headers={"User-Agent": UA, "Accept": "application/json"},
                           timeout=120)
            if r.status_code == 429:
                wait = int(r.headers.get("Retry-After", 60))
                print(f"  Rate limited, sleeping {wait}s...")
                time.sleep(wait)
                continue
            r.raise_for_status()
            return r.json()["results"]["bindings"]
        except Exception as e:
            print(f"  SPARQL attempt {attempt+1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(30 * (attempt + 1))
    return []


def fetch_occupation_qids():
    """Выгружает все QID профессий (instance/subclass of Q28640)."""
    print("Fetching occupation QIDs...")
    query = """
    SELECT DISTINCT ?occ ?isco08 ?isco88 ?enLabel WHERE {
      { ?occ wdt:P31 wd:Q28640 }
      UNION
      { ?occ wdt:P31/wdt:P279* wd:Q28640 }
      UNION
      { ?occ wdt:P279 wd:Q28640 }
      OPTIONAL { ?occ wdt:P3008 ?isco08 }
      OPTIONAL { ?occ wdt:P952 ?isco88 }
      OPTIONAL { ?occ rdfs:label ?enLabel . FILTER(LANG(?enLabel) = "en") }
    }
    """
    results = sparql_query(query)
    occupations = {}
    for r in results:
        qid = r["occ"]["value"].split("/")[-1]
        occupations[qid] = {
            "isco08": r.get("isco08", {}).get("value", ""),
            "isco88": r.get("isco88", {}).get("value", ""),
            "en_label": r.get("enLabel", {}).get("value", ""),
        }
    print(f"  Found {len(occupations)} occupation items")
    return occupations


def fetch_labels_batch(qids, db):
    """Выгружает labels/aliases/descriptions пачками через Wikidata API.
    Wikidata API лимит: 50 языков за запрос. Разбиваем на чанки.
    """
    api = "https://www.wikidata.org/w/api.php"
    total = len(qids)
    processed = 0
    # API limit: 50 languages per request
    LANG_CHUNK = 50
    lang_chunks = [LANGS[i:i+LANG_CHUNK] for i in range(0, len(LANGS), LANG_CHUNK)]

    for i in range(0, total, BATCH_SIZE):
        batch = [q for q in qids[i:i+BATCH_SIZE] if q.startswith("Q")]
        if not batch:
            processed += BATCH_SIZE
            continue
        ids_str = "|".join(batch)

        for lang_chunk in lang_chunks:
            langs_str = "|".join(lang_chunk)
            try:
                r = requests.get(api, params={
                    "action": "wbgetentities",
                    "ids": ids_str,
                    "props": "labels|aliases|descriptions",
                    "languages": langs_str,
                    "format": "json",
                }, headers={"User-Agent": UA}, timeout=60)

                if r.status_code == 429:
                    wait = int(r.headers.get("Retry-After", 30))
                    print(f"  429 rate limited, sleeping {wait}s")
                    time.sleep(wait)
                    continue

                resp = r.json()
                if "error" in resp:
                    print(f"  API error: {resp['error'].get('code')}: {resp['error'].get('info')}")
                    continue

                data = resp.get("entities", {})

                label_rows = []
                alias_rows = []
                desc_rows = []

                for qid, entity in data.items():
                    if "missing" in entity:
                        continue
                    for lang, obj in entity.get("labels", {}).items():
                        label_rows.append((qid, lang, obj["value"]))
                    for lang, arr in entity.get("aliases", {}).items():
                        for obj in arr:
                            alias_rows.append((qid, lang, obj["value"]))
                    for lang, obj in entity.get("descriptions", {}).items():
                        desc_rows.append((qid, lang, obj["value"]))

                if label_rows:
                    db.executemany("INSERT OR REPLACE INTO labels VALUES (?,?,?)", label_rows)
                if alias_rows:
                    db.executemany("INSERT INTO aliases VALUES (?,?,?)", alias_rows)
                if desc_rows:
                    db.executemany("INSERT OR REPLACE INTO descriptions VALUES (?,?,?)", desc_rows)
                db.commit()

            except Exception as e:
                print(f"  Batch error at {i} langs={lang_chunk[0]}: {e}")

            time.sleep(1.2)

        processed += len(batch)
        if processed % 500 == 0 or processed >= total:
            n = db.execute("SELECT COUNT(*) FROM labels").fetchone()[0]
            print(f"  Progress: {processed}/{total} items, {n} labels in DB")


def main():
    print(f"=== GSCO Wikidata Cache Builder ===")
    print(f"Date: {datetime.now().isoformat()}")
    print(f"DB: {DB_PATH}")
    print()

    db = sqlite3.connect(str(DB_PATH))
    init_db(db)

    # Step 1: Fetch all occupation QIDs via SPARQL
    occupations = fetch_occupation_qids()
    if not occupations:
        print("ERROR: No occupations fetched, aborting")
        sys.exit(1)

    # Step 2: Insert into occupations table
    db.execute("DELETE FROM occupations")
    db.executemany(
        "INSERT INTO occupations VALUES (?,?,?,?)",
        [(qid, d["isco08"], d["isco88"], d["en_label"]) for qid, d in occupations.items()]
    )
    db.commit()
    print(f"Occupations table: {len(occupations)} rows")

    # Step 3: Fetch labels/aliases/descriptions via API
    print(f"\nFetching labels for {len(LANGS)} languages...")
    qids = [q for q in occupations.keys() if q.startswith("Q")]

    # Clear old data
    db.execute("DELETE FROM labels")
    db.execute("DELETE FROM aliases")
    db.execute("DELETE FROM descriptions")
    db.commit()

    fetch_labels_batch(qids, db)

    # Step 4: Stats
    n_labels = db.execute("SELECT COUNT(*) FROM labels").fetchone()[0]
    n_aliases = db.execute("SELECT COUNT(*) FROM aliases").fetchone()[0]
    n_descs = db.execute("SELECT COUNT(*) FROM descriptions").fetchone()[0]
    n_langs = db.execute("SELECT COUNT(DISTINCT lang) FROM labels").fetchone()[0]

    db.execute("INSERT OR REPLACE INTO meta VALUES ('last_update', ?)",
               (datetime.now().isoformat(),))
    db.execute("INSERT OR REPLACE INTO meta VALUES ('occupation_count', ?)",
               (str(len(occupations)),))
    db.execute("INSERT OR REPLACE INTO meta VALUES ('label_count', ?)",
               (str(n_labels),))
    db.commit()

    print(f"\n=== CACHE READY ===")
    print(f"Occupations: {len(occupations)}")
    print(f"Labels:      {n_labels} ({n_langs} languages)")
    print(f"Aliases:     {n_aliases}")
    print(f"Descriptions:{n_descs}")
    print(f"DB size:     {DB_PATH.stat().st_size / 1024 / 1024:.1f} MB")

    db.close()


if __name__ == "__main__":
    main()
