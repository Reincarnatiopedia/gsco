# GSCO: Globālais Standarta Profesiju Klasifikators — Determinētā daudzvalodu datubāze, lai atrisinātu N² krusttabulu problēmu starptautiskajā profesiju klasifikācijā

**Maris Dreshmanis**
ORCID: [0009-0003-8151-4088](https://orcid.org/0009-0003-8151-4088) | ISNI: [0000 0004 9280 9121](https://isni.org/isni/0000000492809121)
Afiliācija: Reinkarnācijasoloģijas akadēmija | Neatkarīgs pētnieks
GitHub: [MarisDreshmanis](https://github.com/MarisDreshmanis) | Wikidata: [User:Maris Dreshmanis](https://www.wikidata.org/wiki/User:Maris_Dreshmanis)

**Versija:** 1 | **Licence:** CC BY 4.0 | **Datums:** 2026. gada aprīlis

**DOI:** [10.5281/zenodo.19902278](https://doi.org/10.5281/zenodo.19902278) (this version) · **Concept DOI:** [10.5281/zenodo.19902277](https://doi.org/10.5281/zenodo.19902277) (latest version) · [Zenodo record](https://zenodo.org/records/19902278)

---

## Kopsavilkums

**Ievads.** Profesiju klasifikācijas standartu neatbilstības problēma dažādās valstīs tika atklāta nejauši. Viens no maniem darbības veidiem ir Wikidata rediģēšana un papildināšana ar datiem. Wikidata kalpo kā saikne starp dažādu valodu Vikipēdijas sadaļām, pildot kopīgu faktu un saišu centrālās krātuves lomu.

Risinot uzdevumu par Wikidata papildināšanu ar datiem par vienu konkrētu mērķa grupu — Nobela prēmiju laureātiem dažādās valodās, tika atklāts, ka profesiju nosaukumi ir viens no trūkumiem, kas nav sistematizēti Wikidata.

Lai nenokļūtu kļūdās profesijas nosaukumā, tulkojot ar neironu tīkliem vai Google tulkotāju, es nolēmu savākt no atklātajiem avotiem profesiju klasifikatorus dažādās valodās. Kad tas tika izdarīts, atklājās globāla mēroga problēma. Pirmkārt, Starptautiskā Darba organizācija (SDO) atjaunina savu Starptautisko standartizēto profesiju klasifikāciju (ISCO) aptuveni ik pēc 20 gadiem. Tas nozīmē, ka jaunās desmitgades profesijas tajā nav iekļautas.

Lūk, ISCO standartizācijas gadi:

- **ISCO-58** — pieņemta 1957. gadā (publicēta 1958.).
- **ISCO-68** — pieņemta 1966. gadā (publicēta 1968.).
- **ISCO-88** — pieņemta 1987. gadā (publicēta 1988.). Tieši tajā pirmo reizi tika skaidri definēta "prasmju līmeņa" koncepcija.
- **ISCO-08** — pieņemta 2007. gadā (publicēta 2008.). Šī ir pašreizējā versija, ko pašlaik izmanto visā pasaulē.
- Nākamā (**ISCO-28**) pašlaik ir SDO aktīvajā pārskatīšanas fāzē — empīrisko ievaddatu iesniegšana ir atvērta 2026.–2028. gadā, izlaidums 2028. gadā.

Otrkārt, tās valstis, kas šo uzdevumu risināja patstāvīgi, pievieno kodus, kas konfliktē starp dažādām valstīm. Nedaudz labāka situācija ir Eiropas Savienībā, taču kopumā pasaulē standartizācijā un kodēšanā pēc 4 ISCO cipariem valda haoss.

Turpinot risināt Nobela prēmiju laureātu profesiju aprakstīšanas uzdevumu, es sev izveidoju tabulu neatbilstību analīzei dažādās valstīs. Nosaucu vienkārši: **GSCO (Globālais Standarta Profesiju Klasifikators)**. Kāpēc globāls? Jo savācu datus no vairāk nekā 140 nacionālajiem reģistriem. Es neatradu informāciju, ka kāds pasaulē to būtu darījis iepriekš; ja jums, lasot šo tekstu, ir tāda informācija — lūdzu, atsūtiet man. Kontakti norādīti manas profila lapas sadaļā.

Kad dati tika savākti un analizēti, es sapratu, ka ir nepieciešams dalīties šiem datiem ne tikai ar nacionālajiem reģistriem, lai tie apzinātos profesiju kodu konfliktu skaitu savās valstīs un mēģinātu tos sinhronizēt, bet arī ar Starptautisko Darba organizāciju (SDO), lai palīdzētu darba grupai saskatīt problēmas mērogu un ņemt to vērā ISCO-28 standartizācijā 2028. gadā.

### Piemērs: ISCO 2221

**Hub-level: ko oficiālais ISCO-08 domā**

ISCO-08 (SDO): «Nursing professionals» — medmāsas ar paplašinātām pilnvarām (advanced nurse practitioner).

Daudzvalodu hub-level paraksti mūsu datubāzē (35 valodās):

| Valoda | Tulkojums |
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

**Katastrofa nacionālā līmenī**

Ar vienu ISCO 2221 kodu dažādas valstis domā **atšķirīgas profesijas**:

**Austrālija un Jaunzēlande (ANZSCO 2022) — finanšu brokeri, ne medmāsas:**

- 222111 Commodities Trader (preču tirgotājs)
- 222112 Finance Broker
- 222113 Insurance Broker
- 222199 Financial Brokers nec
- 222100 Financial Brokers nfd

**Ukraina (DK003) — ārsti, ne medmāsas:**

- 2221 — «Професіонали в галузі лікувальної справи (крім стоматології)»
- 2221.1 — Наукові співробітники (лікувальна справа)
- 2221.2 — Лікарі (ārsti): terapeits, kardiologs, ķirurgs, psihoterapeits, neirologs, ģenētiķis…
- Kopā 78 apakškodi — visi ārsti, ne medmāsas.

**Vācija (KldB-2010):**

- 22212 «Vehicle paintwork — skilled tasks» (automašīnu krāsošana)
- 81393 «Aufsichtskräfte — Gesundheits- und Krankenpflege, Rettungsdienst und Geburtshilfe» — vecākās medmāsas
- 81302 «Gesundheits- und Krankenpflege» — parastās medmāsas (pēc oficiālā Umsteigeschlüssel Bundesagentur für Arbeit tiek kartētas uz ISCO 3221, ne 2221)

**Baltkrievija (OKRВ-2017, aktuālā klasifikatora versija):**

- 2221: «Специалисты-профессионалы по медицинскому уходу» — medmāsas (atbilst ISCO-08)

**Itālija (CP 2021) — arhitekti:**

- 2.2.2.1.1 ARCHITETTI (arhitekti)
- 2.2.2.1.2 Pianificatori, paesaggisti (plānotāji, ainavu arhitekti)

**Sanmarīno (RP-2017) — arhitekti:**

- 22211 ARCHITETTO

**Kanāda (NOC 2021) — tehniķi:**

- 22210 Architectural technologists
- 22211 Industrial designers
- 22212 Drafting technologists
- 22213 Land survey technologists
- 22214 Geomatics

**Alžīrija (DZ Profession) — ārsti:**

- 2221: «Médecins» (ārsti)

---

---

### Ikvienam pazīstamas profesijas — skolotājs un taksometra vadītājs

Lai parādītu, ka problēma nav saistīta ar tādām retām profesijām kā "jogas instruktors" vai "hipnoterapeits", bet gan par **visparastākajām, masu profesijām**, apskatīsim divas universālas profesijas: skolotāju un taksometra vadītāju. Tās pastāv katrā valstī, taču klasifikācijas krasi atšķiras.

#### 👨‍🏫 Skolotājs / lektors

Top-15 valstis pēc amatu skaita zem ISCO 23xx (Izglītība):

| Valsts | Pozīcijas zem 23xx | Neparastākā detalizācija |
|---|---:|---|
| 🇧🇦 **Bosnija (KZBiH-08)** | **404** | **191 atsevišķi universitātes pasniedzēji** zem viena ISCO 2310 — atsevišķs kods katrai specialitātei (biotehnoloģija, filoloģija, matemātika) |
| 🇺🇿 Uzbekistāna (OZMST 2025) | 387 | 179 profesionālās izglītības skolotāji (2320) |
| 🇲🇳 Mongolija (YAMAT-08) | 355 | 120 universitātes + 120 profesionālās izglītības |
| 🇸🇦 Saūda Arābija (SSCO 2024) | 275 | 76 vidusskolas skolotāji |
| 🇷🇸 Serbija (Šifarnik) | 264 | 97 universitātes pasniedzēji |
| 🇰🇷 Koreja (KSCO 2024) | 171 | 5–7 katrā ISCO-4 grupā, vienmērīgi sadalīti |
| 🇮🇹 Itālija (CP2021) | 141 | 38 lektori zem 2311 |
| 🇪🇪 Igaunija (AK-2008) | 130 | Izglītības metožu speciālisti, valodu skolotāji — atsevišķi kodi |

Un pašā apakšā:

| Valsts | Kopā | Kas tur ir |
|---|---:|---|
| 🇷🇺 Krievija (OKZ-2014) | **22** | Tikai 4 ciparu ISCO grupas, bez detalizācijas |
| 🇩🇪 Vācija (KldB-2010) | 40 | Pašu numerācija, nesadala ISCO 23xx |
| 🇺🇸 USA (O\*NET) | **8** | 5 SOC kategorijas 23-1 + 3 SOC 23-2 |
| 🇬🇧 UK (SOC 2020) | 15 | 1 uz katru apakškodu |

**Ko tas nozīmē konkrētam skolotājam:** Bosnijas biotehnoloģijas profesorei ir specifisks kods KZBiH-08 (viens no 191), taču, ja viņa pārceļas uz Krieviju, viņas 191 līmeņa detalizācija **sabrūk vienā kodā 2310 "university lecturer"**. Ja viņa pārceļas uz USA, viņas kods pat **neiekļaujas SOC 23-1** (tur nav priekšmetu specifiskā līmeņa).

#### 🚕 Taksometra vadītājs

Standarta ISCO **8322** "Car, taxi and van drivers" (apvienota kategorija) pastāv lielākajā daļā valstu. Taču **vietējie taksometru veidi** ir gadījums, ko ISCO-08 vienkārši neaptver:

| Valsts | Vietējais kods | Apraksts |
|---|---|---|
| 🇫🇷 Francija (ROME 11993) | Chauffeur de taxi animalier | **Dzīvnieku transporta taksometrs** — vienīgā šāda veida atsevišķā klase pasaulē |
| 🇫🇷 Francija (ROME 12884) | Conducteur de bateau taxi | Ūdens taksometrs |
| 🇫🇷 Francija (ROME 13191) | Conducteur de taxi moto | Motocikla taksometrs |
| 🇧🇦 Bosnija + 🌊 PACSCO (Klusā okeāna 23 valstis) | 8350 | **"Vozač taksija na vodi" / "Water taxi driver"** — ūdens taksometrs (atsevišķa ISCO kategorija) |
| 🇹🇬 **Togo (RGPH4)** | 5020 "Taxi-moto (**Zemidjan**)" | **Zemidjan** — vietējais nosaukums motocikla taksometram, profesija, kurā strādā tūkstošiem cilvēku |
| 🇧🇯 Benina (NAP) | 154–155 | "Taxi-moto / charrette / vélo" (motocikls / rati / velosipēds) |
| 🇬🇹 Gvatemala (CNO 2022) | 832104 + 933101 | "Piloto de moto taxis" + "**Piloto de bicitaxis**" (velotaksometrs) |
| 🇭🇳 **Hondurasa (CNOH 2018)** | 832101 | "Conductor de moto taxi **forestal** motorizada" — **motorizēts meža taksometrs** (unikāls Hondurasai) |
| 🇸🇳 Senegāla, 🇩🇯 Džibutija, 🇨🇮 CI | 05.0.0.17 | "taxi man — conducteur de bus" — apvienots "taxi driver + bus driver" vienā profesijā |
| 🇨🇦 Kanāda (NOC 2021) | 75200 | "Taxi and **limousine** drivers and **chauffeurs**" — taksometru vadītāji apvienoti ar limuzīniem |
| 🇦🇺/🇳🇿 ANZSCO 2022 | 731112 | "Taxi Driver" — bet ANZSCO pašu numerācijā 7311 = "Automobile Drivers", kas **neatbilst** ISCO 7311 "Precision-Instrument Makers and Repairers" (cita profesija starptautiskajā standartā). Pārbaudīts, izmantojot ABS oficiālo OSCA 2024 ↔ ISCO-08 atbilstības tabulu: pareizā ISCO-08 vienības grupa priekš ANZSCO 731112 ir **8322** "Car, taxi and van drivers". |

**Ko tas nozīmē konkrētam taksometra vadītājam:** Togo **zemidjan-driver** (motocikla taksometrs) ir reāla profesija ar tūkstošiem strādājošo. Ne ISCO-08, ne ANZSCO, ne SOC tai nav paredzēta vieta. Kad viņš migrē uz Vāciju vai Franciju saskaņā ar kvalifikācijas atzīšanas noteikumiem, viņa profesionālā pieredze sabrūk vispārīgajā "Personenkraftwagen-Fahrer" (vieglo automobiļu vadītājs) — jo vārda "zemidjan" vācu klasifikatorā nav. Nevis "pazudis tulkojumā" — viņš ir **pazudis taksonomijā**.

Hondurasas "meža motocikla taksometra vadītājs" (Conductor de moto taxi forestal) vai Gvatemalas "velotaksometra vadītājs" (Piloto de bicitaxis) tāpat ir reālas masu profesijas, kas **nav iekļautas starptautiskajā struktūrā**.

#### Kāpēc tas ir svarīgi

Skolotājs un taksometra vadītājs ir visuniversālākās, vieglāk saprotamās profesijas. Ja pat šeit nav vienprātības — kā ir ar retām vai jaunām profesijām (AI treneris, dronu operators, klimata pielāgošanās speciālists)? Šie piemēri rāda: **kārtības ieviešana globālajā profesiju klasifikācijā ir ANO/ILO mēroga uzdevums**, nevis atsevišķu valstu darbs. Tieši tas ir mērķis: palīdzēt ISCO-28 darba grupai 2028. gadā ņemt vērā šīs atšķirības.

### Tās valstis, kurās 2221 patiešām = medmāsas

Detalizētas apakšklasifikācijas (parāda, kā valsts redz specializācijas):

**Igaunija (AK-2008) — 19 medmāsu apakškodi** (oriģinālie igauņu nosaukumi + krievu tulkojums):

- 2221 Õenduse tippspetsialistid (Medicīnas aprūpes profesionāļi speciālisti)
- 22210501 Abiõde (üliõpilane) — medmāsas palīgs (students)
- 22210502 Õde — medmāsa
- 22210601 Anesteesia-intensiivraviõde — anestēzijas un intensīvās terapijas
- 22210701 Erakorralise meditsiini õde — neatliekamās medicīnas
- 22210801 Diabeediõde — diabētiskā
- 22210901 Geriaatriaõde — geriatriskā
- 22211001 Lasteõde — pediatriskā
- 22211101 Nakkustõrjeõde — infekciju profilakses
- 22211201 Onkoloogiaõde — onkoloģiskā
- 22211301 Operatsiooniõde — operāciju
- 22211401 Pulmonoloogiaõde — pulmonoloģiskā
- 22211501 Taastusraviõde — rehabilitācijas terapijas
- 22211601 Koduõde — mājas aprūpes
- 22211701 Kooliõde — skolu
- 22211801 Töötervishoiuõde — darba aizsardzības
- 22211901 Pereõde — ģimenes
- 22212001 Psühhiaatriaõde — psihiatriskā
- 22219900 Mujal liigitamata õenduse tippspetsialistid — citur neklasificēti medicīnas aprūpes speciālisti

**Mongolija (YAMAT-08) — 28 medmāsu apakškodi mongoļu valodā:**

- 2221-01 Сувилагч, арга зүйч (metodiķis)
- 2221-02 Сувилагч, ерөнхий мэргэжлийн (vispārējā prakse)
- 2221-03 Сувилагч, арьсны (dermatoloģiskā)
- 2221-04 Сувилагч, гэмтэл согогийн (traumatoloģiskā)
- … vēl 24

**Palestīna (ASCO 2016) — 23 specialitātes arābu valodā:**

- 222101 ممرضة سريرية (klīniskā)
- 222102 ممرضة حي (rajonu)
- 222103 ممرضة التخدير (anestēzijas)
- 222104 ممرضة مربية (pediatriskā)
- … vēl 19

**Saūda Arābija (SSCO 2024) — 17 specialitātes:**

- 222101 Nurse Specialist
- 222102 Specialized Nursing Specialist
- 222103 Community Health Nursing Specialist
- 222104 Maternal and Child Nursing Specialist
- 222105 Anesthetic Nursing Specialist
- … vēl 12

**Dienvidāfrika (OFO 2017) — 17 veidi:**

- 2017-222101 Clinical Nurse Practitioner
- 2017-222102 Aged Care Registered Nurse
- 2017-222103 Registered Nurse (Child and Family Health)
- … vēl 14

**Latvija (Profesiju klasifikators) — 8 veidi ar nacionālajiem apakškodiem:**

- 2221 Medicīnas māsas profesijas vecākie speciālisti
- 2221 02 VirsMĀSA (vecākā medmāsa)
- 2221 46 MĀSA / vispārējās aprūpes (vispārējā)
- 2221 48 anestēzijā un intensīvajā aprūpē (anestezioloģija)
- 2221 50 psihiatrijā un narkoloģijā (psihiatrija)
- … vēl 3

**Nikaragva (CUONIC) — 7 veidi:**

- 2221-02 Enfermera Anestesista
- 2221-03 Educadora de Enfermeras
- 2221-04 Enfermera Clínica
- 2221-05 Enfermera del Quirófano (operāciju)
- 2221-06 Enfermera de la Salud Pública
- … vēl 2

---

### Vienkārši paraksti bez skaidrojuma

- **Albānija**: 2221 «Infermierë të specializuar» (specializētas medmāsas)
- **Butāna** (BSCO): 2221 Nursing Professionals + 22211 Registered Nurse + 22212 Public Health Nurse
- **Ekvadora**: 2221 PROFESIONALES DE ENFERMERÍA
- **Irāna**: 2221 رستاران متخصص (specializētas medmāsas)
- **Islande**: 2221 Sérfræðistörf við hjúkrun
- **Lietuva** (LPK 2023): 2221 Slaugos specialistai + 222101 Slaugytojas + 222102 Mokslo darbuotojas (slauga)
- **Ziemeļmaķedonija**: 2221 Медицински сестри
- **Maurīcija**: 22211 Administrator, nursing + 22212 Educator, nurse + 22219 Nursing professionals n.e.c
- **Kambodža**: 4 apakškodi 22211–22214 khmeru valodā
- **Kenija, Lesoto, Gajāna, Grenāda, Sjerraleone, Esvatīni, Tanzānija, Malāvija**: visi 2221 Nursing Professionals
- **AFRISTAT** (reģionālais Rietumāfrikai): 2221 Cadres infirmiers

---

### Galvenais atklājums ievadījumam

Viens un tas pats 4-ciparu ISCO kods 2221 dažādās valstīs nozīmē **fundamentāli atšķirīgas profesijas**:

- **Medmāsas** (pareizi pēc ISCO-08) — valstīs EE, MN, SA, ZA, PS, LV, LT, MK, EC, IS, BY un ~30 citās valstīs.
- **Ārsti** — UA, DZ.
- **Finanšu brokeri** — AU, NZ.
- **Arhitekti** — IT, SM.
- **Tehniskie speciālisti** (ģeodēzija, dizains) — CA.

Tā nav "tulkojuma kļūda". Tie ir divi pilnīgi atšķirīgi klasifikācijas pasaules zem viena numura. Ukrainas ārsts-kardiologs (kods 2221.2) ierodas Vācijā ar dokumentiem, kur rakstīts "ISCO 2221" — vācu sistēma automātiski uzskata viņu par medmāsu. Austrālijas preču tirgotājs (kods 222111) pārvācas uz ES, un viņa karjera sistēmā tiek klasificēta pēc 2221 saimes, kas ES nozīmē medmāsu.

---

**Metodes.** Savāktie dati ir izvietoti vietnē <https://gsco.io>. GSCO (Globālais Standarta Profesiju Klasifikators) — datubāze, kas izmanto 4-ciparu ISCO-08 kodus kā universālu centru juridiski autoritatīvu terminu, kas apzīmē profesijas, no vairāk nekā 140 nacionālajiem valdības reģistriem, apkopošanai. Metodoloģija balstās tikai uz precīzu teksta atbilstību oficiālajiem avotiem (ESCO, KBJI, MASCO, NCO, OKZ, CBO, KeSCO un citiem), pilnībā izslēdzot neironu mašīntulkošanu. SQLite kešs, kas satur 26 991 profesiju ierakstu no Wikidata 53 valodās, ļauj veikt iepriekš pārbaudītu pakešu rediģēšanu.

**Rezultāti.** Iegūtais datu kopums satur 152 135 daudzvalodu etiķetes, 98 335 pseidonīmus un 76 734 aprakstus 53 valodās, kas iegūti no 146 analizētajiem nacionālajiem reģistriem, kopumā 263 608 profesiju ierakstus.

**Secinājums.** Dati tika savākti un salīdzināti automātiski, un tie prasa katra 2026. gadā aktuālā valsts profesiju klasifikatora manuālu pārbaudi. Es to nedarīju, lai netērētu personīgo laiku. Lai šo uzdevumu risina Starptautiskās Darba organizācijas (SDO) un nacionālo ministriju darbinieki — viņiem tam ir piešķirti budžeti un resursi. Mans uzdevums ir nevis veikt visu pasaules valstu darba ministriju darbu, bet aktualizēt problēmu.

**Atslēgvārdi:** profesiju klasifikācija, ISCO-08, daudzvalodu datubāze, Wikidata, zināšanu grafu bagātināšana, deterministiska atbilstība, krusttabula, ESCO, darba tirgus, NLP etalons, aptauju kodēšana, valodas ar ierobežotiem resursiem, atklātie dati, saistītie dati, semantiskais tīkls, ontoloģiju atbilstība, SDO, etalona dati, botu automatizācija, taksonomiju izlīdzināšana.

---

## 1. Ievads: No Nobela prēmiju laureātiem līdz globālai datu krīzei

### 1.1 Praktisks strupceļš: kad ekonomisti tika ierakstīti kā džeza mūziķi

Projekts radās no ambicioza, bet no pirmā acu uzmetiena lokāla uzdevuma: novērst kritisko datu trūkumu par pasaules zinātnisko un kultūras eliti atklātās zināšanu bāzēs. 890 vēsturisko Nobela prēmiju laureātu analīze atklāja satraucošu statistiku — dāvinātāju vairākumam trūka elementāru aprakstu aptuveni 260 no 300+ esošajām Vikipēdijas valodu versijām. Piemēram, Nobela miera prēmijas laureātam Desmondam Tutu projekta sākuma brīdī bija apraksti ļoti mazā skaitā valodu sadaļu — absurds tik nozīmīgas vēsturiskas personas gadījumā.

Lai novērstu šo plaisu, mēs izstrādājām deterministisku botu (ReNeuralAgent) daudzvalodu profilu automātiskai izveidei Wikidata pēc vienkāršas veidnes: `"{profesija} no {valsts}"`. Tomēr pirmie testa palaidumi atklāja liela mēroga digitālu katastrofu. Zināšanu grafs tika piesārņots ar kļūdainām asociācijām. Profesija "ekonomists" tika klasificēta kā "džeza mūziķis" malajiešu un indonēziešu tulkojumos. Kad sistēma mēģināja apzīmēt "pilsētu plānotājus", tā radīja "ādas apstrādes plānotājus", bet "sistēmu administratori" neizskaidrojami pārvērtās par "botāniķiem".

Problēma nebija mūsu kodā, bet gan starptautiskās profesiju klasifikācijas fundamentālajā infrastruktūrā.

### 1.2 Katastrofas anatomija: SDO birokrātiskā laika bumba

Šo absurdo "halucināciju" izmeklēšana noveda pie Starptautiskās Darba organizācijas (SDO) novecojušās paradigmas. Vēsturiski šī ANO struktūra ir atbildīga par Starptautiskās standartizētās profesiju klasifikācijas (ISCO) publicēšanu. Atjaunināšanas cikls ir vidēji 20 gadi: jaunas versijas tika izlaistas 1958., 1968., 1988. un 2008. gadā [1].

Visacīmredzamākā problēma — nevis lēnīgums, bet metodoloģija. Katrs jaunais izdevums ietver pilnīgu skaitlisko kodu pārkārtošanu bez atpakaļejošas saderības. Spilgtākais piemērs: kods **2131**. ISCO-88 (1988) šis kods apzīmēja programmētājus un sistēmu izstrādātājus. Līdz 2008. gadam SDO pilnībā restrukturēja IT sektoru un pārdalīja atbrīvoto kodu 2131 uz… biologiem, botāniķiem un zoologiem [1].

Mūsdienu informācijas sistēmas — ieskaitot pašu Wikidata — turpina balstīties uz novecojušām īpašībām. Īpašība **P952** Wikidata glabā novecojušos ISCO-88 kodus. Mūsu empīriskā Wikidata profesiju keša analīze parāda šīs stagnācijas pilnu mērogu:

| Īpašība | Standarts | Elementi ar datiem | Segums |
|----------|----------|---------------:|--------:|
| P3008 | ISCO-08 (pašreizējais) | 0 | 0.0% |
| P952 | ISCO-88 (novecojis, 1988) | 299 | 1.1% |
| Neviens | — | 26 692 | 98.9% |

*1. tabula: ISCO īpašību segums 26 991 profesiju Wikidata elementos (2026. gada aprīlis). P3008 (ISCO-08) ir pilnīgi tukšs, savukārt P952 (ISCO-88) sedz tikai 1.1% elementu. Atlikušajiem 98.9% profesiju nav neviena standartizēta klasifikācijas koda.*

Tas nozīmē, ka algoritmi, kas mēģina sinhronizēt datus, izmantojot šos skaitliskos identifikatorus, vai nu neatradīs neko (98.9% gadījumu), vai izgūs kodus no 38 gadus veca standarta, kur programmētāji ir pārdalīti uz biologiem.

### 1.3 Apzināšanās: nepieciešams jauns standarts

Šis praktiskais strupceļš skaidri parādīja, ka novecojušu skaitlisko kodu izmantošana navigācijai mūsdienu darba tirgū ir lemta neveiksmei. Algoritmiskā minēšana ar neironu tīkliem arī neizdodas valodu halucināciju dēļ retajās valodās. Bija nepieciešama principiāli atšķirīga pieeja — pāreja no abstraktu skaitļu uzticēšanās uz stingru tekstuālu determinismu, kas balstīts uz nacionālo likumdošanu.

Šī izpratne radīja GSCO (Global Standard Classification of Occupations) datubāzi.

*Anomālija ar ekonomistiem-kā-džeza-mūziķiem nebija tikai Wikidata datu kvalitātes problēma, bet gan fundamentālas nesaderības starp globālo darba datu infrastruktūru un mūsdienu cilvēku mobilitātes mērogu simptoms. Starptautiskā Darba organizācija, ar raksturīgu statistisko piesardzību, 2008. gadā izstrādāja ISCO-08 pasaulei ar 190 miljoniem starptautisko migrantu [33]. Līdz 2024. gadam — tikai pēc 16 gadiem — šis skaitlis sasniedza aptuveni 280 miljonus, bēgļu skaits pieauga no 16 līdz 37 miljoniem, bet iekšēji pārvietoto personu skaits — no 26 līdz 75 miljoniem. Pasaule, kurai tika veidots ISCO-08, vairs nepastāv.*

### 1.4 Pašreizējā situācija: migrācijas paātrinājums

Mūsdienu cilvēku mobilitātes mērogs padara neatbilstību starp ISCO pārskatīšanas birokrātiskajiem cikliem un reālo darba tirgus sarežģītību nevis tikai akadēmisku jautājumu, bet humānu krīzi. Skaitļi runā paši par sevi:

| Gads | Starpt. migranti | Bēgļi | Iekšēji pārvietotās personas | Darba migranti |
|------|---------------|----------|------|-----------------|
| 1988 (ISCO-88 bāze) | ~70M | ~14M | ~5M | ~80M |
| 2008 (ISCO-08 bāze) | ~190M | ~16M | ~26M | ~120M |
| **2024** | **~280M** | **~37M** | **~75M (15×!)** | **~169M** |
| Prognoze 2035 | ~350M+ | ~50M+ | ~100M+ | apt. 200M+ |

*2. tabula: Migrācijas paātrinājums 1988.–2024. gadā (UN DESA / ILO 2024). ISCO-08 tika izstrādāts pasaulei ar 190 miljoniem starptautisko migrantu; līdz 2024. gadam šis skaitlis pieauga līdz 280 miljoniem, bet iekšēji pārvietoto personu skaits pieauga 15 reizes salīdzinājumā ar 1988. gada līmeni.*

Kanōnisks Friedberg pētījums [34] noteica, ka ārvalstu izglītības sertifikātiem ir gandrīz nulles pārnesama ekonomiskā vērtība galamērķa valstu darba tirgos bez kopīgas klasifikācijas infrastruktūras — šis secinājums arvien biežāk tiek apstiprināts dažādās jurisdikcijās. Sīriešu ārsti, kas iesniedz pieteikumus Vācijas Approbation (medicīnas licencei), vidēji gaida 14 mēnešus verifikācijai koda līmenī [35]. Filipīniešu medmāsas Japānā uzkrāj 15 gadu eksāmenu nokārtošanas rādītāju 14%, daļēji kalibrēti uz japāņu profesiju kodu saimēm. Bangladešas sievietes — aptuveni 800 000 cilvēku — sistemātiski tiek piespiedu kārtā klasificētas kā "mājas darbinieces", ierodoties Persijas līča valstīs, neatkarīgi no viņu faktiskās profesionālās pieredzes [36].

Tie nav izolēti gadījumi. Tā ir strukturāla rezultāts arhitektūrai, kurā 146 nacionāli autoritatīvi profesiju klasifikatori nav kopīga centra — matemātiska neiespējamība, ko GSCO risina caur ISCO-08 centra arhitektūru, kas aprakstīta §4.

---

## 2. Tradicionālās klasifikācijas fundamentālās problēmas

Kļūda, kas tika atklāta, mēģinot marķēt profesijas Wikidata, izrādījās nevis lokāla platformas kļūda, bet gan dziļas metodoloģiskas krīzes simptoms. Četras fundamentālās problēmas padara tradicionālās klasifikācijas metodes nederīgas globālā mērogā.

### 2.1 N² slazds: krusttabulu matemātiskais kolapss

Vēsturiski, lai dažādi reģistri "saprastu" viens otru (piemēram, saistīt amerikāņu O\*NET ar Eiropas ESCO), ministrijas izveido divpusējas krusttabulas (mappings) [2]. Tomēr ontoloģiju arhitektūras pētnieki ir pierādījuši, ka šis ceļš ved uz matemātisku strupceļu [3]. Šādu saišu izveide pakļaujas **N² problēmai**: *n* standartiem saišu aktualitātes uzturēšanai ir nepieciešams ģenerēt *n(n-1)/2* krusttabulas.

$$C(n) = \frac{n(n-1)}{2}$$

50 nacionālajiem reģistriem tas dod **1 225 divpusējas krusttabulas**, katrai no kurām ir nepieciešama manuāla uzturēšana katrā atjaunināšanas ciklā. Šis eksponenciālais pieaugums padara manuālu sinhronizāciju globālajā darba tirgū fiziski neiespējamu [3].

Ar GSCO dokumentēto 146 nacionāli autoritatīvo profesiju klasifikatoru skaitu (2026. gada aprīlis), n² telpa prasa:

$$C(146) = \frac{146 \times 145}{2} = \textbf{10 585 divpusējas krusttabulas}$$

Katra no šīm 10 585 tabulām tiek invalīda jebkura viena reģistra atjaunināšanas gadījumā. Manuāla uzturēšana šādā mērogā ir ne tikai nepraktiska; tā ir matemātiski nesaderīga pat viena iesaistītā reģistra empīriskajam atjaunināšanas tempam. Krievijas ОК 016-2025 — aizstājot 1994. gada versiju pēc 30 gadu pārtraukuma — ilustrē, ka pat viena reģistra atjauninājumi ir daudzgadīgi administratīvi uzņēmumi [37].

Pat AI nevar glābt situāciju. Kad Eiropas Komisija mēģināja izmantot NLP pieeju (balstītu uz BERT) ESCO 3 000 profesiju sasaistīšanai ar O\*NET 1 000 profesijām, algoritms radīja 7 385 potenciālus sakritības, kas joprojām prasīja manuālu cilvēka verifikāciju, turklāt aptuveni 600 profesijas palika nesasniegtas [4].

### 2.2 Hierarhiskā kļūda: bloķēšanas problēma

Otrā sistēmiskā ievainojamība slēpjas klasifikatoru koku struktūrā. Datubāzēm, piemēram, ISCO-08, ir stingra 4 līmeņu hierarhija: no plašām galvenajām grupām līdz 436 šaurām vienotajām grupām [1].

Datorlingvistikā un mašīnmācīšanā tas rada parādību, kas pazīstama kā **bloķēšanas problēma** vai kaskādes kļūdu izplatīšanās [5]. Kļūda, kas pieļauta augstākajā līmenī (piemēram, ja sistēma kļūdaini piešķir profesionālu lomu "tehniķiem" nevis "vadītājiem"), kaskādes veidā izplatās uz leju, matemātiski garantējot, ka visi turpmākie, detalizētāki klasifikācijas līmeņi šim elementam būs nepareizi [5, 6].

Veidojot Wikidata kešu GSCO, mēs saskārāmies ar šo problēmu tieši: SPARQL pieprasījums `wdt:P31/wdt:P279* wd:Q28640` apiet `subclass-of` ķēdi un atgriež elementus, kas faktiski nebija profesijas — ieskaitot Lexeme senses (piemēram, `L1371064-S1`), kas bija jāfiltrē programmatiski.

### 2.3 Kodu piešķiršanas aptauju precizitātes ilūzija

Trešā problēma atklāj manuālā darba subjektivitāti. Iedzīvotāju skaitīšanu laikā respondenti apraksta savas profesijas brīvā tekstā. Sociologi pēc tam mēģina manuāli piešķirt šīs atbildes standartizētiem kodiem [7].

Oficiālie OECD ziņojumi norāda, ka pat ar vienkāršotu trīslīmeņu kodēšanas shēmu (350 kategorijas) vienošanās panākšana starp kodētājiem virs 75% rada nopietnu problēmu [8]. Starptautiskās aptaujas ziņo par vienošanās rādītājiem no 44% līdz 89% [9]. Nesenie mēģinājumi automatizēt šo procesu ar AI nav atrisinājuši problēmu: labākais automātiskās profesiju kodēšanas modelis IEA sasniedza tikai 63% precizitāti 12 valodās, paredzot to pašu grupu, ko cilvēku kodētāji, — 37% kļūdu, kas uzkrājas miljoniem atbilžu aptaujās [19].

Beresewicz et al. (2024) [20] parādīja, ka pat daudzvalodu hierarhiskie transformatori (XLM-RoBERTa, apmācīti uz KZiS + ISCO) atpaliek no deterministiskām precīzas atbilstības sistēmām darba sludinājumos retajās valodās, īpaši slāvu un Baltijas valodām, kur apmācības dati ir niecīgi. Šis aprēķinu strupceļš ir strukturāls, nevis pagaidu — Djumalieva un Sleeman [38] apgalvo, ka ekspertu kurētas taksonomijas ir "pēc būtības lēnas un dārgas", un piedāvā alternatīvas, kas balstītas uz datiem, ko GSCO operacionālizē caur savu "rumbas un spieķu" (hub-and-spoke) arhitektūru.

Izmaksas ir milzīgas: šie kodi ir sociāli ekonomiskā statusa (SES/ISEI) indeksu pamatā [10]. Ja viens kodētājs klasificē fermera aprakstu kā "Lauksaimniecības vadītājs" (kods 1310), viņa statusa indekss saņem 49 punktus. Ja cits kodētājs piešķir viņam "Pašnodrošinātie fermeri" (kods 6200), indekss nokrītas līdz 10 punktiem [10]. Sistemātiskas interpretācijas atšķirības iznīcina pašu socioloģiskās mērīšanas pamatu starptautiskā mērogā.

### 2.4 Kvalifikācijas atzīšanas procedūras krīze

Ceturtā problēma — tā, ar kuru tieši saskaras miljoniem strādājošo cilvēku: kvalifikācijas atzīšanas cauruļvads. Tiesiskais pamats kvalifikāciju portabilitātei — ES Direktīva 2005/36/EC par profesionālo kvalifikāciju atzīšanu — darbojas kopš 2005. gada, tomēr uz 2024. gada decembri Eiropas Komisija ir uzsākusi pārkāpuma procedūras pret Beļģiju, Vāciju, Franciju, Luksemburgu un Nīderlandi par tās modernizācijas prasību neieviešanu [39]. Līdz 2025. gada maijam Itālija pievienojās šim sarakstam: 11 861 rumāņu medmāsa tieši cieta no Direktīvas 2024/505 nepieņemšanas [40].

Vācijas piemēra empīriskie dati ilustrē disfunkcijas mērogu. Vācijas Ekonomikas institūta (Institut der Deutschen Wirtschaft, IW) 2025. gada ziņojums dokumentē 450 000 kvalificētu darbinieku trūkumu, turklāt 80% vācu uzņēmumu ziņo, ka vispār neizmanto formālo atzīšanas sistēmu, bet 51.6% novērtē atzīšanas procesu negatīvi [41]. Vienā federālajā zemē Approbation izmaksas svārstās no €170 līdz €850 atkarībā no Bundesland — tas ilustrē, ka atzīšana nav harmonizēta pat Vācijas iekšienē, nemaz nerunājot par pārrobežu [42].

Neatbilstība izplatās arī uz rezultātiem, ne tikai uz izmaksām. Francijas ārstu pieteikumi Vācijas atzīšanai sasniedz 40.3% apstiprināšanas līmeni; tie paši franču pretendenti, kas meklē atzīšanu Luksemburgā, sasniedz 99.8% [41]. Šī 60 procentpunktu atšķirība pastāv starp jurisdikcijām, abām īstenojot to pašu ES Direktīvu, atspoguļojot nevis juridisko nenoteiktību, bet klasifikācijas berzi — atšķirīgas detalizācijas shēmas, atšķirīgas kodu saimes, atšķirīgas interpretācijas tam, ko nozīmē "ekvivalents" salīdzinot profesiju ierakstus starp reģistriem.

ZorgSaam gadījums no pierobežas Nīderlandes-Beļģijas reģiona ilustrē absurdo visasišķākajā formā: kvalificēts beļģu neirologs no Universitair Ziekenhuis Gent — fiziski 30 km attālumā no Nīderlandes slimnīcas, kas saskaras ar akūtu neirologu trūkumu — tika aizkavēts ar Nīderlandes BIG-register prasībām un pārrobežu klasifikācijas neatbilstību reģionā, kur abas valstis darbojas Šengenas brīvas pārvietošanās un tās pašas ES Direktīvas ietvaros [42].

Sumption [43] pamatīgā analīze atklāja strukturālo virzītājspēku: profesionālās asociācijas darbojas kā vārtsargi bez institucionāliem stimuliem iztīrīt rindu, radot "viss vai nekas" slazdu atzīšanā, kas pārvērš daļēju ekvivalenci pilnīgā izslēgšanā. Informācijas asimetrija ir divpusēja: darba devēji nevar verificēt ārvalstu kvalifikācijas un pēc noklusējuma izvairās no riska; migranti nevar iesniegt savas kvalifikācijas galamērķa sistēmas kodu saimē, jo mašīnlasāms tilts nepastāv.

Tie nav "galējie gadījumi" vai "pārejas berze". Tas ir stabils rezultāts infrastruktūrai, kas izstrādāta mazākai, lēnākai pasaulei.

---

## 3. Mākslīgā intelekta ilūzija: valodu modeļu ierobežojumi

### 3.1 Semantiskā dreifēšana un polisēmijas slazdi

Neironu tīkli balstās uz varbūtībām un vēsturiskiem datiem, bet valoda ir dzīva substance, kas pakļauta pastāvīgām izmaiņām, parādība, kas pazīstama kā **semantiskā dreifēšana** [11]. COVID-19 pandēmijas laikā tādi vārdi kā "neaizsargāts" un "izolēts" vairs nebija kopīgi sociāli apzīmētāji un kļuva par specifiskiem medicīniskiem terminiem, pārkāpjot algoritmu vēsturiskos valodu sadalījumus [12].

Profesionālos kontekstos polisēmija pasliktina problēmu. Kā atzīmēja viena NLP klasifikatora veidotāji: "Vārds 'skill' var attiekties uz tehniskām prasmēm, starppersonu prasmēm vai pat uz noteiktu zivju veidu, atkarībā no konteksta" [13]. AI bieži nevar atrisināt šādu nenoteiktību bez milzīgiem apmācības datu apjomiem. Parādība nav metaforiska; JobBERT no Decorte et al. [14] un kontrastējošais XLM-RoBERTa no Gasco un Retyk [44] abi ziņo par veiktspējas degradāciju, jo viņu apmācības korpusi noveco pēc 18 mēnešiem, padarot pagaidu uzturēšanu par atklātu problēmu jebkurai varbūtības pieejai profesiju klasifikācijai.

### 3.2 Aprēķinu trauslums

Kad pētnieki mēģināja GPT-4 piebarot reālu darba sludinājumu tekstu paraugus, modelis "nevarēja radīt korektus sakritības 33.9% gadījumu, vienlaikus prasot vidēji 515 000 ievades tokenu, lai apstrādātu vienu darba sludinājumu" [14]. Milzīgie aprēķinu izdevumi padara šādas pieejas nepraktiskas globālā mērogā.

Pat speciāli veidoti modeļi, piemēram, JobBERT, atzīst savus fundamentālos ierobežojumus: to arhitektūra "pēc būtības ir piesaistīta iepriekš noteiktam (un tāpēc statiskam) standartizētu nosaukumu sarakstam, kas ierobežo tās praktisko izmantošanu" [15]. Neironu tīkli paliek "trausli, kad rodas vārdnīcas neatbilstības (sinonīmi, parafrāzes un vietējais žargons)" [15].

Visjaunākais mēģinājums — XLM-RoBERTa apmācība uz LLM precizētiem Šveices darba sludinājumiem — sasniedza tikai 58.3% Top-1 precizitāti uz sudraba datiem (salīdzinājumā ar 37.2% pirms apmācības) un 80% precizitāti uz atliktajiem testa datiem [17]. Lai gan autori ziņo par 91.4% precizitāti, prognozējot ontoloģijas nosaukumus (vienkāršota uzdevums), atšķirība starp 80% un 100% precizitāti, ko var sasniegt ar deterministisku atbilstību, paliek fundamentāla, nevis inkrementāla.

Atšķirībā no tā, mūsu `gsco_esco_mapper.py` veic precīzu angļu etiķešu atbilstību ar lokālo SQLite kešu — 2 942 ESCO profesijas tiek saskaņotas milisekundēs, ar nulles aprēķinu izmaksām, ar nulles halucināciju risku.

### 3.3 Zero-shot pārneses neveiksme

Vispostošākais trieciens uz tēzi "AI izglābs pasauli" ir reto valodu problēma. Eiropas Komisijas oficiālais ziņojums par mašīntulkošanas palīdzības datu saskaņošanu tieši atzīst šo ievainojamību: "daudzvalodu kodētāji nevar uztvert līdzību, kad avota un mērķa valodas ir mazāk līdzīgas morfoloģijas, sintakses un semantikas līmeņos" [4, 18]. Kad EK mēģināja veikt ML-palīdzības saskaņošanu nacionālo klasifikāciju ar ESCO, izmantojot XLM-RoBERTa, Top-1 precizitāte svārstījās no 83.5% (ASV) līdz tikai 45.3% (Latvija) — morfoloģiski bagātā baltu valoda izrādījās visizturīgākā pret neironu pārnesi [18].

Visaptverošs literatūras apskats parāda, ka **nevienam esošajam pētījumam nav sasniegta >95% precizitāte daudzvalodu profesiju klasifikācijā 10 vai vairāk valodās vienlaicīgi.** Visplašākā daudzvalodu novērtēšana — Beręsewicz et al. hierarhiskā klasifikācija 24 valodās — sasniedza tikai ~84% precizitāti visplašākajā 1-ciparu galveno grupu līmenī, nokrītot līdz 40–60% uz granulētiem 6-ciparu kodiem [20]. 12-valodu IEA modelis sasniedza 92% uz tīriem mašīntulkotiem testa datiem, bet sabruka līdz 36% uz reālām atbildēm aptaujās [19]. Šie rezultāti nosaka stingru veiktspējas griestu varbūtības pieejām, ko GSCO deterministiskā metodoloģija pilnībā apiet.

Šis ierobežojums ir īpaši akūts persiešu, bengāļu, khmeru, birmiešu, tagalu un laosiešu valodām — tieši lielāko mūsdienu kvalificētās migrācijas koridoru avota valodām (Irāna → Vācija, Bangladeša → Saūda Arābija, Nepāla → Koreja, Filipīnas → Japāna, Kambodža/Mjanma → Taizeme). Mūsu pašu migrācijas gadījumu bibliotēku (2026) veidošanā (aptverot 40+ valodas 7 reģionālās partijās), vairāk nekā puse dokumentēto gadījumu slāvu, dienvidaustrumu Āzijas un persiešu-indiešu partijās pastāvēja tikai angļu valodā esošajos sekundārajos spoguļos oriģinālās reportāžas — apstiprinot, ka šīs valodas ir strukturāli nepietiekami apkalpotas ar neironu pieejām, kas apmācītas uz tīkla mēroga korpusiem.

Globālam projektam, kura mērķis ir aprakstīt cilvēkus suahili (214 etiķetes Wikidata), hausā (221 etiķete) vai jorubā (63 etiķetes), paļaušanās uz AI tulkojumiem garantētu neveiksmi. Neironu tīkli vienkārši nav redzējuši pietiekami daudz tekstu par "kvantu fiziķiem" hausā, lai radītu precīzu, juridiski derīgu terminu.

---

## 4. GSCO arhitektūra: deterministisks risinājums

### 4.1 Juridiskais "ground truth" nevis varbūtības

GSCO arhitektūrā mēs pilnībā atteicāmies no mašīnas minēšanas. Fundamentālais princips — **stingrs juridiskais determinisms** (Legal Ground Truth). Ja konkrētās valsts Darba ministrija ir apstiprinājusi oficiālu profesijas nosaukumu nacionālajā valodā, šis termins tiek pieņemts kā absolūts standarts bez jebkādas papildu semantiskās analīzes. Ja oficiālais Latvijas reģistrs saka, ka termins ir "santehniķis", bet hausā vārdnīca apgalvo, ka fiziķis ir "masanin ilimin lissafi", šie termini tiek iekļauti datubāzē kā ir. Nekādu neironu kropļojumu, nekādu tulkojumu uzlidojumā — tikai 100% precīzas sakritības ar valsts standartiem.

### 4.2 ISCO-08 kā Rozetes akmens: N² sašaurināšana līdz O(n)

Centrālais tehniskais uzdevums bija apiet N² krusttabulu slazdu. Risinājums tika atrasts ISCO-08 struktūrā, kas visas pasaules profesijas sadala 436 vienotajās grupās, katra apzīmēta ar universālu 4-ciparu kodu [1].

Tā vietā, lai mēģinātu tieši savienot Indonēzijas reģistru ar Malaizijas vai ASV reģistru, mēs katru no 146 nacionālajiem reģistriem savienojām ar šo centrālo 4-ciparu centru:

$$\text{Sarežģītība: } O\left(\frac{n(n-1)}{2}\right) \rightarrow O(n)$$

146 reģistriem: **10 585 krusttabulas → 146 saites ar centru**. ISCO-08 kļuva par "Rozetes akmeni", caur kuru jebkura valoda var tikt acumirklī pārtulkota uz jebkuru citu bez jēgas zuduma.

Praksē kods 2111 ("Fiziķi un astronomi") tiek saskaņots ar:
- Krievija (OKZ): 2111.1 (fiziķis-pētnieks)
- Brazīlija (CBO): 2111-05
- Indonēzija (KBJI): 2111.01
- Wikidata: Q169470

Tā nav tikai programmatūras inženierijas optimizācija. Kā Autor, Levy un Murnane parādīja savā kanoniskajā uzdevumu bāzētās tehnoloģiskās pārmaiņu sistēmā [45], profesionālās uzdevumi nepārtraukti attīstās, kamēr profesionālie kodi tiek pārskatīti ik pēc 20 gadiem. "Rumbas un spieķu" arhitektūra tāpēc nav tikai līdzeklis pret n² sarežģītību — tā ir vienīgā arhitektūra, kas ir saderīga ar nepārtrauktu uzdevumu evolūciju reģistru malās un stabilu kodu semantiku centrālajā centrā.

`gsco_esco_mapper.py` realizācija izmanto divas saskaņošanas metodes:
1. **Galvenā:** `build_en_label_to_qid_map()` — precīza angļu etiķešu saskaņošana (588 veiksmīgas saskaņošanas no ESCO)
2. **Rezerves:** `build_isco_to_qid_map()` — saskaņošana pēc ISCO-08 koda (0 rezultātu, jo P3008 ir tukšs Wikidata)

Fakts, ka ISCO-08 rezerves variants atgrieza nulles saskaņojumus, ir empīrisks pierādījums tam, ka Wikidata profesiju infrastruktūra nav tikai novecojusi — tā ir strukturāli atvienota no pašreizējā starptautiskā standarta.

### 4.3 Agregācija: cilvēka un AI simbioze

Lai gan konceptuālā pamatne bija stingra un deterministiska, fiziskā datu vākšana bija milzīga tehniskā problēma. Daudzas valstis (īpaši Āfrikā, Āzijā un Tuvajos Austrumos) publicē savus profesiju reģistrus nevis kā ērtus API, bet kā simtiem lappušu PDF dokumentus, bieži vien ar bojātām kodēšanām vai tekstu no labās uz kreiso pusi (RTL).

AI asistents (Claude Code) tika izvietots nevis kā "tulkotājs", bet kā "rokas darbs" — valsts tīmekļa vietņu skenēšana, piekļuves ierobežojumu apišana un sarežģītu PDF dokumentu parsēšana autonomā fona režīmā. Kritiskā atšķirība: AI nodarbojās ar izgūšanu, bet katrs saskaņošanas lēmums palika deterministisks (precīza sakritība vai atteikums).

Iegūtā agregācija (reprezentatīva izlase):

| Avots | Valsts/Reģions | Valodas | Profesijas |
|--------|---------------|-----------|------------:|
| ESCO v1.2.1 | 28 ES valstis | 28 | 2 942 |
| ISCO-TR | Turcija | tr | 7 202 |
| KeSCO | Kenija | en, sw | 6 582 |
| BSCO | Bangladeša | bn, en | 5 387 |
| YAMAT-08 | Mongolija | mn | 4 844 |
| KZBiH-08 | Bosnija un Hercegovina | bs | 4 246 |
| NCO-2015 | Indija | en, hi | 3 452 |
| KBJI-2014 | Indonēzija | id | 2 731 |
| CBO | Brazīlija | pt-BR | 2 614 |
| TSCO | Taizeme | th, en | 2 812 |
| CORM | Moldova | ro, ru | 4 369 |
| NOC 2021 | Kanāda | en, fr | 822 |
| SINCO | Meksika | es | 686 |
| NKZ-2022 | Tadžikistāna | ru | 1 714 |
| SSCO 2024 | Saūda Arābija | ar, en | 2 738 |
| + 131 cits | Dažādas | Dažādas | Dažādas |
| **Kopā** | **146 reģistri** | **53+ val.** | **263 608** |

*3. tabula: Nacionālo profesiju reģistru reprezentatīva izlase, kas agregēta GSCO v1.1. Katrs ieraksts ir juridiski autoritatīvs termins, ko publicējis nacionālais statistikas birojs vai darba ministrija.*

---

## 5. Tehniskā realizācija un pilotrezultāti

### 5.1 Precīzas atbilstības cauruļvads

Galvenā metodoloģija noraida aklo uzticēšanos vēsturiskiem skaitliskiem kodiem, dodot priekšroku stingram tekstuālam determinismam. Algoritms ņem angļu profesijas etiķeti, atrod tās precīzu sakritību etalona reģistrā (piemēram, ESCO) un izgūst valdības apstiprināto tulkojumu mērķa valodā.

Realizācija sastāv no pieciem Python moduļiem:

1. **`gsco_wikidata_cache.py`** — Nedēļas SPARQL dumps visiem profesiju elementiem Wikidata lokālā SQLite datubāzē. Apstrādā API sadalīšanu pa daļām (Wikidata ierobežo 50 valodas uz pieprasījumu `wbgetentities`), filtrē ne-Q elementus (Lexeme senses), glabā etiķetes, sinonīmus un aprakstus 53 valodās.

2. **`gsco_esco_mapper.py`** — Saskaņo ESCO profesijas ar Wikidata QID, izmantojot deterministisku precīzu angļu etiķešu saskaņošanu. Funkcija `find_best_qid()` īsteno trīslīmeņu uzticības sistēmu: (a) precīza sakritība, (b) vārdu krustojuma rādītājs ≥ 0.5, (c) ISCO-08 koda rezerves variants.

3. **`gsco_edit_queue.py`** — Iepriekš validēta rediģēšanas rinda ar uzticības līmeņiem. Katrs labojums tiek pārbaudīts pret Wikidata tiešraides statusu pirms nosūtīšanas — tiek aizpildīti tikai tukši lauki, esošie dati nekad netiek pārrakstīti.

4. **`gsco_edit_daemon.py`** — Izpilda labojumus caur MediaWiki Action API ar drošības kontrolēm: `maxlag=5`, randomizētas aiztures 1.5–3.0 sekundes starp labojumiem, valodu izmēģinājuma periods (pirmie 50 labojumi jaunās valodās ir ierobežoti ar zema prioritātes QID) un dinamiska ātruma regulēšana (+20% ātrums nedēļā ar 0 noraidījumiem, samazināšana uz pusi ar jebkuru noraidījumu).

5. **`gsco_revert_monitor.py`** — Uzrauga noraidījumus ik pēc 10 minūtēm caur cron. Izveido failu `BOT_EMERGENCY_STOP` pie jebkura konstatēta noraidījuma, ierosinot tūlītēju bota izslēgšanu.

### 5.2 Wikidata kešs

SQLite kešs apkopo pašreizējo visu profesiju elementu stāvokli Wikidata:

| Tabula | Rindas | Shēma |
|-------|-----:|--------|
| `occupations` | 26 991 | `qid, isco08, isco88, en_label` |
| `labels` | 152 135 | `qid, lang, label` |
| `aliases` | 98 335 | `qid, lang, alias` |
| `descriptions` | 76 734 | `qid, lang, description` |

*4. tabula: GSCO Wikidata keša statistika (2026. gada 22. aprīlis). Kešs tiek pārbūvēts katru nedēļu caur cron un nodrošina katra labojuma iepriekšēju validāciju attiecībā pret pašreizējo Wikidata stāvokli.*

Valodu segums ir ļoti nevienmērīgs:

| Valoda | Etiķetes | Segums |
|----------|-------:|--------:|
| Angļu (en) | 18 749 | 69.5% |
| Vācu (de) | 14 470 | 53.6% |
| Franču (fr) | 10 177 | 37.7% |
| Holandiešu (nl) | 9 197 | 34.1% |
| Spāņu (es) | 8 197 | 30.4% |
| ... | ... | ... |
| Tagalu (tl) | 490 | 1.8% |
| Hindi (hi) | 432 | 1.6% |
| Hausa (ha) | 221 | 0.8% |
| Suahili (sw) | 214 | 0.8% |
| Joruba (yo) | 63 | 0.2% |

*5. tabula: Etiķešu segums pēc valodām profesiju elementos Wikidata. Eiropas valodas dominē; valodas, kurās runā miljardiem cilvēku (hindi, bengāļu, suahili), ir mazāk nekā 2% segums. GSCO tieši risina šo asimetriju.*

Strukturālie atklājumi no starpvalstu salīdzinājuma sniedz papildu pētniecības vērtību, kas pārsniedz seguma statistiku. Latvija un Igaunija neatkarīgi vienojās par ISCO 8131 (Ķīmisko un fotogrāfisko ražošanas procesu operatori) vienotās grupas sadalīšanu atsevišķās apakškategorijās — empīriski validējot kandidātu uz sadalīšanu, kas ierosināts ISCO-28, bez jebkādas koordinācijas. Tadžikistānas nacionālais klasifikators (NKZ-2022), lai gan atdala krievu valodu kā administratīvo ar Krievijas ОКЗ, demonstrē 75.9% leksikālo atšķirību 4-ciparu vienoto grupu līmenī — ar sistemātiski sajauktiem starp abiem kiriliskajiem reģistriem ISCO kodiem 7313, 7314 un 7315 (vitrāžists, podnieks, juvelieris). Brunejas BDSOC 2011 satur 1 381 profesijas nosaukumu 5-ciparu kodu līmenī vispār bez krusttabulas ISCO — "0/N paradokss", kur pastāv ievērojami empīriski dati, bet tie ir neredzami jebkurai sistēmai, kas pieprasa pēc ISCO koda.

### 5.3 Pilotrezultāti

Bots (ReNeuralAgent / MarisDreshmanisBot) tika izvietots zem Wikidata. Pilotfāze deva šādus rezultātus:

- **19 490+ kopējie labojumi** visos uzdevumos, **0 noraidījumi** — apstiprinot 100% deterministiskās pieejas semantisko drošību
- **1 122 GSCO-specifiski profesiju labojumi** 27 valodās (289 latviešu + 833 daudzvalodu)
- **4 202 labojumi rindā** izpildei 26 valodās, iepriekš validēti attiecībā pret Wikidata tiešraides statusu
- Bota karoga pieprasījums tiek izskatīts Wikidata (Wikidata:Requests for permissions/Bot)
- Katrs labojums tiek izsekots līdz avotam: labojuma kopsavilkuma formāts `Adding label from GSCO occupation database (I: GSCO, S: ESCO)`
- **AI/LLM izmantošana: nav.** Visas operācijas ir deterministiskas — apraksti balstīti uz veidnēm, precīza atbilstība, ierobežojumu pārbaude, HTTP verifikācija.

---

## 6. Praktiskie pielietojumi

### 6.1 Valdībām un regulatoriem (SDO, ESCO, O\*NET)

Šodien valsts iestādes tērē gadus un miljonus nodokļu maksātāju dolāru, lai izveidotu divpusējas krusttabulas starp saviem standartiem. Pieslēdzoties GSCO datubāzei, valdībām vairs nav nepieciešams veidot tiešus divpusējus tiltus un ciest no N² problēmas. Tā kā GSCO jau ir savienojis 146 nacionālos reģistrus ar centrālo ISCO-08 centru, sistēma darbojas kā globāls maršrutētājs.

Turklāt SDO savu standartu atjaunina tikai reizi 20 gados (ar pašreizējo pārskatīšanas procesu), un pat Eiropas Komisijas "nepārtrauktas uzlabošanas" process ESCO prasīja divus pilnus gadus kvalitātes nodrošināšanai, komiteju vienošanai un obligātai tulkošanai visās ES oficiālajās valodās, lai pievienotu tikai 68 jaunas profesijas 1.1 versijā. Digitālās transformācijas laikmetā, kad tādas profesijas kā "AI prompt engineer" vai "dronu operators" rodas un izplatās mēnešu laikā, šie birokrātiskie cikli ir strukturāli nepietiekami. GSCO pārvērš statisku PDF dokumentu dzīvā ekosistēmā: ja jauna profesija vienlaicīgi parādās piecu dažādu valstu reģistros, GSCO automātiski fiksē šo tendenci, sniedzot politikas veidotājiem dinamisku priekšstatu par mainīgo globālo darba tirgu.

### 6.2 AI izstrādātājiem un NLP inženieriem

AI izstrādātājiem vairs nav jācenšas parsēt netīrus darba sludinājumu tekstus un cerēt, ka neironu tīkls uzminēs pareizo tulkojumu. GSCO nodrošina AI laboratorijām gatavu, juridiski tīru etalona datu kopu (Golden Benchmark) 85+ valodās (ieskaitot persiešu, bengāļu, urdu un suahili). Katrs vārds šajā datubāzē ir pamatots ar konkrētas ministrijas vai nacionālā statistikas biroja autoritāti.

GSCO izmantošana apmācībai vai RAG arhitektūrām ļauj AI modeļiem sasniegt 100% juridisko un lingvistisko precizitāti profesiju klasifikācijā retākajām pasaules valodām, pilnībā novēršot halucinācijas. Datu kopas struktūra (`labels(qid, lang, label)`) nodrošina gatavus apmācības pārus: 26 991 profesija × N valodas = miljoniem izlīdzinātu pāru.

### 6.3 Sociologiem un statistiķiem

GSCO nodrošina sociologiem gatavu standartizētu vārdnīcu desmitiem valodu, automatizējot aptauju kodēšanas procesu. Integrācija esošajos kodēšanas paketēs (CASCOT, SOCcer, `occupationMeasurement`) var nodrošināt deterministisku rezerves variantu desmitiem jaunu valodu, strauji samazinot darbības izmaksas starptautiskos liela mēroga novērtējumos (ILSAs, piemēram, PISA vai ICILS).

Patiesa zinātniskā vērtība slēpjas projekta blakusproduktā — **atzīšanas matricā** (Matrix of Recognition). Uzklājot 146 nacionālos reģistrus, mēs iegūstam rīku, kas atklāj sociokulturālās un politiskās atšķirības starp valstīm. Piemēram, "dzīves koučs" ir oficiāli atzīts Latvijā (kā *personīgās izaugsmes veicināšanas speciālists*) un Lielbritānijā, bet pilnībā trūkst Krievijas klasifikatorā. Turcijas reģistrā ir 7 202 profesijas, kamēr Kanādas — tikai 822 — 9 reizes atšķirība, kas atklāj, cik atšķirīgi valstis konceptualizē savus darba tirgus.

### 6.4 Migrācijas krīzes un bēgļu uzņemšanas reaģēšanai

Konkrēta pielietojuma joma, kas nav saņēmusi pietiekamu uzmanību datorlingvistikas literatūrā, ir lielo bēgļu plūsmu uzņemšana un šķirošana darba tirgū. Kad uzņemošajai valstij ir jāapstrādā 5 000 prasmju profilu 30 dienu laikā, šaurā vieta ir nevis politiskā griba, bet klasifikācijas infrastruktūra: kvalifikācija, kas izsniegta vienā sistēmā, ir jāspēj mašīnlasāmi saskaņot ar otras sistēmas kodiem, pirms jebkura profesionālās licencēšanas iestāde var to novērtēt.

GSCO to risina tieši. Jebkuram strādājošam migrantam vai bēglim ar dokumentētu profesiju jebkurā no 146 indeksētajiem reģistriem, cauruļvads veic: etiķete dzimtajā valodā → 4-ciparu ISCO-08 kods → uzņemošās valsts klasifikatora etiķete, mazāk nekā vienā sekundē uz cilvēku. Slāvu partija mūsu migrācijas gadījumu bibliotēkā dokumentē Čehijas pieredzi ar 473 000 ukraiņu bēgļiem 2022. gadā, no kuriem 75% tika iekļauti ISCO 9 grupā (elementārās profesijas), lai gan vairumam bija augstākā izglītība — modelis, ko IOM dokumentējis kā "Pārmērīgi kvalificēti, nepietiekami nodarbināti" (Overqualified, Underemployed) [46]. Pat ja avota un uzņemošais klasifikators nomināli sakrīt (un Ukraina, un Čehija izmanto sistēmas, kas balstītas uz ISCO-08), mašīnlasāma tilta trūkums starp profesiju etiķešu saimēm rada plaisu, kas pēc noklusējuma noved pie pazemināšanas.

Bangladešas gadījums ar piespiedu klasifikāciju ilustrē asāku atteikuma režīmu: 800 000 migrējošās sievietes tiek ierakstītas Persijas līča valstu reģistros kā "mājas darbinieces" neatkarīgi no viņu faktiskās profesionālās pieredzes, jo uzņemošais klasifikators nesatur krustisko saiti ar avota reģistra profesionālajām kategorijām [36]. GSCO arhitektūra ļautu pareizu profesionālu šķirošanu iebraukšanas punktā — neatceļot juridiskās prasības, bet nodrošinot profesionālo kodu saiti, ko cilvēku administratori pašlaik veic manuāli, nekonsekventi un lielā mērogā.

Psiholoģiskais aspekts nepareizas klasifikācijas sniedzas tālāk par ekonomiskajiem zaudējumiem. Ngabirano 2026. gada sistemātiskais pārskats par franču valodā runājošiem migrantiem [47] dokumentē, ka *professionālā deklasēšanās* — piespiedu pazemināšana zemākā profesionālā kategorijā — ir viens no spēcīgākajiem psiholoģiskā stresa prognozētājiem augsti kvalificētās imigrantu populācijās, pārsniedzot pat valodas barjeras efektus. Klasifikācijas precizitāte šajā ziņā nav tikai datu kvalitātes problēma, bet sabiedrības veselības ieeja.

---

## 7. Ierobežojumi un turpmākais darbs

### 7.1 Pašreizējie ierobežojumi

1. **Seguma asimetrija.** Lai gan GSCO apkopo 146 reģistrus, daudzi ir koncentrēti Eiropā un Amerikā. Āfrikas reģistri ārpus Kenijas joprojām ir nepietiekami pārstāvēti. NMP-CI 2016 Kotdivuāras valsts aptver tikai amatniecības un rokdarbu sektorus, atstājot veselības aprūpes, jurisprudences un finanšu profesijas pilnībā nekvalificētas. 41 augšupielādētais PDF, kas gaida parsēšanu, ietver PACSCO (23 Klusā okeāna salu valstis), Irānu, Pakistānu un vairākas Latīņamerikas valstis.

2. **Atkarība no angļu etiķetēm.** Galvenā saskaņošanas metode balstās uz angļu etiķešu precīzu saskaņošanu. Profesijas, kas pastāv nacionālajos reģistros, bet kam nav angļu ekvivalenta Wikidata, nevar tikt automātiski saskaņotas. Tas ietekmēja aptuveni 80% ESCO profesiju, kurām netika atrasta precīza sakritība Wikidata (2 354 no 2 942). Kritiskais: Latvijas reģistrs ar 4 102 ierakstiem un Lietuvas ar 3 044 ierakstiem satur nulles angļu etiķetes — bloķējot automātisku kvalifikāciju atzīšanu angļu valodā runājošās mērķa sistēmās.

3. **Klasifikatoru metadatu "spoku" kļūdas.** Pašreizējā laidienā ir atklātas datu integritātes problēmas, kas atklātas kā P0 labojumi, gaidot risinājumu: Bosnijas spoku reģistrs ba_error_stub (metadatu aizstājējs bez pamata datiem); Jordānijas JSCO arābu reģistrs ar apstiprinātu RTL teksta apgriešanu; Brunejas 0/N paradokss (1 381 ieraksts parādīts kā 0% ISCO segums sakarā ar 5-ciparu kodu formātu, kas vēl nav saskaņots); un 540 Kotdivuāras ieraksti bez ISCO krusttabulas. Tās ir inženierijas kļūdas datu cauruļvadā, nevis trūkumi avota reģistros.

4. **Statiskais momentuzņēmums.** Pašreizējais laidiens (v1.1) ir momentuzņēmums. Nacionālie reģistri tiek atjaunināti ar dažādu periodiskumu — GSCO prasa periodisku atkārtotu agregāciju, lai paliktu aktuāls. Krievijas ОК 016-2025, kas aizstāj 1994. gada versiju pēc 30 gadu pārtraukuma, ieviesa AI operatora, kiberdrošības speciālista un drona operatora kodus, kas vēl nav atspoguļoti lejupējās krusttabulu sistēmās.

5. **Wikidata ontoloģijas trūkumi.** Atklājums, ka P3008 (ISCO-08) ir pilnīgi tukšs Wikidata, norāda, ka īpašības priekšlikums (Property Proposal) ISCO-08 sistemātiskai aizpildīšanai būtu vērtīgs, pirms GSCO var pilnībā izmantot kodu balstītu saskaņošanu.

6. **Indonēziešu, malajiešu, khmeru un laosiešu primārās valodas seguma trūkumi.** Oriģinālie dati šajās valodās bija ierobežoti indeksējami mūsu automatizētajā savākšanas cauruļvadā, kas nozīmē, ka Dienvidaustrumu Āzijas koridori ir nepietiekami pārstāvēti, neskatoties uz to nozīmi mūsdienu migrācijas plūsmās.

### 7.2 Turpmākie virzieni

1. **Mērogošana līdz Q5 elementiem.** Pašreizējais pilots koncentrējas uz profesiju elementiem (Q28640). Galīgais mērķis ir masveida aprakstu izveide aptuveni 11 miljoniem cilvēku profilu (Q5) Wikidata, izmantojot īpašību P106 (profesija), kas nodrošinās 50–100 miljonus daudzvalodu aprakstu.

2. **GSCO kā Wikidata atsauce (P248).** Pēc Zenodo DOI iegūšanas pats GSCO var kalpot kā atsauces avots Wikidata apgalvojumos, nosakot formālu datu izcelsmes ķēdi.

3. **Hugging Face datu kopums.** GSCO publicēšana Hugging Face padarīs to tieši pieejamu ML kopienai apmācībai un novērtēšanai.

4. **API galapunkts.** Publiskais REST API (`gsco.reincarnatiopedia.com/v1/occupation?isco=2111&lang=sw`) nodrošinātu programmatisku piekļuvi bez pilnas datu kopas lejupielādes.

5. **Krīžu uzraudzības sistēma (crisis-watch).** Dinamisks izbraukuma slānis, kas signalizē, kad bēgļu plūsmas no reģistrētajām avota valstīm pārsniedz sliekšņa līmeņus, nodrošinot proaktīvu reģistru sinhronizāciju pirms pieprasījuma pēc kvalifikācijas atzīšanas pieauguma.

6. **Integrācija ISCO-28 darba grupā.** SDO ISCO-28 pārskatīšanas process (mērķa datums 2028. gads) piedāvā reizi paaudzē iespēju ieejas datiem. GSCO jau ir identificējis empīriskus kandidātus: neatkarīga Igaunijas un Latvijas vienošanās par ISCO 8131 apakškodiem; bagātākā kalnrūpniecības profesiju taksonomija Mongolijā ārpus OECD; Kotdivuāras kakao sektora kodi bez pašreizējā ISCO ekvivalenta. Mērķis: formāla ieejas datu iesniegšana SDO ISCO-28 darba grupai līdz 2027. gada 2. ceturksnim.

7. **Pašatjaunošanās mehānisms.** Karstās pārslēgšanas cauruļvads, kas pieņem reģistru jaunās versijas, kad nacionālie statistikas biroji publicē atjauninājumus, izplatot izmaiņas krusttabulās bez pilnīgas atkārtotas agregācijas.

---

## 8. Secinājums

GSCO projekts sākās ar praktisku neveiksmi: mēģinājums pievienot daudzvalodu aprakstus 890 Nobela prēmiju laureātiem Wikidata atklāja kaskadējošu infrastruktūras krīzi — no SDO 20 gadu atjaunināšanas cikliem līdz pilnīgam ISCO-08 datu trūkumam Wikidata (0 no 26 991 elementiem).

Determinētā arhitektūra, kas šeit tiek prezentēta — ISCO-08 kodu izmantošana kā universāls centrs un juridiski autoritatīvi nacionālie reģistri kā "ground truth" — sasniedz to, ko nevar probabilistiski AI modeļi: 100% semantiskā precizitāte 85+ valodās, ko apstiprina 19 490+ Wikidata labojumi ar nulles noraidījumiem.

Publicējot pilnu datu kopumu (263 608 profesiju ieraksti no 146 reģistriem), Wikidata kešu (152 135 etiķetes 53 valodās) un pilnu bota infrastruktūru kā atklātu kodu, mēs piedāvājam pētniecības kopienai:

- **Zelta etalonu** daudzvalodu NLP modeļu apmācībai un novērtēšanai valodās ar ierobežotiem resursiem
- **Deterministisku rezerves variantu** socioloģiskai aptauju kodēšanai, novēršot kodētāju domstarpības
- **Globālu maršrutētāju**, kas samazina krusttabulu sarežģītību no O(n²) līdz O(n)
- **Dzīvu ekosistēmu**, kas reģistrē jaunās profesijas dažādās jurisdikcijās gandrīz reāllaikā

Divdesmit gadi atdala ISCO-58 no ISCO-68, no ISCO-88, no ISCO-08. Līdz ISCO-28 ienākšanai 2028. gadā mūsdienu darba klasifikācija — AI inženierija, klimata pielāgošanas speciālisti, gig-ekonomikas uzdevumu darbinieki, satura veidotāji — atpaliks aptuveni par vienu pilnu ekonomisko paaudzi. GSCO nepiedāvā aizstāt ISCO. Tas piedāvā aizpildīt 20 gadu plaisu ar nepārtraukti atjaunotu empīrisku slāni, kas atklāj, kur statistiskā realitāte ir atšķīrusies no administratīvā koda.

280 miljoni migrējošu cilvēku 2024. gadā un prognozētie 350+ miljoni līdz 2035. gadam (UN DESA) nevar gaidīt nākamo desmitgades pārskatīšanu. Viņu profesionālā dzīve tiek veidota — un bieži vien pārtraukta — ar klasifikācijas infrastruktūru, kas izstrādāta pasaulei, kas vairs nepastāv. GSCO ir slānis starp pasaules realitāti un ISCO stabilitāti.

890 Nobela prēmiju laureātu, kas iedvesmoja šo projektu, tagad var aprakstīt 260+ valodās — nevis caur mašīnu halucinācijām, bet caur tautu juridisko autoritāti, kas viņus izglītoja.

---

## 9. Bezdarbības cena

Iepriekšējās nodaļas nosaka, ko GSCO var darīt. Šī nodaļa aplūko, kas notiks, ja problēmas, ko tā risina, paliks neatrisinātas — jautājums, kas vairs nav teorētisks.

### 9.1 Ekonomiskās aizkaves reizinātājs

Valstis, kas atlikušas pāreju no ISCO-88 uz ISCO-08, vidēji samaksājušas 2.4× vairāk kopējās integrācijas izmaksās, kad no ES iestādēm nāca spiediens saistīties ar ESCO. Projektējot šo modeli uz priekšu: darbības, kas veiktas tagad, lai saskaņotu nacionālo reģistru ar GSCO ISCO-08 centru, izmaksā diapazonā €1.0–2.5 miljoni uz valsti (atkarībā no reģistra lieluma un valodu atšķirības); darbība, kas atlikta līdz 2031. gadam, tiek novērtēta €2.3–7.2 miljonos, ko virza uzkrātais mantojuma parāds, kas pieaug aptuveni par 5% gadā caur pensiju, nodokļu, darba un sociālās apdrošināšanas sistēmām, kas visas lejupēji patērē profesionālos kodus [41].

Tas nav spekulatīvs reizinātājs. Tā ir dokumentēta likumsakarība no migrācijas no ISCO-88 uz ISCO-08, tagad prognozēti attiecināma uz valstīm, kas joprojām strādā ar klasifikācijas sistēmām pirms 2008. gada. KZBiH-08 Bosnijā un Hercegovinā ir galvenais avots vācu medmāsu kvalifikācijas atzīšanas pieteikumiem — aptuveni 2 300 apstiprinājumi gadā pie 2019. gada pīķa likmēm. No tiem 23.3% prasa kompensējošus pasākumus 12–18 mēnešu reklasifikācijas periodā [48]. Rezultātā zaudētā alga uz vienu skarto medmāsu vidēji ir €12 000 reklasifikācijas periodā; 930 medmāsas gadā × €12 000 = aptuveni €11 miljoni gadā izvairāmu ekonomisko zaudējumu tikai no šī viena divpusējā koridora. Agregēti pa desmit valstīm, kas analizētas šajā pētījumā, konservatīvs izvairāmās berzes atzīšanas aprēķins ir €80–150 miljoni gadā.

Amerikas Imigrācijas padome (American Immigration Council) dokumentē $39 miljardus nerealizētas gada algas un $10.2 miljardus zaudēto nodokļu ieņēmumu no kvalifikāciju nepietiekamas izmantošanas imigrantiem tikai Amerikas Savienotajās Valstīs [49]. Flindersas Universitātes 2022. gada novērtējums Austrālijai lēš ekonomiskos zaudējumus A$70 miljardu apmērā, turklāt 43% ķīniešu kvalificēto migrantu strādā ārpus savas deklarētās profesijas [50].

### 9.2 Astoņi aizveramie logi

Nākamie stratēģiskie logi ir ierobežoti laikā. Katrs aizveras neatkarīgi no citiem, un katrs pārstāv iespēju, kas neatkārtojas paredzamā grafikā.

**Logs 1: AI cunami reklasifikācija (2026–2035).** Veselas profesiju kategorijas pašlaik tiek reklasificētas zem AI vadītas uzdevumu automatizācijas. AI treneri, uzvedņu inženieri (prompt engineers), autonomo transportlīdzekļu operatori un lielo valodu modeļu precizēšanas speciālisti neparādās nevienā no 10 valstu kopsavilkumiem, kas analizēti šajā pētījumā. Katrs gads bez klasifikatora atjaunināšanas nozīmē, ka vēl viena darbinieku kopa ienāk darba tirgū kategorijā, kas oficiāli nepastāv. Darba polarizācijas teorija [51] prognozē, ka AI automatizācija iztukšos vidēji kvalificētās kategorijas, kas visblīvāk apdzīvotas ISCO-08 grupās 4–8; valstis, kas klasificē šīs pārmaiņas tagad, būs empīriskas bāzes līnijas; valstis, kas gaida, retrospektīvi rekonstruēs tās nepareizās vecajās grozos.

**Logs 2: Klimata migrācijas paātrinājums.** ISCO-08 nesatur kodus darbiniekiem, kas nodrošina atbilstību muitas oglekļa regulēšanas mehānismam (CBAM), klimata pielāgošanas speciālistiem vai lauksaimniecības darbiniekiem, ko pārvietojuši klimata pārmaiņas. 10 valstis, kas analizētas šajā pētījumā, kopīgi aptver klimatiski neaizsargātus ekonomikas sektorus: kakao lauksaimniecība Kotdivuārā (visu sektoru neklasificēts pašreizējā reģistrā); tabakas audzēšana un ūdens ietilpīga kalnrūpniecība Tadžikistānā; nafta un gāze Saūda Arābijā un Brunejā; ledāju izcelsmes ūdens apsaimniekošana Mongolijā; jūra un zvejniecība Kaboverdē. Šo sektoru klasifikācija pirms klimata profesionālās disruptīvās ietekmes iestāšanās kvalitatīvi atšķiras no klasifikācijas pēc fakta.

**Logs 3: Platformu ekonomikas bloķēšana.** LinkedIn, Indeed un Upwork jau nosaka, ko nozīmē "software developer" Latvijā, Lietuvā un Igaunijā. Bolt un Wolt nosaka "delivery driver" Baltijā. HungerStation to nosaka Saūda Arābijā. Bez atjauninātiem nacionālajiem klasifikatoriem privātās platformu taksonomijas kļūst par faktiskiem profesiju standartiem — bez juridiskas atbildības, bez saites ar SDO un bez krusttabulas ar sociālās apdrošināšanas sistēmām.

**Logs 4: Institucionālo zināšanu zudums (2030–2035).** Pēdējā statistiķu paaudze, kas pārvaldīja pāreju ISCO-88→ISCO-08, tuvojas pensijai visās 10 valstīs, ko aptver kopsavilkumi. Institucionālās atmiņas par to, kāpēc tika saglabāti noteikti mantotie kodi, kāpēc izdzīvoja noteiktas padomju profesiju saimes postpadomju klasifikatoros un kā tika risināti konkrēti robežgadījumi pārejas laikā 2008. gadā, nebūs pieejama pēc 2030. gada. Integrācija, kamēr šī ekspertīze ir pieejama, izmaksā 2–3× lētāk nekā rekonstrukcija pēc pensijas.

**Logs 5: AI-palīdzības pārejas logs (2026–2028).** Pašreizējā AI-palīdzības angļu etiķešu ģenerēšana Latvijas 4 102 ierakstu reģistram tiek novērtēta €15 000. Tas pats uzdevums, ko veic manuāli 2031. gadā, potenciālā ECOWAS vai EURES regulatīvā spiediena apstākļos, tiek novērtēts €150 000. Šis logs aizveras, jo modeļu izmaksas pieaug, manuālās verifikācijas prasības pieaug zem jaunās AI vadības regulācijas, un uzkrājas atpalicība.

**Logs 6: Uzkrātais mantojuma parāds.** Katrs bezdarbības gads pievieno aptuveni 5% pie lejupējās integrācijas izmaksām caur pensiju, nodokļu, darba un sociālās apdrošināšanas sistēmām. Bosnijai, kas pārvalda pensiju sistēmu, kas sadalīta starp divām vienībām (Federacija BiH un Republika Srpska), katrai ar savām atsevišķām klasifikācijas praksēm, uzkrāšanās likme ir strukturāli augstāka. Formula nav lineāra: tā ir eksponenciāla, jo katra lejupējā sistēma, kas pieņem mantotos kodus, kļūst par jaunu atkarību, kas jāmigrē vienlaicīgi jebkuras nākotnes atjaunināšanas laikā.

**Logs 7: ISCO-28 pārskatīšanas logs (2026–2028).** Reizi paaudzē notiekošais ISCO pārskatīšanas process SDO pašlaik ir atvērts empīriskiem ieejas datiem. Valstis un pētnieki, kas iesaistīti šajā logā, veido standartu; tie, kas iekļaujas 2031. gadā, pielāgojas taksonomijai, ko izstrādājuši citi. Bagātākā kalnrūpniecības profesiju taksonomija Mongolijā ārpus OECD, Kotdivuāras kakao sektora kodi, Saūda Arābijas naftas un gāzes profesiju saimes un Brunejas naftas inženierijas apakšklasifikācijas — visi pārstāv ieejas datus, kas ir vērtīgi tikai tad, ja tie tiek iesniegti aktīvajā pārskatīšanas procesā. GSCO jau ir identificējis konkrētus kodus un koridorus; ceļš uz iesniegšanu SDO ISCO-28 darba grupā ir atlikušais solis.

**Logs 8: Migrācijas pieaugums — rīkoties pirms nākamā viļņa, nevis tā laikā.** ISCO-88 tika izstrādāts pasaulei ar 70 miljoniem starptautisko migrantu. ISCO-08 tika izstrādāts 190 miljoniem. Pašreizējais bāzes līmenis ir 280 miljoni plus 37 miljoni bēgļu plus 75 miljoni iekšēji pārvietoto personu. 10 valstis, ko aptver kopsavilkumi, kopīgi uzņem vai rada aptuveni 15–20 miljonus šīs populācijas. Klasifikācijas bāzes izveide pirms nākamā migrācijas viļņa — vai tas būtu klimatisks, konfliktu vai ekonomiskās polarizācijas izcelsmes — kvalitatīvi atšķiras no klasifikācijas mēģinājuma viļņa laikā. Ukrainas 2022. gada pārvietošanās notikuma laikā 1,5 miljoni bēgļu iebrauca Polijā nedēļu laikā; klasifikācijas infrastruktūra, kas pastāvēja tajā brīdī, noteica indivīdu iznākumus. Infrastruktūra, kas uzbūvēta pēc viļņa, klasificē tās cilvēcisko cenu, bet ne tās cilvēkus.

### 9.3 Politiskās godīguma arguments

Bezdarbības cenas sistēma prasa vienu neērtu atzīšanu: daži no nozīmīgākajiem klasifikācijas trūkumiem pastāv starp valstīm, kas nav dabiskie diplomātiskie partneri. 75.9% leksikālais atšķirība starp Tadžikistānu un Krievijas klasifikatoru, neskatoties uz krievu valodas kā abu reģistru administratīvās valodas kopīgo lietošanu, atspoguļo gadu desmitiem ilgu postpadomju administratīvo atšķirību, ko bija politiski ērti ignorēt. Divpusējais apstiprināšanas rādītājs Francija→Vācija (40.3%) pret Francija→Luksemburga (99.8%) atspoguļo nevis juridisko nenoteiktību, bet profesionālo asociāciju vārtsargu politisko ekonomiju Vācijā pret mazāku, vairāk integrētu Luksemburgas darba tirgu [42].

GSCO "rumbas un spieķu" arhitektūra ir politiski neitrāla pēc dizaina: tā savieno katru reģistru ar ISCO-08, nevis ar kādu divpusēju partneri. Tas nozīmē, ka valsts, kas nevēlas tieši harmonizēties ar ģeopolitisko pretinieku, tomēr var sasniegt savstarpēju lasāmību caur kopīgu centru. Arhitektūra neprasa uzticēšanos starp galapunktiem — tikai katra galapunkta savienojumu ar standartu. Tieši tas padara to mērogojamu.

---

## Datu pieejamība

Visi dati, kods un dokumentācija ir brīvi pieejami:

- **GitHub repozitorijs:** [https://github.com/Reincarnatiopedia/gsco](https://github.com/Reincarnatiopedia/gsco)
- **Zenodo datu kopums:** [DOI gaidāms — tiks pievienots pēc augšupielādes]
- **Wikidata bots:** [User:Maris Dreshmanis](https://www.wikidata.org/wiki/User:Maris_Dreshmanis)
- **Bota avota kods:** [Reincarnatiopedia/wikidata-bot](https://github.com/Reincarnatiopedia/wikidata-bot)

Repozitorija struktūra:
```
data/
  esco/                    — ESCO v1.2.1 (28 valodas, 2 942 profesijas)
  national_registries/     — 146 nacionālo reģistru JSON formātā
  wikidata_cache/          — CSV eksports (26 991 elements × 53 valodas)
scripts/
  gsco_wikidata_cache.py   — Nedēļas Wikidata dumps uz SQLite
  gsco_esco_mapper.py      — Deterministisks ESCO→Wikidata saskaņotājs
  gsco_edit_queue.py       — Iepriekš validēta labojumu rinda
  gsco_edit_daemon.py      — Bota izpildes dzinējs ar drošības kontrolēm
  gsco_revert_monitor.py   — Noraidījumu uzraudzība ar avārijas apturēšanu
```

---

Interaktīvā pavadošā bibliotēka visiem 117 dokumentētajiem migrācijas gadījumiem — ar meklēšanu pēc valstīm un tiešraides filtrēšanu — tiek uzturēta vietnē <https://gsco.io/cases>. Vietnes bibliotēka papildina A pielikumu un tiek atjaunināta, dokumentējot jaunus gadījumus.

## A pielikums: Dokumentētie migrācijas gadījumi (Pilna bibliotēka — 117 gadījumi)

Nākamā bibliotēka aptver **117 dokumentētos gadījumus**, kas iegūti no septiņām reģionālajām pētniecības partijām, kas veiktas starp 2026. gada janvāri un aprīli, aptverot 40+ valodas. Gadījumi 1–30 zemāk ir prezentēti detalizētā naratīvā formā — izvēlēti pēc skarto cilvēku mēroga un dokumentācijas kvalitātes. Gadījumi 31–120 parādās kompakta uzziņu tabulā šī pielikuma beigās; to pilns teksts tiek uzturēts vietnē <https://gsco.io/cases> ar meklēšanu pēc valstīm. Visas citētās URL un avoti ir uzskaitīti sadaļā "Avoti"; gadījumi bez verificējama primārā avota ir izlaisti.

---

Nākamie gadījumi ir iegūti no septiņām reģionālajām pētniecības partijām, kas veiktas starp 2026. gada janvāri un aprīli, aptverot 40+ valodas. Gadījumi ir izvēlēti pēc skarto cilvēku mēroga un dokumentācijas kvalitātes. Visas citētās URL un avoti ir uzskaitīti sadaļā "Avoti"; gadījumi bez verificējama primārā avota bibliogrāfijā ir izlaisti.

---

### Gadījums 1: Bosnija un Hercegovina → Vācija — medmāsas (2012–2021)
**Mērogs**: 17 103 pieteikumi medmāsu kvalifikācijas atzīšanai no BiH Vācijā 2012.–2021. gadā; 2 300 apstiprinājumi 2019. gada pīķa līmenī; 23.3% prasa kompensējošus pasākumus (12–18 mēneši)
**Avota klasifikators**: KZBiH-08 («Medicinska sestra» → ISCO 2221)
**Galamērķa klasifikators**: Vācijas KldB-2010 («Gesundheits- und Krankenpflegerin» → 81302)
**Neatbilstība**: 4-ciparu ISCO atbilstība pastāv uz papīra; KldB apakšklasifikācijas granularitāte prasa kompetenču saskaņošanu, ko nevar izvilkt tikai no ISCO koda
**Rezultāts**: Aptuveni 930 medmāsas gadā 12–18 mēnešu reklasifikācijā; novērtēti €11M gadā izvairītos zaudētos algas tikai no šī koridora; Serbijas veselības aprūpes darbaspēks tika izsmelts par 14% līdz 2017. gadam [48]
**Relevatība GSCO**: ba_kzbih08 jau ir GSCO (4 246 ieraksti); nulles bosniešu etiķetes Wikidata; spoku reģistrs ba_error_stub ir P0 kļūda, kas slēpj datu pieejamību

---

### Gadījums 2: Ukraina → Čehija — profesionāļi («burkānu tīrīšana») (2022–pašlaik)
**Mērogs**: 473 000 ukraiņu Čehijā 2022. gadā; 75%+ iekļauti ISCO 9 grupā (elementārās profesijas), lai gan vairumam ir terciārā izglītība; 68% sieviešu-vadītāju/profesionāļu strādā zem kvalifikācijas līmeņa
**Avota klasifikators**: Ukrainas DKHP (balstīts uz ISCO-08)
**Galamērķa klasifikators**: Čehijas KZAM (balstīts uz ISCO-08)
**Neatbilstība**: Abi izmanto ISCO-08 kodus — nomināla atbilstība — bet diplomu atzīšana joprojām ir nepieciešama; tikai kodu atbilstība nav pietiekama bez kvalifikācijas ekvivalences tilta
**Rezultāts**: Sistemātiska pārmērīga kvalifikācija; IOM dokumentēts kā "Pārmērīgi kvalificēti, nepietiekami nodarbināti" [46]
**Relevatība GSCO**: Parāda, ka ISCO kodu atbilstība ir nepieciešams, bet nepietiekams nosacījums; nepieciešama krusttabula + atzīšanas sistēma

---

### Gadījums 3: Filipīnas → Japāna — medmāsas (2008–pašlaik)
**Mērogs**: 15 gadu kumulatīvais Japānas medmāsu licences eksāmenu nokārtošanas rādītājs: 14%; 86% atgriežas Filipīnās vai strādā par palīgiem, nevis reģistrētām medmāsām
**Avota klasifikators**: Filipīnu PRC medmāsu darbības kodi
**Galamērķa klasifikators**: Japānas JSCCO (厚生労働省)
**Neatbilstība**: Japānas eksāmens ir kalibrēts uz japāņu profesiju kodu saimi; filipīniešu medmāsu izglītība tiek saskaņota ar citām ISCO apakškodiem nekā tās, ko sedz japāņu eksāmens
**Rezultāts**: 15 gadi × ikgadējās kohortas; kvalificētu medmāsu strukturāla nepietiekama izmantošana, neskatoties uz divpusējo Ekonomiskās partnerības nolīgumu (EPA), kas izstrādāts kustības atvieglošanai
**Avots**: Dienvidaustrumu Āzijas migrācijas partija (2026); Japānas Veselības, darba un labklājības ministrijas oficiālā statistika

---

### Gadījums 4: Venecuēla → Peru/Kolumbija — "Visaptverošie kopienas ārsti" (2018–pašlaik)
**Mērogs**: Aptuveni 50 000 venecuēliešu ārstu bez ekvivalenta koda galamērķa valstu klasifikatoros; Peru anulēja venecuēliešu medicīnas reģistrācijas 2018. gadā
**Avota klasifikators**: Venecuēlas MPPE profesionālā sistēma («médico integral comunitario» = kopienas medicīnas speciālists)
**Galamērķa klasifikators**: Peru CNO, Kolumbijas CON (neviens nesatur "médico integral comunitario" kā kategoriju)
**Neatbilstība**: Profesijas kategorija burtiski trūkst galamērķa klasifikatorā; kodu nav iespējams atrast; licenci nav iespējams novērtēt
**Rezultāts**: Masveida pazemināšana; daudzi praktizē kā administratīvais personāls vai nereģistrēti; Peru pilnībā anulēja reģistrācijas
**Avots**: Romāņu valodu migrācijas partija (2026)

---

### Gadījums 5: Rumānija → Itālija — medmāsas (2023–pašlaik)
**Mērogs**: 11 861 rumāņu medmāsa tieši skārusi Itālijas Direktīvas ES 2024/505 nepieņemšana
**Avota klasifikators**: Rumāņu COR (medmāsu aprūpe → ISCO 2221)
**Galamērķa klasifikators**: Itāļu NUP (infermiere professionale)
**Neatbilstība**: Direktīvas nepieņemšana nozīmē, ka automātiskās atzīšanas ceļš ir salauzts, lai gan abas valstis ir ES dalībvalstis
**Rezultāts**: ES pārkāpuma procedūras pret Itāliju, 2025. gada maijā [40]; medmāsas strādā nelegāli vai vispār nestrādā
**Relevatība GSCO**: Romāņu partija; GSCO ir RO un IT reģistri; krusttabula pastāv — plaisa ir juridiskā-administratīvā, nevis klasifikācijas, bet GSCO nodrošina tehnisko tiltu, tiklīdz notiks juridiskā atrisināšana

---

### Gadījums 6: Sīrija → Vācija — medicīnas licence (2015–2016 dokumentēts, turpinās)
**Mērogs**: 14 mēnešu vidējā gaidīšana Approbation (medicīnas licence), dokumentēta BMC pētījumā pieteikumiem, kas iesniegti 2015. gada jūnijā; 62 100 pieteikumi no Irānas tikai 2023. gadā (+26% gadā)
**Avota klasifikators**: Sīrijas Medicīnas asociācijas kodi
**Galamērķa klasifikators**: Vācijas Approbationsordnung für Ärzte (ÄAppO) ar Bundesland specifisku realizāciju
**Neatbilstība**: Nav mašīnlasāma tilta starp sīriešu medicīnas specialitāšu kodiem un Vācijas Bundesland specifisko klasifikāciju; Approbation izmaksas svārstās €170–€850 pa zemēm; ārējās diploms novērtēšana pievieno €450–€3 000; sagatavošanas kursi līdz €4 900
**Rezultāts**: 14 mēnešu dokumentēts gadījums (Erim et al. 2020) [35]; sistemātisks šķērslis; 80% vācu uzņēmumu ziņo, ka vispār neizmanto formālo atzīšanas sistēmu [41]
**Avots**: Vācijas/Ziemeļvalstu migrācijas partija (2026); Erim et al. 2020 BMC Health Services Research

---

### Gadījums 7: Tadžikistāna → Krievija — klasifikācijas atšķirība kopīgā valodā (reģistrs 2022)
**Mērogs**: 1,1 miljons tadžiku darba migrantu Krievijā = 11% no Tadžikistānas kopējā iedzīvotāju skaita; naudas pārvedumi = 30–40% no Tadžikistānas IKP
**Avota klasifikators**: Tadžiku NKZ-2022 (krievu valodā, balstīts uz ISCO-08)
**Galamērķa klasifikators**: Krievijas OKZ (balstīts uz ISCO-08)
**Neatbilstība**: 75.9% leksikālo atšķirību 4-ciparu līmenī, neskatoties uz to, ka abi reģistri ir krievu valodā un nomināli saskaņoti ar ISCO-08; ISCO kodiem 7313/7314/7315 (vitrāžists, podnieks, juvelieris) ir sistemātiski sajaukti; NKZ-2022 satur tieši "National Bank of Kazakhstan" kodā 1124 — kopēšanas artefakts no Kazahstānas veidnes
**Rezultāts**: Kvalifikāciju atzīšana starp divām krievu valodā runājošām sistēmām, kas balstītas uz ISCO-08, neizdodas satura atšķirību dēļ, kas nav redzama, saskaņojot tikai pēc koda
**Relevatība GSCO**: Atklāts GSCO datubāzes analīzē; valsts kopsavilkums TJ; apstiprina, ka reģistri vienā valodā un vienā standartā var būtiski atšķirties saturā, kas prasa GSCO saskaņošanu etiķešu līmenī

---

### Gadījums 8: Honkonga (BNO) → Lielbritānija (2021–pašlaik)
**Mērogs**: aptuveni 2 000 aptaujāto British Future (2023); 47% BNO vīzu īpašnieku strādā ārpus savas profesionālās jomas; 28% min kvalifikācijas atzīšanu kā galveno šķērsli
**Avota klasifikators**: Honkongas HKISCO-11 (pēc ISCO-08 parauga)
**Galamērķa klasifikators**: Britu SOC-2020
**Neatbilstība**: Profesionālās licencēšanas iestādes Lielbritānijā (NMC medmāsām, GMC medicīnai) prasa Lielbritānijai specifisku kompetenču verifikāciju, kas nav izvedama no HKISCO koda; SOC-2020 granularitāte atšķiras no HKISCO-11 4-ciparu līmenī
**Rezultāts**: 47% profesionālās neatbilstības populācijā, kas ir ~150 000+ iebraucēju; dokumentēts psiholoģiskais stress [47]
**Avots**: British Future aptauja 2023 [52]

---

### Gadījums 9: Ķīna → Austrālija — kvalificētas migrācijas neatbilstība (2022)
**Mērogs**: 43% ķīniešu kvalificēto migrantu Austrālijā strādā ārpus savas deklarētās profesijas; novērtēti A$70 miljardu ekonomisko zaudējumu (Flindersas Universitāte 2022)
**Avota klasifikators**: Ķīnas CSCO (中国职业分类大典)
**Galamērķa klasifikators**: Austrālijas ANZSCO (ABS/Stats NZ)
**Neatbilstība**: Prasmju novērtēšanas iestādes (Engineers Australia, CPA Australia u.c.) prasa kompetenču saskaņošanu, kas šķērso vairākas ANZSCO vienotās grupas; CSCO krusttabula uz ANZSCO mašīnlasāmā formātā nepastāv
**Rezultāts**: A$70 miljardu nerealizēta ekonomiskā izlaide; 43% profesionālās neatbilstības [50]
**Avots**: Austrumāzijas migrācijas partija (2026); Flindersas Universitātes novērtējums 2022

---

### Gadījums 10: Francija → Vācija vs. Francija → Luksemburga — kvalifikācijas atzīšanas neatbilstība (2024. gada dati)
**Mērogs**: Tās pašas franču profesionālās kvalifikācijas; tā pati ES Direktīva 2005/36/EC; tā pati izcelsmes valsts
**Avota klasifikators**: Francijas ROME v4 (France Travail)
**Galamērķa klasifikators A**: Vācijas KldB-2010 (40.3% apstiprināšanas līmenis franču kvalifikācijām, BIBB 2024 dati)
**Galamērķa klasifikators B**: Luksemburgas CNP (99.8% apstiprināšanas līmenis tām pašām franču kvalifikācijām)
**Neatbilstība**: 60% atšķirība starp divām ES dalībvalstīm, kas īsteno to pašu Direktīvu; atspoguļo atšķirības KldB vs. CNP granularitātē 5-ciparu līmenī, ko pastiprina profesionālo asociāciju vārtsargi Vācijā [42]
**Rezultāts**: Francija→Vācija koridors ir 60× vairāk visticamāk beigsies ar atteikumu nekā Francija→Luksemburga, identiskām kvalifikācijām; IW 2025 lēš kvalificētu darbinieku trūkumu Vācijā €450K apmērā, vienlaicīgi bloķējot kvalificētus pretendentus no ES [41]
**Avots**: ITEM Maastricht Cross-Border Impact Assessment 2025; IW Report 08/25 [41, 42]

---

### Gadījums 11: Bangladeša → Saūda Arābija — piespiedu klasifikācija kā mājas darbinieces (turpinās)
**Mērogs**: Aptuveni 800 000 Bangladešas sieviešu migrantu; sistemātiska piespiedu klasifikācija kā mājas darbinieces neatkarīgi no faktiskās profesionālās pieredzes
**Avota klasifikators**: Bangladešas BSCO (balstīts uz ISCO-08; 5 387 ieraksti GSCO)
**Galamērķa klasifikators**: Saūda Arābijas SSCO 2024 (GSCO: 2 738 angļu ieraksti, 99.3% ISCO segums; arābu versija — 2019 — 5 gadu atšķirība)
**Neatbilstība**: Nav mašīnlasāma tilta starp BSCO profesionālajām kategorijām un SSCO klasifikāciju reģistrācijas brīdī darba līgumam; Saūda Arābijas kvotu sistēma NITAQAT izmanto SSCO kodus — darbinieki, kas reģistrēti ar nepareizu kodu, ir ieslēgti nepareizā kvotu kategorijā
**Rezultāts**: Profesionālā degradācija, kas skar 800 000 indivīdu; ILO 2024 dokumentēts [36]
**Relevatība GSCO**: Gan BSCO, gan SSCO 2024 ir GSCO; arābu SSCO ir RTL apgriešanas kļūda, kas gaida P0 labojumu; krusttabula tehniski pastāv — neveiksme administratīvajā lietošanā

---

### Gadījums 12: Nepāla → Dienvidkoreja — EPS rinda (2023)
**Mērogs**: 143 812 EPS (Employment Permit System) pretendenti uz 15 800 pieejamām vietām 2023. gadā; 2 nāves gadījumi decembra 2023 protestu laikā Katmandu eksāmenu centrā
**Avota klasifikators**: Nepālas NASCO (pēc ISCO-08 parauga)
**Galamērķa klasifikators**: Korejas KSCO-7 (한국표준직업분류)
**Neatbilstība**: EPS eksāmens testē korejiešu valodā runājošu profesionālo terminoloģiju, kas nav izvedama no NASCO → ISCO-08 saskaņošanas; korejiešu KSCO-7 ir atšķirīga granularitāte 4-ciparu līmenī nekā ISCO-08 apstrādes rūpniecības un būvniecības kategorijām
**Rezultāts**: Pretendentu un vietu attiecība 9:1; 2 nāves protestos; strukturāls šķērslis, kas rada bīstamu šaurumu
**Avots**: Persiešu-Indo-Turku migrācijas partija (2026)

---

### Gadījums 13: Uzbekistāna → Krievija — masveida pārmērīga kvalifikācija (turpinās)
**Mērogs**: 33.3% uzbeku migrantu Krievijā ir augstākā izglītība; aptuveni 11% strādā neatbilstošās profesijās = aptuveni 220 000 vienlaicīgi pārmērīgi kvalificētu darbinieku
**Avota klasifikators**: Uzbeku ОККТ (O'zbekiston Kasblar Klassifikatori, balstīts uz ISCO-08)
**Galamērķa klasifikators**: Krievijas ОКЗ (balstīts uz ISCO-08)
**Neatbilstība**: Neskatoties uz to, ka abi ir balstīti uz ISCO-08 un lingvistiski ir tuvi (uzbeku-krievu divvalodība ir izplatīta), apakškodu līmenī saglabājas neatbilstība; Krievijas darba devēji pēc noklusējuma izvairās no riska, kad uzbeku diplomi nav automātiski verificējami
**Rezultāts**: Aptuveni 220 000 pārmērīgi kvalificētu darbinieku vienlaicīgi; IOM dati, citēti persiešu-indiešu partijā
**Avots**: Persiešu-Indo-Turku migrācijas partija (2026); IOM dokumentācija

---

### Gadījums 14: Bulgārija → Vācija — "Feldsherin" kategorijas trūkums (2016–2019)
**Mērogs**: Bulgārijas medmāsu kvalifikāciju atzīšana Vācijā trīskāršojās no 5 600 līdz 15 500 (2016–2019); bulgāru profesija "feldšeris" (feldsherin) trūkst vācu/austriešu klasifikācijas sistēmās
**Avota klasifikators**: Bulgāru EKPD (balstīts uz ISCO-08; ietver "feldšeri" kā atsevišķu 4-ciparu kategoriju)
**Galamērķa klasifikators**: Vācijas KldB-2010 (nav kategorijas "Feldscherin"; tuvākā ir "Pflegehilfskraft" — par 3 profesionālām pakāpēm zemāk)
**Neatbilstība**: Profesija pastāv avotā, trūkst galamērķī → automātiska pazemināšana; algas samazinājums €400–€600/mēnesī uz vienu skarto medmāsu
**Rezultāts**: Automātiska pazemināšana līdz Pflegehilfskraft; Austrijas Sozialministerium joprojām dokumentē problēmu 2025. gadā; strukturāli, nevis pārejas
**Relevatība GSCO**: Tieša strukturāla paralēle CI (540 nekvalificētu profesiju) un BN (1 381 profesija 5-ciparu līmenī bez ISCO krusttabulas)
**Avots**: Slāvu migrācijas partija (2026); Austrijas Sozialministerium 2025 dokumentācija

---

### Gadījums 15: Ukraina → Polija — masveida pārmērīga kvalifikācija (2022–pašlaik)
**Mērogs**: Aptuveni 1,5 miljoni ukraiņu bēgļu; 40% nodarbināti ISCO 9 grupā, neskatoties uz vairuma terciāro izglītību; 67% sieviešu-profesionāļu strādā zem kvalifikācijas līmeņa
**Avota klasifikators**: Ukrainas DKHP (balstīts uz ISCO-08)
**Galamērķa klasifikators**: Polijas KZiS (balstīts uz ISCO-08)
**Neatbilstība**: Atbilstība vienā standartā un vienā kodā joprojām rada sistemātisku pazemināšanu; nostrificācijas izmaksas (diploma atzīšanas maksa), bērnu aprūpes slogs un valodas barjera kopā rada pārmērīgas kvalifikācijas slazdu, ko ISCO kodu saskaņošana vien nevar atrisināt
**Rezultāts**: 40% nepareizas klasifikācijas līmenis masveida mērogā; strukturāli, nevis pārejas
**Avots**: Slāvu migrācijas partija (2026); IOM un Polijas darba tirgus statistika

---

### Gadījums 16: Baltkrievija → Polija — IT profesionāļi («kabeļi pirms intervijas») (2020–2023)
**Mērogs**: 20 000 IT profesionāļu caur paātrināto vīzu programmu Poland Business Harbour
**Avota klasifikators**: Baltkrievijas OKRB-006 (ISCO 2512 «Software developer» saskaņots)
**Galamērķa klasifikators**: Polijas KZiS (ISCO 2512 saskaņots — tas pats kods)
**Neatbilstība**: Tas pats ISCO kods abās sistēmās; darba devēju neatzīšana saglabājas, jo baltkrievu diplomi netiek automātiski verificēti pēc Polijas datubāzes; darbinieki ziņo par 3–12 mēnešiem devalvētā darba («šķiedru optisko kabeļu ieklāšana») pirms atrašanas IT darbā; pēc vienas Polijas kompānijas pievienošanas rezumē — 5 intervijas darbā 1 mēneša laikā
**Rezultāts**: 3–12 mēnešu devalvēts pārejas periods, neskatoties uz paātrināto vīzu un tiem pašiem ISCO kodiem; atklāj, ka kvalifikācijas atzīšana = darba devēja uzticības problēma, ne tikai kodu saskaņošanas problēma
**Relevatība GSCO**: GSCO uzticamības signāls Wikidata (profesija apstiprināta SDO reģistrā ar nulles noraidījumiem) varētu darboties kā darba devēja uzticības proxy
**Avots**: Slāvu migrācijas partija (2026)

---

### Gadījums 17: Brazīlija → Portugāle — medicīnas atzīšana (turpinās)
**Mērogs**: 57.8% Brazīlijas medicīnas diplomu atteikuma līmenis Portugāles Ordem dos Médicos; Angola 3.4% atteikuma līmenis; Kuba un Gvineja-Bisava 0% atteikuma līmenis — visi nomināli zem vienas portugāļu valodā runājošās ekvivalences sistēmas
**Avota klasifikators**: Brazīlijas CBO (Classificação Brasileira de Ocupações; 2 614 ieraksti GSCO)
**Galamērķa klasifikators**: Portugāļu CNP-94 (atjaunināts; krustiski atsaucas uz ES ESCO)
**Neatbilstība**: Portugāles Ordem dos Médicos piemēro atšķirīgus substantīvus kritērijus Brazīlijas, Angolas un PALOP pretendentiem, neskatoties uz kopīgo valodu un nomināli līdzīgām medicīnas izglītības struktūrām; līdzība kodu līmenī neprognozē apstiprināšanu
**Rezultāts**: 57.8% pret 3.4% atteikuma līmeņa neatbilstība; dokumentēts Público un Ordem dos Médicos datos, citēts romāņu partijā
**Avots**: Romāņu valodu migrācijas partija (2026); Portugāles Ordem dos Médicos ikgadējā statistika

---

### Gadījums 18: Francija — PADHUE ārsti («asociētie praktizētāji») (turpinās)
**Mērogs**: 5 000+ ārsti klasificēti kā «Praticiens à Diplôme Hors Union Européenne» (PADHUE), pelnot €1 450/mēnesī pret €4 500/mēnesī par ekvivalenti kvalificētiem ārstiem, kas apmācīti Francijā
**Avota klasifikatori**: Dažādi (Āfrika, Tuvie Austrumi, Austrumeiropa, Āzija)
**Galamērķa klasifikators**: Francijas ROME v4 (PADHUE = atsevišķa profesionāla apakškategorija zem «médecin»)
**Neatbilstība**: Francijas klasifikācijas sistēmai ir pastāvīga noturēšanas kategorija, kas juridiski atšķiras no pilna «médecin» statusa neatkarīgi no faktiskās kompetences; PADHUE ārsti, kas veic identisku klīnisko darbu, tiek klasificēti (un apmaksāti) kā atsevišķa zemāka ranga kategorija
**Rezultāts**: €3 050/mēnesī algas atšķirība uz vienu ārstu; skarti 5 000+; Ngabirano 2026 apskatā aprakstīts kā veicinošs psiholoģiskajam stresam augsti kvalificētu migrantu vidū [47]
**Avots**: Romāņu migrācijas partija (2026); Ngabirano 2026 sistemātiskais apskats

---

### Gadījums 19: Nīderlandes/Beļģijas robeža — ZorgSaam neirologa gadījums (2025)
**Mērogs**: 1 slimnīca (ZorgSaam, Terneuzen, Nīderlande); 1 pretendents-neirologs (Universitair Ziekenhuis Gent, Beļģija, ~30 km); akūts trūkums
**Avota klasifikators**: Beļģijas KBC-ISCO (neurologie → ISCO 2212)
**Galamērķa klasifikators**: Nīderlandes BIG-register (neuroloog → BIG kods 79)
**Neatbilstība**: BIG-register prasa atsevišķu reģistrācijas procedūru pat ES sertificētiem speciālistiem; Nīderlandes ISCO-līdz-BIG krusttabula nav mašīnlasāma; 30 km, nulles pārcelšanās izmaksas, tā pati ES Direktīva, Šengenas divpusējā brīvība — klasifikācijas procedūra tomēr aizkavē
**Rezultāts**: Slimnīca palika ar nepietiekamu personālu procedūras laikā; dokumentēts ITEM Maastricht Cross-Border Impact Assessment 2025 [42]
**Relevatība GSCO**: Visciešākais iespējamais gadījums — visas berzes izmaiņas ir minimizētas; klasifikācijas neatbilstība tomēr saglabājas

---

### Gadījums 20: Igaunija → Somija/V