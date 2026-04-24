# GSCO Canonicalization Methodology

**Version:** 1.0
**Date:** 2026-04-24
**Author:** Maris Dreshmanis + Claude Code session `7d9dc355`
**Status:** Specification (pre-implementation)
**Related:** `docs/GSCO_ARTICLE_DRAFT_v1.md` §4.1 (Legal Ground Truth), §5.3 (Pilot Results)

---

## 1. Purpose

GSCO's foundational claim is **deterministic exact-matching against legally authoritative sources**. When a country's classification exists across multiple files in our repository, this determinism is compromised: downstream pipelines (Wikidata writes, analytics, conflict detection) produce inconsistent results. This document defines the rules for identifying, consolidating, and maintaining **one canonical source per country** while preserving legitimate historical and multilingual variants.

**Goals:**
1. Eliminate parse-generation pollution (N copies of the same registry)
2. Correctly model multilingual single-source registries (Canada NOC, Belgium, etc.)
3. Correctly model multi-version registries (historical publications at different dates)
4. Produce an auditable provenance chain: every Wikidata claim → canonical source file → commit hash → official government URL
5. Enable safe migration when canonical changes (update references in already-written claims)

## 2. Terminology

| Term | Definition |
|---|---|
| **Canonical source** | The single file designated as authoritative for a country, from which pipeline builds `gsco_unified.json` and Wikidata edits derive |
| **Parse generation** | A re-parse of the same official document with an improved script (e.g., v1 flat → v2 with hierarchy → v3 with EN placeholders). Same data, different schema richness |
| **Official version** | A distinct publication of the registry at a specific date (e.g., Latvia PK 2010 vs PK 2024). Different reality — must be preserved with time qualifiers |
| **Archive** | `data/_archive/YYYY-MM/` — legacy files removed from pipeline input but physically retained for provenance/rollback |
| **Multilingual single-source** | One official classification containing labels in multiple languages (Macau: ZH+PT; Canada: EN+FR). Treated as single file with nested `labels: {lang: ...}` |
| **Split-by-language** | Incorrect pattern: same country registry distributed across several files, one per language. Must be merged during canonicalization |
| **ISCO-4 key** | The 4-digit ISCO-08 code used as primary join key across sources and as Wikidata `P3008` property value |

## 3. Decision Tree

When multiple files are associated with the same country, classify the scenario:

```
Multiple files for country X?
│
├── SCENARIO A: Parse-generation duplicates
│   (same registry, same publication date, re-parsed with better script)
│   → Consolidate: pick newest-richest as canonical. Others → archive.
│
├── SCENARIO B: Multilingual single-source (already merged)
│   (one file, `labels: {lang: ...}` structure, multiple languages inside)
│   → Leave as-is. Nothing to consolidate. Ensure schema conforms.
│
├── SCENARIO C: Split-by-language
│   (same registry, same date, different files for different languages)
│   → Merge into single file with nested `labels: {lang: ...}`. Archive splits.
│
├── SCENARIO D: Different official versions
│   (same country, different publication dates — legitimate historical divergence)
│   → Keep all. Primary = latest. Others get P580/P582 time qualifiers in Wikidata.
│
└── SCENARIO E: Unknown / ambiguous
    → Manual review. Do NOT write to Wikidata until resolved.
```

**How to detect which scenario:**

- **A vs D**: compare publication dates if available in file metadata. If absent, compare label content for same ISCO codes — if labels match 95%+ → A. If significantly different → D (real version change).
- **B vs C**: inspect file schema. If single file has `labels: {en:..., fr:...}` → B. If filename pattern `{country}_{lang}.json` with separate files → C.
- **A+C combined**: possible (split-by-language across multiple parse generations). Consolidate generations first, then merge languages.

## 4. Canonical Selection Criteria

When Scenario A (consolidation) applies, select canonical by priority:

1. **Schema richness** — prefer file with:
   - Parent-child hierarchy (`parent` field)
   - ISCO-4 mapping explicit (`isco4` field)
   - English placeholders (`name_en` or `labels.en`) even if null — signals pipeline-ready design
2. **Coverage** — prefer file with more entries, IF superset (spot-check 20 codes to confirm the larger one contains all of smaller)
3. **Freshness of parse** — prefer file with latest modification date (assumes newer parse uses better tools)
4. **Official source provenance** — prefer file whose parsing is closest to primary .gov source (check parser metadata or README)
5. **Manual review status** — prefer file that has been manually audited (tracked in `CANONICAL_SOURCES.json` under `reviewed_by`)

If two files tie on criteria 1-4 and neither has been reviewed, **run cross-source validation (§5)** to detect any divergences before picking.

## 5. Cross-Source Validation Process

Before selecting canonical in Scenario A, run comparison:

### 5.1 Normalization pipeline

Each label string passes through:
```python
def normalize(s: str) -> str:
    import unicodedata
    s = unicodedata.normalize("NFC", s)  # canonicalize unicode
    s = s.strip()                         # remove leading/trailing whitespace
    s = " ".join(s.split())               # collapse internal whitespace
    return s  # preserve case: compare case-insensitive separately
```

Plus optional fold for comparison only (never stored normalized):
```python
def fold_for_compare(s: str) -> str:
    return normalize(s).casefold()
```

### 5.2 Coverage matrix

For N sources over country X, compute set membership on ISCO-4 codes:

| Intersection | Count |
|---|---|
| ∩ all N | X₀ (should be majority) |
| Only in source_i | Xᵢ |
| In (N-1) but missing from source_j | ... |

**Red flag**: large disjoint sets between sources indicate Scenario D (different versions) or parse errors.

### 5.3 Label divergence matrix

For each code in the intersection:
- `labels_equal_after_normalization` — count
- `labels_equal_after_fold` (case-insensitive) — count
- `labels_levenshtein_≤2` — count (accept minor OCR/typo differences)
- `labels_different` — count + list divergent codes

**Decision thresholds:**
- ≥95% equal after fold → Scenario A confirmed, pick canonical
- 80-95% equal → investigate: possibly Scenario A with parser errors, or Scenario D with partial overlap
- <80% equal → Scenario D likely, escalate to manual review

### 5.4 Schema divergence summary

Report per-source: fields present, nesting depth, hierarchy present (yes/no), language coverage.

## 6. Multilingual Merge Procedure (Scenario C)

When split-by-language files detected:

**Input:**
- `country_en.json`, `country_fr.json`, `country_de.json`, ...

**Algorithm:**
1. Load all N language files into memory
2. Join on primary key (prefer `code`, fall back to `isco4 + subcode`)
3. Build merged structure:
   ```json
   {
     "code": "2511",
     "isco4": "2511",
     "parent": "251",
     "labels": {
       "en": "Systems analysts",
       "fr": "Analystes de systèmes",
       "de": null
     },
     "source": "country_noc_2024"
   }
   ```
4. For codes present in some languages but not others: keep entry, set missing `labels.{lang} = null`
5. For codes present in one but missing in others: log as `partial_coverage`, still keep entry
6. Write to canonical `country_noc.json`
7. Archive originals to `data/_archive/{YYYY-MM}/`

**Wikidata impact:** single `gsco_edit_daemon` pass writes all language labels in batch — fewer API round-trips vs N separate passes.

## 7. Archive Policy

- **Where:** `data/_archive/{YYYY-MM}/` on server (month of consolidation)
- **Never delete** — required for:
  - Retroactive Wikidata reference rebuild if canonical changes
  - Diff analysis (what changed between parse generations)
  - Regulatory/audit questions ("why did this claim change in April?")
- **Metadata**: each archived file gets a sidecar `<name>.archived.json`:
  ```json
  {
    "archived_at": "2026-04-24T14:00:00Z",
    "superseded_by": "lv_profesiju.json",
    "reason": "parse-generation-duplicate",
    "last_pipeline_use": "2026-04-22",
    "wikidata_claims_written": 1122,
    "validation_report": "LV_CANONICALIZATION_REPORT.md"
  }
  ```
- **Git**: archived files committed to repo; never force-removed

## 8. Canonical Source Registry

File: `tools/CANONICAL_SOURCES.json`

Schema:
```json
{
  "LV": {
    "file": "data/national_registries_new/lv_profesiju.json",
    "version_label": "Profesiju klasifikators 2024",
    "schema_version": 3,
    "published": "2024",
    "validity_start": "2024-01-01",
    "validity_end": null,
    "languages": ["lv"],
    "official_url": "https://likumi.lv/...",
    "parser_script": "tools/parsers/parse_lv_pk.py",
    "parser_version": "1.3.0",
    "reviewed_by": "Maris Dreshmanis",
    "reviewed_at": "2026-04-24",
    "archived_predecessors": [
      "data/_archive/2026-04/lv_professions.json",
      "data/_archive/2026-04/lv_profesiju_2026.json"
    ],
    "wikidata_pilot_stats": {
      "first_deployment": "2026-04-22",
      "total_claims_written": 1122,
      "total_reverts": 0
    }
  },
  "CA": {
    "file": "data/national_registries_new/ca_noc_2021.json",
    "version_label": "NOC 2021",
    "schema_version": 3,
    "published": "2021",
    "languages": ["en", "fr"],
    "official_url": "https://noc.esdc.gc.ca/",
    "merged_from": [
      "data/_archive/2026-04/ca_noc_en.json",
      "data/_archive/2026-04/ca_noc_fr.json"
    ],
    ...
  }
}
```

This file is **the source of truth**. Pipeline components (`build_gsco_unified.py`, `gsco_edit_daemon.py`, webapp) all read from it.

## 9. Wikidata Reference Strategy

Every Wikidata claim written by GSCO bot MUST include reference block:

```
<Q{occupation}> <P1843 native_label> "label"
  REF: P143 imported from=Q{Wikimedia project or self-QID for GSCO dataset}
       P854 reference URL=https://github.com/.../CANONICAL_SOURCES.json#LV
       P813 retrieved=YYYY-MM-DD
       P248 stated in=Q{country's classification on Wikidata, if it has its own QID}
```

For **Scenario D (multiple official versions)** — add qualifiers to claim itself:
```
<Q{occupation}> <P1843 native_label> "label"
  QUALIFIERS: P580 start time=2024-01-01
              P582 end time=(empty, if current)
  REF: ... (as above)
```

### 9.1 Canonical change migration

When canonical for country X changes (new version released, or parser improvement produces different labels):

1. **Diff canonical_old vs canonical_new**:
   - Labels unchanged for code C → no action
   - Label changed for code C → existing claim needs update
   - Code C removed → existing claim needs deprecation (P2241 reason for deprecation)
   - Code C added → new claim to write

2. **Query SPARQL for affected claims**:
   ```sparql
   SELECT ?item ?statement WHERE {
     ?item p:P1843 ?statement .
     ?statement prov:wasDerivedFrom/pr:P854 ?url .
     FILTER CONTAINS(?url, "CANONICAL_SOURCES.json#LV")
   }
   ```

3. **Apply changes via bot with dry-run first**:
   - Dry-run: log intended changes to `migration_<country>_<date>.log`
   - Human review of log
   - Execute

4. **Update `CANONICAL_SOURCES.json`** with new version_label, archived predecessor, fresh pilot_stats

## 10. Audit Automation

### 10.1 Daily detection script (`tools/gsco_audit/daily_canonical_check.py`)

Runs via cron, outputs `docs/GSCO_CANONICALIZATION_STATUS.md`:

- Detect new files added to `data/national_registries*/` not yet in CANONICAL_SOURCES.json
- Detect files in CANONICAL_SOURCES.json that no longer exist (broken refs)
- Detect parse-generation patterns (files with similar names, different modification times) — flag for consolidation
- Detect split-by-language patterns (files matching `{country}_{lang}.json` regex)
- Summary: N countries with canonical defined, M pending, K conflicts

### 10.2 Compare tool (`tools/gsco_audit/compare_sources.py --country XX`)

Parameterized runner of §5 validation. Used during canonicalization decisions.

Outputs: `docs/audit/{COUNTRY}_CANONICALIZATION_REPORT.md`

## 11. Success Criteria

A country is considered **canonicalized** when:

1. Exactly one entry exists for it in `CANONICAL_SOURCES.json`
2. All other files for the country are archived (with sidecar metadata)
3. Pipeline (`build_gsco_unified.py`) reads only the canonical
4. Webapp displays only the canonical (no 3× search duplicates)
5. Wikidata claims for this country carry references pointing to the canonical
6. `reviewed_by` and `reviewed_at` populated by human reviewer

## 12. Pilot: Latvia

See `docs/audit/LV_CANONICALIZATION_REPORT.md` (to be produced by `compare_sources.py --country LV`).

Expected findings:
- 3 files, all appear to be parse generations of same Profesiju klasifikators
- v3 (`lv_profesiju.json`) has richest schema: hierarchy + EN placeholder
- v3 coverage ≥ v2 ≥ v1 entries
- Label divergence expected in 0-5% range (case normalization, whitespace) — Scenario A confirmed
- Canonical = v3, archive v1 + v2
- Already-written Wikidata claims (1,122 LV-specific) likely referenced v1 or v2 — migration required after canonical switch

Once LV pilot complete and report written, update this methodology with any new lessons (e.g., if a Scenario E case emerges).

## 13. Implementation Roadmap

**Phase 1** — methodology (this document) ✓
**Phase 2** — LV pilot: write `compare_sources.py`, run on LV, produce report, consolidate
**Phase 3** — extend to all ~124 countries: batch audit, identify scenarios A/B/C/D
**Phase 4** — implement multilingual merge for Scenario C countries (if any)
**Phase 5** — canonical migration for already-written Wikidata claims (Wikidata cleanup)
**Phase 6** — automation: daily cron audit, drift detection, self-healing

## 14. References to GSCO Article (v1)

This methodology operationalizes:
- §4.1 "Legal Ground Truth Instead of Probabilities" — requires single authoritative source
- §4.3 "Human-AI Symbiosis: Aggregation" — canonical selection is human-reviewed, bot execution automated
- §5.3 "Pilot Results" — 0 reverts claim presupposes clean canonical inputs

Article v2 should add a new subsection referencing this methodology:
- **§5.5 "Canonical Source Resolution — Operational Workflow"** — case study: LV consolidation

---

**Change log:**
- 2026-04-24 v1.0 — Initial specification (before LV pilot)
