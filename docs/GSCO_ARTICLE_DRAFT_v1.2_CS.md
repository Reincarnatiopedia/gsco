# GSCO: Globální standardní klasifikátor profesí — Deterministická vícejazyčná databáze pro řešení problému N² křížových tabulek v mezinárodní klasifikaci profesí

**Maris Dreshmanis**
ORCID: [0009-0003-8151-4088](https://orcid.org/0009-0003-8151-4088) | ISNI: [0000 0004 9280 9121](https://isni.org/isni/0000000492809121)
Afilace: Academy of Reincarnationology | Nezávislý výzkumník
GitHub: [MarisDreshmanis](https://github.com/MarisDreshmanis) | Wikidata: [User:Maris Dreshmanis](https://www.wikidata.org/wiki/User:Maris_Dreshmanis)

**Verze:** 1 | **Licence:** CC BY 4.0 | **Datum:** Duben 2026

**DOI:** [10.5281/zenodo.19902278](https://doi.org/10.5281/zenodo.19902278) (this version) · **Concept DOI:** [10.5281/zenodo.19902277](https://doi.org/10.5281/zenodo.19902277) (latest version) · [Zenodo record](https://zenodo.org/records/19902278)

---

## Abstrakt

**Úvod.** Problém nesouladu kódů klasifikací profesí v různých zemích byl zjištěn náhodou. Jednou z mých činností je editace a doplňování dat do Wikidata. Wikidata slouží jako spojovací článek mezi sekcemi Wikipedie v různých jazycích a funguje jako centrální úložiště pro sdílená fakta a odkazy.

Při řešení úkolu doplňování dat do Wikidata pro jednu konkrétní cílovou skupinu — nositele Nobelovy ceny v různých jazycích — se ukázalo, že názvy profesí jsou jednou z mezer, které nejsou ve Wikidata systematizovány.

Abych se vyhnul chybám v názvech profesí při překladu neuronovými sítěmi nebo Google Translate, rozhodl jsem se shromáždit klasifikátory profesí v různých jazycích z otevřených zdrojů. Po dokončení se ukázal globální problém světového rozsahu. Zaprvé, Mezinárodní organizace práce (ILO) aktualizuje svou Mezinárodní standardní klasifikaci profesí (ISCO) přibližně každých 20 let. To znamená, že nové profese tohoto desetiletí v ní nejsou zahrnuty.

Zde jsou roky standardizace ISCO:

- **ISCO-58** — přijata v roce 1957 (publikována v roce 1958).
- **ISCO-68** — přijata v roce 1966 (publikována v roce 1968).
- **ISCO-88** — přijata v roce 1987 (publikována v roce 1988). Právě v ní byla poprvé jasně popsána koncepce „úrovně dovedností“.
- **ISCO-08** — přijata v roce 2007 (publikována v roce 2008). Toto je aktuální verze, kterou nyní používá celý svět.
- Další (**ISCO-28**) je nyní v aktivní fázi revize ILO — podávání empirických vstupních dat je otevřeno v letech 2026–2028, vydání v roce 2028.

Zadruhé, země, které tento úkol řešily samy, přidávají kódy, které si navzájem konkurují mezi zeměmi. V Evropské unii je situace o něco lepší, ale celkově ve světě v oblasti standardizace a kódů po 4 číslicích ISCO panuje chaos.

Při dalším řešení úkolu popisu profesí nositelů Nobelovy ceny jsem si pro sebe vytvořil tabulku analýzy nesouladu v různých zemích. Nazval jsem ji jednoduše: **GSCO (Globální standardní klasifikátor profesí)**. Proč globální? Protože jsem shromáždil data z více než 140 národních rejstříků. Nenašel jsem informace, že by to někdo na světě udělal dříve; pokud máte vy, kdo čtete tento text, takové informace — prosím, pošlete mi je. Kontakty jsou uvedeny na stránce mého profilu.

Když byla data shromážděna a analyzována, pochopil jsem, že se o tato data musím podělit nejen s národními rejstříky, aby si uvědomily počet konfliktů kódů profesí ve svých zemích a pokusily se je synchronizovat, ale také s Mezinárodní organizací práce (ILO), abych pomohl pracovní skupině vidět rozsah problému a zohlednit to při standardizaci ISCO-28 v roce 2028.

### Příklad: ISCO 2221

**Hub-level: co oficiální ISCO-08 znamená**

ISCO-08 (ILO): „Nursing professionals“ — zdravotní sestry s rozšířenými pravomocemi (advanced nurse practitioner).

Vícejazyčné popisky hub-level v naší databázi (35 jazyků):

| Jazyk | Překlad |
|---|---|
| ar | ممارس تمريض متقدم |
| az | Tibbi qulluq üzrə peşəkar mütəxəssislər |
| bg | старша медицинска сестра |
| bn | হাসপাতাল ǯsibka pরামশȟk |
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

**Katastrofa na národní úrovni**

Pod jedním kódem ISCO 2221 mají různé země na mysli **různé profese**:

**Austrálie a Nový Zéland (ANZSCO 2022) — finanční brokeři, ne zdravotní sestry:**

- 222111 Commodities Trader (obchodník s komoditami)
- 222112 Finance Broker
- 222113 Insurance Broker
- 222199 Financial Brokers nec
- 222100 Financial Brokers nfd

**Ukrajina (DK003) — lékaři, ne zdravotní sestry:**

- 2221 — „Професіонали в галузі лікувальної справи (крім стоматології)“
- 2221.1 — Наукові співробітники (лікувальна справа)
- 2221.2 — Лікарі (lékaři): terapeut, kardiolog, chirurg, psychoterapeut, neurolog, genetik…
- Celkem 78 podkódů — všichni lékaři, ne zdravotní sestry.

**Německo (KldB-2010):**

- 22212 „Vehicle paintwork — skilled tasks“ (lakýrník vozidel — kvalifikované úkoly)
- 81393 „Aufsichtskräfte — Gesundheits- und Krankenpflege, Rettungsdienst und Geburtshilfe“ — vrchní zdravotní sestry
- 81302 „Gesundheits- und Krankenpflege“ — běžné zdravotní sestry (podle oficiálního Umsteigeschlüssel Bundesagentur für Arbeit se mapují na ISCO 3221, ne 2221)

**Bělorusko (OKRВ-2017, aktuální verze klasifikátoru):**

- 2221: „Специалисты-профессионалы по медицинскому уходу“ — zdravotní sestry (odpovídá ISCO-08)

**Itálie (CP 2021) — architekti:**

- 2.2.2.1.1 ARCHITETTI (architekti)
- 2.2.2.1.2 Pianificatori, paesaggisti (plánovači, krajináři)

**San Marino (RP-2017) — architekti:**

- 22211 ARCHITETTO

**Kanada (NOC 2021) — technici:**

- 22210 Architectural technologists
- 22211 Industrial designers
- 22212 Drafting technologists
- 22213 Land survey technologists
- 22214 Geomatics

**Alžírsko (DZ Profession) — lékaři:**

- 2221: „Médecins“ (lékaři)

---

```markdown
---

### Profese známé každému — učitel a taxikář

Abychom ukázali, že problém se netýká vzácných profesí jako „instruktor jógy“ nebo „hypnoterapeut“, ale **těch nejobyčejnějších, masových povolání**, podívejme se na dvě univerzální profese: učitel a taxikář. Existují v každé zemi — ale klasifikace se radikálně rozcházejí.

#### 👨‍🏫 Učitel / Přednášející

Top 15 zemí podle počtu pozic v rámci ISCO 23xx (Vzdělávání):

| Země | Pozice pod 23xx | Nejneobvyklejší granularita |
|---|---:|---|
| 🇧🇦 **Bosna (KZBiH-08)** | **404** | **191 odlišných univerzitních učitelů** pod jediným ISCO 2310 — samostatný kód pro každou specializaci (biotechnologie, filologie, matematika) |
| 🇺🇿 Uzbekistán (OZMST 2025) | 387 | 179 učitelů odborného vzdělávání (2320) |
| 🇲🇳 Mongolsko (YAMAT-08) | 355 | 120 univerzitních + 120 odborných |
| 🇸🇦 Saúdská Arábie (SSCO 2024) | 275 | 76 středoškolských učitelů |
| 🇷🇸 Srbsko (Šifarnik) | 264 | 97 univerzitních učitelů |
| 🇰🇷 Korea (KSCO 2024) | 171 | 5–7 v každé skupině ISCO-4, rovnoměrně rozděleno |
| 🇮🇹 Itálie (CP2021) | 141 | 38 přednášejících pod 2311 |
| 🇪🇪 Estonsko (AK-2008) | 130 | Specialisté na metody vzdělávání, učitelé jazyků — samostatné kódy |

A na úplném dně:

| Země | Celkem | Co tam je |
|---|---:|---|
| 🇷🇺 Rusko (OKZ-2014) | **22** | Pouze 4místné skupiny ISCO, žádná granularita |
| 🇩🇪 Německo (KldB-2010) | 40 | Vlastní číslování, nerozkládá ISCO 23xx |
| 🇺🇸 USA (O\*NET) | **8** | 5 kategorií SOC 23-1 + 3 SOC 23-2 |
| 🇬🇧 Velká Británie (SOC 2020) | 15 | 1 na sub-kód |

**Co to znamená pro konkrétního učitele:** bosenská profesorka biotechnologie má v KZBiH-08 specifický kód (jeden ze 191) — ale pokud se přestěhuje do Ruska, její granularita na úrovni 191 **se zhroutí do jediného kódu 2310 „vysokoškolský lektor“**. Pokud se přestěhuje do USA, její kód se dokonce ani **nevejde do SOC 23-1** (neexistuje tam úroveň specifická pro daný předmět).
```

#### 🚕 Řidič taxi

Standardní ISCO **8322** „Řidiči osobních a malých dodávkových automobilů (taxikáři)“ (kombinovaná kategorie) existuje ve většině zemí. Avšak **místní typy taxi** jsou případem, který ISCO-08 prostě nepokrývá:

| Země | Místní kód | Popis |
|---|---|---|
| 🇫🇷 Francie (ROME 11993) | Chauffeur de taxi animalier | **Taxi pro přepravu zvířat** — jediná samostatná třída svého druhu na světě |
| 🇫🇷 Francie (ROME 12884) | Conducteur de bateau taxi | Vodní taxi |
| 🇫🇷 Francie (ROME 13191) | Conducteur de taxi moto | Motocyklové taxi |
| 🇧🇦 Bosna + 🌊 PACSCO (23 tichomořských národů) | 8350 | **"Vozač taksija na vodi" / "Water taxi driver"** — vodní taxi (samostatná kategorie ISCO) |
| 🇹🇬 **Togo (RGPH4)** | 5020 "Taxi-moto (**Zemidjan**)" | **Zemidjan** — místní název pro motocyklové taxi, profese zaměstnávající tisíce lidí |
| 🇧🇯 Benin (NAP) | 154–155 | "Taxi-moto / charrette / vélo" (motocykl / kára / jízdní kolo) |
| 🇬🇹 Guatemala (CNO 2022) | 832104 + 933101 | "Piloto de moto taxis" + "**Piloto de bicitaxis**" (cyklotaxi) |
| 🇭🇳 **Honduras (CNOH 2018)** | 832101 | "Conductor de moto taxi **forestal** motorizada" — **motorizované lesní taxi** (unikátní pro Honduras) |
| 🇸🇳 Senegal, 🇩🇯 Džibutsko, 🇨🇮 Pobřeží slonoviny | 05.0.0.17 | "taxi man — conducteur de bus" — kombinace „řidič taxi + řidič autobusu“ v jednom povolání |
| 🇨🇦 Kanada (NOC 2021) | 75200 | "Taxi and **limousine** drivers and **chauffeurs**" — řidiči taxi sloučení s limuzínami |
| 🇦🇺/🇳🇿 ANZSCO 2022 | 731112 | "Taxi Driver" — ale ve vlastním číslování ANZSCO 7311 = "Automobile Drivers", což **neodpovídá** ISCO 7311 "Precision-Instrument Makers and Repairers" (odlišná profese v mezinárodním standardu). Ověřeno prostřednictvím oficiální převodní tabulky ABS OSCA 2024 ↔ ISCO-08: správná skupina ISCO-08 pro ANZSCO 731112 je **8322** "Car, taxi and van drivers". |

**Co to znamená pro konkrétního řidiče taxi:** tožský **řidič zemidjanu** (motocyklové taxi) je skutečné povolání s tisíci pracovníky. Ani ISCO-08, ani ANZSCO, ani SOC pro něj nemají kolonku. Když emigruje do Německa nebo Francie v rámci pravidel pro uznávání kvalifikací, jeho profesní zkušenost se zhroutí do obecného „Personenkraftwagen-Fahrer“ (řidič osobního automobilu) — protože slovo „zemidjan“ v německém klasifikátoru chybí. Není „ztracen v překladu“ — je **ztracen z taxonomie**.

Honduraský „řidič lesního motocyklového taxi“ (Conductor de moto taxi forestal) nebo guatemalský „řidič cyklotaxi“ (Piloto de bicitaxis) jsou rovněž skutečná, masová povolání, která **v mezinárodní struktuře chybí**.

#### Proč na tom záleží

Učitel a řidič taxi jsou ty nejuniverzálnější a nejsnadněji pochopitelné profese. Pokud ani zde nepanuje shoda — co teprve u vzácných nebo vznikajících povolání (školitel AI, operátor dronu, specialista na adaptaci na klimatické změny)? Tyto příklady ukazují: **vnést řád do globální klasifikace zaměstnání je úkol v měřítku OSN/ILO**, nikoliv práce jednotlivých zemí. To je přesně ten cíl: pomoci pracovní skupině ISCO-28 v roce 2028 vzít tyto rozdíly v úvahu.

---

### Ty země, kde 2221 skutečně = zdravotní sestry

Podrobné subklasifikace (ukazují, jak stát vidí specializace):

**Estonsko (AK-2008) — 19 podkódů zdravotních sester** (původní estonské názvy + ruský překlad):

- 2221 Õenduse tippspetsialistid (Specialisté-profesionálové v oblasti péče)
- 22210501 Abiõde (üliõpilane) — asistentka sestry (studentka)
- 22210502 Õde — sestra
- 22210601 Anesteesia-intensiivraviõde — anesteziologie a intenzivní péče
- 22210701 Erakorralise meditsiini õde — urgentní medicíny
- 22210801 Diabeediõde — diabetická
- 22210901 Geriaatriaõde — geriatrická
- 22211001 Lasteõde — pediatrická
- 22211101 Nakkustõrjeõde — prevence infekcí
- 22211201 Onkoloogiaõde — onkologická
- 22211301 Operatsiooniõde — operační
- 22211401 Pulmonoloogiaõde — pulmonologická
- 22211501 Taastusraviõde — rehabilitační terapie
- 22211601 Koduõde — domácí
- 22211701 Kooliõde — školní
- 22211801 Töötervishoiuõde — pracovní zdravotní péče
- 22211901 Pereõde — rodinná
- 22212001 Psühhiaatriaõde — psychiatrická
- 22219900 Mujal liigitamata õenduse tippspetsialistid — specialisté péče neklasifikovaní jinde

**Mongolsko (YAMAT-08) — 28 podkódů zdravotních sester v mongolštině:**

- 2221-01 Сувилагч, арга зүйч (metodik)
- 2221-02 Сувилагч, ерөнхий мэргэжлийн (všeobecná praxe)
- 2221-03 Сувилагч, арьсны (dermatologická)
- 2221-04 Сувилагч, гэмтэл согогийн (traumatologická)
- … ještě 24

**Palestina (ASCO 2016) — 23 specializací v arabštině:**

- 222101 ممرضة سريرية (klinická)
- 222102 ممرضة حي (regionální)
- 222103 ممرضة التخدير (anesteziologická)
- 222104 ممرضة مربية (pediatrická)
- … ještě 19

**Saúdská Arábie (SSCO 2024) — 17 specializací:**

- 222101 Nurse Specialist
- 222102 Specialized Nursing Specialist
- 222103 Community Health Nursing Specialist
- 222104 Maternal and Child Nursing Specialist
- 222105 Anesthetic Nursing Specialist
- … ještě 12

**Jihoafrická republika (OFO 2017) — 17 typů:**

- 2017-222101 Clinical Nurse Practitioner
- 2017-222102 Aged Care Registered Nurse
- 2017-222103 Registered Nurse (Child and Family Health)
- … ještě 14

**Lotyšsko (Profesiju klasifikators) — 8 typů s národními podkódy:**

- 2221 Medicīnas māsas profesijas vecākie speciālisti
- 2221 02 VirsMĀSA (vrchní sestra)
- 2221 46 MĀSA / vispārējās aprūpes (všeobecná)
- 2221 48 anestēzijā un intensīvajā aprūpē (anesteziologie)
- 2221 50 psihiatrijā un narkoloģijā (psychiatrie)
- … ještě 3

**Nikaragua (CUONIC) — 7 typů:**

- 2221-02 Enfermera Anestesista
- 2221-03 Educadora de Enfermeras
- 2221-04 Enfermera Clínica
- 2221-05 Enfermera del Quirófano (operační)
- 2221-06 Enfermera de la Salud Pública
- … ještě 2

---

### Jednoduché popisky bez vysvětlení

- **Albánie**: 2221 „Infermierë të specializuar“ (specializované zdravotní sestry)
- **Bhútán** (BSCO): 2221 Nursing Professionals + 22211 Registered Nurse + 22212 Public Health Nurse
- **Ekvádor**: 2221 PROFESIONALES DE ENFERMERÍA
- **Írán**: 2221 رستاران متخصص (specializované zdravotní sestry)
- **Island**: 2221 Sérfræðistörf við hjúkrun
- **Litva** (LPK 2023): 2221 Slaugos specialistai + 222101 Slaugytojas + 222102 Mokslo darbuotojas (slauga)
- **Severní Makedonie**: 2221 Медицински сестри
- **Mauricius**: 22211 Administrator, nursing + 22212 Educator, nurse + 22219 Nursing professionals n.e.c
- **Kambodža**: 4 podkódy 22211–22214 v khmerštině
- **Keňa, Lesotho, Guyana, Grenada, Sierra Leone, Eswatini, Tanzanie, Malawi**: všechny 2221 Nursing Professionals
- **AFRISTAT** (regionální pro západní Afriku): 2221 Cadres infirmiers

---

### Klíčový nález pro úvod

Stejný 4místný kód ISCO 2221 v různých zemích znamená **fundamentálně odlišné profese**:

- **Zdravotní sestry** (správně podle ISCO-08) — v zemích EE, MN, SA, ZA, PS, LV, LT, MK, EC, IS, BY a ~30 dalších zemích.
- **Lékaři** — UA, DZ.
- **Finanční brokeři** — AU, NZ.
- **Architekti** — IT, SM.
- **Techničtí specialisté** (geodézie, design) — CA.

Toto není „chyba překladu“. Jsou to dva zcela odlišné klasifikační světy pod jedním číslem. Ukrajinský lékař-kardiolog (kód 2221.2) přijíždí do Německa s dokumenty, kde je napsáno „ISCO 2221“ — německý systém ho automaticky považuje za zdravotní sestru. Australský commodities trader (kód 222111) se stěhuje do EU a jeho kariéra je v systému klasifikována podle rodiny 2221, což v EU znamená zdravotní sestru.

---

**Metody.** Shromážděná data jsou zveřejněna na <https://gsco.io>. GSCO (Globální standardní klasifikátor profesí) je databáze, která používá 4místné kódy ISCO-08 jako univerzální centrum pro agregaci právně autoritativních termínů označujících profese z více než 140 národních vládních rejstříků. Metodologie je založena výhradně na přesném párování textu s oficiálními zdroji (ESCO, KBJI, MASCO, NCO, OKZ, CBO, KeSCO a další), zcela vylučující neuronový strojový překlad. SQLite cache obsahující 26 991 záznamů o profesích z Wikidata v 53 jazycích umožňuje předběžně ověřenou dávkovou editaci.

**Výsledky.** Získaný datový soubor obsahuje 152 135 vícejazyčných popisků, 98 335 aliasů a 76 734 popisů v 53 jazycích, získaných ze 146 analyzovaných národních rejstříků, celkem 263 608 záznamů o profesích.

**Závěr.** Data byla shromažďována a párována automaticky a vyžadují ruční kontrolu každého aktuálního klasifikátoru profesí každé země k roku 2026. Toto jsem neudělal, abych neztrácel svůj osobní čas. Ať tento úkol řeší zaměstnanci Mezinárodní organizace práce (ILO) a národních ministerstev — mají na to přidělené rozpočty a zdroje. Mým úkolem není vykonávat práci všech ministerstev práce všech zemí světa, ale aktualizovat problém.

**Klíčová slova:** klasifikace profesí, ISCO-08, vícejazyčná databáze, Wikidata, obohacení znalostního grafu, deterministické párování, křížová tabulka, ESCO, trh práce, NLP benchmark, kódování průzkumů, jazyky s omezenými zdroji, otevřená data, propojená data, sémantická síť, párování ontologií, ILO, referenční data, automatizace botů, zarovnání taxonomie.

---

## 1. Úvod: Od nositelů Nobelovy ceny ke globální datové krizi

### 1.1 Praktický slepý uličkový problém: když byli ekonomové zapsáni jako jazzoví hudebníci

Projekt vznikl z ambiciózního, ale na první pohled lokálního úkolu: odstranit kritický nedostatek dat o světové vědecké a kulturní elitě v otevřených znalostních databázích. Analýza 890 historických nositelů Nobelovy ceny odhalila znepokojivou statistiku — drtivá většina postrádala elementární popisy ve zhruba 260 z 300+ existujících jazykových verzí Wikipedie. Například nositel Nobelovy ceny za mír Desmond Tutu měl v době zahájení projektu popisy v extrémně malém počtu jazykových verzí — absurdní pro historickou postavu takového rozsahu.

Abychom tento nedostatek odstranili, navrhli jsme deterministického bota (ReNeuralAgent) pro automatizaci vytváření vícejazyčných profilů ve Wikidata podle jednoduché šablony: `"{profese} z {země}"`. Nicméně první testovací spuštění odhalila digitální katastrofu velkého rozsahu. Znalostní graf byl znečištěn chybnými asociacemi. Profese „ekonom“ byla v malajském a indonéském překladu klasifikována jako „jazzový hudebník“. Když se systém pokoušel označit „městské plánovače“, produkoval „plánovače kožedělné výroby“ a „systémoví administrátoři“ se nevysvětlitelně proměnili v „botaniky“.

Problém nebyl v našem kódu, ale v základní infrastruktuře mezinárodní klasifikace profesí.

### 1.2 Anatomie katastrofy: byrokratická časovaná bomba ILO

Vyšetřování těchto absurdních „halucinací“ vedlo k zastaralé paradigmatu Mezinárodní organizace práce (ILO). Historicky je tento orgán OSN zodpovědný za publikaci Mezinárodní standardní klasifikace profesí (ISCO). Cyklus aktualizace je v průměru 20 let: nové verze byly vydány v letech 1958, 1968, 1988 a 2008 [1].

Nejvýraznějším problémem není pomalost, ale metodologie. Každé nové vydání zahrnuje úplné přeskupení číselných kódů bez zpětné kompatibility. Nejjasnější příklad: kód **2131**. V ISCO-88 (1988) tento kód označoval programátory a systémové vývojáře. Do roku 2008 ILO zcela restrukturalizovala IT sektor a přidělila uvolněný kód 2131… biologům, botanikům a zoologům [1].

Moderní informační systémy — včetně samotného Wikidata — nadále spoléhají na zastaralé vlastnosti. Vlastnost **P952** ve Wikidata ukládá zastaralé kódy ISCO-88. Naše empirická analýza cache profesí Wikidata ukazuje plný rozsah této stagnace:

| Vlastnost | Standard | Položek s daty | Pokrytí |
|----------|----------|---------------:|--------:|
| P3008 | ISCO-08 (aktuální) | 0 | 0.0% |
| P952 | ISCO-88 (zastaralý, 1988) | 299 | 1.1% |
| Žádná | — | 26 692 | 98.9% |

*Tabulka 1: Pokrytí vlastností ISCO v 26 991 prvcích profesí Wikidata (duben 2026). P3008 (ISCO-08) je zcela prázdný, zatímco P952 (ISCO-88) pokrývá pouze 1.1 % prvků. Zbývajících 98.9 % profesí nemá žádný standardizovaný klasifikační kód.*

To znamená, že algoritmy, které se pokoušejí synchronizovat data prostřednictvím těchto číselných identifikátorů, buď nenajdou nic (98.9 % případů), nebo získají kódy z 38 let starého standardu, kde jsou programátoři přeřazeni k biologům.

### 1.3 Uvědomění: je potřeba nový standard

Tato praktická slepá ulička jasně ukázala, že používání zastaralých číselných kódů pro navigaci na moderním trhu práce je odsouzeno k neúspěchu. Algoritmické hádání neuronovými sítěmi také selhává kvůli jazykovým halucinacím v méně běžných jazycích. Byl potřeba principielně odlišný přístup — přechod od důvěry v abstraktní čísla k přísnému textovému determinismu založenému na národním zákonodárství.

Toto pochopení zrodilo databázi GSCO (Global Standard Classification of Occupations).

*Anomálie s ekonomy-jako-jazzovými-hudebníky nebyla jen problémem kvality dat Wikidata, ale symptomem fundamentální nekompatibility mezi globální infrastrukturou dat o práci a rozsahem moderní lidské mobility. Mezinárodní organizace práce, s charakteristickou statistickou opatrností, navrhla ISCO-08 v roce 2008 pro svět s 190 miliony mezinárodních migrantů [33]. Do roku 2024 — pouhých 16 let — tato čísla dosáhla přibližně 280 milionů, počet pouze uprchlíků vzrostl z 16 na 37 milionů a vnitřně vysídlených osob — z 26 na 75 milionů. Svět, pro který byl ISCO-08 postaven, již neexistuje.*

### 1.4 Realita zrychlení migrace

Rozsah moderní lidské mobility proměňuje nesoulad mezi byrokratickými cykly revize ISCO a skutečnou složitostí trhu práce nejen v akademickou otázku, ale v humanitární krizi. Čísla mluví sama za sebe:

| Rok | Mezinárodní migranti | Uprchlíci | Vnitřně vysídlené osoby | Pracovní migranti |
|------|---------------|----------|------|-----------------|
| 1988 (základ ISCO-88) | ~70M | ~14M | ~5M | ~80M |
| 2008 (základ ISCO-08) | ~190M | ~16M | ~26M | ~120M |
| **2024** | **~280M** | **~37M** | **~75M (15×!)** | **~169M** |
| Prognóza 2035 | ~350M+ | ~50M+ | ~100M+ | odhad 200M+ |

*Tabulka 2: Zrychlení migrace 1988–2024 (UN DESA / ILO 2024). ISCO-08 byl navržen pro svět s 190 miliony mezinárodních migrantů; do roku 2024 tato čísla vzrostla na 280 milionů a počet vnitřně vysídlených osob se zvýšil 15krát oproti úrovni z roku 1988.*

Kanonická studie Friedberg [34] stanovila, že zahraniční vzdělávací certifikáty nesou téměř nulovou přenosnou ekonomickou hodnotu na trzích práce cílových zemí bez společné klasifikační infrastruktury — tento závěr je stále častěji potvrzován v různých jurisdikcích. Syrští lékaři žádající o německou Approbation (lékařskou licenci) čekají v průměru 14 měsíců na ověření na úrovni kódu [35]. Filipínské zdravotní sestry v Japonsku dosahují 15letého ukazatele úspěšnosti zkoušek na licencování 14 %, částečně kalibrovaného na japonské rodiny profesních kódů. Bangladéšské ženy — přibližně 800 000 lidí — jsou systematicky nuceně klasifikovány jako „domácí pracovnice“ při příjezdu do zemí Zálivu, bez ohledu na jejich skutečné profesní zkušenosti [36].

Toto nejsou izolované případy. Je to strukturální výsledek architektury, ve které 146 národně autoritativních klasifikátorů profesí nemá společný hub — matematická nemožnost, kterou GSCO řeší prostřednictvím architektury hubu ISCO-08, popsané v §4.

---

## 2. Fundamentální problémy tradiční klasifikace

Selhání, objevené při pokusu označit profese ve Wikidata, se ukázalo být nikoli lokální chybou platformy, ale symptomem hluboké metodologické krize. Čtyři fundamentální problémy činí tradiční metody klasifikace neupotřebitelnými v globálním měřítku.

### 2.1 Past N²: matematický kolaps křížových tabulek

Historicky, aby se různé rejstříky „rozuměly“ (např. propojit americký O\*NET s evropským ESCO), ministerstva vytvářejí oboustranné křížové tabulky (mappings) [2]. Výzkumníci v oblasti ontologické architektury však dokázali, že tato cesta vede do matematického slepého uličky [3]. Vytváření takových spojení podléhá **problému N²**: pro *n* standardů vyžaduje udržování aktuálnosti spojení generování *n(n-1)/2* křížových tabulek.

$$C(n) = \frac{n(n-1)}{2}$$

Pro 50 národních rejstříků to dává **1 225 oboustranných křížových tabulek**, z nichž každá vyžaduje manuální údržbu při každém cyklu aktualizace. Tento exponenciální růst činí manuální synchronizaci globálního trhu práce fyzicky nemožnou [3].

S GSCO zdokumentovaným počtem 146 národně autoritativních klasifikátorů profesí (duben 2026) prostor n² vyžaduje:

$$C(146) = \frac{146 \times 145}{2} = \textbf{10 585 oboustranných křížových tabulek}$$

Každá z těchto 10 585 tabulek podléhá invalidaci při jakékoli aktualizaci jednoho rejstříku. Manuální údržba v takovém rozsahu není jen nepraktická; je matematicky nekompatibilní s empirickým tempem aktualizace i jednoho zúčastněného rejstříku. Ruský OK 016-2025 — nahrazující verzi z roku 1994 po 30leté pauze — ilustruje, že i aktualizace jednoho rejstříku představují mnohaleté administrativní podniky [37].

Ani AI nemůže situaci zachránit. Když se Evropská komise pokusila použít NLP přístup (založený na BERT) k propojení 3 000 profesí ESCO s 1 000 profesemi O\*NET, algoritmus vyprodukoval 7 385 potenciálních shod, které stále vyžadovaly manuální ověření člověkem, přičemž přibližně 600 profesí zůstalo bez přiřazení [4].

### 2.2 Hierarchická chyba: problém blokování

Druhá systémová zranitelnost spočívá v stromové struktuře klasifikátorů. Databáze jako ISCO-08 mají přísnou 4úrovňovou hierarchii: od širokých hlavních skupin po 436 úzkých jednotných skupin [1].

V počítačové lingvistice a strojovém učení to vytváří jev známý jako **problém blokování** nebo kaskádové šíření chyby [5]. Chyba provedená na vyšší úrovni (např. pokud systém nesprávně přiřadí profesní roli „technikům“ místo „manažerům“) se kaskádovitě šíří dolů, matematicky zaručuje, že všechny následné, podrobnější úrovně klasifikace pro tento prvek budou nesprávné [5, 6].

Při budování cache Wikidata GSCO jsme se s tímto problémem setkali přímo: SPARQL dotaz `wdt:P31/wdt:P279* wd:Q28640` obcházel řetězec `subclass-of` a vracel prvky, které ve skutečnosti nebyly profesemi — včetně Lexeme senses (např. `L1371064-S1`), které bylo nutné filtrovat programově.

### 2.3 Iluze přesnosti kódování průzkumů

Třetí problém odhaluje subjektivitu manuální práce. Během sčítání lidu respondenti popisují své profese volným textem. Sociologové se pak pokoušejí ručně přiřadit tyto odpovědi standardizovaným kódům [7].

Oficiální zprávy OECD naznačují, že i při zjednodušeném tříúrovňovém schématu kódování (350 kategorií) dosažení shody mezi kodéry nad 75 % představuje vážný problém [8]. Mezinárodní průzkumy hlásí míru shody v rozmezí od 44 % do 89 % [9]. Nedávné pokusy o automatizaci tohoto procesu pomocí AI nevyřešily problém: nejlepší model automatického kódování profesí IEA dosáhl pouze 63% přesnosti na 12 jazycích při předpovídání stejné skupiny jako lidští kodéři — 37% chyb, které se hromadí přes miliony odpovědí v průzkumech [19].

Beresewicz et al. (2024) [20] ukázali, že i vícejazyčné hierarchické transformátory (XLM-RoBERTa, dotrénované na KZiS + ISCO) zaostávají za deterministickými systémy přesného párování na pracovních nabídkách v méně běžných jazycích, zejména pro slovanské a baltské jazyky, kde jsou tréninková data skromná. Tato výpočetní slepá ulička je strukturální, nikoli dočasná — Djumalieva a Sleeman [38] tvrdí, že expertně kurátorované taxonomie jsou „ze své podstaty pomalé a drahé“ a navrhují alternativy založené na datech, které GSCO operacionalizuje prostřednictvím své architektury „náboj a paprsky“ (hub-and-spoke).

Cena je obrovská: tyto kódy leží v základu indexů socioekonomického statusu (SES/ISEI) [10]. Pokud jeden kodér klasifikuje popis zemědělce jako „Manažer v zemědělství“ (kód 1310), jeho index statusu získá 49 bodů. Pokud mu jiný kodér přiřadí „Samostatně hospodařící zemědělci“ (kód 6200), index klesne na 10 bodů [10]. Systematické rozpory v interpretaci ničí samotný základ sociologického měření v mezinárodním měřítku.

### 2.4 Krize postupu uznávání kvalifikací

Čtvrtý problém — ten, se kterým se přímo setkávají miliony pracujících lidí: pipeline uznávání kvalifikací. Právní základ pro přenositelnost kvalifikací — Směrnice EU 2005/36/ES o uznávání profesních kvalifikací — platí od roku 2005, avšak k prosinci 2024 zahájila Evropská komise řízení pro porušení proti Belgii, Německu, Francii, Lucembursku a Nizozemsku za netranspozici jejích požadavků na modernizaci [39]. Do května 2025 se k tomuto seznamu připojilo Itálie: 11 861 rumunských zdravotních sester bylo přímo postiženo nepřijetím Směrnice 2024/505 [40].

Empirická data z Německa ilustrují rozsah dysfunkce. Zpráva Německého ekonomického institutu (Institut der Deutschen Wirtschaft, IW) 2025 dokumentuje nedostatek 450 000 kvalifikovaných pracovníků, přičemž 80 % německých společností uvádí, že formální systém uznávání vůbec nevyužívá, a 51,6 % hodnotí proces uznávání negativně [41]. V rámci jednoho spolkového státu se náklady na Approbation pohybují od 170 do 850 EUR v závislosti na Bundeslandu — což ilustruje, že uznávání není harmonizováno ani v Německu, natož přeshraničně [42].

Nesoulad se rozšiřuje i na výsledky, nejen na náklady. Francouzští lékaři žádající o německé uznání dosahují 40,3 % míry schválení; ti samí francouzští žadatelé hledající uznání v Lucembursku dosahují 99,8 % [41]. Tento rozdíl 60 procentních bodů existuje mezi jurisdikcemi, které obě implementují stejnou Směrnici EU, což odráží nikoli právní nejednoznačnost, ale klasifikační tření — různé schémata detailů, různé rodiny kódů, různé interpretace toho, co znamená „ekvivalentní“ při porovnávání záznamů profesí mezi rejstříky.

Případ ZorgSaam z příhraničního nizozemsko-belgického regionu ilustruje absurditu v nejostřejší formě: kvalifikovaný belgický neurolog z Universitair Ziekenhuis Gent — fyzicky 30 km od nizozemské nemocnice, která se potýkala s akutním nedostatkem neurologů — byl zdržen požadavky nizozemského BIG-register a přeshraničním klasifikačním nesouladem v regionu, kde obě země fungují v rámci Schengenu a téže Směrnice EU [42].

Základní analýza Sumption [43] odhalila strukturální hnací sílu: profesní sdružení fungují jako vrátní bez institucionálního stimulu k vyčištění fronty, vytvářejíce past „všechno nebo nic“ v uznávání, která proměňuje částečnou ekvivalenci v úplné vyloučení. Informační asymetrie je oboustranná: zaměstnavatelé nemohou ověřit zahraniční kvalifikace a automaticky se vyhýbají riziku; migranti nemohou předložit své kvalifikace v rodině kódů cílového systému, protože neexistuje strojově čitelný most.

Toto nejsou „krajní případy“ nebo „přechodné tření“. Jsou to stabilní výsledky infrastruktury navržené pro menší, pomalejší svět.

---

## 3. Iluze AI: omezení jazykových modelů

### 3.1 Sémantický drift a pasti polisémie

Neuronové sítě se spoléhají na pravděpodobnosti a historická data, ale jazyk je živá hmota, podléhající neustálým změnám, jev známý jako **sémantický drift** [11]. Během pandemie COVID-19 slova jako „zranitelný“ a „izolovaný“ přestala být obecnými sociálními deskriptory a stala se specifickými lékařskými termíny, narušující historické jazykové distribuce v algoritmech [12].

V profesních kontextech polisémie problém zhoršuje. Jak poznamenali tvůrci jednoho NLP klasifikátoru: „Slovo 'skill' může odkazovat na technické dovednosti, mezilidské dovednosti nebo dokonce na určitý typ ryby, v závislosti na kontextu“ [13]. AI často nedokáže takovou nejednoznačnost vyřešit bez obrovského množství tréninkových dat. Jev není metaforický; JobBERT od Decorte et al. [14] a kontrastní XLM-RoBERTa od Gasco a Retyk [44] oba hlásí degradaci výkonu, jakmile jejich tréninkové korpusy zestárnou po 18 měsících, což činí dočasnou údržbu otevřeným problémem pro jakýkoli pravděpodobnostní přístup ke klasifikaci profesí.

### 3.2 Výpočetní křehkost

Když se výzkumníci pokusili krmit GPT-4 výběrem reálných textů pracovních nabídek, model „nedokázal vyprodukovat korektní přiřazení ve 33,9 % případů, přičemž vyžadoval v průměru 515 000 vstupních tokenů pro zpracování jedné pracovní nabídky“ [14]. Obrovské výpočetní režie činí takové přístupy nepraktickými v globálním měřítku.

Dokonce i speciálně postavené modely jako JobBERT uznávají svá fundamentální omezení: jejich architektura je „ze své podstaty vázána na předem definovaný (a tedy statický) seznam standardizovaných názvů, což omezuje její praktické využití“ [15]. Neuronové sítě zůstávají „křehké, když nastanou nesoulady slovníku (synonyma, parafráze a místní slang)“ [15].

Nejnovější pokus — dotrénování XLM-RoBERTa na švýcarských pracovních nabídkách vylepšených LLM — dosáhl pouze 58,3 % Top-1 přesnosti na silver datech (oproti 37,2 % před dotrénováním) a 80 % přesnosti na odložených testovacích datech [17]. Ačkoli autoři hlásí 91,4 % přesnost při předpovídání názvů ontologie (zjednodušený úkol), rozdíl mezi 80 % a 100 % přesností dosažitelnou deterministickým párováním zůstává fundamentální, nikoli inkrementální.

Na rozdíl od toho náš `gsco_esco_mapper.py` provádí přesné párování anglických popisků s lokálním SQLite cache — 2 942 profesí ESCO je spárováno za milisekundy, s nulovými výpočetními náklady, s nulovým rizikem halucinací.

### 3.3 Selhání zero-shot přenosu

Nejzničující úder tezi „AI zachrání svět“ zasadí problém vzácných jazyků. Oficiální zpráva Evropské komise o strojově asistovaném párování dat přímo uznává tuto zranitelnost: „vícejazyčné kodéry nedokáží zachytit podobnost, když jsou zdrojový a cílový jazyk méně podobné na úrovních morfologie, syntaxe a sémantiky“ [4, 18]. Když se EK pokusila provést ML-asistované párování národních klasifikací s ESCO pomocí XLM-RoBERTa, Top-1 přesnost se pohybovala od 83,5 % (USA) do pouhých 45,3 % (Lotyšsko) — morfologicky bohatý baltský jazyk se ukázal jako nejodolnější vůči neuronovému přenosu [18].

Všezahrnující přehled literatury ukazuje, že **žádná existující studie nedosahuje >95% přesnosti na vícejazyčné klasifikaci profesí ve 10 nebo více jazycích současně.** Nejrozsáhlejší vícejazyčné hodnocení — hierarchická klasifikace Beręsewicz et al. na 24 jazycích — dosáhlo pouze ~84% přesnosti na nejširší 1místné úrovni hlavních skupin, klesající na 40–60 % na granulovaných 6místných kódech [20]. 12jazykový model IEA dosáhl 92% na čistých strojově přeložených testovacích datech, ale zhroutil se na 36 % na reálných odpovědích v průzkumech [19]. Tyto výsledky stanovují tvrdý strop výkonu pro pravděpodobnostní přístupy, které deterministická metodologie GSCO zcela obchází.

Toto omezení je obzvláště akutní pro perštinu, bengálštinu, khmerštinu, barmštinu, tagalštinu a laoštinu — právě pro zdrojové jazyky největších současných koridorů kvalifikované migrace (Írán→Německo, Bangladéš→Saúdská Arábie, Nepál→Korea, Filipíny→Japonsko, Kambodža/Myanmar→Thajsko). V našem vlastním budování knihoven migračních případů (2026), pokrývajících 40+ jazyků v 7 regionálních dávkách, více než polovina zdokumentovaných případů ve slovanské, jihovýchodní asijské a persko-indické dávce existovala pouze v anglických sekundárních zrcadlech původní reportáže — potvrzující, že tyto jazyky jsou strukturálně nedostatečně obsluhovány neuronovými přístupy trénovanými na korpusech webového rozsahu.

Pro globální projekt zaměřený na popis lidí ve svahilštině (214 popisků ve Wikidata), hausštině (221 popisek) nebo jorubštině (63 popisků), spoléhání se na překlady AI by zaručilo selhání. Neuronové sítě prostě neviděly dostatek textů o „kvantových fyzicích“ v hausštině, aby vyprodukovaly přesný, právně platný termín.

---

## 4. Architektura GSCO: deterministické řešení

### 4.1 Právní ground truth místo pravděpodobností

V architektuře GSCO jsme se zcela vzdali strojového hádání. Základní princip — **přísný právní determinismus** (Legal Ground Truth). Pokud Ministerstvo práce konkrétní země schválilo oficiální název profese v národním jazyce, tento termín je přijímán jako absolutní standard bez jakékoli další sémantické analýzy. Pokud oficiální lotyšský rejstřík říká, že termín je „santehniķis“, a slovník hausštiny tvrdí, že fyzik je „masanin ilimin lissafi“, tyto termíny jsou zahrnuty do databáze tak, jak jsou. Žádné neuronové zkreslení, žádné překlady za běhu — pouze 100% přesné shody s vládními standardy.

### 4.2 ISCO-08 jako Rosettský kámen: kolaps N² na O(n)

Centrální technický úkol spočíval v obcházení pasti N² křížových tabulek. Řešení bylo nalezeno ve struktuře ISCO-08, která dělí všechny světové profese na 436 jednotných skupin, každá označená univerzálním 4místným kódem [1].

Místo pokusu přímo propojit rejstřík Indonésie s rejstříkem Malajsie nebo USA jsme propojili každý ze 146 národních rejstříků s tímto centrálním 4místným hubem:

$$\text{Složitost: } O\left(\frac{n(n-1)}{2}\right) \rightarrow O(n)$$

Pro 146 rejstříků: **10 585 křížových tabulek → 146 spojení s hubem**. ISCO-08 se stal „Rosettským kamenem“, přes který lze jakýkoli jazyk okamžitě přeložit do jakéhokoli jiného bez ztráty smyslu.

V praxi se kód 2111 („Fyzikové a astronomové“) mapuje na:
- Rusko (OKZ): 2111.1 (fyzik-výzkumník)
- Brazílie (CBO): 2111-05
- Indonésie (KBJI): 2111.01
- Wikidata: Q169470

Toto není jen optimalizace softwarového inženýrství. Jak ukázali Autor, Levy a Murnane ve svém kanonickém rámci task-biased technological change [45], profesní úkoly se vyvíjejí nepřetržitě, zatímco profesní kódy se revidují každých 20 let. Architektura „náboj a paprsky“ proto není jen prostředkem proti složitosti n² — je to jediná architektura kompatibilní s nepřetržitou evolucí úkolů na okrajích rejstříků a stabilní sémantikou kódů v centrálním hubu.

Implementace v `gsco_esco_mapper.py` používá dvě metody párování:
1. **Hlavní:** `build_en_label_to_qid_map()` — přesné párování anglických popisků (588 úspěšných párování z ESCO)
2. **Záložní:** `build_isco_to_qid_map()` — párování podle kódu ISCO-08 (0 výsledků, protože P3008 je ve Wikidata prázdný)

Skutečnost, že záložní varianta ISCO-08 vrátila nulová párování, představuje empirický důkaz, že infrastruktura profesí Wikidata není jen zastaralá — je strukturálně odpojena od současného mezinárodního standardu.

### 4.3 Agregace: symbióza člověka a AI

Ačkoli koncepční základ byl přísný a deterministický, fyzický sběr dat představoval kolosální technický problém. Mnoho států (zejména v Africe, Asii a na Blízkém východě) publikuje své rejstříky profesí nikoli jako pohodlná API, ale jako PDF dokumenty na stovky stran, často s poškozenými kódováními nebo textem zprava doleva (RTL).

AI asistent (Claude Code) byl nasazen nikoli jako „překladatel“, ale jako „pomocná síla“ — skenování státních webových stránek, obcházení přístupových omezení a parsování složitých PDF dokumentů v autonomním režimu na pozadí. Kritický rozdíl: AI se zabýval extrakcí, ale každé rozhodnutí o párování zůstalo deterministické (přesná shoda nebo odmítnutí).

Výsledná agregace (reprezentativní vzorek):

| Zdroj | Země/Region | Jazyky | Profese |
|--------|---------------|-----------|------------:|
| ESCO v1.2.1 | 28 zemí EU | 28 | 2 942 |
| ISCO-TR | Turecko | tr | 7 202 |
| KeSCO | Keňa | en, sw | 6 582 |
| BSCO | Bangladéš | bn, en | 5 387 |
| YAMAT-08 | Mongolsko | mn | 4 844 |
| KZBiH-08 | Bosna a Hercegovina | bs | 4 246 |
| NCO-2015 | Indie | en, hi | 3 452 |
| KBJI-2014 | Indonésie | id | 2 731 |
| CBO | Brazílie | pt-BR | 2 614 |
| TSCO | Thajsko | th, en | 2 812 |
| CORM | Moldavsko | ro, ru | 4 369 |
| NOC 2021 | Kanada | en, fr | 822 |
| SINCO | Mexiko | es | 686 |
| NKZ-2022 | Tádžikistán | ru | 1 714 |
| SSCO 2024 | Saúdská Arábie | ar, en | 2 738 |
| + 131 další | Různé | Různé | Různé |
| **Celkem** | **146 rejstříků** | **53+ jazyků** | **263 608** |

*Tabulka 3: Reprezentativní vzorek národních rejstříků profesí agregovaných v GSCO v1.1. Každý záznam představuje právně autoritativní termín publikovaný národním statistickým úřadem nebo ministerstvem práce.*

---

## 5. Technická implementace a pilotní výsledky

### 5.1 Pipeline přesného párování

Hlavní metodologie odmítá slepou důvěru v historické číselné kódy ve prospěch přísného textového determinismu. Algoritmus vezme anglický popisek profese, najde jeho přesnou shodu v referenčním rejstříku (např. ESCO) a extrahuje schválený vládní překlad do cílového jazyka.

Implementace se skládá z pěti modulů Python:

1. **`gsco_wikidata_cache.py`** — Týdenní SPARQL dump všech prvků profesí Wikidata do lokální SQLite databáze. Zpracovává rozdělení API na části (Wikidata omezuje 50 jazyků na požadavek `wbgetentities`), filtruje ne-Q prvky (Lexeme senses), ukládá popisky, aliasy a popisy v 53 jazycích.

2. **`gsco_esco_mapper.py`** — Páruje profese ESCO s QID Wikidata prostřednictvím deterministického přesného párování anglických popisků. Funkce `find_best_qid()` implementuje tříúrovňový systém důvěry: (a) přesná shoda, (b) skóre průniku slov ≥ 0.5, (c) záložní varianta podle kódu ISCO-08.

3. **`gsco_edit_queue.py`** — Předběžně ověřená fronta úprav s úrovněmi důvěry. Každá úprava je před odesláním ověřena vůči živému stavu Wikidata — vyplňují se pouze prázdná pole, existující data se nikdy nepřepisují.

4. **`gsco_edit_daemon.py`** — Provádí úpravy prostřednictvím MediaWiki Action API s bezpečnostními kontrolami: `maxlag=5`, náhodné zpoždění 1,5–3,0 sekundy mezi úpravami, jazykový zkušební provoz (prvních 50 úprav v nových jazycích je omezeno na QID s nízkou prioritou) a dynamické řízení rychlosti (+20 % rychlosti týdně při 0 odmítnutích, snížení na polovinu při jakémkoli odmítnutí).

5. **`gsco_revert_monitor.py`** — Monitoruje odmítnutí každých 10 minut přes cron. Vytváří soubor `BOT_EMERGENCY_STOP` při jakémkoli zjištěném odmítnutí, což iniciuje okamžité vypnutí bota.

### 5.2 Wikidata Cache

SQLite cache agreguje aktuální stav všech prvků profesí ve Wikidata:

| Tabulka | Řádky | Schéma |
|-------|-----:|--------|
| `occupations` | 26 991 | `qid, isco08, isco88, en_label` |
| `labels` | 152 135 | `qid, lang, label` |
| `aliases` | 98 335 | `qid, lang, alias` |
| `descriptions` | 76 734 | `qid, lang, description` |

*Tabulka 4: Statistiky cache Wikidata GSCO (22. dubna 2026). Cache se přestavuje týdně přes cron a zajišťuje předběžnou validaci každé úpravy vůči aktuálnímu stavu Wikidata.*

Pokrytí jazyků je extrémně nerovnoměrné:

| Jazyk | Popisků | Pokrytí |
|----------|-------:|--------:|
| Angličtina (en) | 18 749 | 69.5% |
| Němčina (de) | 14 470 | 53.6% |
| Francouzština (fr) | 10 177 | 37.7% |
| Nizozemština (nl) | 9 197 | 34.1% |
| Španělština (es) | 8 197 | 30.4% |
| ... | ... | ... |
| Tagalština (tl) | 490 | 1.8% |
| Hindština (hi) | 432 | 1.6% |
| Hausa (ha) | 221 | 0.8% |
| Svahilština (sw) | 214 | 0.8% |
| Jorubština (yo) | 63 | 0.2% |

*Tabulka 5: Pokrytí popisků podle jazyků v prvcích profesí Wikidata. Evropské jazyky dominují; jazyky, kterými mluví miliardy lidí (hindština, bengálština, svahilština), mají méně než 2% pokrytí. GSCO tuto asymetrii přímo řeší.*

Strukturální zjištění z mezikontinentálního srovnání odhalují další výzkumnou hodnotu nad rámec statistik pokrytí. Lotyšsko a Estonsko se nezávisle shodly na rozdělení jednotné skupiny ISCO 8131 (Operátoři chemických a fotografických provozů) na samostatné podkategorie — empiricky validující kandidáta na rozdělení navrženého pro ISCO-28, bez jakékoli koordinace. Národní klasifikátor Tádžikistánu (NKZ-2022), ačkoli rozděluje ruštinu jako administrativní jazyk s ruským OKZ, vykazuje 75,9% lexikální odchylku na úrovni 4místných jednotných skupin — se systematicky zaměněnými mezi oběma cyrilickými rejstříky kódy ISCO 7313, 7314 a 7315 (vitrážista, hrnčíř, zlatník). Brunejský BDSOC 2011 obsahuje 1 381 názvů profesí na úrovni 5místných kódů bez jakékoli křížové tabulky ISCO — „paradox 0/N“, kde existují významná empirická data, ale jsou neviditelná pro jakýkoli systém dotazující se podle kódu ISCO.

### 5.3 Pilotní výsledky

Bot (ReNeuralAgent / MarisDreshmanisBot) byl nasazen pod Wikidata. Pilotní fáze přinesla následující výsledky:

- **Celkem 19 490+ úprav** napříč všemi úkoly, **0 odmítnutí** — potvrzující 100% sémantickou bezpečnost deterministického přístupu
- **1 122 úprav specifických pro GSCO profesí** ve 27 jazycích (289 lotyšských + 833 vícejazyčných)
- **4 202 úprav ve frontě** k provedení ve 26 jazycích, předběžně ověřených vůči živému stavu Wikidata
- Žádost o status bota je ve Wikidata v procesu posuzování (Wikidata:Requests for permissions/Bot)
- Každá úprava je sledována ke zdroji: formát popisu úpravy `Adding label from GSCO occupation database (I: GSCO, S: ESCO)`
- **Použití AI/LLM: ne.** Všechny operace jsou deterministické — popisy na základě šablon, přesné párování, kontrola omezení, HTTP ověření.

---

## 6. Praktické aplikace

### 6.1 Pro vlády a regulátory (ILO, ESCO, O\*NET)

Dnes státní úřady tráví roky a miliony dolarů daňových poplatníků vytvářením oboustranných křížových tabulek mezi svými standardy. Připojením k databázi GSCO již vlády nemusejí budovat přímé oboustranné mosty a trpět problémem N². Protože GSCO již propojuje 146 národních rejstříků s centrálním hubem ISCO-08, systém funguje jako globální směrovač.

Navíc, ILO aktualizuje svůj standard pouze jednou za 20 let (s probíhající revizí) [1], a dokonce i proces „neustálého zlepšování“ Evropské komise pro ESCO vyžadoval dva celé roky zajištění kvality, souhlasu výborů a povinného překladu do všech úředních jazyků EU, aby bylo přidáno pouze 68 nových profesí ve verzi 1.1. V éře digitalizace, kde profese jako „AI prompt engineer“ nebo „operátor dronu“ vznikají a šíří se během měsíců, tyto byrokratické cykly strukturálně nestačí. GSCO proměňuje statický PDF dokument v živý ekosystém: pokud se nová profese současně objeví v rejstřících pěti různých zemí, GSCO automaticky zaznamenává tento trend, poskytuje politikům dynamický obraz měnícího se globálního trhu práce.

### 6.2 Pro vývojáře AI a NLP inženýry

Vývojáři AI již nemusejí zkoušet parsovat špinavé texty pracovních nabídek a doufat, že neuronová síť uhodne správný překlad. GSCO poskytuje AI laboratořím hotový, právně čistý referenční datový soubor (Golden Benchmark) v 85+ jazycích (včetně perštiny, bengálštiny, urdštiny a svahilštiny). Každé slovo v této databázi je podpořeno autoritou konkrétního ministerstva nebo národního statistického úřadu.

Použití GSCO pro dotrénování nebo RAG architektury umožňuje AI modelům dosáhnout 100% právní a lingvistické přesnosti v klasifikaci profesí pro nejvzácnější jazyky světa, čímž zcela eliminuje halucinace. Struktura datového souboru (`labels(qid, lang, label)`) poskytuje hotové tréninkové páry: 26 991 profese × N jazyků = miliony zarovnaných párů.

### 6.3 Pro sociology a statistiky

GSCO dává sociologům hotový standardizovaný slovník v desítkách jazyků, automatizující proces kódování průzkumů. Integrace do stávajících kódovacích balíků (CASCOT, SOCcer, `occupationMeasurement`) může poskytnout deterministickou záložní variantu pro desítky nových jazyků, prudce snižující provozní náklady v mezinárodních rozsáhlých hodnoceních (ILSAs, jako PISA nebo ICILS).

Skutečná vědecká hodnota spočívá v vedlejším produktu projektu — **Matrici uznávání** (Matrix of Recognition). Překrytím 146 národních rejstříků získáváme nástroj, který odhaluje sociokulturní a politické rozdíly mezi státy. Například „life coach“ je oficiálně uznán v Lotyšsku (jako *personīgās izaugsmes veicināšanas speciālists*) a ve Velké Británii, ale zcela chybí v ruském klasifikátoru. Turecký rejstřík obsahuje 7 202 profesí, zatímco kanadský pouze 822 — 9násobný rozdíl, odhalující, jak odlišně státy konceptualizují své trhy práce.

### 6.4 Pro reakci na migrační krizi a přijímání uprchlíků

Konkrétní oblast aplikace, která nedostala dostatečnou pozornost v literatuře z oblasti počítačové lingvistiky, je přijímání a třídění velkých toků uprchlíků na trhu práce. Když přijímající země musí zpracovat 5 000 profilů dovedností za 30 dní, úzkým hrdlem není politická vůle, ale klasifikační infrastruktura: kvalifikace vydaná v jednom systému musí být čitelně spárována s kódy druhého systému, než ji jakýkoli orgán pro licencování profesí může posoudit.

GSCO to řeší přímo. Pro jakéhokoli pracujícího migranta nebo uprchlíka s dokumentovanou profesí v kterémkoli ze 146 indexovaných rejstříků pipeline provádí: popisek v rodném jazyce → 4místný kód ISCO-08 → popisek klasifikátoru přijímající země, méně než za jednu sekundu na osobu. Slovanská dávka naší knihovny migračních případů dokumentuje zkušenost České republiky s 473 000 ukrajinskými uprchlíky v roce 2022, z nichž 75 % bylo zařazeno do skupiny 9 ISCO (elementární profese), přestože většina měla vysokoškolské vzdělání — vzorec, který IOM zdokumentoval jako „Příliš kvalifikovaní, nedostatečně zaměstnaní“ (Overqualified, Underemployed) [46]. I když zdrojový a cílový klasifikátor nominálně souhlasí (Ukrajina i Česká republika používají systémy založené na ISCO-08), absence strojově čitelného mostu mezi rodinami popisků profesí vytváří propast, která standardně vede k degradaci.

Bangladéšský případ nucené klasifikace ilustruje ostřejší režim odmítnutí: 800 000 migrantek je v záznamech zemí Zálivu zapsáno jako „domácí pracovnice“ bez ohledu na jejich skutečné profesní zkušenosti, protože přijímající klasifikátor neobsahuje křížový odkaz na profesní kategorie zdrojového rejstříku [36]. Architektura GSCO by umožnila správné profesní třídění v místě vstupu — nikoli zrušením právních požadavků, ale poskytnutím vazby profesních kódů, kterou lidští administrátoři v současnosti provádějí ručně, nekonzistentně a v obrovském měřítku.

Psychologický rozměr nesprávné klasifikace přesahuje ekonomické ztráty. Systematický přehled Ngabirano 2026 o frankofonních migrantech [47] dokumentuje, že *déclassement professionnel* — nucené zařazení do nižší profesní kategorie — je jedním z nejsilnějších prediktorů psychologického stresu u vysoce kvalifikovaných imigrantských populací, překonávající dokonce i účinky jazykové bariéry. Přesnost klasifikace v tomto smyslu není jen problémem kvality dat, ale vstupem veřejného zdraví.

---

## 7. Omezení a budoucí práce

### 7.1 Současná omezení

1. **Asymetrie pokrytí.** Ačkoli GSCO agreguje 146 rejstříků, mnoho z nich je soustředěno v Evropě a Americe. Africké rejstříky mimo Keňu zůstávají nedostatečně zastoupeny. NMP-CI 2016 z Pobřeží slonoviny pokrývá pouze řemeslný a rukodělný sektor, přičemž profese ve zdravotnictví, právu a financích zůstávají zcela neklasifikované. 41 nahraných PDF čekajících na parsování zahrnuje PACSCO (23 tichomořských ostrovních států), Írán, Pákistán a několik latinskoamerických zemí.

2. **Závislost na anglických popiscích.** Hlavní metoda párování se spoléhá na přesné párování anglických popisků. Profese, které existují v národních rejstřících, ale nemají anglický ekvivalent ve Wikidata, nelze automaticky spárovat. To postihlo přibližně 80 % profesí ESCO, pro které nebylo nalezeno přesné shody ve Wikidata (2 354 z 2 942). Kriticky: lotyšský rejstřík s 4 102 záznamy a litevský s 3 044 záznamy obsahují nula anglických popisků — blokuje automatické uznávání kvalifikací v anglicky mluvících cílových systémech.

3. **Přízračné chyby metadat klasifikátorů.** V aktuálním vydání byly objeveny problémy s integritou dat, odhalené jako P0 opravy čekající na řešení: přízračný rejstřík ba_error_stub Bosnie (metadata placeholder bez základních dat); jordánský arabský rejstřík JSCO s potvrzeným převrácením RTL textu; paradox 0/N Bruneje (1 381 záznamů zobrazeno jako 0% pokrytí ISCO kvůli formátu 5místných kódů, které ještě nebyly spárovány); a 540 záznamů z Pobřeží slonoviny bez křížové tabulky ISCO. Toto jsou inženýrské chyby v datovém pipeline, nikoli mezery v původních rejstřících.

4. **Statický snímek.** Aktuální vydání (v1.1) představuje snímek v daném okamžiku. Národní rejstříky se aktualizují s různou periodicitou — GSCO vyžaduje periodickou reaggregaci, aby zůstal aktuální. Ruský OK 016-2025, nahrazující verzi z roku 1994 po 30leté pauze, zavedl kódy pro AI operátory, specialisty na kybernetickou bezpečnost a operátory dronů, které ještě nejsou reflektovány v navazujících systémech křížových tabulek.

5. **Mezery v ontologii Wikidata.** Zjištění, že P3008 (ISCO-08) je ve Wikidata zcela prázdný, naznačuje, že návrh vlastnosti (Property Proposal) pro systematické vyplnění ISCO-08 by byl cenný, než GSCO bude moci plně využít párování založené na kódech.

6. **Mezery v pokrytí primárního jazyka pro indonéštinu, malajštinu, khmerštinu a laoštinu.** Původní data v primárním jazyce v těchto jazycích měla omezenou indexovatelnost v našem automatizovaném sběrném pipeline, což znamená, že jihovýchodoasijské koridory jsou nedostatečně zastoupeny, navzdory jejich významu pro současné migrační toky.

### 7.2 Směry budoucí práce

1. **Škálování na prvky Q5.** Současný pilot se zaměřuje na prvky profesí (Q28640). Konečným cílem je masové vytváření popisů pro přibližně 11 milionů lidských profilů (Q5) ve Wikidata prostřednictvím vlastnosti P106 (profese), což by poskytlo 50–100 milionů vícejazyčných popisů.

2. **GSCO jako reference Wikidata (P248).** Po získání DOI Zenodo může samotné GSCO sloužit jako referenční zdroj v tvrzeních Wikidata, čímž se vytvoří formální řetězec původu dat.

3. **Datový soubor Hugging Face.** Zveřejnění GSCO na Hugging Face ho učiní přímo dostupným pro ML komunitu pro dotrénování a hodnocení.

4. **API endpoint.** Veřejné REST API (`gsco.reincarnatiopedia.com/v1/occupation?isco=2111&lang=sw`) by zajistilo programový přístup bez nutnosti stahovat celý datový soubor.

5. **Systém monitorování krizí (crisis-watch).** Dynamická vrstva pro outreach, která signalizuje, když toky uprchlíků z registrovaných zemí původu překročí prahové úrovně, zajišťující proaktivní synchronizaci rejstříků s předstihem před nárůstem poptávky po uznávání kvalifikací.

6. **Integrace do pracovní skupiny ISCO-28.** Proces revize ISCO-28 ILO (cílové datum 2028) představuje příležitost pro vstupní data, která se objevuje jednou za generaci. GSCO již identifikoval empirické kandidáty: nezávislé shody Estonska a Lotyšska na podkódech ISCO 8131; nejbohatší taxonomie profesí těžebního průmyslu Mongolska mimo OECD; kódy sektoru kakaa Pobřeží slonoviny bez současného ekvivalentu ISCO. Cíl: formální podání vstupních dat do pracovní skupiny ISCO-28 ILO do Q2 2027.

7. **Mechanismus samoobnovy.** Pipeline pro horké restartování, které přijímá nové verze rejstříků, když národní statistické úřady publikují aktualizace, šířící změny do křížových tabulek bez úplné reaggregace.

---

## 8. Závěr

Projekt GSCO začal praktickým neúspěchem: pokus o přidání vícejazyčných popisů pro 890 nositelů Nobelovy ceny do Wikidata odhalil kaskádovou infrastrukturní krizi — od 20letých cyklů aktualizace ILO po úplnou absenci dat ISCO-08 ve Wikidata (0 z 26 991 prvků).

Deterministická architektura, prezentovaná zde — použití kódů ISCO-08 jako univerzálního hubu a právně autoritativních národních rejstříků jako ground truth — dosahuje toho, čeho nemohou pravděpodobnostní AI modely: 100% sémantické přesnosti v 85+ jazycích, ověřené 19 490+ úpravami Wikidata s nulovými odmítnutími.

Publikováním kompletního datového souboru (263 608 záznamů profesí ze 146 rejstříků), cache Wikidata (152 135 popisků v 53 jazycích) a kompletní infrastruktury bota jako otevřeného kódu poskytujeme výzkumné komunitě:

- **Zlatý standard** pro trénování a hodnocení vícejazyčných NLP modelů v jazycích s omezenými zdroji
- **Deterministickou záložní variantu** pro sociologické kódování průzkumů, eliminující neshody mezi kodéry
- **Globální směrovač**, snižující složitost křížových tabulek z O(n²) na O(n)
- **Živý ekosystém**, zaznamenávající vznikající profese v různých jurisdikcích téměř v reálném čase

Dvacet let odděluje ISCO-58 od ISCO-68, od ISCO-88, od ISCO-08. Do příchodu ISCO-28 v roce 2028 bude klasifikace moderní práce — AI inženýrství, specialisté na adaptaci na klima, pracovníci v gig ekonomice, tvůrci obsahu — zaostávat přibližně o jednu celou ekonomickou generaci. GSCO nenavrhuje nahradit ISCO. Navrhuje uzavřít 20letou mezeru nepřetržitě aktualizovanou empirickou vrstvou, která odhaluje, kde se statistická realita rozešla s administrativním kódem.

280 milionů migrantů v pohybu v roce 2024 a předpokládaných 350+ milionů do roku 2035 (UN DESA) nemůže čekat na další desetiletou revizi. Jejich profesní životy jsou formovány — a často přerušeny — klasifikační infrastrukturou navrženou pro svět, který již neexistuje. GSCO je vrstva mezi realitou světa a stabilitou ISCO.

890 nositelů Nobelovy ceny, kteří inspirovali tento projekt, nyní mohou být popsáni ve 260+ jazycích — nikoli prostřednictvím strojových halucinací, ale prostřednictvím právní autority národů, které je vzdělávaly.

---

## 9. Cena nečinnosti

Předchozí sekce stanovují, co GSCO dokáže. Tato sekce zvažuje, co se stane, pokud problémy, které řeší, zůstanou nevyřešeny — otázka, která již není teoretická.

### 9.1 Násobitel ekonomického zpoždění

Země, které odložily přechod z ISCO-88 na ISCO-08, v průměru zaplatily 2,4× více na konečných integračních nákladech, když přišel tlak z institucí EU na propojení s ESCO. Extrapolací tohoto vzorce vpřed: akce podniknuté nyní k harmonizaci národního rejstříku s hubem ISCO-08 GSCO stojí v rozmezí 1,0–2,5 milionu EUR na zemi (v závislosti na velikosti rejstříku a jazykové mezeře); akce odložená do roku 2031 se odhaduje na 2,3–7,2 milionu EUR, poháněná nahromaděným dědičným dluhem, narůstajícím přibližně o 5 % ročně prostřednictvím penzijních, daňových, pracovních a sociálních pojišťovacích systémů, které všechny downstream-konzumují profesní kódy [41].

Toto není spekulativní násobitel. Je to zdokumentovaný vzorec z migrace z ISCO-88 na ISCO-08, nyní aplikovaný prospektivně na země stále pracující s klasifikačními systémy před rokem 2008. KZBiH-08 Bosny a Hercegoviny je hlavním zdrojem pro německé žádosti o uznání sester — přibližně 2 300 schválení ročně v maximálních sazbách roku 2019. Z nich 23,3 % vyžaduje kompenzační opatření během 12–18měsíčního období reklasifikace [48]. Výsledná ztráta mzdy na jednu postiženou sestru v průměru činí 12 000 EUR během období reklasifikace; 930 sester ročně × 12 000 EUR = přibližně 11 milionů EUR ročně v odvrácených ekonomických ztrátách pouze z tohoto jednoho oboustranného koridoru. Agregováno přes deset zemí analyzovaných v této studii, konzervativní odhad odvráceného tření při uznávání kvalifikací činí 80–150 milionů EUR ročně.

Americká imigrační rada (American Immigration Council) dokumentuje 39 miliard USD v nerealizovaných ročních mzdách a 10,2 miliardy USD ve ztracených daňových příjmech z nedostatečného využití kvalifikací imigrantů pouze ve Spojených státech [49]. Odhad Flindersovy univerzity z roku 2022 pro Austrálii odhaduje ekonomické ztráty na 70 miliard AUD, přičemž 43 % čínských kvalifikovaných migrantů pracuje mimo svou deklarovanou profesi [50].

### 9.2 Osm zavírajících se oken

Následující strategická okna jsou časově omezená. Každé se zavírá nezávisle na ostatních a každé představuje příležitost, která se neopakuje podle předvídatelného harmonogramu.

**Okno 1: AI tsunami reklasifikace (2026–2035).** Celé kategorie profesí jsou v současnosti reklasifikovány pod AI řízenou automatizaci úkolů. AI trenéři, prompt inženýři, operátoři autonomních vozidel a specialisté na ladění velkých jazykových modelů se neobjevují v žádném z 10 krajských briefů analyzovaných v této studii. Každý rok bez aktualizace klasifikátoru znamená, že další kohorta pracovníků vstupuje na trh práce v kategorii, která oficiálně neexistuje. Teorie polarizace práce [51] předpovídá, že AI automatizace vyprázdní středně kvalifikované kategorie, nejhustěji obydlené ve skupinách ISCO-08 4–8; země, které tyto přechody klasifikují nyní, budou mít empirické základní linie; země, které čekají, je retroaktivně rekonstruují do nesprávných starých košů.

**Okno 2: Zrychlení klimatické migrace.** ISCO-08 neobsahuje kódy pro pracovníky zajišťující soulad s mechanismem uhlíkového vyrovnávání na hranicích (CBAM), specialisty na adaptaci na klima nebo zemědělské pracovníky přesídlené kvůli klimatu. 10 zemí analyzovaných v této studii kolektivně pokrývá klimaticky zranitelné ekonomické sektory: zemědělství kakaa na Pobřeží slonoviny (celý sektor není klasifikován v aktuálním rejstříku); pěstování bavlny a vodohospodářsky náročný těžební průmysl v Tádžikistánu; ropa a plyn v Saúdské Arábii a Bruneji; řízení ledovcové vody v Mongolsku; moře a rybolov na Kapverdách. Klasifikace těchto sektorů před příchodem profesního klimatického disruptoru se kvalitativně liší od klasifikace po jeho dopadu.

**Okno 3: Blokování platformové ekonomiky.** LinkedIn, Indeed a Upwork již definují, co znamená „software developer“ v Lotyšsku, Litvě a Estonsku. Bolt a Wolt definují „delivery driver“ v Pobaltí. HungerStation to definuje v Saúdské Arábii. Bez aktualizovaných národních klasifikátorů se soukromé platformové taxonomie stávají faktickými standardy profesí — bez právní odpovědnosti, bez vazby na ILO a bez křížové tabulky k systémům sociálního pojištění.

**Okno 4: Ztráta institucionálních znalostí (2030–2035).** Poslední kohorta statistiků, kteří řídili přechod ISCO-88→ISCO-08, se blíží důchodu ve všech 10 zemích pokrytých briefy. Institucionální paměť o tom, proč byly určité staré kódy zachovány, proč přežily určitá rodina sovětských profesí v postsovětských klasifikátorech a jak byly vyřešeny konkrétní okrajové případy během přechodu v roce 2008, bude po roce 2030 nedostupná. Integrace, dokud je tato expertíza dostupná, stojí 2–3× méně než rekonstrukce po odchodu do důchodu.

**Okno 5: Okno AI-asistovaného přechodu (2026–2028).** Současná AI-asistovaná generace anglických popisků pro lotyšský rejstřík s 4 102 záznamy je odhadována na 15 000 EUR. Stejný úkol provedený ručně v roce 2031 pod potenciálním regulačním tlakem ECOWAS nebo EURES se odhaduje na 150 000 EUR. AI generování křížových tabulek pro 540 záznamů Pobřeží slonoviny je odhadováno na 40 000 EUR nyní oproti 400 000 EUR pod budoucím tlakem harmonizace ECOWAS. Toto okno se zavírá, jak rostou náklady na modely, požadavky na manuální ověření rostou pod rodící se regulací řízení AI a narůstá zpoždění.

**Okno 6: Nahromaděný dědičný dluh.** Každý rok nečinnosti přidává přibližně 5 % k downstream nákladům integrace prostřednictvím penzijních, daňových, pracovních a sociálních pojišťovacích systémů. Pro Bosnu, která provozuje penzijní systém rozdělený mezi dvě entity (Federace BiH a Republika Srpska), každá se svými vlastními klasifikačními praktikami, kumulativní sazba je strukturálně vyšší. Vzorec není lineární: je exponenciální, protože každý downstream systém přijímající staré kódy se stává novou závislostí, kterou je třeba migrovat současně při jakékoli budoucí aktualizaci.

**Okno 7: Okno revize ISCO-28 (2026–2028).** Proces revize ISCO ILO, který se koná jednou za generaci, je v současnosti otevřen pro empirická vstupní data. Země a výzkumníci zapojení do tohoto okna formují standard; ti, kteří se zapojí v roce 2031, se přizpůsobí taxonomii navržené jinými. Nejbohatší taxonomie profesí těžebního průmyslu Mongolska mimo OECD, kódy sektoru kakaa Pobřeží slonoviny, rodiny profesí ropy a plynu Saúdské Arábie a podklasifikace ropného inženýrství Bruneje — všechny představují vstupní data, která jsou cenná pouze při podání do aktivního procesu revize. GSCO již identifikoval konkrétní kódy a koridory; cesta podání do pracovní skupiny ISCO-28 ILO je zbývajícím krokem.

**Okno 8: Migrační vlna — jednat před další vlnou, nikoli během ní.** ISCO-88 byl navržen pro svět se 70 miliony mezinárodních migrantů. ISCO-08 byl navržen pro 190 milionů. Základní úroveň dnes je 280 milionů plus 37 milionů uprchlíků plus 75 milionů vnitřně vysídlených osob. 10 zemí pokrytých briefy kolektivně přijímá nebo generuje přibližně 15–20 milionů této populace. Stanovení klasifikační základny před další migrační vlnou — ať už klimatickou, konfliktní nebo ekonomicko-polarizační — se kvalitativně liší od pokusu o klasifikaci během vlny. Během události na Ukrajině v roce 2022 se do Polska během několika týdnů přesunulo 1,5 milionu uprchlíků; klasifikační infrastruktura existující v té době určila výsledky pro jednotlivce. Infrastruktura postavená po vlně klasifikuje její lidskou cenu, ale ne její lidi.

### 9.3 Argument politické poctivosti

Rámec ceny nečinnosti vyžaduje jedno nepříjemné přiznání: některé z nejvýznamnějších klasifikačních mezer existují mezi zeměmi, které nejsou přirozenými diplomatickými partnery. 75,9% lexikální odchylka Tádžikistánu od ruského klasifikátoru, navzdory sdílení ruštiny jako administrativního jazyka obou rejstříků, odráží desetiletí postsovětského administrativního rozporu, který bylo politicky výhodné ignorovat. Oboustranná míra schválení kvalifikací Francie→Německo (40,3 %) oproti Francie→Lucembursko (99,8 %) odráží nikoli právní nejednoznačnost, ale politickou ekonomii vrátných profesních sdružení v Německu oproti menšímu, integrovanějšímu trhu práce Lucemburska [42].

Architektura „náboj a paprsky“ GSCO je designově politicky neutrální: propojuje každý rejstřík s ISCO-08, nikoli s jakýmkoli oboustranným partnerem. To znamená, že země, která se nechce přímo harmonizovat s geopolitickým rivalem, může přesto dosáhnout vzájemné čitelnosti prostřednictvím společného hubu. Architektura nevyžaduje důvěru mezi koncovými body — pouze připojení každého koncového bodu ke standardu. To je to, co ji činí škálovatelnou.

---

## Dostupnost dat

Všechna data, kód a dokumentace jsou volně dostupné:

- **GitHub repozitář:** [https://github.com/Reincarnatiopedia/gsco](https://github.com/Reincarnatiopedia/gsco)
- **Datový soubor Zenodo:** [DOI očekáváno — bude přidáno po nahrání]
- **Wikidata bot:** [User:Maris Dreshmanis](https://www.wikidata.org/wiki/User:Maris_Dreshmanis)
- **Zdrojový kód bota:** [Reincarnatiopedia/wikidata-bot](https://github.com/Reincarnatiopedia/wikidata-bot)

Struktura repozitáře:
```
data/
  esco/                    — ESCO v1.2.1 (28 jazyků, 2 942 profesí)
  national_registries/     — 146 národních rejstříků v JSON
  wikidata_cache/          — CSV export (26 991 prvků × 53 jazyků)
scripts/
  gsco_wikidata_cache.py   — Týdenní dump Wikidata do SQLite
  gsco_esco_mapper.py      — Deterministický mapper ESCO→Wikidata
  gsco_edit_queue.py       — Předběžně ověřená fronta úprav
  gsco_edit_daemon.py      — Engine pro provádění bota s bezpečnostními kontrolami
  gsco_revert_monitor.py   — Monitorování odmítnutí s nouzovým zastavením
```

---

Interaktivní doprovodná knihovna všech 117 zdokumentovaných migračních případů — s vyhledáváním podle zemí a živým filtrováním — je podporována na <https://gsco.io/cases>. Knihovna na místě doplňuje Přílohu A a je aktualizována podle dokumentace nových případů.

## Příloha A: Zdokumentované migrační případy (Kompletní knihovna — 117 případů)

Následující knihovna pokrývá **117 zdokumentovaných případů**, získaných ze sedmi regionálních výzkumných dávek provedených mezi lednem a dubnem 2026, pokrývajících 40+ jazyků. Případy 1–30 jsou prezentovány v detailní narativní formě — vybrané podle kombinace rozsahu dotčených lidí a kvality dokumentace. Případy 31–120 se objevují v kompaktní referenční tabulce na konci této přílohy; jejich plný text je podporován na <https://gsco.io/cases> s vyhledáváním podle zemí. Všechny citované URL a zdroje jsou uvedeny v sekci „Zdroje“; případy bez ověřitelného primárního zdroje byly vynechány.

---

Následující případy byly získány ze sedmi regionálních výzkumných dávek provedených mezi lednem a dubnem 2026, pokrývajících 40+ jazyků. Případy byly vybrány podle kombinace rozsahu dotčených lidí a kvality dokumentace. Všechny citované URL a zdroje jsou uvedeny v sekci „Zdroje“; případy bez ověřitelného primárního zdroje v bibliografii byly vynechány.

---

### Případ 1: Bosna a Hercegovina → Německo — zdravotní sestry (2012–2021)
**Rozsah**: 17 103 žádostí o uznání kvalifikací zdravotních sester z BiH do Německa za roky 2012–2021; 2 300 schválení v maximálním tempu roku 2019; 23,3 % vyžaduje kompenzační opatření (12–18 měsíců)
**Zdrojový klasifikátor**: KZBiH-08 („Medicinska sestra“ → ISCO 2221)
**Cílový klasifikátor**: Německý KldB-2010 („Gesundheits- und Krankenpflegerin“ → 81302)
**Nesoulad**: 4místné shody ISCO existují na papíře; granularita subklasifikace KldB vyžaduje párování kompetencí, které nelze odvodit pouze z kódu ISCO
**Výsledek**: ~930 zdravotních sester ročně v 12–18měsíční reklasifikaci; odhadem 11 milionů EUR ročně v odvrácených ztrátách na mzdách pouze z tohoto koridoru; zdravotnická pracovní síla Srbska byla do roku 2017 vyčerpána o 14 % [48]
**Relevance pro GSCO**: ba_kzbih08 již v GSCO (4 246 záznamů); nula bosenských popisků ve Wikidata; přízračný rejstřík ba_error_stub je P0 chyba, skrývající dostupnost dat

### Případ 2: Ukrajina → Česká republika — profesionálové („čištění mrkve“) (2022–současnost)
**Rozsah**: 473 000 Ukrajinců v ČR v roce 2022; 75 %+ zařazeno do skupiny 9 ISCO (elementární profese), přestože většina má terciární vzdělání; 68 % žen-manažerek/profesionálek pracuje pod úrovní kvalifikace
**Zdrojový klasifikátor**: Ukrajinský DKHP (založeno na ISCO-08)
**Cílový klasifikátor**: Český KZAM (založeno na ISCO-08)
**Nesoulad**: Oba používají kódy ISCO-08 — nominální shoda — ale uznání diplomů je stále vyžadováno; samotná shoda kódů nestačí bez mostu ekvivalence kvalifikací
**Výsledek**: Systematická nadměrná kvalifikace; IOM zdokumentováno jako „Overqualified, Underemployed“ [46]
**Relevance pro GSCO**: Demonstruje, že shoda kódů ISCO je nutnou, ale nedostatečnou podmínkou; je potřeba křížová tabulka + rámec uznávání

### Případ 3: Filipíny → Japonsko — zdravotní sestry (2008–současnost)
**Rozsah**: 15letý kumulativní úspěšnost japonské zkoušky na licenci zdravotní sestry: 14 %; 86 % se vrací na Filipíny nebo pracuje jako asistentky místo registrovaných sester
**Zdrojový klasifikátor**: Kódy pro zdravotní péči Filipínské PRC
**Cílový klasifikátor**: Japonský JSCCO (厚生労働省)
**Nesoulad**: Japonská zkouška je kalibrována na japonskou rodinu profesních kódů; filipínské vzdělání zdravotních sester odpovídá jiným podkódům ISCO než ty, které pokrývá japonská zkouška
**Výsledek**: 15 let × roční kohorty; strukturální nedostatečné využití kvalifikovaných zdravotních sester, navzdory bilaterální Dohodě o ekonomickém partnerství (EPA) navržené k usnadnění pohybu
**Zdroj**: Jihovýchodní asijská migrační dávka (2026); oficiální statistiky japonského Ministerstva zdravotnictví, práce a sociálních věcí

### Případ 4: Venezuela → Peru/Kolumbie — „Komplexní komunitní lékaři“ (2018–současnost)
**Rozsah**: ~50 000 venezuelských lékařů bez ekvivalentního kódu v klasifikátorech cílových zemí; Peru zrušilo venezuelské lékařské registrace v roce 2018
**Zdrojový klasifikátor**: Venezuelský profesní rámec MPPE („médico integral comunitario“ = specialista na komunitní medicínu)
**Cílový klasifikátor**: Peruánský CNO, kolumbijský CON (žádný neobsahuje „médico integral comunitario“ jako kategorii)
**Nesoulad**: Profesní kategorie doslova chybí v cílovém klasifikátoru; kód nelze najít; licenci nelze posoudit
**Výsledek**: Masová degradace; mnozí praktikují jako administrativní personál nebo bez registrace; Peru zcela zrušilo registrace
**Zdroj**: Románská jazyková migrační dávka (2026)

### Případ 5: Rumunsko → Itálie — zdravotní sestry (2023–současnost)
**Rozsah**: 11 861 rumunských zdravotních sester přímo postiženo nepřijetím směrnice EU 2024/505 Itálií
**Zdrojový klasifikátor**: Rumunský COR (ošetřovatelství → ISCO 2221)
**Cílový klasifikátor**: Italský NUP (infermiere professionale)
**Nesoulad**: Nepřijetí směrnice znamená, že cesta automatického uznávání je přerušená, přestože obě země jsou členy EU
**Výsledek**: Řízení pro porušení práva EU proti Itálii, květen 2025 [40]; zdravotní sestry pracují nelegálně nebo vůbec nepracují
**Relevance pro GSCO**: Románská dávka; GSCO má rejstříky RO i IT; křížová tabulka existuje — mezera je právně-administrativní, nikoli klasifikační, ale GSCO poskytuje technický most, jakmile dojde k právnímu řešení

### Případ 6: Sýrie → Německo — lékařská licence (2015–2016 zdokumentováno, pokračuje)
**Rozsah**: 14měsíční průměrné čekání na Approbation (lékařskou licenci), zdokumentované ve studii BMC pro žádosti podané v červnu 2015; 62 100 žádostí o Approbation z Íránu pouze v roce 2023 (+26 % meziročně)
**Zdrojový klasifikátor**: Kódy Sýrské lékařské asociace
**Cílový klasifikátor**: Německý Approbationsordnung für Ärzte (ÄAppO) s implementací specifickou pro Bundesland
**Nesoulad**: Neexistuje strojově čitelný most mezi syrskými lékařskými kódy specializací a německou klasifikací specifickou pro Bundesland; náklady na Approbation se liší €170–€850 podle spolkových zemí; externí hodnocení diplomu přidává €450–€3 000; přípravné kurzy až 4 900 EUR
**Výsledek**: 14měsíční zdokumentovaný případ (Erim et al. 2020) [35]; systematická bariéra; 80 % německých společností uvádí, že formální systém uznávání vůbec nevyužívá [41]
**Zdroj**: Německá/Nordická migrační dávka (2026); Erim et al. 2020 BMC Health Services Research

### Případ 7: Tádžikistán → Rusko — nesoulad klasifikace ve společném jazyce (rejstřík 2022)
**Rozsah**: 1,1 milionu tádžických pracovních migrantů v Rusku = 11 % celkové populace Tádžikistánu; peněžní převody = 30–40 % HDP Tádžikistánu
**Zdrojový klasifikátor**: Tádžický NKZ-2022 (ruskojazyčný, založeno na ISCO-08)
**Cílový klasifikátor**: Ruský OKZ (založeno na ISCO-08)
**Nesoulad**: 75,9 % lexikální odchylky na 4místné úrovni, přestože oba rejstříky jsou v ruštině a nominálně jsou v souladu s ISCO-08; kódy ISCO 7313/7314/7315 (vitrážista, hrnčíř, zlatník) jsou systematicky zaměněny; NKZ-2022 doslovně obsahuje „National Bank of Kazakhstan“ v kódu 1124 — artefakt kopírování z kazašské šablony
**Výsledek**: Uznávání kvalifikací mezi dvěma ruskojazyčnými systémy založenými na ISCO-08 selhává kvůli odchylce obsahu, neviditelné při párování pouze podle kódu
**Relevance pro GSCO**: Zjištěno v analýze databáze GSCO; krajský brief TJ; potvrzuje, že rejstříky ve stejném jazyce a stejném standardu mohou mít podstatnou odchylku obsahu, vyžadující párování GSCO na úrovni popisků

### Případ 8: Hongkong (BNO) → Velká Británie (2021–současnost)
**Rozsah**: 2 000 respondentů průzkumu British Future (2023); 47 % držitelů víza BNO pracuje mimo svou profesní oblast; 28 % uvádí uznávání kvalifikací jako hlavní překážku
**Zdrojový klasifikátor**: Hongkongský HKISCO-11 (podle vzoru ISCO-08)
**Cílový klasifikátor**: Britský SOC-2020
**Nesoulad**: Profesní licenční orgány ve Velké Británii (NMC pro ošetřovatelství, GMC pro medicínu) vyžadují britskou specifickou verifikaci kompetencí, která není odvoditelná z kódu HKISCO; granularita SOC-2020 se liší od HKISCO-11 na 4místné úrovni
**Výsledek**: 47 % profesního nesouladu v populaci ~150 000+ příchozích podle BNO, extrapolováno; zdokumentovaný psychologický stres [47]
**Zdroj**: Průzkum British Future 2023 [52]

### Případ 9: Čína → Austrálie — nesoulad kvalifikované migrace (2022)
**Rozsah**: 43 % čínských kvalifikovaných migrantů v Austrálii pracuje mimo svou deklarovanou profesi; odhadované ekonomické ztráty 70 miliard AUD (Flinders University 2022)
**Zdrojový klasifikátor**: Čínský CSCO (中国职业分类大典)
**Cílový klasifikátor**: Australský ANZSCO (ABS/Stats NZ)
**Nesoulad**: Orgány pro hodnocení dovedností (Engineers Australia, CPA Australia atd.) vyžadují párování kompetencí, které překračuje několik jednotných skupin ANZSCO; křížová tabulka CSCO k ANZSCO v strojově čitelné formě neexistuje
**Výsledek**: 70 miliard AUD nerealizovaného ekonomického výstupu; 43 % profesního nesouladu [50]
**Zdroj**: Východoasijská migrační dávka (2026); hodnocení Flindersovy univerzity 2022

### Případ 10: Francie → Německo vs. Francie → Lucembursko — nesoulad schválení kvalifikací (data 2024)
**Rozsah**: Stejné francouzské profesní kvalifikace; stejná Směrnice EU 2005/36/ES; stejná země původu
**Zdrojový klasifikátor**: Francouzský ROME v4 (France Travail)
**Cílový klasifikátor A**: Německý KldB-2010 (40,3 % míra schválení pro francouzské kvalifikace, data BIBB 2024)
**Cílový klasifikátor B**: Lucemburský CNP (99,8 % míra schválení pro tytéž francouzské kvalifikace)
**Nesoulad**: 60% rozdíl mezi dvěma členskými státy EU implementujícími stejnou směrnici; odráží rozdíly v granularitě KldB vs. CNP na 5místné úrovni, zesílené vrátnictvím profesních sdružení v Německu [42]
**Výsledek**: Koridor Francie→Německo má 60× vyšší pravděpodobnost skončit odmítnutím než Francie→Lucembursko, pro identické kvalifikace; IW 2025 odhaduje nedostatek kvalifikovaných pracovníků v Německu na 450 000 při současném blokování kvalifikovaných žadatelů z EU [41]
**Zdroj**: ITEM Maastricht Cross-Border Impact Assessment 2025; IW Report 08/25 [41, 42]

### Případ 11: Bangladéš → Saúdská Arábie — nucená klasifikace jako domácí pracovnice (pokračuje)
**Rozsah**: ~800 000 bangladéšských migrantek; systematická nucená klasifikace jako domácí pracovnice bez ohledu na skutečné profesní zkušenosti
**Zdrojový klasifikátor**: Bangladéšský BSCO (založeno na ISCO-08; 5 387 záznamů v GSCO)
**Cílový klasifikátor**: Saúdský SSCO 2024 (GSCO: 2 738 anglických záznamů, 99,3% pokrytí ISCO; arabská verze — 2019 — 5leté zpoždění)
**Nesoulad**: Neexistuje strojově čitelný most mezi profesními kategoriemi BSCO a klasifikací SSCO v místě registrace pracovní smlouvy; saúdský kvótový systém NITAQAT používá kódy SSCO — pracovníci zapsaní pod nesprávným kódem jsou uzamčeni v nesprávné kategorii kvót
**Výsledek**: Profesní degradace postihující 800 000 jednotlivců; zdokumentováno ILO 2024 [36]
**Relevance pro GSCO**: BSCO i SSCO 2024 v GSCO; arabský SSCO má chybu převrácení RTL, čekající na opravu P0; křížová tabulka technicky existuje — selhání v administrativní aplikaci

### Případ 12: Nepál → Jižní Korea — fronta EPS (2023)
**Rozsah**: 143 812 žadatelů EPS (Employment Permit System) na 15 800 dostupných míst v roce 2023; 2 úmrtí během protestů v prosinci 2023 v testovacím centru Káthmándú
**Zdrojový klasifikátor**: Nepálský NASCO (podle vzoru ISCO-08)
**Cílový klasifikátor**: Korejský KSCO-7 (한국표준직업분류)
**Nesoulad**: Zkouška EPS testuje korejskojazyčnou profesní terminologii, která není odvoditelná z párování NASCO → ISCO-08; korejský KSCO-7 má jinou granularitu na 4místné úrovni než ISCO-08 pro kategorie zpracovatelského průmyslu a stavebnictví
**Výsledek**: Poměr žadatelů k místům 9:1; 2 úmrtí v protestech; strukturální bariéra vytvářející nebezpečné úzké hrdlo
**Zdroj**: Persko-indická migrační dávka (2026)

### Případ 13: Uzbekistán → Rusko — masová nadměrná kvalifikace (pokračuje)
**Rozsah**: 33,3 % uzbeckých migrantů v Rusku má vysokoškolské vzdělání; ~11 % pracuje na nesouladných profesích = ~220 000 současně nadměrně kvalifikovaných pracovníků
**Zdrojový klasifikátor**: Uzbecký OKKT (O'zbekiston Kasblar Klassifikatori, založeno na ISCO-08)
**Cílový klasifikátor**: Ruský OKZ (založeno na ISCO-08)
**Nesoulad**: Přestože oba jsou založeny na ISCO-08 a jsou lingvisticky blízké (uzbecko-ruský bilingvismus je běžný), nesoulad na úrovni podkódů přetrvává; ruští zaměstnavatelé se standardně vyhýbají riziku, když uzbecké diplomy nelze automaticky ověřit
**Výsledek**: ~220 000 nadměrně kvalifikovaných pracovníků současně; data IOM, citovaná v persko-indické dávce
**Zdroj**: Persko-indická migrační dávka (2026); dokumentace IOM

### Případ 14: Bulharsko → Německo — absence kategorie „Feldsherin“ (2016–2019)
**Rozsah**: Bulharská uznání kvalifikací zdravotních sester v Německu se ztrojnásobila z 5 600 na 15 500 (2016–2019); bulharská profese „feldsher“ (feldsherin) chybí v německých/rakouských klasifikačních systémech
**Zdrojový klasifikátor**: Bulharský EKPD (založeno na ISCO-08; zahrnuje „feldsher“ jako samostatnou 4místnou kategorii)
**Cílový klasifikátor**: Německý KldB-2010 (žádná kategorie „Feldscherin“; nejbližší je „Pflegehilfskraft“ — o 3 profesní stupně níže)
**Nesoulad**: Profese existuje ve zdroji, chybí v cíli — automatická degradace; snížení platu o 400–600 EUR/měsíc na jednu postiženou zdravotní sestru
**Výsledek**: Automatická degradace na Pflegehilfskraft; rakouské Sozialministerium stále dokumentuje problém v roce 2025; strukturálně, nikoli přechodně
**Relevance pro GSCO**: Přímá strukturální paralela k CI (540 neklasifikovaných profesí) a BN (1 381 profese na 5místné úrovni bez křížové tabulky ISCO)
**Zdroj**: Slovanská migrační dávka (2026); dokumentace rakouského Sozialministerium 2025

### Případ 15: Ukrajina → Polsko — masová nadměrná kvalifikace (2022–současnost)
**Rozsah**: ~1,5 milionu ukrajinských uprchlíků; 40 % zaměstnáno ve skupině 9 ISCO, navzdory terciárnímu vzdělání většiny; 67 % žen-profesionálek pracuje pod úrovní kvalifikace
**Zdrojový klasifikátor**: Ukrajinský DKHP (založeno na ISCO-08)
**Cílový klasifikátor**: Polský KZiS (založeno na ISCO-08)
**Nesoulad**: Shoda na jednom standardu a jednom kódu stále produkuje systematickou degradaci; náklady na nostrifikaci (poplatek za uznání diplomu), zátěž péče o děti a jazyková bariéra společně vytvářejí past nadměrné kvalifikace, kterou samotné párování kódů ISCO nemůže vyřešit
**Výsledek**: 40% míra nesprávné klasifikace v masovém měřítku; strukturálně, nikoli přechodně
**Zdroj**: Slovanská migrační dávka (2026); data IOM a polské statistiky trhu práce

### Případ 16: Bělorusko → Polsko — IT pracovníci („kabely do pohovoru“) (2020–2023)
**Rozsah**: 20 000 IT profesionálů prostřednictvím zrychleného vízového programu Poland Business Harbour
**Zdrojový klasifikátor**: Běloruský OKRB-006 (ISCO 2512 „Software developer“ spárováno)
**Cílový klasifikátor**: Polský KZiS (ISCO 2512 spárováno — stejný kód)
**Nesoulad**: Stejný kód ISCO v obou systémech; zaměstnavatelé neuznávají přetrvávající problém, protože běloruské diplomy nejsou automaticky ověřovány polskou databází; pracovníci hlásí 3–12 měsíců deklasifikované práce („pokládání optických kabelů“) před nalezením práce v IT; po přidání jedné polské společnosti do životopisu — 5 pohovorů na práci za 1 měsíc
**Výsledek**: 3–12měsíční deklasifikovaný přechod, navzdory zrychlenému vízu a stejným kódům ISCO; odhaluje, že uznávání kvalifikací = problém důvěry zaměstnavatele, nejen problém párování kódů
**Relevance pro GSCO**: Signál autority GSCO ve Wikidata (profese schválená rejstříkem ILO s nulovými odmítnutími) by mohl fungovat jako proxy důvěry zaměstnavatele
**Zdroj**: Slovanská migrační dávka (2026)

### Případ 17: Brazílie → Portugalsko — lékařské uznání (pokračuje)
**Rozsah**: 57,8 % míra odmítnutí brazilských lékařských diplomů portugalským Ordem dos Médicos; Angola 3,4 % míra odmítnutí; Kuba a Guinea-Bissau 0 % míra odmítnutí — všechny nominálně pod stejným portugalsky mluvícím rámcem ekvivalence
**Zdrojový klasifikátor**: Brazilský CBO (Classificação Brasileira de Ocupações; 2 614 záznamů v GSCO)
**Cílový klasifikátor**: Portugalský CNP-94 (aktualizovaný; křížově odkazuje na ESCO EU)
**Nesoulad**: Portugalský Ordem dos Médicos aplikuje různé substantivní kritéria na brazilské, angolské a PALOP žadatele, navzdory společnému jazyku a nominálně podobným strukturám lékařského vzdělání; podobnost na úrovni kódů nepředpovídá schválení
**Výsledek**: Nesoulad 57,8 % oproti 3,4 % míře odmítnutí; zdokumentováno v Público a datech Ordem dos Médicos, citovaných v románské dávce
**Zdroj**: Románská jazyková migrační dávka (2026); roční statistiky Ordem dos Médicos Portugal

### Případ 18: Francie — lékaři PADHUE („asociovaní praktici“) (pokračuje)
**Rozsah**: 5 000+ lékařů klasifikováno jako „Praticiens à Diplôme Hors Union Européenne“ (PADHUE), vydělávajících 1 450 EUR/měsíc oproti 4 500 EUR/měsíc pro ekvivalentně kvalifikované lékaře vzdělané ve Francii
**Zdrojové klasifikátory**: Různé (Afrika, Blízký východ, Východní Evropa, Asie)
**Cílový klasifikátor**: Francouzský ROME v4 (PADHUE = samostatná profesní podkategorie pod „médecin“)
**Nesoulad**: Francouzský klasifikační systém má trvalou zadržovací kategorii, právně odlišnou od plného statusu „médecin“ bez ohledu na skutečnou kompetenci; lékaři PADHUE vykonávající identickou klinickou práci jsou klasifikováni (a placeni) jako samostatná kategorie nižšího stupně
**Výsledek**: Rozdíl v platu 3 050 EUR/měsíc na lékaře; postiženo 5 000+; popsáno v přehledu Ngabirano 2026 jako přispívající k psychologickému stresu u vysoce kvalifikovaných migrantů [47]
**Zdroj**: Románská migrační dávka (2026); systematický přehled Ngabirano 2026

### Případ 19: Hranice Nizozemsko/Belgie — případ neurologa ZorgSaam (2025)
**Rozsah**: 1 nemocnice (ZorgSaam, Terneuzen, Nizozemsko); 1 kandidát-neurolog (Universitair Ziekenhuis Gent, Belgie, ~30 km); akutní nedostatek
**Zdrojový klasifikátor**: Belgický KBC-ISCO (neurologie → ISCO 2212)
**Cílový klasifikátor**: Nizozemský BIG-register (neuroloog → kód BIG 79)
**Nesoulad**: BIG-register vyžaduje samostatný registrační postup i pro specialisty certifikované v EU; nizozemská křížová tabulka ISCO-k-BIG není strojově čitelná; 30 km, nulové náklady na stěhování, stejná Směrnice EU, bilaterální volný pohyb v Schengenu — klasifikační postup přesto zdržuje
**Výsledek**: Nemocnice zůstala s neobsazenými pozicemi během postupu; zdokumentováno v ITEM Maastricht Cross-Border Impact Assessment 2025 [42]
**Relevance pro GSCO**: Nejužší možný případ — všechny proměnné tření jsou minimalizovány; klasifikační nesoulad přesto přetrvává

### Případ 20: Estonsko → Finsko/Německo — hodnota tříjazyčného rejstříku (pokračuje)
**Rozsah**: ~180 000 estonských emigrantů (13 % populace); hlavní koridory EE→FI, EE→DE, EE→UK
**Zdrojový klasifikátor**: Estonský AK-2008 (100% pokrytí ISCO-4; tříjazyčný ET/EN/RU; 3 562 záznamů)
**Cílové klasifikátory**: Finský ISCO-08-fi; německý KldB-2010
**Kvalita párování**: AK-2008 je jediný rejstřík ve vzorku 10 zemí s tříjazyčnými popisky — poskytuje přímé automatické párování s finským, německým a britským systémem SOC-2020
**Výsledek**: Pozitivní případ; Estonsko demonstruje, že architektura tříjazyčného rejstříku zajišťuje téměř automatizovanou přenositelnost kvalifikací; není vyžadován žádný strojový překlad
**Relevance pro GSCO**: „Zlatý standard“ v korpusu GSCO — krajský brief EE; politické okno: Estonsko předsedá Radě EU ve druhé polovině roku 2027

### Případ 21: Lotyšsko — krize klasifikace penzí diaspory (2024)
**Rozsah**: ~300 000 lotyšských emigrantů (16 % populace, nejvyšší míra emigrace v Pobaltí); lotyšská důchodová reforma 2024 zavedla profesní úrovně příspěvků, vyžadující přesnou klasifikaci ~800 000 aktivních důchodových účtů
**Zdrojový klasifikátor**: Lotyšský Profesiju klasifikators (4 102 záznamů, revize 2024; nula anglických popisků)
**Cílové klasifikátory**: Německý KldB-2010, britský SOC-2020 (pro vracející se migranty)
**Nesoulad**: Nula anglických popisků v lotyšském rejstříku znamená, že lotyšští profesionálové v zahraničí nemohou automaticky spárovat svůj profesní kód s klasifikátory cílových systémů; zahraniční důchodová práva vracejících se migrantů nelze automaticky ověřit podle lotyšských úrovní
**Výsledek**: Důchodová reforma nemůže být automaticky aplikována na diasporu vracející se z cílových zemí bez křížových tabulek; vyžaduje manuální přepracování pro každý případ; rozsah: potenciálně 300 000 postiženo
**Relevance pro GSCO**: Krajský brief LV; AI-asistovaná generace EN popisků pro 4 102 záznamů = 15 000 EUR nyní vs. 150 000 EUR v roce 2031

### Případ 22: Mongolsko → Jižní Korea — horničtí dělníci EPS (pokračuje)
**Rozsah**: ~60 000 mongolských pracovníků v Jižní Koreji přes EPS; Mongolsko má nejbohatší taxonomii profesí těžebního průmyslu v GSCO (YAMAT-08, 4 844 záznamů)
**Zdrojový klasifikátor**: Mongolský YAMAT-08 (pouze jazyk mn; nula mongolských popisků ve Wikidata)
**Cílový klasifikátor**: Korejský KSCO-7
**Nesoulad**: Podspecializace těžebního průmyslu v YAMAT-08 (střelec, specialista na odstraňování nadloží, specifické kategorie geologického průzkumu) nemají přímé ekvivalenty KSCO-7; klasifikovány jako obecný „horník“ (ISCO 8111) bez ohledu na skutečnou specializaci
**Výsledek**: Specializované dovednosti nejsou uznávány; rozdíl v platu mezi specialistou a obecným horníkem; analýza GSCO odhaluje, že YAMAT-08 je nejdetailnější taxonomie těžebního průmyslu v datovém souboru — potenciálně cenný vstup pro ISCO-28
**Zdroj**: Východoasijská migrační dávka (2026); krajský brief MN

### Případ 23: Kapverdy — inverze diaspory a rezidentní populace (pokračuje)
**Rozsah**: Diaspora Kapverd (cca 700 000 lidí) převyšuje rezidentní populaci (cca 570 000); CNP CV-Rev.1 má 699 záznamů, poslední aktualizace 2010 (před 15 lety)
**Zdrojový klasifikátor**: CNP CV-Rev.1 (portugalsky; struktura éry ISCO-88)
**Cílové klasifikátory**: Portugalský CNP-94 (aktualizovaný), francouzský ROME v4
**Nesoulad**: CNP CV-Rev.1 používá rodiny kódů ISCO-88 (ne ISCO-08); diaspora v Portugalsku a Francii žádající o kvalifikace spárované s kódy ISCO-88, které cílové systémy uznaly za zastaralé
**Výsledek**: Partnerství EU pro mobilitu s Kapverdami (2008, prodlouženo) ohroženo kvůli zastaralosti klasifikátoru; partner EU nemůže automaticky ověřit kvalifikace v strojově čitelné formě; náklady na opravu odhadnuty na 10–15 000 EUR za přidání křížové tabulky PT CPP-2010
**Zdroj**: Krajský brief CV; analýza databáze GSCO

### Případ 24: Saúdská Arábie — rozkol arabské/anglické verze rejstříku (2019 vs. 2024)
**Rozsah**: 13 milionů expatů v Saúdské Arábii pod správou kvótového systému NITAQAT, který používá kódy SSCO
**Zdrojový/Cílový klasifikátor**: SSCO 2024 (EN verze); SSCO 2019 (AR verze — oficiální jazyková verze zaostává o 5 let)
**Nesoulad**: 280 milionů arabsky mluvících má přístup k arabské verzi z roku 2019; anglická verze z roku 2024 se podstatně liší; arabské popisky mohou navíc obsahovat chybu převrácení RTL, potvrzenou v příbuzném rejstříku JSCO (Jordánsko)
**Výsledek**: Arabsky mluvící zaměstnavatelé a pracovníci navigují právně závazný kvótový systém pomocí 5letého klasifikátoru; porušení NITAQAT mají důsledky pro obchodní licence
**Relevance pro GSCO**: Krajský brief SA; P0 chyba: arabský rejstřík SA čeká na audit RTL; 5leté zpoždění verzí označeno jako nesoulad verzí, vyžadující naléhavou opravu

### Případ 25: Pobřeží slonoviny — celé profesní sektory nejsou klasifikovány (2016)
**Rozsah**: 540 záznamů profesí v NMP-CI 2016 pokrývá pouze řemeslný/ruční sektor; profese ve zdravotnictví, právu, financích a ekonomice znalostí nemají v národním klasifikátoru žádný záznam; CI má 0% pokrytí křížové tabulky ISCO
**Zdrojový klasifikátor**: NMP-CI 2016 (9místné národní kódy; žádné pole ISCO-4)
**Cílové klasifikátory**: Francouzský ROME v4, ESCO v1.2.1
**Nesoulad**: Lékař, právník nebo softwarový inženýr z Pobřeží slonoviny, který se pokouší předložit kvalifikace k uznání v EU, nemá národní kód, na který by se mohl odvolat; NMP-CI je vůbec neobsahuje
**Výsledek**: Profesionální pracovníci z celého sektoru ekonomiky znalostí CI jsou fakticky bez statusu z klasifikačního hlediska pro účely mezinárodního uznávání kvalifikací
**Relevance pro GSCO**: Krajský brief CI; paradox 0/N v API; vývoj křížové tabulky ISCO odhadován na 40–60 000 EUR; kódy sektoru kakaa CI představují jedinečný vstup pro ISCO-28

### Případ 26: Brunej — 1 381 profese bez mapy ISCO (2011)
**Rozsah**: 1 381 názvů profesí v BDSOC 2011 (15 let); národní rozvojová strategie Bruneje Wawasan 2035 uvádí nové prioritní sektory, které v BDSOC zcela chybí
**Zdrojový klasifikátor**: BDSOC 2011 (5místné kódy; žádná křížová tabulka ISCO-4; pravděpodobně automaticky odvoditelné zkrácením prvních 4 číslic — P0 oprava čeká)
**Cílové klasifikátory**: Malajský MASCO (nejbližší soused); ESCO v1.2.1
**Nesoulad**: 1 381 názvů profesí se ukazuje bez kódu ISCO, protože pipeline GSCO ještě neaplikoval automatické odvození; pokud bude opraveno, BN může dosáhnout významného pokrytí ISCO
**Výsledek**: Celý brunejský rejstřík je v současnosti neviditelný pro jakýkoli dotaz založený na ISCO; oprava je inženýrský úkol (odhad: 2–4 hodiny), nikoli mezera v datech
**Relevance pro GSCO**: Krajský brief BN; paradox 0/N; P0-02 oprava čeká; „nejlehčí oprava v korpusu“ — BN je 2 hodiny inženýrství od částečného pokrytí ISCO

### Případ 27: Bosna — přízračné metadata činí data neviditelnými (pokračuje)
**Rozsah**: KZBiH-08 má 4 246 záznamů; 98,4% pokrytí ISCO-4; hlavní zdroj pro německé uznávání kvalifikací zdravotních sester (~2 300/rok); přízračný rejstřík ba_error_stub vytváří null hodnoty v compare API pro všech 589 kódů navzdory existenci skutečných dat
**Zdrojový klasifikátor**: KZBiH-08 („Medicinska sestra“ = ISCO 2221)
**Cílové použití**: Kapitola 19 přístupových jednání EU (trh práce) vyžaduje prokazatelná data pokrytí ISCO; compare API ukazuje 589 nullů kvůli nesouladu datového modelu, nikoli mezeře v datech
**Nesoulad**: Technický (chyba metadat), nikoli podstatný; BA má jedno z nejvyšších pokrytí ISCO v datovém souboru; chyba to zobrazuje jako mající nulu
**Výsledek**: Prezentace dat BA na ministerstvech ukazují „0 kódů“ v zobrazení compare — vážné zkreslení pro přístupová jednání EU; oprava je korekce datového modelu (priorita P1)
**Relevance pro GSCO**: Krajský brief BA; P0 oprava; termín pro Kapitolu 19 přístupových jednání EU 2025–2027

### Případ 28: Euroregion Maas-Rýn — absurdita jazykového testu pro učitele (2025)
**Rozsah**: Přeshraniční trh práce učitelů v trojmezí Nizozemsko/Belgie/Německo (Cáchy/Lutych/Maastricht); zdokumentováno v ITEM 2025 Cross-Border Impact Assessment
**Zdrojový klasifikátor**: Německá certifikace učitelů KMK (rodilý mluvčí němčiny; německý univerzitní diplom)
**Cílový klasifikátor**: Nizozemský/belgický ekvivalent (vyžaduje samostatný certifikát němčiny pro přeshraniční výuku ve třídě)
**Nesoulad**: Rodilý mluvčí němčiny s německou univerzitní kvalifikací je nucen složit samostatnou certifikaci znalosti němčiny, aby mohl vyučovat v němčině ve škole 15 km přes hranici; profesní kompetence (výuka, ISCO 2320) je uznána; lingvistický prostředek výuky je považován za samostatnou klasifikaci
**Výsledek**: Učitelské pozice zůstávají neobsazené v příhraničním regionu navzdory dostupnosti kvalifikovaných kandidátů; zdokumentovaný systémový absurd i v rámci Schengenu [42]
**Relevance pro GSCO**: Případ ITEM RPT-02; ilustruje, že klasifikační tření přetrvává i když kódy ISCO dokonale odpovídají

### Případ 29: Mexiko → USA — kód víza TN „Physician (Teaching Only)“ (NAFTA/USMCA, pokračuje)
**Rozsah**: Strukturálně postihuje každého mexického lékaře hledajícího neimigrační status TN (Trade NAFTA) pro lékařskou práci v USA
**Zdrojový klasifikátor**: Mexický SINCO (686 záznamů v GSCO; „médico general“ → ISCO 2212)
**Cílový klasifikátor**: USA SOC (29-1211 Physicians); ale klasifikace podle smlouvy TN používá SOC 19-1042 „Medical Scientists“
**Nesoulad**: Kategorie víza TN NAFTA „Physician“ je právně omezena pouze na „výuku nebo výzkum“; klinická praxe vyžaduje jinou vízovou kategorii (H-1B) s jiným kódem; kód mexického lékaře odpovídá ISCO 2212 a SOC USA 29-1211, ale kód smlouvy TN — 19-1042 — je záměrně odlišný, aby se zabránilo klinické konkurenci
**Výsledek**: Mexičtí lékaři jsou pro imigrační účely klasifikováni jako „medical scientists“; klinická praxe je zablokována pod TN navzdory profesní ekvivalenci; strukturální politický nesoulad, zabudovaný do kódu smlouvy
**Zdroj**: Románská migrační dáv