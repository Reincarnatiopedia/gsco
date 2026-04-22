#!/usr/bin/env python3
"""
GSCO ESCO Mapper — сопоставляет ESCO labels с Wikidata QID через ISCO-08 коды.
Находит labels которых НЕТ в Wikidata и добавляет в edit_queue.

Это ключевой pipeline: ESCO (28 языков, 2942 профессии) → Wikidata.

Запуск: python3 gsco_esco_mapper.py [--lang sw] [--limit 1000] [--dry-run]
"""
import sqlite3, json, argparse, sys, requests, time
from pathlib import Path
from datetime import datetime

DB_PATH = Path(__file__).parent / "gsco_wikidata.db"
ESCO_PATH = Path(__file__).parent / "esco_occupations.json"
UA = "GSCO-ESCOMapper/1.0 (wikidata@marisdreshmanis.com) python-requests"
API = "https://www.wikidata.org/w/api.php"
BATCH_SIZE = 50


def load_esco():
    """Загружает ESCO данные."""
    data = json.loads(ESCO_PATH.read_text())
    return data["occupations"]


def build_isco_to_qid_map(db):
    """Строит маппинг ISCO-08 код → список QID из кэша."""
    rows = db.execute("""
        SELECT qid, isco08, en_label FROM occupations
        WHERE isco08 != '' AND qid LIKE 'Q%'
    """).fetchall()

    mapping = {}
    for qid, isco08, en_label in rows:
        code = isco08.strip().replace(".", "").replace("-", "")
        if code not in mapping:
            mapping[code] = []
        mapping[code].append({"qid": qid, "en_label": en_label})

    return mapping


def build_en_label_to_qid_map(db):
    """Строит маппинг EN label → QID. Основной метод — по названию."""
    rows = db.execute("""
        SELECT qid, en_label FROM occupations
        WHERE en_label != '' AND qid LIKE 'Q%'
    """).fetchall()

    mapping = {}
    for qid, en_label in rows:
        key = en_label.lower().strip()
        if key not in mapping:
            mapping[key] = qid
        # If duplicate — keep first (lower QID = older = more established)

    return mapping


def check_wikidata_labels(qids, language):
    """Проверяет какие QID не имеют label на данном языке."""
    empty = []
    for i in range(0, len(qids), BATCH_SIZE):
        batch = qids[i:i+BATCH_SIZE]
        try:
            r = requests.get(API, params={
                "action": "wbgetentities",
                "ids": "|".join(batch),
                "props": "labels",
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
                label = entity.get("labels", {}).get(language, {}).get("value", "")
                if not label:
                    empty.append(qid)

        except Exception as e:
            print(f"  Batch check error: {e}")

        time.sleep(0.5)

    return empty


def find_best_qid(isco_code, esco_en_label, isco_map):
    """Находит лучший QID для ESCO профессии по ISCO-08 коду и EN label."""
    candidates = isco_map.get(isco_code, [])
    if not candidates:
        return None

    if len(candidates) == 1:
        return candidates[0]["qid"]

    # Multiple candidates — match by English label
    esco_en = esco_en_label.lower().strip() if esco_en_label else ""
    best_match = None
    best_score = 0

    for c in candidates:
        wd_en = (c["en_label"] or "").lower().strip()
        if wd_en == esco_en:
            return c["qid"]  # Exact match
        # Simple overlap score
        esco_words = set(esco_en.split())
        wd_words = set(wd_en.split())
        if esco_words and wd_words:
            overlap = len(esco_words & wd_words) / max(len(esco_words), len(wd_words))
            if overlap > best_score:
                best_score = overlap
                best_match = c["qid"]

    # Only return if reasonable match
    if best_score >= 0.5:
        return best_match

    # Fallback: return first candidate (same ISCO code)
    return candidates[0]["qid"]


def main():
    parser = argparse.ArgumentParser(description="GSCO ESCO → Wikidata Mapper")
    parser.add_argument("--lang", default=None, help="Target language (e.g. 'sw'). None = all ESCO languages")
    parser.add_argument("--limit", type=int, default=5000)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--stats", action="store_true")
    args = parser.parse_args()

    db = sqlite3.connect(str(DB_PATH))

    if args.stats:
        # Show mapping coverage
        esco = load_esco()
        isco_map = build_isco_to_qid_map(db)
        en_map = build_en_label_to_qid_map(db)

        mapped_isco = 0
        mapped_en = 0
        unmapped = 0
        for o in esco:
            isco_code = o["isco_code"].replace(".", "")
            en_label = o.get("labels", {}).get("en", o.get("labels", {}).get("en-us", ""))
            if isco_code in isco_map:
                mapped_isco += 1
            elif en_label and en_label.lower().strip() in en_map:
                mapped_en += 1
            else:
                unmapped += 1

        total_mapped = mapped_isco + mapped_en
        print(f"ESCO occupations: {len(esco)}")
        print(f"ISCO→QID mapping: {len(isco_map)} codes ({mapped_isco} matched)")
        print(f"EN label→QID mapping: {len(en_map)} labels ({mapped_en} matched)")
        print(f"Total mapped: {total_mapped}/{len(esco)} ({100*total_mapped/len(esco):.1f}%)")
        print(f"Unmapped: {unmapped}")

        # Languages available in ESCO
        all_langs = set()
        for o in esco:
            all_langs.update(o.get("labels", {}).keys())
        print(f"Languages in ESCO: {len(all_langs)}")
        print(f"  {sorted(all_langs)}")
        db.close()
        return

    print(f"=== GSCO ESCO → Wikidata Mapper ===")
    print(f"Date: {datetime.now().isoformat()}")
    print(f"Mode: {'DRY RUN' if args.dry_run else 'LIVE'}")
    print()

    # Load data
    esco = load_esco()
    isco_map = build_isco_to_qid_map(db)
    en_map = build_en_label_to_qid_map(db)
    print(f"ESCO: {len(esco)} occupations")
    print(f"ISCO→QID: {len(isco_map)} codes")
    print(f"EN label→QID: {len(en_map)} labels")

    # Determine target languages
    if args.lang:
        target_langs = [args.lang]
    else:
        # All ESCO languages except en-us (duplicates en)
        all_langs = set()
        for o in esco:
            all_langs.update(o.get("labels", {}).keys())
        target_langs = sorted(all_langs - {"en-us"})

    total_queued = 0

    for lang in target_langs:
        print(f"\n--- Language: {lang} ---")

        # Build candidates: ESCO label exists, has mapping to Wikidata QID
        candidates = []
        for occ in esco:
            label = occ.get("labels", {}).get(lang)
            if not label:
                continue
            isco_code = occ["isco_code"].replace(".", "")
            en_label = occ.get("labels", {}).get("en", occ.get("labels", {}).get("en-us", ""))

            # Try ISCO mapping first, then EN label matching
            qid = find_best_qid(isco_code, en_label, isco_map)
            if not qid and en_label:
                qid = en_map.get(en_label.lower().strip())
            if qid:
                candidates.append({"qid": qid, "label": label, "isco": isco_code})

        print(f"  Candidates with ISCO mapping: {len(candidates)}")

        if not candidates:
            continue

        # Check which ones are empty in Wikidata
        # Normalize language code for Wikidata (no-nb → nb, en-us → skip)
        wd_lang = lang
        if lang == "en-us":
            continue
        if lang == "no":
            wd_lang = "nb"  # Norwegian Bokmål in Wikidata

        qid_to_label = {c["qid"]: c["label"] for c in candidates}
        qids = list(qid_to_label.keys())[:args.limit]

        empty_qids = check_wikidata_labels(qids, wd_lang)
        print(f"  Empty in Wikidata: {len(empty_qids)}")

        if not empty_qids:
            continue

        # Add to edit_queue
        queued = 0
        for qid in empty_qids:
            label = qid_to_label[qid]
            if len(label) < 2 or len(label) > 250:
                continue

            if args.dry_run:
                print(f"  DRY: {qid} {wd_lang} = {label}")
                queued += 1
            else:
                db.execute("""
                    INSERT OR IGNORE INTO edit_queue
                    (qid, edit_type, language, value, confidence, source, priority)
                    VALUES (?, 'label', ?, ?, 1.0, 'ESCO', 1)
                """, (qid, wd_lang, label))
                queued += 1

        if not args.dry_run:
            db.commit()

        print(f"  Queued: {queued}")
        total_queued += queued

        if total_queued >= args.limit:
            break

    print(f"\n=== TOTAL QUEUED: {total_queued} ===")

    # Show queue stats
    if not args.dry_run:
        stats = db.execute("""
            SELECT language, COUNT(*) FROM edit_queue
            WHERE status='pending' GROUP BY language ORDER BY COUNT(*) DESC
        """).fetchall()
        print("\nQueue by language:")
        for lang, cnt in stats:
            print(f"  {lang}: {cnt}")

    db.close()


if __name__ == "__main__":
    main()
