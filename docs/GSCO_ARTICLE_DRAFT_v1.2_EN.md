# GSCO: The Global Standard Classification of Occupations — A Deterministic Multilingual Database to Solve the N² Cross-Table Problem in International Occupation Classification

**Maris Dreshmanis**
ORCID: [0009-0003-8151-4088](https://orcid.org/0009-0003-8151-4088) | ISNI: [0000 0004 9280 9121](https://isni.org/isni/0000000492809121)
Affiliation: Academy of Reincarnationology | Independent Researcher
GitHub: [MarisDreshmanis](https://github.com/MarisDreshmanis) | Wikidata: [User:Maris Dreshmanis](https://www.wikidata.org/wiki/User:Maris_Dreshmanis)

**Version:** 1 | **License:** CC BY 4.0 | **Date:** April 2026

**DOI:** [10.5281/zenodo.19902278](https://doi.org/10.5281/zenodo.19902278) (this version) · **Concept DOI:** [10.5281/zenodo.19902277](https://doi.org/10.5281/zenodo.19902277) (latest version) · [Zenodo record](https://zenodo.org/records/19902278)

---

## Abstract

**Introduction.** The problem of inconsistent occupation classification codes across countries was discovered by chance. One of my activities involves editing and populating Wikidata. Wikidata serves as a link between Wikipedia editions in different languages, acting as a central repository for shared facts and references.

While working on populating Wikidata with data for a specific target group—Nobel laureates in different languages—I found that occupation titles were one of the areas not systematically organized in Wikidata.

To avoid errors in occupation titles when translating with neural networks or Google Translate, I decided to collect occupation classifiers from open sources in various languages. Once this was done, a global problem of worldwide scale became apparent. Firstly, the International Labour Organization (ILO) updates its International Standard Classification of Occupations (ISCO) approximately every 20 years. This means that new occupations from the current decade are not included.

Here are the ISCO standardization years:

- **ISCO-58** — Adopted in 1957 (published in 1958).
- **ISCO-68** — Adopted in 1966 (published in 1968).
- **ISCO-88** — Adopted in 1987 (published in 1988). This was the first to clearly define the concept of "skill level."
- **ISCO-08** — Adopted in 2007 (published in 2008). This is the current version used worldwide.
- The next version (**ISCO-28**) is currently in the active revision phase by the ILO—empirical input submission is open from 2026–2028, with release in 2028.

Secondly, countries that have independently tackled this task have added codes that conflict between different nations. The situation is slightly better in the European Union, but globally, after 4 digits of ISCO, there is chaos in standardization and codes.

Continuing to work on describing the occupations of Nobel laureates, I created a table to analyze discrepancies across countries. I simply named it: **GSCO (Global Standard Classification of Occupations)**. Why global? Because I collected data from over 140 national registries. I haven't found any information that anyone in the world has done this before; if you, the reader of this text, have such information—please send it to me. Contact details are provided on my profile page.

Once the data was collected and analyzed, I realized I needed to share this data not only with national registries so they could recognize the number of occupation code conflicts in their countries and attempt to synchronize them, but also with the International Labour Organization (ILO) to help the working group see the scale of the problem and consider it during the standardization of ISCO-28 in 2028.

### Example: ISCO 2221

**Hub-level: What official ISCO-08 means**

ISCO-08 (ILO): "Nursing professionals" — nurses with advanced practice (advanced nurse practitioner).

Multilingual hub-level labels in our database (35 languages):

| Language | Translation |
|---|---|
| ar | ممارس تمريض متقدم |
| az | Tibbi qulluq üzrə peşəkar mütəxəssislər |
| bg | старша медицинска сестра |
| bn | হাসপাতাল ǯসিবকা পরামশȟক |
| cs | kvalifikovaná zdravotní sestra |
| da | oversygeplejerske |
| de | Akademischer Krankenpfleger |
| el | νοσηλευτής προηγμένης πρακτικής |
| en | advanced nurse practitioner |
| es | enfermero de práctica avanzada |
| et | vastutav õde |
| fi | kliinisen hoitotyön asiantuntija |
| fr | infirmier de pratique avancée |
| ga | altra ardchleachtais |
| hr | viši medicinski tehničar |
| hu | osztályvezető ápoló |
| id | Profesional Keperawatan |
| is | hjúkrunarsérfræðingur |
| it | infermiere di pratica avanzata |
| ka | სპეციალისტი-პროფესიონალი ექთნები |
| lt | vyresnysis slaugytojas |
| lv | vecākā medicīnas māsa |
| ms | PROFESIONAL KEJURURAWATAN |
| mt | infermier prattikant avvanzat |
| nl | leidinggevend verpleegkundige |
| no | oversykepleier |
| pl | pielęgniarz zaawansowanej praktyki |
| pt | Enfermeiro de prática avançada |
| ro | asistent medical șef |
| ru | Специалисты по медицинскому уходу |
| sk | zdravotný brat |
| sl | višji medicinski tehnik |
| sv | distriktssköterska |
| th | แพทย์ |
| tr | Diğer Hemşireler |

**Catastrophe at the National Level**

Under one ISCO code, 2221, different countries mean **different professions**:

**Australia and New Zealand (ANZSCO 2022) — Financial Brokers, Not Nurses:**

- 222111 Commodities Trader
- 222112 Finance Broker
- 222113 Insurance Broker
- 222199 Financial Brokers nec
- 222100 Financial Brokers nfd

**Ukraine (DK003) — Doctors, Not Nurses:**

- 2221 — "Professionals in the field of medical practice (excluding dentistry)"
- 2221.1 — Scientific researchers (medical practice)
- 2221.2 — Doctors (physicians): therapist, cardiologist, surgeon, psychotherapist, neurologist, geneticist…
- A total of 78 subcodes — all doctors, not nurses.

**Germany (KldB-2010):**

- 22212 "Vehicle paintwork — skilled tasks"
- 81393 "Aufsichtskräfte — Gesundheits- und Krankenpflege, Rettungsdienst und Geburtshilfe" — senior nurses
- 81302 "Gesundheits- und Krankenpflege" — regular nurses (according to the official Umsteigeschlüssel Bundesagentur für Arbeit, they map to ISCO 3221, not 2221)

**Belarus (OKRВ-2017, current classifier version):**

- 2221: "Professional nurses" — nurses (corresponds to ISCO-08)

**Italy (CP 2021) — Architects:**

- 2.2.2.1.1 ARCHITETTI (architects)
- 2.2.2.1.2 Pianificatori, paesaggisti (planners, landscape architects)

**San Marino (RP-2017) — Architects:**

- 22211 ARCHITETTO

**Canada (NOC 2021) — Technologists:**

- 22210 Architectural technologists
- 22211 Industrial designers
- 22212 Drafting technologists
- 22213 Land survey technologists
- 22214 Geomatics

**Algeria (DZ Profession) — Doctors:**

- 2221: "Médecins" (doctors)

---

### Professions Familiar to Everyone — Teacher and Taxi Driver

To show that the problem is not about rare professions like "yoga instructor" or "hypnotherapist" but about **the most ordinary, mass occupations**, let us look at two universal professions: teacher and taxi driver. They exist in every country — but the classifications diverge radically.

#### 👨‍🏫 Teacher / Lecturer

Top-15 countries by number of positions under ISCO 23xx (Education):

| Country | Positions under 23xx | Most unusual granularity |
|---|---:|---|
| 🇧🇦 **Bosnia (KZBiH-08)** | **404** | **191 distinct university teachers** under a single ISCO 2310 — separate code for each specialty (biotech, philology, mathematics) |
| 🇺🇿 Uzbekistan (OZMST 2025) | 387 | 179 vocational teachers (2320) |
| 🇲🇳 Mongolia (YAMAT-08) | 355 | 120 university + 120 vocational |
| 🇸🇦 Saudi Arabia (SSCO 2024) | 275 | 76 secondary teachers |
| 🇷🇸 Serbia (Šifarnik) | 264 | 97 university teachers |
| 🇰🇷 Korea (KSCO 2024) | 171 | 5–7 in each ISCO-4 group, evenly spread |
| 🇮🇹 Italy (CP2021) | 141 | 38 lecturers under 2311 |
| 🇪🇪 Estonia (AK-2008) | 130 | Education-methods specialists, language teachers — separate codes |

And at the very bottom:

| Country | Total | What's there |
|---|---:|---|
| 🇷🇺 Russia (OKZ-2014) | **22** | Only 4-digit ISCO groups, no granularity |
| 🇩🇪 Germany (KldB-2010) | 40 | Own numbering, doesn't break down ISCO 23xx |
| 🇺🇸 USA (O\*NET) | **8** | 5 SOC categories 23-1 + 3 SOC 23-2 |
| 🇬🇧 UK (SOC 2020) | 15 | 1 per sub-code |

**What this means for an individual teacher:** a Bosnian biotechnology professor has a specific code in KZBiH-08 (one of 191) — but if she moves to Russia, her 191-level granularity **collapses into the single code 2310 "university lecturer"**. If she moves to the USA, her code does not even **fit into SOC 23-1** (no subject-specific level there).

#### 🚕 Taxi Driver

The standard ISCO **8322** "Car, taxi and van drivers" (a combined category) exists in most countries. But **local taxi types** are a case ISCO-08 simply does not cover:

| Country | Local code | Description |
|---|---|---|
| 🇫🇷 France (ROME 11993) | Chauffeur de taxi animalier | **Animal-transport taxi** — the only stand-alone class of its kind worldwide |
| 🇫🇷 France (ROME 12884) | Conducteur de bateau taxi | Water taxi |
| 🇫🇷 France (ROME 13191) | Conducteur de taxi moto | Motorcycle taxi |
| 🇧🇦 Bosnia + 🌊 PACSCO (Pacific 23 nations) | 8350 | **"Vozač taksija na vodi" / "Water taxi driver"** — water taxi (separate ISCO category) |
| 🇹🇬 **Togo (RGPH4)** | 5020 "Taxi-moto (**Zemidjan**)" | **Zemidjan** — the local name for motorcycle taxi, a profession employing thousands |
| 🇧🇯 Benin (NAP) | 154–155 | "Taxi-moto / charrette / vélo" (motorcycle / cart / bicycle) |
| 🇬🇹 Guatemala (CNO 2022) | 832104 + 933101 | "Piloto de moto taxis" + "**Piloto de bicitaxis**" (cycle taxi) |
| 🇭🇳 **Honduras (CNOH 2018)** | 832101 | "Conductor de moto taxi **forestal** motorizada" — **motorized forest taxi** (unique to Honduras) |
| 🇸🇳 Senegal, 🇩🇯 Djibouti, 🇨🇮 CI | 05.0.0.17 | "taxi man — conducteur de bus" — combined "taxi driver + bus driver" in one occupation |
| 🇨🇦 Canada (NOC 2021) | 75200 | "Taxi and **limousine** drivers and **chauffeurs**" — taxi drivers merged with limousines |
| 🇦🇺/🇳🇿 ANZSCO 2022 | 731112 | "Taxi Driver" — but in ANZSCO's own numbering 7311 = "Automobile Drivers", which **does not** correspond to ISCO 7311 "Precision-Instrument Makers and Repairers" (a different profession in the international standard). Verified via the ABS official OSCA 2024 ↔ ISCO-08 correspondence table: the correct ISCO-08 unit group for ANZSCO 731112 is **8322** "Car, taxi and van drivers". |

**What this means for an individual taxi driver:** the Togolese **zemidjan-driver** (motorcycle taxi) is a real profession with thousands of workers. Neither ISCO-08 nor ANZSCO nor SOC has a slot for it. When he migrates to Germany or France under qualification-recognition rules, his professional experience collapses into the generic "Personenkraftwagen-Fahrer" (passenger-car driver) — because the word "zemidjan" is absent from the German classifier. Not "lost in translation" — he is **lost from the taxonomy**.

The Honduran "forest motorcycle-taxi driver" (Conductor de moto taxi forestal) or the Guatemalan "cycle-taxi driver" (Piloto de bicitaxis) are likewise real, mass occupations **absent from the international structure**.

#### Why This Matters

Teacher and taxi driver are the most universal, easy-to-grasp professions. If even here there is no agreement — what about rare or emerging occupations (AI trainer, drone operator, climate-adaptation specialist)? These examples show: **bringing order to the global classification of occupations is a UN/ILO-scale task**, not the work of individual countries. That is precisely the goal: to help the ISCO-28 working group in 2028 take these divergences into account.

---

### Countries Where 2221 Truly = Nurses

Detailed sub-classifications (showing how the state views specializations):

**Estonia (AK-2008) — 19 subcodes for nurses** (original Estonian names + Russian translation):

- 2221 Õenduse tippspetsialistid (Nursing top specialists)
- 22210501 Abiõde (üliõpilane) — Assistant nurse (student)
- 22210502 Õde — Nurse
- 22210601 Anesteesia-intensiivraviõde — Anesthesia and intensive care nurse
- 22210701 Erakorralise meditsiini õde — Emergency medicine nurse
- 22210801 Diabeediõde — Diabetes nurse
- 22210901 Geriaatriaõde — Geriatric nurse
- 22211001 Lasteõde — Pediatric nurse
- 22211101 Nakkustõrjeõde — Infection control nurse
- 22211201 Onkoloogiaõde — Oncology nurse
- 22211301 Operatsiooniõde — Operating room nurse
- 22211401 Pulmonoloogiaõde — Pulmonology nurse
- 22211501 Taastusraviõde — Rehabilitation nurse
- 22211601 Koduõde — Home care nurse
- 22211701 Kooliõde — School nurse
- 22211801 Töötervishoiuõde — Occupational health nurse
- 22211901 Pereõde — Family nurse
- 22212001 Psühhiaatriaõde — Psychiatric nurse
- 22219900 Mujal liigitamata õenduse tippspetsialistid — Nursing top specialists not classified elsewhere

**Mongolia (YAMAT-08) — 28 subcodes for nurses in Mongolian:**

- 2221-01 Сувилагч, арга зүйч (Nurse, methodologist)
- 2221-02 Сувилагч, ерөнхий мэргэжлийн (Nurse, general practice)
- 2221-03 Сувилагч, арьсны (Nurse, dermatological)
- 2221-04 Сувилагч, гэмтэл согогийн (Nurse, traumatological)
- … 24 more

**Palestine (ASCO 2016) — 23 specialties in Arabic:**

- 222101 ممرضة سريرية (Clinical nurse)
- 222102 ممرضة حي (District nurse)
- 222103 ممرضة التخدير (Anesthesia nurse)
- 222104 ممرضة مربية (Pediatric nurse)
- … 19 more

**Saudi Arabia (SSCO 2024) — 17 specialties:**

- 222101 Nurse Specialist
- 222102 Specialized Nursing Specialist
- 222103 Community Health Nursing Specialist
- 222104 Maternal and Child Nursing Specialist
- 222105 Anesthetic Nursing Specialist
- … 12 more

**South Africa (OFO 2017) — 17 types:**

- 2017-222101 Clinical Nurse Practitioner
- 2017-222102 Aged Care Registered Nurse
- 2017-222103 Registered Nurse (Child and Family Health)
- … 14 more

**Latvia (Profesiju klasifikators) — 8 types with national subcodes:**

- 2221 Medicīnas māsas profesijas vecākie speciālisti (Senior specialists in nursing professions)
- 2221 02 VirsMĀSA (Head nurse)
- 2221 46 MĀSA / vispārējās aprūpes (Nurse / general care)
- 2221 48 anestēzijā un intensīvajā aprūpē (in anesthesia and intensive care)
- 2221 50 psihiatrijā un narkoloģijā (in psychiatry and narcology)
- … 3 more

**Nicaragua (CUONIC) — 7 types:**

- 2221-02 Enfermera Anestesista (Anesthetist Nurse)
- 2221-03 Educadora de Enfermeras (Nurse Educator)
- 2221-04 Enfermera Clínica (Clinical Nurse)
- 2221-05 Enfermera del Quirófano (Operating Room Nurse)
- 2221-06 Enfermera de la Salud Pública (Public Health Nurse)
- … 2 more

---

### Simple Labels Without Detailed Breakdown

- **Albania**: 2221 "Infermierë të specializuar" (specialized nurses)
- **Bhutan** (BSCO): 2221 Nursing Professionals + 22211 Registered Nurse + 22212 Public Health Nurse
- **Ecuador**: 2221 PROFESIONALES DE ENFERMERÍA
- **Iran**: 2221 رستاران متخصص (specialized nurses)
- **Iceland**: 2221 Sérfræðistörf við hjúkrun (Specialist nursing work)
- **Lithuania** (LPK 2023): 2221 Slaugos specialistai (Nursing specialists) + 222101 Slaugytojas (Nurse) + 222102 Mokslo darbuotojas (slauga) (Research worker (nursing))
- **North Macedonia**: 2221 Медицински сестри (Nurses)
- **Mauritius**: 22211 Administrator, nursing + 22212 Educator, nurse + 22219 Nursing professionals n.e.c
- **Cambodia**: 4 subcodes 22211–22214 in Khmer
- **Kenya, Lesotho, Guyana, Grenada, Sierra Leone, Eswatini, Tanzania, Malawi**: all 2221 Nursing Professionals
- **AFRISTAT** (regional for West Africa): 2221 Cadres infirmiers (Nursing staff)

---

### Key Finding for Introduction

The same 4-digit ISCO code 2221 means **fundamentally different professions** in different countries:

- **Nurses** (correct according to ISCO-08) — in countries EE, MN, SA, ZA, PS, LV, LT, MK, EC, IS, BY and ~30 other countries.
- **Doctors** — UA, DZ.
- **Financial Brokers** — AU, NZ.
- **Architects** — IT, SM.
- **Technical Specialists** (surveying, design) — CA.

This is not a "translation error." These are two completely different classification worlds under one number. A Ukrainian cardiologist (code 2221.2) arrives in Germany with documents stating "ISCO 2221"—the German system automatically considers them a nurse. An Australian commodities trader (code 222111) moves to the EU, and their career is classified within the 2221 family, which in the EU means a nurse.

---

**Methods.** The collected data is available at <https://gsco.io>. GSCO (Global Standard Classification of Occupations) is a database that uses the 4-digit ISCO-08 codes as a universal hub for aggregating legally authoritative terms denoting occupations from over 140 national government registries. The methodology is based exclusively on exact text matching with official sources (ESCO, KBJI, MASCO, NCO, OKZ, CBO, KeSCO, and others), completely excluding neural machine translation. An SQLite cache containing 26,991 occupation entries from Wikidata in 53 languages allows for pre-validated batch editing.

**Results.** The resulting dataset contains 152,135 multilingual labels, 98,335 aliases, and 76,734 descriptions in 53 languages, obtained from 146 analyzed national registries, totaling 263,608 occupation entries.

**Conclusion.** The data was collected and matched automatically and requires manual verification of every occupation classifier of every country that is current as of 2026. I did not do this to save my personal time. Let the employees of the International Labour Organization (ILO) and national ministries handle this task—they have budgets and resources allocated for it. My task is not to do the work of all the labor ministries of all the countries in the world, but to highlight the problem.

**Keywords:** occupation classification, ISCO-08, multilingual database, Wikidata, knowledge graph enrichment, deterministic matching, cross-table, ESCO, labor market, NLP benchmark, survey coding, low-resource languages, open data, linked data, semantic web, ontology alignment, ILO, reference data, bot automation, taxonomy alignment.

---

## 1. Introduction: From Nobel Laureates to a Global Data Crisis

### 1.1 A Practical Dead End: When Economists Were Classified as Jazz Musicians

The project originated from an ambitious, yet seemingly localized task: to eliminate a critical deficit of data on the global scientific and cultural elite in open knowledge bases. An analysis of 890 historical Nobel laureates revealed a disturbing statistic—the vast majority lacked basic descriptions in approximately 260 out of over 300 existing Wikipedia language editions. For example, Nobel Peace Prize laureate Desmond Tutu had descriptions in a very small number of language editions at the time the project began—an absurdity for a historical figure of such magnitude.

To address this gap, we designed a deterministic bot (ReNeuralAgent) to automate the creation of multilingual profiles in Wikidata using a simple template: `"{occupation} from {country}"`. However, the very first test runs exposed a large-scale digital catastrophe. The knowledge graph was contaminated with erroneous associations. The occupation "economist" was classified as "jazz musician" in Malay and Indonesian translations. When the system attempted to label "urban planners," it produced "leather production planners," and "system administrators" inexplicably turned into "botanists."

The problem was not in our code but in the fundamental infrastructure of international occupation classification.

### 1.2 Anatomy of a Catastrophe: The ILO's Bureaucratic Time Bomb

Investigating these absurd "hallucinations" led to the outdated paradigm of the International Labour Organization (ILO). Historically, this UN body is responsible for publishing the International Standard Classification of Occupations (ISCO). The update cycle averages 20 years: new versions were released in 1958, 1968, 1988, and 2008 [1].

The most egregious problem is not the slowness but the methodology. Each new release involves a complete reshuffling of numerical codes without backward compatibility. The most striking example: code **2131**. In ISCO-88 (1988), this code designated programmers and system developers. By 2008, the ILO had completely restructured the IT sector and reassigned the freed-up code 2131 to... biologists, botanists, and zoologists [1].

Modern information systems—including Wikidata itself—continue to rely on outdated properties. Property **P952** in Wikidata stores outdated ISCO-88 codes. Our empirical analysis of the Wikidata occupation cache shows the full scale of this stagnation:

| Property | Standard | Items with Data | Coverage |
|----------|----------|---------------:|--------:|
| P3008 | ISCO-08 (current) | 0 | 0.0% |
| P952 | ISCO-88 (outdated, 1988) | 299 | 1.1% |
| None | — | 26,692 | 98.9% |

*Table 1: Coverage of ISCO properties in 26,991 occupation items in Wikidata (April 2026). P3008 (ISCO-08) is completely empty, while P952 (ISCO-88) covers only 1.1% of items. The remaining 98.9% of occupations have no standardized classification code.*

This means that algorithms attempting to synchronize data through these numerical identifiers will either find nothing (98.9% of cases) or retrieve codes from a 38-year-old standard where programmers have been reassigned to biologists.

### 1.3 Realization: A New Standard is Needed

This practical dead end clearly showed that using outdated numerical codes to navigate the modern labor market is doomed to failure. Algorithmic guessing by neural networks also fails due to linguistic hallucinations in rare languages. A fundamentally different approach was needed—a shift from trusting abstract numbers to strict textual determinism based on national legislation.

This understanding gave rise to the GSCO (Global Standard Classification of Occupations) database.

*The anomaly with economists as jazz musicians was not just a Wikidata data quality issue but a symptom of a fundamental incompatibility between the global labor data infrastructure and the scale of modern human mobility. The International Labour Organization, with characteristic statistical caution, designed ISCO-08 in 2008 for a world with 190 million international migrants [33]. By 2024—just 16 years later—this figure has reached approximately 280 million, the number of refugees alone has grown from 16 to 37 million, and internally displaced persons from 26 to 75 million. The world for which ISCO-08 was built no longer exists.*

### 1.4 The Reality of Accelerating Migration

The scale of modern human mobility transforms the mismatch between bureaucratic ISCO revision cycles and the real complexity of the labor market from merely an academic issue into a humanitarian crisis. The numbers speak for themselves:

| Year | Int. Migrants | Refugees | IDPs | Labor Migrants |
|------|---------------|----------|------|-----------------|
| 1988 (ISCO-88 base) | ~70M | ~14M | ~5M | ~80M |
| 2008 (ISCO-08 base) | ~190M | ~16M | ~26M | ~120M |
| **2024** | **~280M** | **~37M** | **~75M (15×!)** | **~169M** |
| Forecast 2035 | ~350M+ | ~50M+ | ~100M+ | est. 200M+ |

*Table 2: Acceleration of Migration 1988–2024 (UN DESA / ILO 2024). ISCO-08 was designed for a world with 190 million international migrants; by 2024, this figure grew to 280 million, and the number of internally displaced persons increased 15-fold compared to the 1988 level.*

The canonical study by Friedberg [34] established that foreign educational certificates carry almost zero transferable economic value in destination country labor markets without a common classification infrastructure—a conclusion increasingly confirmed across jurisdictions. Syrian doctors applying for German Approbation (medical license) wait an average of 14 months for code-level verification [35]. Filipino nurses in Japan accumulate a 15-year pass rate of 14% for licensing exams, partially calibrated to Japanese professional code families. Bangladeshi women—approximately 800,000—are systematically forced into classification as "domestic workers" upon arrival in Gulf countries, regardless of their actual professional experience [36].

These are not isolated cases. They are a structural result of an architecture where 146 nationally authoritative occupation classifiers lack a common hub—a mathematical impossibility that GSCO resolves through its ISCO-08 hub architecture described in §4.

---

## 2. Fundamental Problems of Traditional Classification

The failure discovered when attempting to tag occupations in Wikidata turned out not to be a localized platform error but a symptom of a deep methodological crisis. Four fundamental problems render traditional classification methods unsuitable on a global scale.

### 2.1 The N² Trap: Mathematical Collapse of Cross-Tables

Historically, for different registries to "understand" each other (e.g., linking US O\*NET to European ESCO), ministries create bilateral cross-tables (mappings) [2]. However, ontology architecture researchers have proven that this path leads to a mathematical dead end [3]. Creating such links follows the **N² problem**: for *n* standards, maintaining the currency of links requires generating *n(n-1)/2* cross-tables.

$$C(n) = \frac{n(n-1)}{2}$$

For 50 national registries, this yields **1,225 bilateral cross-tables**, each requiring manual maintenance with every update cycle. This exponential growth makes manual synchronization of the global labor market physically impossible [3].

With the documented GSCO count of 146 nationally authoritative occupation classifiers (April 2026), the n² space requires:

$$C(146) = \frac{146 \times 145}{2} = \textbf{10,585 bilateral cross-tables}$$

Each of these 10,585 tables is invalidated by any update to a single registry. Manual maintenance at this scale is not just impractical; it is mathematically incompatible with the empirical update rate of even one participating registry. The Russian OK 016-2025—replacing the 1994 version after a 30-year gap—illustrates that even single-registry updates are multi-year administrative undertakings [37].

Even AI cannot save the situation. When the European Commission attempted to use an NLP approach (based on BERT) to link 3,000 ESCO occupations to 1,000 O\*NET occupations, the algorithm produced 7,385 potential matches that still required manual human verification, with approximately 600 occupations remaining unmapped [4].

### 2.2 Hierarchical Error: The Blocking Problem

The second systemic vulnerability lies in the tree-like structure of classifiers. Databases like ISCO-08 have a strict 4-level hierarchy: from broad major groups to 436 narrow unit groups [1].

In computational linguistics and machine learning, this creates a phenomenon known as the **blocking problem** or cascading error propagation [5]. An error made at the top level (e.g., if a system mistakenly assigns the professional role of "technicians" instead of "managers") cascades downwards, mathematically guaranteeing that all subsequent, more detailed classification levels for that item will be incorrect [5, 6].

When building the GSCO Wikidata cache, we encountered this problem directly: a SPARQL query `wdt:P31/wdt:P279* wd:Q28640` traversed the `subclass-of` chain and returned items that were not actually occupations—including Lexeme senses (e.g., `L1371064-S1`), which had to be filtered programmatically.

### 2.3 The Illusion of Survey Coding Accuracy

The third problem exposes the subjectivity of manual work. During censuses, respondents describe their occupations in free text. Sociologists then attempt to manually assign these answers to standardized codes [7].

Official OECD reports indicate that even with a simplified three-level coding scheme (350 categories), achieving inter-coder agreement above 75% presents a serious challenge [8]. International surveys report agreement rates ranging from 44% to 89% [9]. Recent attempts to automate this process with AI have not solved the problem: the best IEA automatic occupation coding model achieved only 63% accuracy across 12 languages in predicting the same group as human coders—37% errors accumulating through millions of survey responses [19].

Beresewicz et al. (2024) [20] showed that even multilingual hierarchical transformers (XLM-RoBERTa, fine-tuned on KZiS + ISCO) underperform deterministic exact matching systems on job ads in rare languages, especially for Slavic and Baltic languages where training data is scarce. This computational bottleneck is structural, not temporary—Djumalieva and Sleeman [38] argue that expert-curated taxonomies are "inherently slow and expensive," and propose data-driven alternatives, which GSCO operationalizes through its hub-and-spoke architecture.

The cost is immense: these codes underpin Socio-Economic Status (SES/ISEI) indices [10]. If one coder classifies a farmer's description as "Agricultural Manager" (code 1310), their status index scores 49 points. If another coder assigns them "Self-Employed Farmers" (code 6200), the index drops to 10 points [10]. Systematic interpretation discrepancies destroy the very foundation of sociological measurement on an international scale.

### 2.4 The Qualification Recognition Procedure Crisis

The fourth problem is the one directly faced by millions of working people: the qualification recognition pipeline. The legal basis for portability of qualifications—EU Directive 2005/36/EC on the recognition of professional qualifications—has been in effect since 2005, yet as of December 2024, the European Commission has initiated infringement procedures against Belgium, Germany, France, Luxembourg, and the Netherlands for failing to transpose its modernization requirements [39]. By May 2025, Italy joined this list: 11,861 Romanian nurses were directly affected by the non-adoption of Directive 2024/505 [40].

Empirical data from Germany illustrates the scale of dysfunction. A 2025 report by the Institute of German Economy (Institut der Deutschen Wirtschaft, IW) documents a shortage of 450,000 skilled workers, with 80% of German companies reporting they do not use the formal recognition system at all, and 51.6% rate the recognition process negatively [41]. Within a single federal state, the cost of Approbation varies from €170 to €850 depending on the Bundesland—illustrating that recognition is not harmonized even within Germany, let alone cross-border [42].

The discrepancy extends to outcomes, not just costs. French doctors applying for German recognition achieve a 40.3% approval rate; the same French applicants seeking recognition in Luxembourg achieve 99.8% [41]. This 60 percentage point gap exists between jurisdictions both implementing the same EU Directive, reflecting not legal ambiguity but classification friction—different granularity schemes, different code families, different interpretations of what "equivalent" means when comparing occupation entries between registries.

The case of ZorgSaam from the Dutch-Belgian border region illustrates the absurdity in its sharpest form: a qualified Belgian neurologist from Universitair Ziekenhuis Gent—physically 30 km from a Dutch hospital facing an acute neurologist shortage—was delayed by the requirements of the Dutch BIG-register and cross-border classification mismatch in a region where both countries operate within Schengen free movement and the same EU Directive [42].

The foundational analysis by Sumption [43] identified a structural driver: professional associations function as gatekeepers without institutional incentive to clear the queue, creating an "all-or-nothing" recognition trap that turns partial equivalence into complete exclusion. Information asymmetry is bilateral: employers cannot verify foreign qualifications and default to avoiding risk; migrants cannot present their qualifications within the destination system's code family because a machine-readable bridge does not exist.

These are not "edge cases" or "transitional friction." They are a persistent result of an infrastructure designed for a smaller, slower world.

---

## 3. The Illusion of AI: Limitations of Language Models

### 3.1 Semantic Drift and Polysemy Traps

Neural networks rely on probabilities and historical data, but language is a living entity subject to constant change, a phenomenon known as **semantic drift** [11]. During the COVID-19 pandemic, words like "vulnerable" and "isolated" ceased being general social descriptors and became specific medical terms, disrupting historical language distributions in algorithms [12].

In professional contexts, polysemy exacerbates the problem. As the creators of one NLP classifier noted: "The word 'skill' can refer to technical skills, soft skills, or even a specific type of fish, depending on the context" [13]. AI often cannot resolve such ambiguity without vast amounts of training data. The phenomenon is not metaphorical; JobBERT by Decorte et al. [14] and the contrastive XLM-RoBERTa by Gasco and Retyk [44] both report performance degradation as their training corpora age beyond 18 months, making temporal maintenance an open problem for any probabilistic approach to occupation classification.

### 3.2 Computational Fragility

When researchers attempted to feed GPT-4 a sample of real job ad texts, the model "failed to produce correct matches in 33.9% of cases, while requiring an average of 515,000 input tokens to process a single job ad" [14]. The enormous computational overhead makes such approaches impractical on a global scale.

Even specialized models like JobBERT acknowledge their fundamental limitations: their architecture is "inherently tied to a predefined (and therefore static) list of standardized titles, limiting its practical use" [15]. Neural networks remain "fragile when vocabulary mismatches (synonyms, paraphrases, and local jargon) arise" [15].

The most recent attempt—fine-tuning XLM-RoBERTa on LLM-refined Swiss job ads—achieved only 58.3% Top-1 accuracy on silver data (compared to 37.2% before fine-tuning) and 80% accuracy on a held-out test set [17]. While the authors report 91.4% accuracy in predicting ontology labels (a simplified task), the gap between 80% and 100% accuracy achievable through deterministic matching remains fundamental, not incremental.

In contrast, our `gsco_esco_mapper.py` performs exact matching of English labels against a local SQLite cache—2,942 ESCO occupations are mapped in milliseconds, with zero computational overhead, and zero risk of hallucinations.

### 3.3 The Failure of Zero-Shot Transfer

The most devastating blow to the "AI will save the world" thesis is the problem of rare languages. An official report by the European Commission on machine-assisted data mapping directly acknowledges this vulnerability: "multilingual encoders cannot capture similarity when the source and target languages are less similar at the levels of morphology, syntax, and semantics" [4, 18]. When the EC attempted to perform ML-assisted mapping of national classifications to ESCO using XLM-RoBERTa, Top-1 accuracy ranged from 83.5% (USA) to a mere 45.3% (Latvia)—a morphologically rich Baltic language proved most resistant to neural transfer [18].

A comprehensive literature review shows that **no existing study achieves >95% accuracy on multilingual occupation classification across 10 or more languages simultaneously.** The most extensive multilingual evaluation—Beręsewicz et al.'s hierarchical classification across 24 languages—achieved only ~84% accuracy at the broadest 1-digit major group level, dropping to 40–60% at the granular 6-digit codes [20]. The IEA's 12-language model achieved 92% on clean machine-translated test data but collapsed to 36% on real survey responses [19]. These results establish a hard performance ceiling for probabilistic approaches that the deterministic GSCO methodology completely bypasses.

This limitation is particularly acute for Persian, Bengali, Khmer, Burmese, Tagalog, and Lao—precisely the source languages of major contemporary skilled migration corridors (Iran→Germany, Bangladesh→Saudi Arabia, Nepal→Japan, Philippines→Japan, Cambodia/Myanmar→Thailand). In our own construction of migration case libraries (2026), covering 40+ languages in 7 regional batches, over half of the documented cases in the Slavic, Southeast Asian, and Persian-Indian batches existed only in English-language secondary mirrors of original reportage—confirming that these languages are structurally underserved by neural approaches trained on web-scale corpora.

For a global project aiming to describe people in Swahili (214 labels in Wikidata), Hausa (221 labels), or Yoruba (63 labels), relying on AI translations would guarantee failure. Neural networks simply haven't seen enough texts about "quantum physicists" in Hausa to produce an accurate, legally valid term.

---

## 4. GSCO Architecture: A Deterministic Solution

### 4.1 Legal Ground Truth Instead of Probabilities

In the GSCO architecture, we have completely abandoned machine guessing. The foundational principle is **strict Legal Ground Truth**. If the Ministry of Labor of a specific country has approved an official occupation title in the national language, that term is accepted as the absolute standard without any further semantic analysis. If the official Latvian registry says the term is "santehniķis," and the Hausa dictionary states that a physicist is "masanin ilimin lissafi," these terms are included in the database as is. No neural distortions, no on-the-fly translations—only 100% exact matches with government standards.

### 4.2 ISCO-08 as the Rosetta Stone: Collapsing N² to O(n)

The central technical challenge was to bypass the N² cross-table trap. The solution was found in the structure of ISCO-08, which divides all global occupations into 436 unit groups, each designated by a universal 4-digit code [1].

Instead of attempting to directly link the registry of Indonesia with the registry of Malaysia or the USA, we linked each of the 146 national registries to this central 4-digit hub:

$$\text{Complexity: } O\left(\frac{n(n-1)}{2}\right) \rightarrow O(n)$$

For 146 registries: **10,585 cross-tables → 146 links to the hub**. ISCO-08 became the "Rosetta Stone" through which any language can be instantly translated into any other without loss of meaning.

In practice, code 2111 ("Physicists and astronomers") maps to:
- Russia (OKZ): 2111.1 (physicist-researcher)
- Brazil (CBO): 2111-05
- Indonesia (KBJI): 2111.01
- Wikidata: Q169470

This is not just a software engineering optimization. As Autor, Levy, and Murnane demonstrated in their canonical framework of task-biased technological change [45], occupational tasks evolve continuously, while occupational codes are revised every 20 years. The hub-and-spoke architecture is therefore not just a means to counter n² complexity—it is the only architecture compatible with the continuous evolution of tasks at the edges of registries and the stable semantics of codes in the central hub.

The implementation in `gsco_esco_mapper.py` uses two matching methods:
1. **Primary:** `build_en_label_to_qid_map()` — exact matching of English labels (588 successful matches from ESCO)
2. **Fallback:** `build_isco_to_qid_map()` — matching by ISCO-08 code (0 results, because P3008 is empty in Wikidata)

The fact that the ISCO-08 fallback returned zero matches is empirical evidence that the Wikidata occupation infrastructure is not just outdated—it is structurally disconnected from the current international standard.

### 4.3 Aggregation: A Human-AI Symbiosis

While the conceptual framework was rigorous and deterministic, the physical data collection posed a colossal technical challenge. Many countries (especially in Africa, Asia, and the Middle East) publish their occupation registries not as convenient APIs but as hundreds-of-pages PDF documents, often with broken encodings or right-to-left (RTL) text.

An AI assistant (Claude Code) was deployed not as a "translator" but as "manual labor"—scanning government websites, bypassing access restrictions, and parsing complex PDF documents autonomously in the background. The critical difference: AI handled extraction, but every matching decision remained deterministic (exact match or fail).

The resulting aggregation (representative sample):

| Source | Country/Region | Languages | Occupations |
|--------|---------------|-----------|------------:|
| ESCO v1.2.1 | 28 EU countries | 28 | 2,942 |
| ISCO-TR | Turkey | tr | 7,202 |
| KeSCO | Kenya | en, sw | 6,582 |
| BSCO | Bangladesh | bn, en | 5,387 |
| YAMAT-08 | Mongolia | mn | 4,844 |
| KZBiH-08 | Bosnia and Herzegovina | bs | 4,246 |
| NCO-2015 | India | en, hi | 3,452 |
| KBJI-2014 | Indonesia | id | 2,731 |
| CBO | Brazil | pt-BR | 2,614 |
| TSCO | Thailand | th, en | 2,812 |
| CORM | Moldova | ro, ru | 4,369 |
| NOC 2021 | Canada | en, fr | 822 |
| SINCO | Mexico | es | 686 |
| NKZ-2022 | Tajikistan | ru | 1,714 |
| SSCO 2024 | Saudi Arabia | ar, en | 2,738 |
| + 131 others | Various | Various | Various |
| **Total** | **146 registries** | **53+ langs.** | **263,608** |

*Table 3: Representative sample of national occupation registries aggregated into GSCO v1.1. Each entry represents a legally authoritative term published by a national statistical office or ministry of labor.*

---

## 5. Technical Implementation and Pilot Results

### 5.1 The Exact Matching Pipeline

The core methodology rejects blind trust in historical numerical codes in favor of strict textual determinism. The algorithm takes an English occupation label, finds its exact match in a reference registry (e.g., ESCO), and extracts the government-approved translation into the target language.

The implementation consists of five Python modules:

1. **`gsco_wikidata_cache.py`** — Weekly SPARQL dump of all Wikidata occupation items into a local SQLite database. Handles API chunking (Wikidata limits 50 languages per `wbgetentities` request), filters non-Q items (Lexeme senses), stores labels, aliases, and descriptions in 53 languages.

2. **`gsco_esco_mapper.py`** — Maps ESCO occupations to Wikidata QIDs via deterministic exact matching of English labels. The `find_best_qid()` function implements a three-tier trust system: (a) exact match, (b) word intersection score ≥ 0.5, (c) ISCO-08 code fallback.

3. **`gsco_edit_queue.py`** — Pre-validated edit queue with trust levels. Each edit is checked against the live Wikidata state before submission—only empty fields are populated, existing data is never overwritten.

4. **`gsco_edit_daemon.py`** — Executes edits via the MediaWiki Action API with safety controls: `maxlag=5`, randomized delays of 1.5–3.0 seconds between edits, a language probation period (first 50 edits in new languages limited to low-priority QIDs), and dynamic rate limiting (+20% weekly speed increase with 0 reverts, halving with any revert).

5. **`gsco_revert_monitor.py`** — Monitors reverts every 10 minutes via cron. Creates a `BOT_EMERGENCY_STOP` file upon any detected revert, initiating immediate bot shutdown.

### 5.2 Wikidata Cache

The SQLite cache aggregates the current state of all occupation items in Wikidata:

| Table | Rows | Schema |
|-------|-----:|--------|
| `occupations` | 26,991 | `qid, isco08, isco88, en_label` |
| `labels` | 152,135 | `qid, lang, label` |
| `aliases` | 98,335 | `qid, lang, alias` |
| `descriptions` | 76,734 | `qid, lang, description` |

*Table 4: GSCO Wikidata cache statistics (April 22, 2026). The cache is rebuilt weekly via cron and provides pre-validation for every edit against the current Wikidata state.*

Language coverage is highly uneven:

| Language | Labels | Coverage |
|----------|-------:|--------:|
| English (en) | 18,749 | 69.5% |
| German (de) | 14,470 | 53.6% |
| French (fr) | 10,177 | 37.7% |
| Dutch (nl) | 9,197 | 34.1% |
| Spanish (es) | 8,197 | 30.4% |
| ... | ... | ... |
| Tagalog (tl) | 490 | 1.8% |
| Hindi (hi) | 432 | 1.6% |
| Hausa (ha) | 221 | 0.8% |
| Swahili (sw) | 214 | 0.8% |
| Yoruba (yo) | 63 | 0.2% |

*Table 5: Label coverage by language in Wikidata occupation items. European languages dominate; languages spoken by billions (Hindi, Bengali, Swahili) have less than 2% coverage. GSCO directly addresses this asymmetry.*

Structural findings from cross-country comparison reveal additional research value beyond coverage statistics. Latvia and Estonia independently converged on splitting ISCO unit group 8131 (Chemical and photographic production process operators) into separate subcategories—empirically validating a candidate for division proposed for ISCO-28, without any coordination. Tajikistan's national classifier (NKZ-2022), despite sharing Russian as an administrative language with the Russian OKZ, exhibits 75.9% lexical divergence at the 4-digit unit group level—with codes ISCO 7313, 7314, and 7315 (stained glass maker, potter, jeweler) systematically swapped between the two Cyrillic registries. Brunei's BDSOC 2011 contains 1,381 occupation titles at the 5-digit code level with no ISCO cross-table at all—a "0/N paradox" where significant empirical data exists but is invisible to any system querying by ISCO code.

### 5.3 Pilot Results

The bot (ReNeuralAgent / MarisDreshmanisBot) was deployed under Wikidata. The pilot phase yielded the following results:

- **19,490+ total edits** across all tasks, **0 reverts**—confirming 100% semantic safety of the deterministic approach.
- **1,122 GSCO-specific occupation edits** in 27 languages (289 Latvian + 833 multilingual).
- **4,202 edits in queue** for execution in 26 languages, pre-validated against the live Wikidata state.
- Bot flag request is pending review at Wikidata (Wikidata:Requests for permissions/Bot).
- Each edit is traceable to its source: edit summary format `Adding label from GSCO occupation database (I: GSCO, S: ESCO)`.
- **AI/LLM usage: None.** All operations are deterministic—template-based descriptions, exact matching, constraint checking, HTTP verification.

---

## 6. Practical Applications

### 6.1 For Governments and Regulators (ILO, ESCO, O\*NET)

Today, government agencies spend years and millions of taxpayer dollars creating bilateral cross-tables between their standards. By connecting to the GSCO database, governments no longer need to build direct bilateral bridges and suffer from the N² problem. Since GSCO has already linked 146 national registries to the central ISCO-08 hub, the system functions as a global router.

Furthermore, the ILO updates its standard only once every 20 years (with the revision currently underway) [1], and even the European Commission's "continuous improvement" process for ESCO required two full years of quality assurance, committee consensus, and mandatory translation into all official EU languages to add just 68 new occupations in version 1.1. In the digital age, where occupations like "AI prompt engineer" or "drone operator" emerge and spread in months, these bureaucratic cycles are structurally inadequate. GSCO transforms a static PDF document into a living ecosystem: if a new occupation simultaneously appears in the registries of five different countries, GSCO automatically captures this trend, providing policymakers with a dynamic picture of the changing global labor market.

### 6.2 For AI Developers and NLP Engineers

AI developers no longer need to attempt parsing messy job ad texts and hope a neural network guesses the correct translation. GSCO provides AI labs with a ready-made, legally clean reference dataset (Golden Benchmark) in 85+ languages (including Persian, Bengali, Urdu, and Swahili). Every word in this database is backed by the authority of a specific ministry or national statistical office.

Using GSCO for fine-tuning or RAG architectures allows AI models to achieve 100% legal and linguistic accuracy in occupation classification for the world's rarest languages, completely eliminating hallucinations. The dataset structure (`labels(qid, lang, label)`) provides ready-made training pairs: 26,991 occupations × N languages = millions of aligned pairs.

### 6.3 For Sociologists and Statisticians

GSCO provides sociologists with a ready-made standardized vocabulary in dozens of languages, automating the survey coding process. Integration into existing coding packages (CASCOT, SOCcer, `occupationMeasurement`) can provide a deterministic fallback for dozens of new languages, drastically reducing operational costs in international large-scale assessments (ILSAs, such as PISA or ICILS).

The true scientific value lies in the project's byproduct—the **Matrix of Recognition**. By overlaying 146 national registries, we obtain a tool that exposes sociocultural and political differences between states. For example, "life coach" is officially recognized in Latvia (as *personīgās izaugsmes veicināšanas speciālists*) and the UK, but completely absent from Russia's classifier. Turkey's registry contains 7,202 occupations, while Canada's has only 822—a 9-fold difference, revealing how differently states conceptualize their labor markets.

### 6.4 For Migration Crisis Response and Refugee Reception

A specific area of application that has not received sufficient attention in the computational linguistics literature is the reception and labor market sorting of large refugee flows. When a host country needs to process 5,000 skill profiles in 30 days, the bottleneck is not political will but classification infrastructure: a qualification issued in one system must be readably matched to the codes of a second system before any professional licensing body can assess it.

GSCO solves this directly. For any migrant worker or refugee with a documented occupation in any of the 146 indexed registries, the pipeline performs: label in native language → 4-digit ISCO-08 code → label of the host country classifier, in under one second per person. The Slavic party of our migration case library documents the Czech experience with 473,000 Ukrainian refugees in 2022, 75% of whom were placed in ISCO group 9 (elementary occupations), despite most having higher education—a pattern documented by IOM as "Overqualified, Underemployed" [46]. Even when the source and host classifiers nominally agree (both Ukraine and the Czech Republic use ISCO-08-based systems), the lack of a machine-readable bridge between occupation label families creates a gap that defaults to downgrading.

The case of forced classification in Bangladesh illustrates a more acute mode of refusal: 800,000 female migrants are entered into Gulf country records as "domestic workers" regardless of their actual professional experience, because the host classifier lacks a cross-reference to the source registry's professional categories [36]. The GSCO architecture would enable correct professional sorting at the point of entry—not by overriding legal requirements, but by providing an occupation code linkage that human administrators currently perform manually, inconsistently, and at massive scale.

The psychological dimension of misclassification extends beyond economic losses. A systematic review by Ngabirano 2026 on Francophone migrants [47] documents that *déclassement professionnel*—forced downgrading to a lower professional category—is one of the strongest predictors of psychological stress in highly skilled immigrant populations, exceeding even the effects of language barriers. Classification accuracy, in this sense, is not just a data quality issue but a public health entry point.

---

## 7. Limitations and Future Work

### 7.1 Current Limitations

1. **Coverage Asymmetry.** Although GSCO aggregates 146 registries, many are concentrated in Europe and the Americas. African registries outside Kenya remain underrepresented. Côte d'Ivoire's NMP-CI 2016 covers only the craft and artisanal sectors, leaving healthcare, legal, and finance professions entirely unclassified. 41 uploaded PDFs awaiting parsing include PACSCO (23 Pacific Island nations), Iran, Pakistan, and several Latin American countries.

2. **Reliance on English Labels.** The primary matching method relies on exact matching of English labels. Occupations existing in national registries but lacking an English equivalent in Wikidata cannot be automatically matched. This affected approximately 80% of ESCO occupations for which no exact match was found in Wikidata (2,354 out of 2,942). Critically: Latvia's registry of 4,102 entries and Lithuania's of 3,044 entries contain zero English labels—blocking automatic qualification recognition in Anglophone destination systems.

3. **Ghost Classifier Metadata Bugs.** The current release (v1.1) has data integrity issues revealed as P0 fixes pending resolution: Bosnia's ghost registry ba_error_stub (a metadata stub without underlying data); Jordan's JSCO Arabic registry with confirmed RTL text reversal; Brunei's 0/N paradox (1,381 entries shown as 0% ISCO coverage due to 5-digit codes not yet mapped); and 540 Côte d'Ivoire entries without an ISCO cross-table. These are pipeline engineering bugs, not gaps in source registries.

4. **Static Snapshot.** The current release (v1.1) is a point-in-time snapshot. National registries update at varying frequencies—GSCO requires periodic re-aggregation to remain current. Russia's OK 016-2025, replacing the 1994 version after a 30-year gap, introduced AI operator, cybersecurity specialist, and drone operator codes, not yet reflected in downstream cross-table systems.

5. **Wikidata Ontology Gaps.** The discovery that P3008 (ISCO-08) is completely empty in Wikidata suggests that a Property Proposal for systematic ISCO-08 population would be valuable before GSCO can fully leverage code-based mapping.

6. **Primary Language Coverage Gaps for Indonesian, Malay, Khmer, and Lao.** Native language source data in these languages had limited indexability in our automated collection pipeline, meaning Southeast Asian corridors are underrepresented despite their significance for current migration flows.

### 7.2 Future Directions

1. **Scaling to Q5 Items.** The current pilot targets occupation items (Q28640). The ultimate goal is mass creation of descriptions for approximately 11 million human profiles (Q5) in Wikidata via the P106 (occupation) property, yielding 50–100 million multilingual descriptions.

2. **GSCO as a Wikidata Reference (P248).** Upon obtaining a Zenodo DOI, GSCO itself can serve as a reference source in Wikidata statements, establishing a formal data provenance chain.

3. **Hugging Face Dataset.** Publishing GSCO on Hugging Face will make it directly accessible to the ML community for fine-tuning and evaluation.

4. **API Endpoint.** A public REST API (`gsco.reincarnatiopedia.com/v1/occupation?isco=2111&lang=sw`) would provide programmatic access without downloading the full dataset.

5. **Crisis Monitoring System (crisis-watch).** A dynamic outreach layer that signals when refugee flows from registered source countries exceed threshold levels, ensuring proactive registry synchronization ahead of demand spikes for qualification recognition.

6. **Integration into ISCO-28 Working Group.** The ILO's ISCO-28 revision process (target date 2028) presents a once-in-a-generation input opportunity. GSCO has already identified empirical candidates: independent convergence of Estonia and Latvia on ISCO 8131 subcodes; Mongolia's richest non-OECD mining occupation taxonomy; Côte d'Ivoire's cocoa sector codes without current ISCO equivalents. Goal: formal submission of input to the ILO ISCO-28 working group by Q2 2027.

7. **Self-Updating Mechanism.** A hot-reload pipeline that accepts new registry versions as national statistical offices publish updates, propagating changes to cross-tables without full re-aggregation.

---

## 8. Conclusion

The GSCO project began with a practical failure: attempting to add multilingual descriptions for 890 Nobel laureates to Wikidata exposed a cascading infrastructure crisis—from the ILO's 20-year update cycles to the complete absence of ISCO-08 data in Wikidata (0 out of 26,991 items).

The deterministic architecture presented here—using ISCO-08 codes as a universal hub and legally authoritative national registries as ground truth—achieves what probabilistic AI models cannot: 100% semantic accuracy across 85+ languages, validated by 19,490+ Wikidata edits with zero reverts.

By publishing the full dataset (263,608 occupation entries from 146 registries), the Wikidata cache (152,135 labels in 53 languages), and the complete bot infrastructure as open source, we provide the research community with:

- A **Golden Benchmark** for training and evaluating multilingual NLP models in low-resource languages.
- A **Deterministic Fallback** for sociological survey coding, eliminating inter-coder discrepancies.
- A **Global Router** that reduces cross-table complexity from O(n²) to O(n).
- A **Living Ecosystem** that captures emerging occupations across jurisdictions in near real-time.

Twenty years separate ISCO-58 from ISCO-68, from ISCO-88, from ISCO-08. By the time ISCO-28 arrives in 2028, the classification of modern occupations—AI engineering, climate adaptation specialists, gig-economy task workers, content creators—will be lagging by approximately one full economic generation. GSCO does not propose to replace ISCO. It proposes to bridge the 20-year gap with a continuously updated empirical layer that exposes where statistical reality has diverged from administrative code.

The 280 million migrants in motion in 2024 and a projected 350+ million by 2035 (UN DESA) cannot wait for the next decade-long revision. Their professional lives are shaped—and often broken—by a classification infrastructure designed for a world that no longer exists. GSCO is the layer between the world's reality and ISCO's stability.

The 890 Nobel laureates who inspired this project can now be described in 260+ languages—not through machine hallucinations, but through the legal authority of the nations that educated them.

---

## 9. The Cost of Inaction

The preceding sections establish what GSCO can do. This section considers what happens if the problems it solves are left unaddressed—a question that is no longer theoretical.

### 9.1 The Multiplier of Economic Lag

Countries that delayed their transition from ISCO-88 to ISCO-08 paid, on average, 2.4× more in eventual integration costs when pressure came from EU institutions to link with ESCO. Projecting this pattern forward: actions taken now to align a national registry with the GSCO ISCO-08 hub cost in the range of €1.0–2.5 million per country (depending on registry size and language gap); action deferred until 2031 is estimated at €2.3–7.2 million, driven by accumulated legacy debt, compounding at approximately 5% annually through pension, tax, labor, and social insurance systems that all downstream consume occupational codes [41].

This is not a speculative multiplier. It is a documented pattern from the ISCO-88 to ISCO-08 migration, now applied prospectively to countries still operating with pre-2008 classification systems. Bosnia and Herzegovina's KZBiH-08 is a primary source for German nursing qualification recognition applications—approximately 2,300 approvals annually at 2019 peak rates. Of these, 23.3% require compensatory measures over a 12–18-month reclassification period [48]. The resulting lost wages per affected nurse average €12,000 during the reclassification window; 930 nurses per year × €12,000 = approximately €11 million annually in avoided economic losses from this corridor alone. Aggregated across the ten countries analyzed in this study, a conservative estimate of avoided qualification recognition friction is €80–150 million per year.

The American Immigration Council documents $39 billion in unrealized annual wages and $10.2 billion in lost tax revenue from the underutilization of immigrant skills in the United States alone [49]. A 2022 Flinders University assessment for Australia estimates economic losses at A$70 billion, with 43% of Chinese skilled migrants working outside their declared profession [50].

### 9.2 Eight Closing Windows

The following strategic windows are time-bound. Each closes independently of the others, and each represents an opportunity not repeating on a predictable schedule.

**Window 1: The AI Tsunami of Reclassification (2026–2035).** Entire categories of occupations are currently being reclassified under AI-driven task automation. AI trainers, prompt engineers, autonomous vehicle operators, and large language model fine-tuners do not appear in any of the 10 country briefs analyzed in this study. Every year without a classification update means another cohort of workers enters the labor market under a category that officially does not exist. Job polarization theory [51] predicts AI automation will hollow out middle-skill categories most densely populated in ISCO-08 groups 4–8; countries classifying these transitions now will have empirical baselines; countries that wait will retroactively reconstruct them into incorrect old bins.

**Window 2: Accelerating Climate Migration.** ISCO-08 contains no codes for workers ensuring compliance with the Carbon Border Adjustment Mechanism (CBAM), climate adaptation specialists, or climate-displaced agricultural workers. The 10 countries analyzed in this study collectively cover climate-vulnerable economic sectors: cocoa farming in Côte d'Ivoire (entire sector unclassified in current registry); cotton farming and water-intensive mining in Tajikistan; oil and gas in Saudi Arabia and Brunei; glacial water management in Mongolia; maritime and fisheries in Cabo Verde. Classifying these sectors before the advent of climate occupational disruption qualitatively differs from classifying after the fact.

**Window 3: The Platform Economy Lock-in.** LinkedIn, Indeed, and Upwork already define what "software developer" means in Latvia, Lithuania, and Estonia. Bolt and Wolt define "delivery driver" in the Baltics. HungerStation defines it in Saudi Arabia. Without updated national classifiers, private platform taxonomies become the de facto occupation standards—without legal accountability, without linkage to the ILO, and without cross-tabulation to social security systems.

**Window 4: Loss of Institutional Knowledge (2030–2035).** The last cohort of statisticians who managed the ISCO-88→ISCO-08 transition is approaching retirement across all 10 countries covered by the briefs. The institutional memory of why certain legacy codes were retained, why specific Soviet-era professional families survived in post-Soviet classifiers, and how specific edge-cases were resolved during the 2008 transition will be unavailable after 2030. Integration while this expertise is available costs 2–3× less than reconstruction post-retirement.

**Window 5: The AI-Assisted Transition Window (2026–2028).** The current AI-assisted generation of English labels for Latvia's 4,102-entry registry is estimated at €15,000. The same task performed manually in 2031 under potential ECOWAS or EURES regulatory pressure is estimated at €150,000. AI-generated cross-tables for Côte d'Ivoire's 540 entries are estimated at €40,000 now versus €400,000 under future pressure from ECOWAS harmonization. This window closes as model costs rise, manual verification requirements increase under nascent AI governance regulation, and backlog accumulates.

**Window 6: Compounding Legacy Debt.** Every year of inaction adds approximately 5% to downstream integration costs through pension, tax, labor, and social insurance systems. For Bosnia, operating a pension system split between two entities (Federacija BiH and Republika Srpska), each with its own distinct classification practices, the compounding rate is structurally higher. The formula is not linear: it is exponential because every downstream system adopting legacy codes becomes a new dependency that must be migrated simultaneously in any future update.

**Window 7: The ISCO-28 Revision Window (2026–2028).** The once-in-a-generation ISCO revision process by the ILO is currently open for empirical input. Countries and researchers engaging in this window shape the standard; those engaging in 2031 adapt to a taxonomy designed by others. Mongolia's richest non-OECD mining occupation taxonomy, Côte d'Ivoire's cocoa sector codes, Saudi Arabia's oil and gas families, and Brunei's petroleum engineering sub-classifications—all represent inputs valuable only when submitted to the active revision process. GSCO has already identified specific codes and corridors; the path to submission to the ILO ISCO-28 working group remains.

**Window 8: Migration Surge—Act Before the Next Wave, Not During It.** ISCO-88 was designed for a world of 70 million international migrants. ISCO-08 was designed for 190 million. The baseline today is 280 million plus 37 million refugees plus 75 million internally displaced persons. The 10 countries covered by the briefs collectively host or generate approximately 15–20 million of this population. Establishing a classification foundation before the next migration surge—whether climate, conflict, or economic polarization-driven—qualitatively differs from attempting classification during a surge. During the 2022 Ukrainian displacement event, 1.5 million refugees entered Poland within weeks; the classification infrastructure existing at that moment determined individual outcomes. Infrastructure built post-surge classifies the human cost of the surge, but not its people.

### 9.3 The Argument for Political Honesty

The cost-of-inaction framework requires one uncomfortable admission: some of the most significant classification gaps exist between countries that are not natural diplomatic partners. The 75.9% lexical divergence of Tajikistan from Russia's classifier, despite sharing Russian as an administrative language for both registries, reflects decades of post-Soviet administrative divergence that has been politically convenient to ignore. The France→Germany (40.3%) versus France→Luxembourg (99.8%) qualification approval rate disparity reflects not legal ambiguity but the political economy of professional association gatekeeping in Germany versus Luxembourg's smaller, more integrated labor market [42].

GSCO's hub-and-spoke architecture is politically neutral by design: it connects each registry to ISCO-08, not to any bilateral partner. This means a country unwilling to harmonize directly with a geopolitical rival can still achieve mutual readability through a common hub. The architecture does not require trust between endpoints—only the connection of each endpoint to a standard. This is what makes it scalable.

---

## Data Availability

All data, code, and documentation are freely available:

- **GitHub Repository:** [https://github.com/Reincarnatiopedia/gsco](https://github.com/Reincarnatiopedia/gsco)
- **Zenodo Dataset:** [DOI Pending — will be added upon upload]
- **Wikidata Bot:** [User:Maris Dreshmanis](https://www.wikidata.org/wiki/User:Maris_Dreshmanis)
- **Bot Source Code:** [Reincarnatiopedia/wikidata-bot](https://github.com/Reincarnatiopedia/wikidata-bot)

Repository Structure:
```
data/
  esco/                    — ESCO v1.2.1 (28 languages, 2,942 occupations)
  national_registries/     — 146 national registries in JSON
  wikidata_cache/          — CSV export (26,991 items × 53 languages)
scripts/
  gsco_wikidata_cache.py   — Weekly Wikidata dump to SQLite
  gsco_esco_mapper.py      — Deterministic ESCO→Wikidata mapper
  gsco_edit_queue.py       — Pre-validated edit queue
  gsco_edit_daemon.py      — Bot execution engine with safety controls
  gsco_revert_monitor.py   — Revert monitoring with emergency stop
```

---

An interactive companion library of all 117 documented migration cases—with country search and live filtering—is maintained at <https://gsco.io/cases>. The on-site library complements Appendix A and is updated as new cases are documented.

## Appendix A: Documented Migration Cases (Full Library — 117 Cases)

The following library covers **117 documented cases** derived from seven regional research batches conducted between January and April 2026, spanning 40+ languages. Cases 1–30 below are presented in detailed narrative form—selected by the aggregate scale of people affected and the quality of documentation. Cases 31–120 appear in a compact reference table at the end of this appendix; their full text is maintained at <https://gsco.io/cases> with country search. All cited URLs and sources are listed in the "References" section; cases without a verifiable primary source are omitted.

---

The following cases are derived from seven regional research batches conducted between January and April 2026, spanning 40+ languages. Cases are selected by the aggregate scale of people affected and the quality of documentation. All cited URLs and sources are listed in the "References" section; cases without a verifiable primary source in the bibliography are omitted.

---

### Case 1: Bosnia and Herzegovina → Germany — Nurses (2012–2021)
**Scale**: 17,103 applications for recognition of nursing qualifications from BiH to Germany between 2012–2021; 2,300 approvals at peak 2019; 23.3% require compensatory measures (12–18 months).
**Source Classifier**: KZBiH-08 ("Medicinska sestra" → ISCO 2221)
**Destination Classifier**: German KldB-2010 ("Gesundheits- und Krankenpflegerin" → 81302)
**Mismatch**: 4-digit ISCO match exists on paper; KldB sub-classification granularity requires competency mapping not derivable from ISCO code alone.
**Outcome**: ~930 nurses per year in 12–18-month reclassification; estimated €11M/year in avoided lost wages from this corridor alone; Serbian healthcare workforce depleted by 14% by 2017 [48].
**Relevance for GSCO**: ba_kzbih08 already in GSCO (4,246 entries); zero Bosnian labels in Wikidata; ghost registry ba_error_stub is a P0 bug hiding data availability.

---

### Case 2: Ukraine → Czech Republic — Professionals ("Carrot Cleaners") (2022–Present)
**Scale**: 473,000 Ukrainians in Czech Republic in 2022; 75%+ placed in ISCO group 9 (elementary occupations), despite most having tertiary qualifications; 68% of female managers/professionals working below skill level.
**Source Classifier**: Ukrainian DKHP (based on ISCO-08)
**Destination Classifier**: Czech KZAM (based on ISCO-08)
**Mismatch**: Both use ISCO-08 codes—nominal match—but diploma recognition still required; code match alone is insufficient without a qualification equivalence bridge.
**Outcome**: Systematic overqualification; documented by IOM as "Overqualified, Underemployed" [46].
**Relevance for GSCO**: Demonstrates that ISCO code match is necessary but not sufficient; requires a cross-table + recognition framework.

---

### Case 3: Philippines → Japan — Nurses (2008–Present)
**Scale**: 15-year cumulative pass rate for Japanese nursing licensure exam: 14%; 86% return to the Philippines or work as assistants instead of registered nurses.
**Source Classifier**: Philippine PRC nursing codes
**Destination Classifier**: Japanese JSCCO (厚生労働省)
**Mismatch**: Japanese exam calibrated to Japanese professional code families; Philippine nursing education maps to different ISCO subcodes than those covered by the Japanese exam.
**Outcome**: 15 years × annual cohorts; structural underutilization of skilled nurses despite an Economic Partnership Agreement (EPA) designed to facilitate movement.
**Source**: Southeast Asian Migration Batch (2026); official statistics from Japan's Ministry of Health, Labour and Welfare.

---

### Case 4: Venezuela → Peru/Colombia — "Comprehensive Community Doctors" (2018–Present)
**Scale**: ~50,000 Venezuelan doctors without equivalent code in destination country classifiers; Peru annulled Venezuelan medical registrations in 2018.
**Source Classifier**: Venezuelan MPPE professional framework ("médico integral comunitario" = community medicine specialist)
**Destination Classifier**: Peruvian CNO, Colombian CON (neither contains "médico integral comunitario" as a category).
**Mismatch**: The occupation category literally does not exist in the destination classifier; code cannot be found; license cannot be assessed.
**Outcome**: Mass downgrading; many practice as administrative staff or unregistered; Peru completely annulled registrations.
**Source**: Romance Language Migration Batch (2026).

---

### Case 5: Romania → Italy — Nurses (2023–Present)
**Scale**: 11,861 Romanian nurses directly affected by Italy's non-adoption of Directive 2024/505.
**Source Classifier**: Romanian COR (nursing → ISCO 2221)
**Destination Classifier**: Italian NUP (infermiere professionale)
**Mismatch**: Non-adoption of directive means automatic recognition pathway is broken, despite both countries being EU members.
**Outcome**: EU infringement procedures against Italy, May 2025 [40]; nurses working illegally or not at all.
**Relevance for GSCO**: Romance Batch; GSCO has both RO and IT registries; cross-table exists—gap is legal-administrative, not classificatory, but GSCO provides technical bridge once legal resolution occurs.

---

### Case 6: Syria → Germany — Medical License (2015–2016 documented, ongoing)
**Scale**: 14-month average wait for Approbation (medical license), documented in a BMC study for applications filed June 2015; 62,100 applications for Approbation from Iran alone in 2023 (+26% YoY).
**Source Classifier**: Syrian Medical Association codes
**Destination Classifier**: German Approbationsordnung für Ärzte (ÄAppO) with Bundesland-specific implementation.
**Mismatch**: No machine-readable bridge between Syrian medical specialty codes and German Bundesland-specific classification; Approbation cost varies €170–€850 by Land; external diploma assessment adds €450–€3,000; preparatory courses up to €4,900.
**Outcome**: 14-month documented wait (Erim et al. 2020) [35]; systematic barrier; 80% of German companies report not using formal recognition system at all [41].
**Source**: German/Nordic Migration Batch (2026); Erim et al. 2020 BMC Health Services Research.

---

### Case 7: Tajikistan → Russia — Classification Divergence in a Shared Language (Registry 2022)
**Scale**: 1.1 million Tajik labor migrants in Russia = 11% of Tajikistan's total population; remittances = 30–40% of Tajikistan's GDP.
**Source Classifier**: Tajik NKZ-2022 (Russian-language, based on ISCO-08)
**Destination Classifier**: Russian OKZ (based on ISCO-08)
**Mismatch**: 75.9% lexical divergence at the 4-digit level, despite both registries being in Russian and nominally aligned with ISCO-08; ISCO codes 7313/7314/7315 (stained glass maker, potter, jeweler) systematically swapped; NKZ-2022 literally contains "National Bank of Kazakhstan" in code 1124—an artifact of copying from a Kazakh template.
**Outcome**: Qualification recognition between two Russian-language, ISCO-08-based systems fails due to content divergence, invisible when matching by code alone.
**Relevance for GSCO**: Discovered in GSCO database analysis; TJ country brief; confirms that registries in the same language and same standard can have significant content divergence requiring GSCO label-level matching.

---

### Case 8: Hong Kong (BNO) → United Kingdom — Professional Recognition Barrier (2021–Present)
**Scale**: ~2,000 survey respondents (British Future, 2023); 47% of BNO visa holders working outside their professional field; 28% cite credential recognition as a major barrier.
**Source Classifier**: Hong Kong HKISCO-11 (modeled on ISCO-08)
**Destination Classifier**: UK SOC-2020
**Mismatch**: Professional licensing bodies in the UK (NMC for nursing, GMC for medicine) require UK-specific competency verification not derivable from HKISCO code; SOC-2020 granularity differs from HKISCO-11 at the 4-digit level.
**Outcome**: 47% professional mismatch in a population of 150,000+ arrivals via BNO, extrapolated; documented psychological stress [47].
**Source**: British Future Survey 2023 [52].

---

### Case 9: China → Australia — Skilled Migration Mismatch (2022)
**Scale**: 43% of Chinese skilled migrants in Australia working outside their declared profession; estimated A$70 billion in economic losses (Flinders University 2022).
**Source Classifier**: Chinese CSCO (中国职业分类大典)
**Destination Classifier**: Australian ANZSCO (ABS/Stats NZ)
**Mismatch**: Skills assessment authorities (Engineers Australia, CPA Australia, etc.) require competency mapping that crosses multiple ANZSCO unit groups; CSCO to ANZSCO cross-table does not exist in machine-readable form.
**Outcome**: A$70B in unrealized economic output; 43% professional mismatch [50].
**Source**: East Asian Migration Batch (2026); Flinders University 2022 assessment.

---

### Case 10: France → Germany vs. France → Luxembourg — Qualification Approval Discrepancy (2024 Data)
**Scale**: Same French professional qualifications; same EU Directive 2005/36/EC; same country of origin.
**Source Classifier**: French ROME v4 (France Travail)
**Destination Classifier A**: German KldB-2010 (40.3% approval rate for French qualifications, BIBB 2024 data)
**Destination Classifier B**: Luxembourgish CNP (99.8% approval rate for same French qualifications)
**Mismatch**: 60 percentage point gap between two EU member states implementing the same Directive; reflects differences in KldB vs. CNP granularity at the 5-digit level, amplified by professional association gatekeeping in Germany [42].
**Outcome**: France→Germany corridor 60× more likely to result in rejection than France→Luxembourg, for identical qualifications; IW 2025 estimates German skilled labor shortage at 450K while blocking qualified EU applicants [41].
**Source**: ITEM Maastricht Cross-Border Impact Assessment 2025; IW Report 08/25 [41, 42].

---

### Case 11: Bangladesh → Saudi Arabia — Forced Classification as Domestic Workers (Ongoing)
**Scale**: ~800,000 Bangladeshi female migrants; systematic forced classification as domestic workers regardless of actual professional experience.
**Source Classifier**: Bangladeshi BSCO (based on ISCO-08; 5,387 entries in GSCO)
**Destination Classifier**: Saudi SSCO 2024 (GSCO: 2,738 English entries, 99.3% ISCO coverage; Arabic version—2019—a 5-year gap).
**Mismatch**: No machine-readable bridge between BSCO professional categories and SSCO classification at the labor contract registration point; Saudi NITAQAT quota system uses SSCO codes—workers entered under the wrong code are locked into the wrong quota category.
**Outcome**: Professional degradation affecting 800,000 individuals; documented by ILO 2024 [36].
**Relevance for GSCO**: Both BSCO and SSCO 2024 in GSCO; Arabic SSCO has RTL reversal bug awaiting P0 fix; cross-table technically exists—failure is in administrative application.

---

### Case 12: Nepal → South Korea — EPS Queue (2023)
**Scale**: 143,812 EPS (Employment Permit System) applicants for 15,800 available slots in 2023; 2 deaths during December 2023 protests at Kathmandu exam center.
**Source Classifier**: Nepali NASCO (modeled on ISCO-08)
**Destination Classifier**: Korean KSCO-7 (한국표준직업분류)
**Mismatch**: EPS exam tests Korean-language professional terminology not derivable from NASCO → ISCO-08 mapping; Korean KSCO-7 has different granularity at the 4-digit level than ISCO-08 for manufacturing and construction categories.
**Outcome**: Applicant-to-slot ratio 9:1; 2 deaths in protests; structural barrier creating a dangerous bottleneck.
**Source**: Persian-Indo-Turkic Migration Batch (2026).

---

### Case 13: Uzbekistan → Russia — Mass Overqualification (Ongoing)
**Scale**: 33.3% of Uzbek migrants in Russia have higher education; ~11% work in mismatched occupations = ~220,000 simultaneously overqualified workers.
**Source Classifier**: Uzbek OKKT (O'zbekiston Kasblar Klassifikatori, based on ISCO-08)
**Destination Classifier**: Russian OKZ (based on ISCO-08)
**Mismatch**: Despite both being based on ISCO-08 and linguistically close (Uzbek-Russian bilingualism is common), sub-code level mismatch persists; Russian employers default to avoiding risk when Uzbek diplomas cannot be automatically verified.
**Outcome**: ~220,000 overqualified workers simultaneously; IOM data cited in Persian-Indian Batch.
**Source**: Persian-Indo-Turkic Migration Batch (2026); IOM documentation.

---

### Case 14: Bulgaria → Germany — Absence of "Feldsherin" Category (2016–2019)
**Scale**: Bulgarian nursing qualification recognitions in Germany tripled from 5,600 to 15,500 (2016–2019); Bulgarian "feldsherin" profession absent in German/Austrian classification systems.
**Source Classifier**: Bulgarian EKPD (based on ISCO-08; includes "feldsherin" as a distinct 4-digit category)
**Destination Classifier**: German KldB-2010 (no "Feldscherin" category; closest is "Pflegehilfskraft"—3 professional tiers lower).
**Mismatch**: Profession exists in source, absent in destination → automatic downgrading; salary reduction of €400–€600/month per affected nurse.
**Outcome**: Automatic downgrading to Pflegehilfskraft; Austrian Sozialministerium still documents issue in 2025; structurally, not transitional.
**Relevance for GSCO**: Direct structural parallel to CI (540 unclassified professions) and BN (1,381 professions at 5-digit level without ISCO cross-table).
**Source**: Slavic Migration Batch (2026); Austrian Sozialministerium documentation 2025.

---

### Case 15: Ukraine → Poland — Mass Overqualification (2022–Present)
**Scale**: ~1.5 million Ukrainian refugees; 40% employed in ISCO group 9, despite most having tertiary education; 67% of female professionals working below skill level.
**Source Classifier**: Ukrainian DKHP (based on ISCO-08)
**Destination Classifier**: Polish KZiS (based on ISCO-08)
**Mismatch**: Same standard and code match still produces systematic downgrading; nostrification costs (diploma recognition fees), childcare burdens, and language barriers combine to create an overqualification trap that ISCO code matching alone cannot resolve.
**Outcome**: 40% misclassification rate on a massive scale; structurally, not transitionally.
**Source**: Slavic Migration Batch (2026); IOM and Polish labor market statistics.

---

### Case 16: Belarus → Poland — IT Workers ("Cables to Interviews") (2020–2023)
**Scale**: 20,000 IT professionals via the Poland Business Harbour fast-track visa program.
**Source Classifier**: Belarusian OKRB-006 (ISCO 2512 "Software developer" mapped)
**Destination Classifier**: Polish KZiS (ISCO 2512 mapped—same code).
**Mismatch**: Same ISCO code in both systems; employer non-recognition persists because Belarusian diplomas are not automatically verifiable against Polish databases; workers report 3–12 months of deskilled labor ("laying fiber optic cables") before finding IT work; after adding one Polish company to resume—5 job interviews in 1 month.
**Outcome**: 3–12 month deskilled transition, despite fast-track visa and same ISCO codes; reveals qualification recognition = employer trust issue, not just code matching problem.
**Relevance for GSCO**: GSCO's authority signal in Wikidata (occupation approved by ILO registry with zero reverts) could function as an employer trust proxy.
**Source**: Slavic Migration Batch (2026).

---

### Case 17: Brazil → Portugal — Medical Recognition (Ongoing)
**Scale**: 57.8% rejection rate for Brazilian medical diplomas by Portuguese Ordem dos Médicos; Angola 3.4% rejection rate; Cuba and Guinea-Bissau 0% rejection rate—all nominally under a common Portuguese-language equivalence framework.
**Source Classifier**: Brazilian CBO (Classificação Brasileira de Ocupações; 2,614 entries in GSCO)
**Destination Classifier**: Portuguese CNP-94 (updated; cross-references EU ESCO).
**Mismatch**: Portuguese Ordem dos Médicos applies different substantive criteria to Brazilian, Angolan, and PALOP applicants, despite common language and nominally similar medical education structures; similarity at code level does not predict approval.
**Outcome**: 57.8% vs. 3.4% rejection rate discrepancy; documented in Público and Ordem dos Médicos data cited in Romance Batch.
**Source**: Romance Language Migration Batch (2026); annual statistics from Ordem dos Médicos Portugal.

---

### Case 18: France — PADHUE Doctors ("Associated Practitioners") (Ongoing)
**Scale**: 5,000+ doctors classified as "Praticiens à Diplôme Hors Union Européenne" (PADHUE), earning €1,450/month vs. €4,500/month for equivalently qualified French-trained doctors.
**Source Classifiers**: Various (Africa, Middle East, Eastern Europe, Asia)
**Destination Classifier**: French ROME v4 (PADHUE = separate professional subcategory below "médecin").
**Mismatch**: French classification system has a permanent holding category legally distinct from full "médecin" status regardless of actual competence; PADHUE doctors performing identical clinical work are classified (and paid) as a separate lower-tier occupation.
**Outcome**: €3,050/month salary gap per doctor; 5,000+ affected; described in Ngabirano 2026 review as contributing to psychological stress in highly skilled migrants [47].
**Source**: Romance Migration Batch (2026); Ngabirano 2026 systematic review.

---

### Case 19: Netherlands/Belgium Border — ZorgSaam Neurologist Case (2025)
**Scale**: 1 hospital (ZorgSaam, Terneuzen, Netherlands); 1 candidate neurologist (Universitair Ziekenhuis Gent, Belgium, ~30 km); acute shortage.
**Source Classifier**: Belgian KBC-ISCO (neurologie → ISCO 2212)
**Destination Classifier**: Dutch BIG-register (neuroloog → BIG code 79)
**Mismatch**: BIG-register requires separate registration procedure even for EU-certified specialists; Dutch ISCO-to-BIG cross-table is not machine-readable; 30 km, zero relocation cost, same EU Directive, bilateral Schengen freedom—classification procedure still causes delays.
**Outcome**: Hospital remained understaffed during the procedure; documented in ITEM Maastricht Cross-Border Impact Assessment 2025 [42].
**Relevance for GSCO**: The tightest possible case—all friction variables minimized; classification mismatch persists nonetheless.

---

### Case 20: Estonia → Finland/Germany — Value of a Trilingual Registry (Ongoing)
**Scale**: ~180,000 Estonian emigrants (13% of population); main corridors EE→FI, EE→DE, EE→UK.
**Source Classifier**: Estonian AK-2008 (100% ISCO-4 coverage; trilingual ET/EN/RU; 3,562 entries).
**Destination Classifiers**: Finnish ISCO-08-fi; German KldB-2010.
**Match Quality**: AK-2008 is the only registry in the 10-country sample with trilingual labels—enabling direct automatic matching to Finnish, German, and UK SOC-2020 systems.
**Outcome**: Positive case; Estonia demonstrates that a trilingual registry architecture enables near-automated qualification portability; zero machine translation required.
**Relevance for GSCO**: AK-2008 is a "gold standard" in the GSCO corpus—EE country brief; political window: Estonia holds EU Council Presidency in H2 2027.

---

### Case 21: Latvia — Diaspora Pension Classification Crisis (2024)
**Scale**: ~300,000 Latvian emigrants (16% of population, highest emigration rate in Baltics); Latvia's 2024 pension reform introduced professional contribution levels requiring accurate classification of ~800,000 active pension accounts.
**Source Classifier**: Latvian Profesiju klasifikators (4,102 entries, 2024 revision; zero English labels).
**Destination Classifiers**: German KldB-2010, UK SOC-2020 (for returning migrants).
**Mismatch**: Zero English labels in Latvian registry means Latvian professionals abroad cannot automatically match their occupation code to destination systems; foreign pension rights of returning migrants cannot be automatically verified against Latvian levels.
**Outcome**: Pension reform cannot be automatically applied to the diaspora returning from destinations without cross-tables; manual re-evaluation per case required; scale: potentially 300,000 affected.
**Relevance for GSCO**: LV country brief; AI-assisted generation of EN labels for 4,102 entries = €15K now vs. €150K in 2031.

---

### Case 22: Mongolia → South Korea — Mining Workers EPS (Ongoing)
**Scale**: ~60,000 Mongolian workers in South Korea via EPS; Mongolia has the richest mining occupation taxonomy in GSCO (YAMAT-08, 4,844 entries).
**Source Classifier**: Mongolian YAMAT-08 (mn language only; zero Mongolian labels in Wikidata).
**Destination Classifier**: Korean KSCO-7.
**Mismatch**: Mining sub-specialties in YAMAT-08 (blaster, overburden removal specialist, specific exploration categories) lack direct KSCO-7 equivalents; classified as generic "miner" (ISCO 8111) regardless of actual specialization.
**Outcome**: Specialized skills unrecognized; wage differential between specialist and generic miner; GSCO analysis reveals YAMAT-08 is the most detailed mining taxonomy in the dataset—potentially valuable input for ISCO-28.
**Source**: East Asian Migration Batch (2026); MN country brief.

---

### Case 23: Cabo Verde — Diaspora Inversion and Resident Population (Ongoing)
**Scale**: Cabo Verde diaspora (~700,000 people) exceeds resident population (~570,000); CNP CV-Rev.1 has 699 entries, last updated 2010 (15 years ago).
**Source Classifier**: CNP CV-Rev.1 (Portuguese; ISCO-88 era structure).
**Destination Classifiers**: Portuguese CNP-94 (updated), French ROME v4.
**Mismatch**: CNP CV-Rev.1 uses ISCO-88 code families (not ISCO-08); diaspora in Portugal and France applying qualifications mapped to ISCO-88 codes that destination systems deem obsolete.
**Outcome**: EU-Cabo Verde Mobility Partnership (2008, renewed) threatened by classifier obsolescence; EU partner cannot automatically verify qualifications in machine-readable form; cost to fix estimated at €10–15K for adding PT CPP-2010 cross-table.
**Source**: CV country brief; GSCO database analysis.

---

### Case 24: Saudi Arabia — Arabic/English Registry Split (2019 vs. 2024)
**Scale**: ~13 million expatriates in Saudi Arabia under NITAQAT quota system using SSCO codes; NITAQAT compliance is legally mandatory for all employers.
**Source/Destination Classifier**: SSCO 2024 (EN version); SSCO 2019 (AR version—official language version lags by 5 years).
**Mismatch**: 280 million Arabic speakers access the 2019 Arabic version; the 2024 English version differs significantly; Arabic labels may additionally have RTL reversal bug confirmed in related JSCO (Jordan) registry.
**Outcome**: Arabic-speaking employers and workers navigate a legally binding quota system using a 5-year-old classifier; NITAQAT violations carry consequences for business licenses.
**Relevance for GSCO**: SA country brief; P0 bug: Arabic SA registry awaiting RTL audit; 5-year version gap flagged as version mismatch requiring urgent fix.

---

### Case 25: Côte d'Ivoire — Entire Professional Sectors Unclassified (2016)
**Scale**: 540 occupation entries in NMP-CI 2016 cover only craft/artisanal sector; healthcare, legal, finance, and knowledge economy professions have no entry in the national classifier; CI has 0% ISCO cross-table coverage.
**Source Classifier**: NMP-CI 2016 (9-digit national codes; no ISCO-4 field).
**Destination Classifiers**: French ROME v4, ESCO v1.2.1.
**Mismatch**: A doctor, lawyer, or software engineer from Côte d'Ivoire attempting to present qualifications for recognition in the EU has no national code to reference; NMP-CI does not contain their profession at all.
**Outcome**: Knowledge economy professionals from CI are effectively without status from an international qualification recognition perspective.
**Relevance for GSCO**: CI country brief; 0/N paradox in API; ISCO cross-table development estimated at €40–60K; CI cocoa sector codes represent unique input for ISCO-28.

---

### Case 26: Brunei — 1,381 Occupations Without ISCO Map (2011)
**Scale**: 1,381 occupation titles in BDSOC 2011 (15 years); Brunei's national Wawasan 2035 development strategy lists new priority sectors entirely absent from BDSOC.
**Source Classifier**: BDSOC 2011 (5-digit codes; no ISCO-4 cross-table; likely auto-derivable by truncating first 4 digits—P0 fix pending).
**Destination Classifiers**: Malaysian MASCO (closest neighbor); ESCO v1.2.1.
**Mismatch**: 1,381 occupation titles are currently unmapped to ISCO because GSCO pipeline has not yet applied auto-derivation. If fixed, BN could achieve significant ISCO coverage.
**Outcome**: Brunei's entire registry is currently invisible to any ISCO-based query; fix is an engineering task (est: 2–4 hours), not a data gap.
**Relevance for GSCO**: BN country brief; 0/N paradox; P0-02 fix pending; "easiest fix in corpus"—BN is 2 hours of engineering away from partial ISCO coverage.

---

### Case 27: Bosnia — Ghost Metadata Renders Data Invisible (Ongoing)
**Scale**: KZBiH-08 has 4,246 entries; 98.4% ISCO-4 coverage; primary source for German nursing qualification recognitions (~2,300/year); ghost registry ba_error_stub creates null values in compare API for all 589 codes despite real data existing.
**Source Classifier**: KZBiH-08 ("Medicinska sestra" = ISCO 2221).
**Destination Usage**: Chapter 19 of EU accession (labour market) requires demonstrable ISCO coverage data; compare API shows 589 nulls due to data model mismatch, not data gap.
**Mismatch**: Technical (metadata bug), not substantive; BA has one of the highest ISCO coverages in the dataset; bug presents it as having zero.
**Outcome**: BA ministerial data presentations show "0 codes" in compare view—serious misrepresentation for EU accession; fix is data model adjustment (Priority P1).
**Relevance for GSCO**: BA country brief; P0 fix ba_error_stub; EU accession Chapter 19 deadline 2025–2027.

---

### Case 28: Euroregion Maas-Rhine — Absurdity of Language Test for Teachers (2025)
**Scale**: Cross-border teacher labor market in the Netherlands-Belgium-Germany tri-border region (Aachen/Liège/Maastricht); documented in ITEM 2025 Cross-Border Impact Assessment.
**Source Classifier**: German KMK teacher certification (native German speaker; German university degree).
**Destination Classifier**: Dutch/Belgian equivalent (requires separate German language certification for cross-border classroom teaching).
**Mismatch**: Native German speaker with German university qualification forced to take separate German language proficiency certification to teach in German at a school 15 km across the border; professional competence (teaching, ISCO 2320) recognized; linguistic medium of instruction treated as separate classification.
**Outcome**: Teaching positions remain unfilled in the border region despite qualified candidates; documented systemic absurdity even within Schengen [42].
**Relevance for GSCO**: ITEM RPT-02 case; illustrates classification friction persists even when ISCO codes match perfectly.

---

### Case 29: Mexico → USA — TN Visa Code "Physician (Teaching Only)" (NAFTA/USMCA, Ongoing)
**Scale**: Structural, affects every Mexican doctor seeking non-immigrant TN status for medical work in the US.
**Source Classifier**: Mexican SINCO (686 entries in GSCO; "médico general" → ISCO 2212).
**Destination Classifier**: US SOC (29-1211 Physicians); but TN treaty classification uses SOC 19-1042 "Medical Scientists".
**Mismatch**: TN NAFTA visa category "Physician" is legally restricted to "teaching or research only"; clinical practice requires a different visa category (H-1B) with a different code; Mexican doctor's code maps to ISCO 2212 and US SOC 29-1211, but the TN treaty code—19-1042—is intentionally different to prevent clinical competition.
**Outcome**: Mexican doctors classified as "medical scientists" for immigration purposes; clinical practice blocked under TN despite professional equivalence; structural political mismatch embedded in treaty code.
**Source**: Romance Migration Batch (2026); US Citizenship and Immigration Services TN category guidelines.

---

### Case 30: Russia — OK 016-2025: A 30-Year Classification Gap (2025)
**Scale**: New Russian national occupation classifier OK 016-2025, replacing the 1994 version, introduces codes for AI operator, cybersecurity specialist, drone operator, and 40+ other new digital-era professional codes after a 31-year gap.
**Source (Legacy)**: OKPDTR (1994)—no AI, no cybersecurity, no drone codes.
**Updated Classifier**: OK 016-2025—adds these categories; also continues to use some ISCO-88 era code families in parallel.
**Mismatch**: 31 years of labor market evolution classified into legacy bins; workers in AI, cybersecurity, and the platform economy are officially classified under adjacent 1994 categories in all administrative systems (pension, tax, insurance) until January 2025.
**Outcome**: Retroactive reclassification required across all downstream administrative systems; RPT-14 documents this as the most significant post-Soviet occupational reclassification event [37].
**Relevance for GSCO**: Confirms even large economies experience decade-long classification gaps; GSCO captures OK 016-2025 as a new registry; provides bridge to ISCO-08 hub, ensuring downstream compatibility.

---

### Cases 31–120: Compact Reference Table

The cases below—drawn from the same 7-batch research output as Cases 1–30—are presented in compact form for completeness. The interactive on-site library at <https://gsco.io/cases> provides the full text of each case along with its primary source citation.

*Note for Russian reader: specific numbers (applications, percentages, Euros), primary citations, and exact agency names in the table below are retained in original English to avoid translation distortion of key statistics and agency names. Full Russian commentary for each case is available via `/cases?country=ISO` on the GSCO website. Column headers are translated below:*

**Headers**: # | Countries | Title (year) | Scale | Mismatch | Outcome | Source

| # | Countries | Title (year) | Scale | Mismatch | Outcome | Source |
|---|---|---|---|---|---|---|
| 31 | GB / IT | Italian Professionals in UK Post-Brexit — Mutual Recognition Ended, EU Automatic System Lost *(2021–2024)* | ~700,000 Italians in UK (pre-Brexit estimate; Il Fatto Quotidiano 2023 notes actual figure 3x higher than Istat official counts). UK… | 1. *Architecture*: Italian laurea magistrale (5-year, CNAPPC-accredited) no longer automatically recognised. ARB requires Part 3… | UK-EU TCA (Trade and Cooperation Agreement) does not include mutual recognition of professional… | [link](https://www.architecture.com/knowledge-and-resources/resources-landing-page/brexit-recognition-of-professional-qualifications) |
| 32 | GB / PL / UK | Polish Workers in UK — Mass Overqualification *(2004–2019)* | ~900,000 Polish workers in UK at peak (2014–2020); Ośrodek Badań nad Migracjami UW (Centre for Migration Research, Warsaw University): 30%… | For regulated professions (medicine, law, engineering): automatic EU recognition existed but required administrative registration (GMC,… | Sobieski Institute estimated 900,000 Polish workers 2014–2020 generated €64 billion for UK economy while… | [link](https://polishexpress.eu/polacy-skazani-na-zmywak-mamy-dyplomy-a-pracujemy-ponizej-kwalifikacji23/;) |
| 33 | DE / IT | Italian Doctors and Skilled Professionals Emigrating to Germany — "Berufserlaubnis" Limbo and 50% Salary Gap *(2008–2024)* | 1,637 Italian physicians without German citizenship working in Germany (end 2022, Bundesärztekammer/BÄK data). 155,732 total Italian… | 1. *Medicine — Berufserlaubnis trap*: Italian EU doctors arriving in Germany are entitled to Approbation under Dir 2005/36/EC but… | 180,000 Italian healthcare professionals emigrated 2000–2022 (Quotidiano Sanità, 2023). German BÄK: Italian… | [link](https://www.ilfattoquotidiano.it/2025/11/11/fuga-cervelli-espatri-aumento-38-percento-laureati-fuga-mezzogiorno/8191929/) |
| 34 | BE / FR / GB / GH / IN / NG / NL / PH / SN | African Nurses in EU — Deskilling and Back-to-Square-One *(2015–2024)* | "African nurses on the move" scoping review (PMC11929199, 2024) covers Nigeria, Ghana, Senegal, Cameroon → UK, France, Belgium,… | Non-EU African nurses placed in lowest Band 5 regardless of prior specialty (e.g., ICU, emergency) because UK/EU systems require… | 2–10 years to full recognition. Many African nurses with 10+ years ICU experience work as healthcare… | PMC "African nurses on the move: scoping review" (2024, PMC11929199); PMC… |
| 35 | DE / UA | Ukrainian Doctors in Germany — Approbation Queue *(2022–2024)* | 1,674+ Ukrainian doctors applied for Approbation (full medical licence) post-Feb 2022; only 187 authorised to practice by mid-2023; ~1,400… | Germany requires full Approbation for independent medical practice. Ukrainian doctors without Approbation can only work under… | 56% of approved Ukrainian vocational recognition cases (regulated professions, 2024) required… | [link](https://www.bibb.de/de/213410.php;) |
| 36 | BG / GB / UK | Bulgarian Doctors in UK — Mass Outflow, Diploma Recognition Paradox *(2023–2024)* | 2023: 435 of 622 doctors (70%) who joined UK workforce in one year graduated from Bulgarian medical schools. Bulgaria now #1 source… | Pre-Brexit: Bulgarian EU-diploma auto-recognised under Dir 2005/36/WE — smooth recognition path. Post-Brexit 2021: Bulgarian doctors now… | UK Health Secretary Wes Streeting warned NHS "too dependent on doctors from other countries" — in 2023, 70%… | [link](https://btvnovinite.bg/svetut/70-ot-lekarite-zapochnali-rabota-vav-velikobritanija-prez-2023-g-sa-zavarshili-meditsina-v-balgarija.html;) |
| 37 | AT / BA / MK / RS / WB | Serbian/Bosnian/Macedonian Nurses in Austria — Three-Tier System Gap *(2019–2024)* | Austria receives significant nursing workforce from former Yugoslavia. Recognised nursing shortage: Austria needs 75,000 additional care… | ossaw.at (Serbian-language Austrian portal): recognition (Nostrifikation) of Serbian "diplomirana medicinska sestra" in Austria requires… | Recognition process: 6–18 months. During this time: employed as PA at €2,100–2,400 gross vs DGKP target… | [link](https://www.ossaw.at/nostrifikacija-diploma-diplomirane-medicinske-sestre-i-tehnicari-iz-srbije-bosne-i-hercegovine-makedonije-i-crne-gore/;) |
| 38 | CA / FR / US | Foreign-Trained Teachers in Canada & USA — Certification Fragmentation *(2016–2024)* | Canada: persistent shortage of French immersion, STEM, Special Education teachers. Internationally trained teachers (ITTs) face dual… | An internationally trained teacher's degree is assessed for immigration purposes by WES — may receive "equivalent to Canadian Bachelor's +… | Borgen Project "The Reality of Immigrant Credential Recognition in Canada": credential recognition "complex… | Borgen Project "Reality of Immigrant Credential Recognition in Canada" (2021);… |
| 39 | CA | Foreign-Trained Doctors in Canada — 36% Actually Working in Field *(2019–2024)* | Canada. Only 36.5% of foreign-educated nurses and 41.1% of foreign-educated doctors worked in their related occupations (C.D. Howe… | Foreign medical credentials evaluated by provincial colleges independently — no national standard. A doctor licensed in one province may… | C.D. Howe: University-educated immigrants 12% overqualification rate in STEM — nearly 2x non-immigrant rate.… | C.D. Howe Institute "Harnessing Immigrant Talent" (2024); ESDC "Evaluation of… |
| 40 | BG / GB / UK | Bulgarian Doctors in UK — Mass Outflow, Diploma Recognition Paradox *(2023–2024)* | 2023: 435 of 622 doctors (70%) who joined UK workforce in one year graduated from Bulgarian medical schools. Bulgaria now #1 source… | Pre-Brexit: Bulgarian EU-diploma auto-recognised under Dir 2005/36/WE — smooth recognition path. Post-Brexit 2021: Bulgarian doctors now… | UK Health Secretary Wes Streeting warned NHS "too dependent on doctors from other countries" — in 2023, 70%… | [link](https://btvnovinite.bg/svetut/70-ot-lekarite-zapochnali-rabota-vav-velikobritanija-prez-2023-g-sa-zavarshili-meditsina-v-balgarija.html;) |
| 41 | BD / NP / QA | Nepali & Bangladeshi Workers Qatar — Systematic Job Substitution *(2018–2023)* | ~1.5 million migrant workers in Qatar during World Cup construction; Nepalis and Bangladeshis among largest groups. Business & Human… | Workers recruited as "plumber" or "electrician" (skilled, higher wage band) systematically reclassified on arrival to "general laborer" or… | Wage theft in 58 cases; different contract in 45 cases; overtime unpaid in 36 cases. Post-World Cup 2023:… | Business & Human Rights Centre "After the Final Whistle" (2023); HRW "Qatar:… |
| 42 | AT / HU | Orvosok és ápolók elvándorlása *(2004–2023)* | 121 000 magyar dolgozik Ausztriában (2023, összes); egészségügy a 4. legnépszerűbb terület; Ausztriában az átlagos órabér 40.9 EUR vs. HU… | EU-n belüli automatikus diplomaelismerés orvosoknak/ápolóknak él, de az osztrák honosítási eljárás nehezebb a németnél (nincs… | Kórházi szakdolgozók sztrájkfenyegetése; Magyar Kórházszövetség: "nincs belső béke"; 2022 szeptembertől… | [link](https://hvg.hu/360/20240410_ausztria-egeszsegugyi-dolgozok) |
| 43 |  | Haitian Professionals in Dominican Republic — Structural Exclusion *(2010–2024)* | ~700,000 Haitians in Dominican Republic as of 2018 (MPI). Majority undocumented. 2013 Constitutional Court ruling TC/0168/13 stripped… | Even formally documented Haitians face structural exclusion: DR constitutional ruling created massive documentation gap. Without Dominican… | Haitians dominate construction sector in DR but cannot obtain formal trade certification. Dominican INFOTEP… | MPI "Haitian Immigrants in the United States 2018" (background on diaspora);… |
| 44 | DE / HR / PL / RS / WB | Croatian/Serbian Engineers in Germany — Short-Cycle Degree Rejection *(2016–2020)* | Croatian engineer recognition applications 2016–2020: ~15% rejection rate; Serbian engineers ~16% rejection rate — highest among European… | IQ Netzwerk / Netzwerk-IQ "Berufliche Anerkennung von Ingenieur*innen" analysis (cited 2020): "In Serbien und Kroatien gibt es Abschlüsse… | Engineers with Croatian/Serbian 3-year degrees classified as "Techniker" (technician, ISCO 3119) rather than… | [link](https://netzwerk-iq.de/fileadmin/Redaktion/Downloads/Fachstelle_Beratung_Qualifizierung/FSBQ_Situationsanalyse_IngenieurInnen.pdf;) |
| 45 | BG / UA | Ukrainian Medics in Bulgaria — Language Gate vs. Healthcare Need *(2022)* | 51 Ukrainian doctors (including professors) + 68 nurses expressed intent to stay and work in Bulgaria post-Feb 2022; Bulgarian Medical… | Bulgarian law requires: (1) Bulgarian language exam; (2) equivalence assessment by MH; (3) state specialty exam for doctors. Bulgarian… | Bulgaria lost potential healthcare workforce augmentation. Compared to Poland (4,000+ applications processed… | lexmedicanews.com "БЛС: Ускорена процедура, но без снижаване на изискванията… |
| 46 | GB | ICT/Tech Workers — SOC Code Mismatches Causing UK Visa Refusals *(2024)* | UK Skilled Worker visa: since April 2024 all applications must use SOC 2020 codes (migration from SOC 2010). Tech sector most affected.… | UK SOC 2020 granularity requires duty-matching, not title-matching. "A 'Software Engineer' might fit SOC 2136, but a 'Web Developer' might… | DavidsonMorris: SOC code mismatch "now a leading cause of refusals and licence action since 2024." AYJ… | DavidsonMorris "UK SOC Codes – Find the Right Job Code for Your Visa 2026";… |
| 47 | AU / GB | Foreign Pharmacists — Systematic Multi-Year Waiting Periods *(2016–2024)* | UK OSPAP programme: 1-year university + 52-week training before GPhC registration. Australia CAOP exam required for non-Anglosphere… | Pharmacy is a "dual-degree" country problem: even pharmacists from Commonwealth countries (India, Nigeria) with equivalent training must… | Indian pharmacists in UK: typically 2–3 year pathway. Irish PSI: documented variable and lengthy timelines.… | Pharmacist Support UK "Overseas Pharmacists' Assessment Programme"; Australian… |
| 48 | US | Immigrant Health Workers in USA — 270,000 Underutilised During COVID *(2020–2022)* | ~270,000 immigrants with college degree in medical/health sciences underemployed or unemployed during COVID-19 in USA. ~2 million total… | H-1B cap (65,000/year) reached yearly since 2008 — thousands of qualified foreign doctors cannot obtain visa pathway. Philippines and… | Registered nurses working as health aides; physicians working in food service during COVID-19. Baker… | American Immigration Council "Untapped Talent: Costs of Brain Waste" (2021);… |
| 49 | BG / CZ / ES / HU / RO / SK | Roma Workers Across EU — Credential Absence and Compound Exclusion *(2016–2024)* | 6–12 million Roma in EU. ERGO Network 2024: 6-country study (Bulgaria, Czech Republic, Hungary, Romania, Slovakia, Spain). 56% Roma youth… | Roma workers face compound mismatch: (a) informal skills/trades (construction, metalwork, music, horse training) have no formal credential… | European Roma Rights Centre: "Discrimination significantly aggravates employment barriers and causes… | ERRC "Systemic Exclusion of Roma from Employment"; ERGO Network "Roma access… |
| 50 | GB / UK / ZA | Geskoolde migrante *(1994–2023)* | ~250 000 Suid-Afrikaners in VK; ~200 000 in Australie; 128 000+ emigreer permanente (2015–2020) — 3× meer as vorige 5-jaar; 67% van… | UK: gemiddelde onderwyssvlak van ZA-gebore immigrante laer as ander hoofbronne; Australie: navorsing toon dat hervaardigheidspogings… | ZA-gesondheidstelsel: 18.6% vakante poste vir spesialiste, 13.7% vir verpleegsters; ~23 400 ZA… | [link](https://maroelamedia.co.za/nuus/sa-nuus/emigrasie-die-syfers-redes-en-implikasies/) |
| 51 | US | Foreign Lawyers in USA — Jurisdiction Fragmentation *(2015–2024)* | Thousands of international lawyers annually. Only ~40 US states allow any form of reciprocal admission; California, Florida, Louisiana… | A "lawyer" in every country maps to single SOC code 23-1011, but actual admission requires jurisdiction-specific bar passage. Common law… | Under-employment as paralegals, legal assistants, compliance officers. Jurisdiction-bound credentialing… | University of Dayton "How International Lawyers Qualify for US Bar"; NCBE… |
| 52 | CA / NL | Agrarisch ondernemer *(2022–2023)* | ~20% van alle NL boeren en tuinders overwoog emigratie (ca. 50 000–80 000 bedrijven totaal); emigratieadviseurs meldden verdubbeling in… | In Canada (PEI, Alberta) worden HBO-diploma en IELTS vereist als primaire visa-aanvraagcriterium; de Nederlander die zijn bedrijf verkoopt… | "Aanzienlijke emigratie" verwacht bij permanent beleid; emigranten die al vertrokken (incl. naar FR, SE, DK)… | [link](https://nos.nl/nieuwsuur/artikel/2449983-boeren-overwegen-vertrek-wordt-dit-de-nieuwe-emigratiegolf) |
| 53 | CU / ES | Cuban Doctors in Spain — Bureaucratic Limbo 2–4 Years *(2017–2025)* | Hundreds of Cuban doctors per year arriving in Spain; cases documented of 2–4 year waits before practicing. Cuba's consulates refuse to… | Spain's Ley 44/2003 requires original "non-disqualification" certificate from Cuba. Cuban government routinely refuses to issue these for… | One documented case: female cardiologist worked as waitress for 2+ years; celebrated credential recognition… | CubaHeadlines "Cuban Doctor in Spain Returns to Medical Practice After… |
| 54 | DZ / FR / MA | Moroccan/North African Engineers in France — Standards Gap *(2016–2024)* | Algeria sends largest non-EU migrant group to France; Morocco second. Engineering a major study field. Estimates: tens of thousands of… | French CTI only accredits French engineering schools (grandes écoles). Moroccan/Algerian engineering degrees from ENSEM Casablanca, ENSET… | Quora response from French engineering recruiter (cited by web sources): "Difficulty arises from cluster of… | Quora "Why is it difficult for African qualified engineers to get a job in… |
| 55 | BG / DE / PL / RO | Eastern European Electricians in Germany — Regulated vs. Unregulated Paradox *(2015–2024)* | Hundreds of thousands of Romanian, Polish, Bulgarian tradespeople in Germany. Electricians specifically: Germany has ~14,000 vacancies for… | Electrician is a non-regulated profession for EU/EEA citizens (no mandatory recognition needed) but without German Meister or equivalent… | Trapped in sub-Meister grade. "If you do not have your qualification recognised, you may end up working in a… | EU-Gleichbehandlungsstelle.de "Recognition of Foreign Professional… |
| 56 | FI / RU / SO | Somali Refugees in Finland — <10% Tertiary Credential Recognition *(2015–2023)* | ~20,000 Somalis in Finland, majority refugees. Of those with tertiary education, fewer than 10% have had credentials recognised (vs. 21%… | Finland (and Czech Republic) identified by European research as countries with "high barriers to recognition of foreign skills." Without… | Somali migrants in Finland: high unemployment, overrepresentation in low-status low-skill jobs, residence in… | Finnish National Agency for Education recognition statistics; UNESCO GEM… |
| 57 | KH / LA / MM / TH | Cambodian/CLM Workers in Thailand — Confined to Elementary Occupations *(2016–2024)* | ~1–2 million Cambodian, Lao, Myanmar (CLM) workers in Thailand. ADB study (2025): majority concentrated in elementary occupations… | Thailand's list of 27 absolutely prohibited jobs for foreigners includes: driving (transport/delivery), accounting, legal work,… | ADB 2025: "CLM migrants are largely concentrated in elementary occupations and many work below their… | ADB "Narrowing Skills Gaps: Labor Mobility from Cambodia, Lao PDR, Myanmar to… |
| 58 |  | West African Workers — ECOWAS Collapse and New Barriers *(2025)* | Hundreds of thousands of Burkinabe, Malian, Nigerien workers in Côte d'Ivoire. Burkina Faso, Mali, Niger formally withdrew from ECOWAS… | Pre-2025: ECOWAS free movement meant workers' qualifications circulated without formal classification matching. Post-withdrawal: citizens… | IOM survey: "It is very difficult to compare and compile information on migrants' occupations, mainly… | Anywr-Group "Burkina Faso, Niger and Mali Standing out from ECOWAS" (2025);… |
| 59 | AU | Foreign Engineers in Australia — ANZSCO 233999 "NEC" Trap *(2016–2024)* | Australia receives ~25,000 skilled engineering visa applications annually. CDR (Competency Demonstration Report) system managed by… | ANZSCO 233 has specific codes for Civil (233211), Electrical (233311), Mechanical (233512), Chemical (233111), etc. "Industrial Engineer,"… | CDRreportwriter.com documents this as a known industry issue. Engineering Professionals NEC: "occupations… | CDRReportWriter "Engineering Professionals NEC (ANZSCO 233999): Your… |
| 60 | HU / NO | Lege/sykepleier *(2014–2023)* | Ungarn er blant topp-bidragsytere av utenlandske helsearbeidere til Norge; 58–67% økning i utenlandsutdannede leger/sykepleiere i regionen… | Ungarsk lege tjente ~70 000 NOK/år i Ungarn; i Norge: ~750 000 NOK — tidobling; norsk er obligatorisk, men etter bestått norskprøve… | Sterk pull-faktor; mange blir værende i Norge permanent; HU mister ca. like mange leger hvert år som gradueres | [link](https://www.aftenposten.no/okonomi/i/Pzbp/Larte-norsk---tidoblet-lonnen) |
| 61 | MM / TH | Burmese/Myanmar Professionals in Thailand — Pink Card Misclassification *(2021–2024)* | ~3–4 million Myanmar migrants in Thailand; 100,000+ politically motivated (post-2021 coup) including former teachers, doctors, university… | Thailand's labor migration registration system has no category for professionals. Former university teachers, doctors, political… | "Downward social mobility, underemployment, and a loss of professional identity, effectively becoming… | CMU School of Public Policy "Misclassified and Unprotected: Survival Migration… |
| 62 | FI / UA | Korkeakoulutetut kielimuurin takana *(2022–2024)* | ~64 000 tilapäistä suojelua saanutta; ~40 000 on jo lähtenyt Suomesta muihin EU-maihin; 50 000 jäänyt; 40% työllisyysaste (vs. 71%… | Suomi vaatii suomen kieltä lähes kaikissa töissä, myös maatiloilla — "englanti ei riitä"; insinöörit ja ekonomit hakevat tehdastöitä ja… | Suomi on Euroopan korkein työttömyysaste 2024 → ukrainalaiset hakevat töitä muualta EU:sta; Yle raportoi… | [link](https://yle.fi/a/74-20215841) |
| 63 | GB / MY / SG | 74% Мигрантов Квалифицированы, Но Система не Признаёт Их *(2022–2024)* | 1.13 млн малайцев в Сингапуре; 381 медсестра + 54 врача эмигрировали из MOH 2020–2024; 3 123 малайских врача в NHS UK (2023, +21% за 2 года) | Исследование Dept. of Statistics Malaysia / Ministry of Economy (2022, опубликовано февраль 2024): 74% малайзийцев в Сингапуре —… | Malaysia MOH — 54 362 вакансии (17% vacancy rate к концу 2024 vs 5% в 2016). Доктор-пациент ratio: 1:412… | [link](https://www.malaymail.com/news/malaysia/2024/02/21/study-warns-of-brain-drain-finds-three-in-four-malaysians-living-working-in-singapore-skilled-or-semi-skilled/119128) |
| 64 | MM / TH | Профессионалы Переклассифицированы в Неквалифицированных Рабочих *(2021–2024)* | ~2.3 млн зарегистрированных мьянманских мигрантов (70% иностранной рабочей силы); 1.5 млн новоприбывших 2023–февраль 2024; 4 млн всего (IOM) | После военного переворота 2021 года в Таиланд бежали представители CDM (Civil Disobedience Movement): врачи (из ~60 000 подписавших CDM… | Принудительная деквалификация; по 25 000 бат за брокерское оформление; в 2024 году 50% рост долгосрочных… | [link](https://spp.cmu.ac.th/misclassified-and-unprotected-survival-migration-from-myanmar-and-the-limits-of-thailands-pink-card-system/) |
| 65 | LA / TH | Trapped in Elementary Occupations *(2023–2024)* | ~280 000 зарегистрированных (сент. 2024); 156 000 — женщины; 17 898 домашних работников (март 2024); реальная оценка значительно выше | Лаосские мигранты — доминирующий поток неквалифицированной рабочей силы в Таиланде. ILO/IOM данные: в 2024 году квалифицированные мигранты… | Круговая миграция без накопления квалификаций; возвращающиеся мигранты приносят денежные переводы, но не… | [link](https://www.ilo.org/sites/default/files/2025-01/QBN%20Q3%202024_LAO%20PDR_final.pdf) |
| 66 | GE / RU | IT-специалисты и творческие профессии *(2022–2025)* | >62 000 российских эмигрантов прибыло в Грузию в 2022 году, >52 500 в 2023; из них постоянно остаётся ~25 000–30 000 в Тбилиси/Батуми | Компании предпочитали нанимать дешёвых сотрудников в Узбекистане; работники хотели Германию/Великобританию — "в итоге встретились где-то в… | Крупные русскоязычные экспат-сообщества в Стамбуле и Анталье; высокий уровень прекариата среди… | [link](https://meduza.io/feature/2024/10/25/dva-goda-nazad-tysyachi-rossiyan-uehali-v-gruziyu-spasayas-ot-mobilizatsii-i-repressiy-kak-emigratsiya-izmenila-ih-i-kak-za-eto-vremya-izmenilas-sama-gruziya) |
| 67 | KH / TH | Принудительный Труд и Классификационный Вакуум *(2022–2023)* | ~459 863 зарегистрированных на янв. 2024; реальная оценка 1–2 млн; 50–90% — нелегальные | Камбоджийские сезонные рабочие концентрируются в провинциях Трат, Са Кэу, Чантхабури (сезон тростник/фрукты — февраль–июнь). Официальная… | Вернувшиеся мигранты (после кризиса 2025) сталкиваются с безработицей: работали в строительстве/сельском… | [link](https://winrock.org/wp-content/uploads/2023/07/Asia-CTIP-Cam-Tha-Seasonsal-Migration-Research.pdf) |
| 68 | AS | Нулевая Мобильность | 8 подписантов MRA; 7 МРА по 8 профессиям (сестринское дело, архитектура, инжиниринг, бухгалтерия, стоматология, медицина, геодезия) | MRA по сестринскому делу подписано в 2006 году. Почти 20 лет спустя — систематические данные из PMC-исследования (2020): «AMoNS did not… | Мобильность осуществляется по неформальным, не-MRA каналам: двусторонние договоры (JP-PH EPA, JP-ID EPA по… | [link](https://pmc.ncbi.nlm.nih.gov/articles/PMC7308680/) |
| 69 | AU / IN / NP / PH | Filipino Nurses in Australia — Excluded from Fast-Track *(2025)* | Philippines is one of top 3 source countries for internationally qualified nurses (IQNs) in Australia, alongside India and Nepal. | Australia's new April 2025 NMBA standard created fast-track "Outcome-Based Assessment" (OBA) pathway for approved jurisdictions.… | Filipino nurses face longer, more expensive assessment pathway. Mandatory OSCE (Objective Structured… | Filipino Inquirer "Filipino nurses and Australia's new policy" (2024); NEAC… |
| 70 | AM / RU | IT и не-IT после мобилизации (сент 2022–2023) | ~110 000 россиян переехали в Грузию в 2022 году; Ереван стал центром IT-релокаций (66% ищущих работу нацелились на IT в AM/GE) | Компании перевели офисы, но не всех сотрудников; для не-IT профессий рынок крайне узкий; конкуренция за вакансии выросла резко; зарплаты… | ВВП Армении +12.6% (2022); приток иностранных инвестиций +172%; для IT-специалистов специальный налоговый… | [link](https://meduza.io/feature/2022/11/10/posle-nachala-voyny-iz-rossii-aktivno-uezzhali-aytishniki-mobilizatsiya-zastavila-emigrirovat-i-sinih-vorotnichkov) |
| 71 | TW / VN | Structural Bottleneck *(2022–2024)* | 763,381 total migrant workers in Taiwan (Q1 2024); ~262,957 Vietnamese; only 4.15% reclassified as mid-skilled in manufacturing | Taiwan launched "中階移工" (Foreign Mid-Skilled Worker Program) in April 2022 allowing manufacturing workers to apply for reclassification… | Workers with genuine manufacturing expertise remain formally classified as blue-collar unskilled. The 5-year… | [link](https://www.pidi.com.tw/post/2024-04-22) |
| 72 | IL / RU | IT-репатрианты и non-Jewish *(2022)* | ~15 000 россиян въехали в Израиль в начале 2022; программа "зелёного коридора" для IT без требования еврейского происхождения | В Израиле не требуется документальное подтверждение IT-квалификаций (в отличие от Европы), однако для работы по специальности вне IT нужна… | Израиль использовал волну как решение дефицита IT-кадров; для гуманитарных и медицинских специальностей —… | [link](https://www.forbes.ru/svoi-biznes/464153-najti-svoih-kto-sejcas-emigriruet-iz-rossii-v-izrail-i-kak-oni-mogut-ego-izmenit) |
| 73 | AT / HU | Ápolók bérkülönbség *(2022–2023)* | Tízszer annyi szakember hagyja el Magyarországot, mint ahány érkezik; 444.hu (2014): "Magyar tanárok, orvosok, isten veletek" | Automatikus EU-elismerés technikailag megkönnyíti — de Ausztriában a tartományi kamara regisztrációja egyedi, vizsgafelkészülési engedély… | Béremelési hullám 2023 júliustól (szakdolgozók), de a különbség fennmarad; elvándorlás strukturálisan beépült | [link](https://iranynemetorszag.com/informaciok/magyarorvosok.html) |
| 74 | AE / IN / KW / PK / QA / SA | Indian & Pakistani Engineers in Gulf — "General Worker" Downgrade *(2015–2024)* | ~3 million Indian nationals + ~1.5 million Pakistanis working in Saudi Arabia; similar concentrations in UAE, Qatar, Kuwait. | SCE Tier assessment requires degree accreditation by Washington Accord members. Indian degree programs from non-NAAC-A accredited… | Pay differential: "Engineering Technician" vs. "Engineer" tier in Saudi is ~2,000–4,000 SAR/month. Arab News… | ArabNews "Saudi Professional Accreditation Program" (2024); SCE Professional… |
| 75 | NO / SE | Eritrean Refugees in Sweden/Norway — Education Not Recognised *(2015–2024)* | Eritreans largest non-European asylum group in Sweden (21% of 2014 applicants). In Norway, among top refugee nationalities. | Eritrean secondary (ESEC) and tertiary credentials assessed by Swedish UHR, but: (a) Eritrea has no functioning national accreditation… | Eritrean and Somali refugees overrepresented in low-skill, low-status jobs in Sweden/Norway/Finland. High… | Swedish UHR "Eritrean Secondary Education Certificate (ESEC)"; DIVA-portal… |
| 76 | DE | Non-EU Doctors in Germany — Approbation Bottleneck *(2015–2024)* | ~64,000 foreign-licensed doctors working in Germany as of 2024. Bundesärztekammer repeatedly reports recognition delays. | No federal standard — each of 16 Bundesländer runs its own Approbation process with conflicting requirements. Gutachtenstelle in Bonn… | 1–2 years average wait. Many work as "Berufserlaubnis" holders (provisional license) with salary/status… | Hessenschau "Nachtwache statt Notaufnahme" (2024); Apotheken Umschau… |
| 77 | TW / US | Taiwanese Physicians as International Medical Graduates (IMGs) *(2022–2023)* | Non-US citizen IMGs (including Taiwanese): 59.4% match rate; 40.6% fail to match into residency (2023 NRMP data) | Taiwanese MD/PhD degrees are valid for ECFMG certification, but Taiwanese physicians must pass USMLE Steps 1–3 and compete against all… | Many Taiwanese physicians accept positions below their home-country seniority level while completing US… | [link](https://www.nrmp.org/wp-content/uploads/2022/07/Charting-Outcomes-IMG-2022_Final.pdf) |
| 78 | EE / UA | Kõrgharidusega töötajad lihttöödel *(2022–2024)* | 44% tööealistest ukrainlastest (20–64) on tööga hõivatud (2024, kasvav); ~10 600 ukrainlast töötab legaalselt | Peaaegu kolmandikul on kõrgharidus, ~40% töötab lihttöödel (koristajad, köögitöölised, laotöölised); eesti keele puudumine muudab inimesed… |  | [link](https://www.lsm.lv/raksts/zinas/latvija/24.01.2024-latvija-strada-mazak-neka-puse-darbspejigo-ukrainas-beglu.a540051/) |
| 79 | CA / CN / GB | Deskilling of Racialized Skilled Immigrants in British Columbia *(2022–2024)* | Mixed-methods study; quantitative n=111, focus groups n=18; Lower Mainland BC; 24.3% East Asian participants | Study (*PMC*, 2024) found 17 of 18 focus-group participants with 4–8 years pre-migration professional experience were working in… | Mean annual income of deskilled immigrants: CAD $61,542 (SD ±$36,456) — significantly below Canadian-trained… | [link](https://pmc.ncbi.nlm.nih.gov/articles/PMC12764677/) |
| 80 | CL / VE | Venezuelan Doctors in Chile — EUNACOM Barrier *(2017–2024)* | Waves of Venezuelan doctors in Chile; 96% of Chilean graduates pass EUNACOM vs. 64% foreign candidates. | Chile requires