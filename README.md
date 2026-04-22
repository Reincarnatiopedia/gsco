# GSCO — Global Standard Classification of Occupations

The first global multilingual occupation database, aggregating 50+ national government registries through ISCO-08 codes as a universal hub.

## Key Statistics

| Metric | Value |
|--------|-------|
| Occupations (Wikidata items) | 26,991 |
| Labels (multilingual names) | 152,135 |
| Aliases (alternative names) | 98,335 |
| Descriptions | 76,734 |
| Languages | 53 |
| National registries | 50+ |
| Wikidata edits (0 reverts) | 16,000+ |

## Problem

Traditional occupation classification suffers from three fundamental issues:

1. **N² complexity** — linking N national registries requires N² bilateral crosswalk tables
2. **LLM hallucinations** — neural machine translation fails catastrophically on low-resource languages (zero-shot transfer failure)
3. **ISCO stagnation** — the ILO updates its standard every ~20 years; code 2131 meant "computer programmers" in ISCO-88 but "biologists" in ISCO-08

## Solution

GSCO uses **deterministic exact matching** against legally authoritative government sources. No AI, no neural machine translation — every label comes from an official national occupation registry.

ISCO-08 4-digit codes serve as a **universal hub**, reducing crosswalk complexity from O(n²) to O(n).

## Repository Structure

```
data/
  esco/                    # European Commission ESCO database (28 languages, 2,942 occupations)
  national_registries/     # 25 national occupation registries in JSON format
  wikidata_cache/          # CSV export of Wikidata occupation items (53 languages)
  isco08_worldwide.json    # ISCO-08 codes with global mappings
  isco08_to_wikidata_qid.json  # ISCO-08 → Wikidata QID mapping
  isco_combined_all_versions.csv  # ISCO-58/68/88/08 combined
  occupation_registries.json  # Registry metadata and sources

scripts/
  gsco_wikidata_cache.py   # Weekly dump of all Wikidata occupation items to SQLite
  gsco_esco_mapper.py      # Maps ESCO labels to Wikidata QIDs via EN exact match
  gsco_edit_queue.py       # Pre-validated edit queue with confidence tiers
  gsco_edit_daemon.py      # Executes edits to Wikidata (maxlag=5, 3-5s delay)
  gsco_revert_monitor.py   # Monitors reverts every 10 minutes, emergency stop

docs/
  CODEBOOK.md              # Data dictionary and schema documentation
```

## Data Dictionary (Codebook)

### Wikidata Cache (`data/wikidata_cache/`)

**gsco_occupations.csv** — All occupation items from Wikidata (instance/subclass of Q28640)
| Column | Type | Description |
|--------|------|-------------|
| `qid` | TEXT | Wikidata item ID (e.g., Q82594) |
| `isco08` | TEXT | ISCO-08 code from P3008 (often empty in Wikidata) |
| `isco88` | TEXT | ISCO-88 code from P952 (legacy, unreliable) |
| `en_label` | TEXT | English label from Wikidata |

**gsco_labels.csv** — Multilingual labels for occupation items
| Column | Type | Description |
|--------|------|-------------|
| `qid` | TEXT | Wikidata item ID |
| `lang` | TEXT | ISO 639 language code (e.g., `lv`, `sw`, `bn`) |
| `label` | TEXT | Label text in that language |

**gsco_aliases.csv** — Alternative names for occupations
| Column | Type | Description |
|--------|------|-------------|
| `qid` | TEXT | Wikidata item ID |
| `lang` | TEXT | ISO 639 language code |
| `alias` | TEXT | Alternative name |

**gsco_descriptions.csv** — Short descriptions
| Column | Type | Description |
|--------|------|-------------|
| `qid` | TEXT | Wikidata item ID |
| `lang` | TEXT | ISO 639 language code |
| `description` | TEXT | Description text |

### National Registries (`data/national_registries/`)

Each JSON file contains occupations from an official government registry:

| File | Country | Language(s) | Occupations | Source |
|------|---------|-------------|-------------|--------|
| `isco_tr_turkey.json` | Turkey | tr | 7,202 | ISCO-TR (TÜİK) |
| `bsco_bangladesh.json` | Bangladesh | bn, en | 5,387 | BSCO (BBS) |
| `nco_india.json` | India | en, hi | 3,452 | NCO-2015 (MoSPI) |
| `kbji_2014.json` | Indonesia | id | 2,731 | KBJI-2014 (BPS) |
| `cbo_brazil_ocupacao.json` | Brazil | pt-BR | 2,614 | CBO (MTE) |
| `noc_canada.json` | Canada | en, fr | 822 | NOC 2021 (StatCan) |
| `sinco_mexico.json` | Mexico | es | 686 | SINCO (INEGI) |
| `okz_russia.json` | Russia | ru | 618 | OKZ (Rosstat) |
| `masco_malaysia.json` | Malaysia | ms, en | 491 groups | MASCO (MOHR) |
| `lv_professions.json` | Latvia | lv | 4,282 | Profesiju klasifikators |
| + 15 more | Various | Various | Various | National statistical offices |

### ESCO (`data/esco/`)

**esco_occupations.json** — European Commission's ESCO v1.2.1 (2,942 occupations in 28 EU languages)

## Methodology

1. **Data collection**: Parse official government PDFs, APIs, and CSV files from national statistical offices and ministries of labor
2. **Hub mapping**: Link each national registry to ISCO-08 4-digit codes (the universal key)
3. **Matching**: Deterministic exact English label match between Wikidata and source registries
4. **Validation**: Pre-check every edit against live Wikidata state; only fill empty fields
5. **Execution**: Bot edits with maxlag=5, 3-5s delay, revert monitoring every 10 minutes, automatic emergency stop

## Wikidata Integration

Bot account: [User:Maris Dreshmanis](https://www.wikidata.org/wiki/User:Maris_Dreshmanis)
Bot operator: ReNeuralAgent ([bot flag request](https://www.wikidata.org/wiki/Wikidata:Requests_for_permissions/Bot/ReNeuralAgent))
Source code: This repository

Edit summary format: `Adding label from GSCO occupation database (I: GSCO, S: ESCO)`

## Languages Covered (53)

en, de, fr, es, it, pt, nl, pl, cs, sk, hu, ro, bg, hr, sl, et, lv, lt, fi, sv, da, el, ga, mt, no, is, ar, ru, uk, be, kk, uz, az, ka, hy, tr, fa, he, hi, bn, ta, te, th, vi, id, ms, ja, ko, zh, sw, ha, yo, tl

## License

- **Code**: MIT License
- **Data (national registries)**: Each file retains its original government license. Most are public domain or open government license.
- **Wikidata cache**: CC0 (mirrors Wikidata's license)
- **ESCO data**: EUPL v1.2 (European Commission)

## Author

**Maris Dreshmanis**
- ORCID: [0009-0003-8151-4088](https://orcid.org/0009-0003-8151-4088)
- ISNI: [0000 0004 9280 9121](https://isni.org/isni/0000000492809121)
- Wikidata: [User:Maris Dreshmanis](https://www.wikidata.org/wiki/User:Maris_Dreshmanis)
- GitHub: [MarisDreshmanis](https://github.com/MarisDreshmanis)

## Citation

```bibtex
@dataset{dreshmanis_gsco_2026,
  author    = {Dreshmanis, Maris},
  title     = {GSCO: Global Standard Classification of Occupations — Multilingual Occupation Database},
  year      = {2026},
  publisher = {Zenodo},
  version   = {1.0},
  license   = {CC-BY-4.0}
}
```
