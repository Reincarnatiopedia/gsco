# GSCO : Le Classificateur Mondial Standard des Professions — Une Base de Données Déterministe Multilingue pour Résoudre le Problème des Tables Croisées N² dans la Classification Internationale des Professions

**Maris Dreshmanis**
ORCID : [0009-0003-8151-4088](https://orcid.org/0009-0003-8151-4088) | ISNI : [0000 0004 9280 9121](https://isni.org/isni/0000000492809121)
Affiliation : Academy of Reincarnationology | Chercheur indépendant
GitHub : [MarisDreshmanis](https://github.com/MarisDreshmanis) | Wikidata : [User:Maris Dreshmanis](https://www.wikidata.org/wiki/User:Maris_Dreshmanis)

**Version :** 1 | **Licence :** CC BY 4.0 | **Date :** Avril 2026

**DOI:** [10.5281/zenodo.19902278](https://doi.org/10.5281/zenodo.19902278) (this version) · **Concept DOI:** [10.5281/zenodo.19902277](https://doi.org/10.5281/zenodo.19902277) (latest version) · [Zenodo record](https://zenodo.org/records/19902278)

---

## Résumé

**Introduction.** Le problème de l'inadéquation des codes de classification des professions entre les pays a été découvert par hasard. L'une de mes activités consiste à éditer et à enrichir Wikidata avec des données. Wikidata sert de lien entre les sections Wikipédia dans différentes langues, agissant comme un dépôt central pour les faits et références communs.

En résolvant la tâche d'enrichissement de Wikidata pour un groupe cible spécifique — les lauréats du prix Nobel dans différentes langues — il est apparu que les noms de professions constituent l'un des lacunes non systématisées dans Wikidata.

Pour éviter les erreurs dans la traduction des noms de professions par les réseaux neuronaux ou Google Translate, j'ai décidé de collecter des classificateurs de professions dans différentes langues à partir de sources ouvertes. Une fois cela fait, un problème mondial d'envergure mondiale est apparu. Premièrement, l'Organisation Internationale du Travail (OIT) met à jour sa Classification Internationale Type des Professions (CITP) environ tous les 20 ans. Cela signifie que les nouvelles professions de la décennie en cours n'y sont pas incluses.

Voici les années de standardisation de la CITP :

- **CITP-58** — Adoptée en 1957 (publiée en 1958).
- **CITP-68** — Adoptée en 1966 (publiée en 1968).
- **CITP-88** — Adoptée en 1987 (publiée en 1988). C'est dans cette version que le concept de « niveau de compétence » a été clairement défini pour la première fois.
- **CITP-08** — Adoptée en 2007 (publiée en 2008). C'est la version actuelle, utilisée dans le monde entier.
- La prochaine (**CITP-28**) est actuellement en phase active de révision par l'OIT — la soumission de données empiriques est ouverte de 2026 à 2028, publication en 2028.

Deuxièmement, les pays qui ont résolu cette tâche de manière indépendante ajoutent des codes qui entrent en conflit entre les pays. La situation est légèrement meilleure dans l'Union européenne, mais globalement, dans le monde, il y a un chaos dans la standardisation et les codes après 4 chiffres de la CITP.

En continuant à résoudre la tâche de description des professions des lauréats du prix Nobel, j'ai créé pour moi-même un tableau d'analyse des incohérences dans différents pays. Je l'ai simplement appelé : **GSCO (Global Standard Classification of Occupations)**. Pourquoi global ? Parce que j'ai collecté des données de plus de 140 registres nationaux. Je n'ai trouvé aucune information indiquant que quelqu'un dans le monde ait fait cela auparavant ; si vous, qui lisez ce texte, avez une telle information — je vous prie de me l'envoyer. Les contacts sont indiqués sur la page de mon profil.

Une fois les données collectées et analysées, j'ai compris qu'il fallait partager ces données non seulement avec les registres nationaux, afin qu'ils prennent conscience du nombre de conflits de codes de professions dans leurs pays et tentent de les synchroniser, mais aussi avec l'Organisation Internationale du Travail (OIT), afin d'aider le groupe de travail à voir l'ampleur du problème et à en tenir compte lors de la standardisation de la CITP-28 en 2028.

### Exemple : CITP 2221

**Niveau Hub : ce que la CITP-08 officielle signifie**

CITP-08 (OIT) : « Professionnels des soins infirmiers » — infirmiers autorisés (infirmier praticien avancé).

Étiquettes multilingues au niveau du hub dans notre base de données (35 langues) :

| Langue | Traduction |
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

**Catastrophe au niveau national**

Sous le même code CITP 2221, différents pays désignent **des professions différentes** :

**Australie et Nouvelle-Zélande (ANZSCO 2022) — courtiers financiers, pas des infirmières :**

- 222111 Commodities Trader (trader de matières premières)
- 222112 Finance Broker
- 222113 Insurance Broker
- 222199 Financial Brokers nec
- 222100 Financial Brokers nfd

**Ukraine (DK003) — médecins, pas des infirmières :**

- 2221 — «Professionnels de la santé (sauf dentisterie)»
- 2221.1 — Chercheurs scientifiques (médecine)
- 2221.2 — Médecins : thérapeute, cardiologue, chirurgien, psychothérapeute, neurologue, généticien…
- Au total 78 sous-codes — tous docteurs, pas des infirmières.

**Allemagne (KldB-2010) :**

- 22212 «Peinture de véhicules — tâches qualifiées» (peinture automobile)
- 81393 «Superviseurs — Soins infirmiers et de santé, services d'urgence et obstétrique» — infirmières chefs
- 81302 «Soins infirmiers et de santé» — infirmières ordinaires (selon le Umsteigeschlüssel officiel de l'Agence fédérale pour l'emploi, ils sont mappés à la CITP 3221, pas 2221)

**Biélorussie (OKRV-2017, version actuelle du classificateur) :**

- 2221 : «Professionnels des soins infirmiers» — infirmières (correspond à la CITP-08)

**Italie (CP 2021) — architectes :**

- 2.2.2.1.1 ARCHITETTI (architectes)
- 2.2.2.1.2 Pianificatori, paesaggisti (urbanistes, paysagistes)

**Saint-Marin (RP-2017) — architectes :**

- 22211 ARCHITETTO

**Canada (NOC 2021) — techniciens :**

- 22210 Technologues en architecture
- 22211 Designers industriels
- 22212 Technologues en dessin
- 22213 Technologues en arpentage
- 22214 Géomatique

**Algérie (DZ Profession) — médecins :**

- 2221 : «Médecins» (médecins)

---

---

### Professions familières à tous — Enseignant et Chauffeur de taxi

Pour montrer que le problème ne concerne pas des professions rares comme « instructeur de yoga » ou « hypnothérapeute » mais bien **les professions de masse les plus ordinaires**, examinons deux professions universelles : enseignant et chauffeur de taxi. Elles existent dans chaque pays — mais les classifications divergent radicalement.

#### 👨‍🏫 Enseignant / Maître de conférences

Top 15 des pays par nombre de postes sous ISCO 23xx (Éducation) :

| Pays | Postes sous 23xx | Granularité la plus inhabituelle |
|---|---:|---|
| 🇧🇦 **Bosnie (KZBiH-08)** | **404** | **191 enseignants universitaires distincts** sous un seul ISCO 2310 — code séparé pour chaque spécialité (biotechnologie, philologie, mathématiques) |
| 🇺🇿 Ouzbékistan (OZMST 2025) | 387 | 179 enseignants de la formation professionnelle (2320) |
| 🇲🇳 Mongolie (YAMAT-08) | 355 | 120 universitaires + 120 professionnels |
| 🇸🇦 Arabie saoudite (SSCO 2024) | 275 | 76 enseignants du secondaire |
| 🇷🇸 Serbie (Šifarnik) | 264 | 97 enseignants universitaires |
| 🇰🇷 Corée (KSCO 2024) | 171 | 5–7 dans chaque groupe ISCO-4, répartis uniformément |
| 🇮🇹 Italie (CP2021) | 141 | 38 maîtres de conférences sous 2311 |
| 🇪🇪 Estonie (AK-2008) | 130 | Spécialistes des méthodes d'éducation, professeurs de langues — codes séparés |

Et tout en bas :

| Pays | Total | Ce qu'on y trouve |
|---|---:|---|
| 🇷🇺 Russie (OKZ-2014) | **22** | Uniquement des groupes ISCO à 4 chiffres, aucune granularité |
| 🇩🇪 Allemagne (KldB-2010) | 40 | Propre numérotation, ne décompose pas ISCO 23xx |
| 🇺🇸 États-Unis (O\*NET) | **8** | 5 catégories SOC 23-1 + 3 SOC 23-2 |
| 🇬🇧 Royaume-Uni (SOC 2020) | 15 | 1 par sous-code |

**Ce que cela signifie pour un enseignant individuel :** une professeure de biotechnologie bosniaque possède un code spécifique dans KZBiH-08 (l'un des 191) — mais si elle s'installe en Russie, sa granularité de niveau 191 **s'effondre dans le code unique 2310 « enseignant universitaire »**. Si elle part aux États-Unis, son code ne **rentre même pas dans SOC 23-1** (aucun niveau spécifique par matière n'y existe).

#### 🚕 Chauffeur de taxi

La norme ISCO **8322** « Conducteurs de voitures, de taxis et de camionnettes » (une catégorie combinée) existe dans la plupart des pays. Mais les **types de taxis locaux** sont un cas que ISCO-08 ne couvre tout simplement pas :

| Pays | Code local | Description |
|---|---|---|
| 🇫🇷 France (ROME 11993) | Chauffeur de taxi animalier | **Taxi pour le transport d'animaux** — la seule classe autonome de ce type au monde |
| 🇫🇷 France (ROME 12884) | Conducteur de bateau taxi | Taxi fluvial/maritime |
| 🇫🇷 France (ROME 13191) | Conducteur de taxi moto | Taxi-moto |
| 🇧🇦 Bosnie + 🌊 PACSCO (23 nations du Pacifique) | 8350 | **"Vozač taksija na vodi" / "Water taxi driver"** — taxi sur l'eau (catégorie ISCO distincte) |
| 🇹🇬 **Togo (RGPH4)** | 5020 "Taxi-moto (**Zemidjan**)" | **Zemidjan** — le nom local du taxi-moto, une profession employant des milliers de personnes |
| 🇧🇯 Bénin (NAP) | 154–155 | "Taxi-moto / charrette / vélo" (moto / charrette / vélo) |
| 🇬🇹 Guatemala (CNO 2022) | 832104 + 933101 | "Piloto de moto taxis" + "**Piloto de bicitaxis**" (vélo-taxi) |
| 🇭🇳 **Honduras (CNOH 2018)** | 832101 | "Conductor de moto taxi **forestal** motorizada" — **taxi forestier motorisé** (unique au Honduras) |
| 🇸🇳 Sénégal, 🇩🇯 Djibouti, 🇨🇮 CI | 05.0.0.17 | "taxi man — conducteur de bus" — combinaison de « chauffeur de taxi + conducteur de bus » en une seule profession |
| 🇨🇦 Canada (NOC 2021) | 75200 | "Taxi and **limousine** drivers and **chauffeurs**" — chauffeurs de taxi fusionnés avec les limousines |
| 🇦🇺/🇳🇿 ANZSCO 2022 | 731112 | "Taxi Driver" — mais dans la numérotation propre à ANZSCO, 7311 = "Automobile Drivers", ce qui **ne correspond pas** à ISCO 7311 "Precision-Instrument Makers and Repairers" (une profession différente dans la norme internationale). Vérifié via la table de correspondance officielle OSCA 2024 ↔ ISCO-08 de l'ABS : le groupe unitaire ISCO-08 correct pour ANZSCO 731112 est **8322** "Car, taxi and van drivers". |

**Ce que cela signifie pour un chauffeur de taxi individuel :** le conducteur de **zemidjan** togolais (taxi-moto) exerce une profession réelle comptant des milliers de travailleurs. Ni ISCO-08, ni ANZSCO, ni SOC n'ont d'emplacement pour elle. Lorsqu'il migre vers l'Allemagne ou la France selon les règles de reconnaissance des qualifications, son expérience professionnelle s'effondre dans la catégorie générique « Personenkraftwagen-Fahrer » (conducteur de voiture de tourisme) — car le mot « zemidjan » est absent du classificateur allemand. Il n'est pas « perdu dans la traduction » — il est **perdu dans la taxonomie**.

Le « conducteur de taxi-moto forestier » hondurien (Conductor de moto taxi forestal) ou le « conducteur de vélo-taxi » guatémaltèque (Piloto de bicitaxis) sont également des professions réelles et de masse **absentes de la structure internationale**.

#### Pourquoi cela est important

L'enseignant et le chauffeur de taxi sont les professions les plus universelles et les plus faciles à appréhender. Si même ici il n'y a pas d'accord — qu'en est-il des professions rares ou émergentes (formateur en IA, opérateur de drone, spécialiste de l'adaptation climatique) ? Ces exemples montrent que : **mettre de l'ordre dans la classification mondiale des professions est une tâche à l'échelle de l'ONU/OIT**, et non le travail de pays individuels. C'est précisément l'objectif : aider le groupe de travail ISCO-28 en 2028 à prendre en compte ces divergences.

---

### Ces pays où 2221 signifie réellement = infirmières

Sous-classifications détaillées (montrant comment l'État perçoit les spécialisations) :

**Estonie (AK-2008) — 19 sous-codes d'infirmières** (noms estoniens originaux + traduction russe) :

- 2221 Õenduse tippspetsialistid (Professionnels des soins infirmiers)
- 22210501 Abiõde (üliõpilane) — Aide-infirmière (étudiant)
- 22210502 Õde — Infirmière
- 22210601 Anesteesia-intensiivraviõde — Anesthésie et soins intensifs
- 22210701 Erakorralise meditsiini õde — Urgences médicales
- 22210801 Diabeediõde — Diabétologie
- 22210901 Geriaatriaõde — Gériatrie
- 22211001 Lasteõde — Pédiatrie
- 22211101 Nakkustõrjeõde — Prévention des infections
- 22211201 Onkoloogiaõde — Oncologie
- 22211301 Operatsiooniõde — Bloc opératoire
- 22211401 Pulmonoloogiaõde — Pneumologie
- 22211501 Taastusraviõde — Réadaptation
- 22211601 Koduõde — Soins à domicile
- 22211701 Kooliõde — Infirmière scolaire
- 22211801 Töötervishoiuõde — Santé au travail
- 22211901 Pereõde — Médecine générale
- 22212001 Psühhiaatriaõde — Psychiatrie
- 22219900 Mujal liigitamata õenduse tippspetsialistid — Spécialistes des soins infirmiers non classifiés ailleurs

**Mongolie (YAMAT-08) — 28 sous-codes d'infirmières en mongol :**

- 2221-01 Сувилагч, арга зүйч (infirmier, méthodologue)
- 2221-02 Сувилагч, ерөнхий мэргэжлийн (infirmier, pratique générale)
- 2221-03 Сувилагч, арьсны (infirmier, dermatologique)
- 2221-04 Сувилагч, гэмтэл согогийн (infirmier, traumatologique)
- … encore 24

**Palestine (ASCO 2016) — 23 spécialités en arabe :**

- 222101 ممرضة سريرية (clinique)
- 222102 ممرضة حي (de quartier)
- 222103 ممرضة التخدير (anesthésiste)
- 222104 ممرضة مربية (pédiatrique)
- … encore 19

**Arabie Saoudite (SSCO 2024) — 17 spécialités :**

- 222101 Nurse Specialist
- 222102 Specialized Nursing Specialist
- 222103 Community Health Nursing Specialist
- 222104 Maternal and Child Nursing Specialist
- 222105 Anesthetic Nursing Specialist
- … encore 12

**Afrique du Sud (OFO 2017) — 17 types :**

- 2017-222101 Clinical Nurse Practitioner
- 2017-222102 Aged Care Registered Nurse
- 2017-222103 Registered Nurse (Child and Family Health)
- … encore 14

**Lettonie (Profesiju klasifikators) — 8 types avec sous-codes nationaux :**

- 2221 Medicīnas māsas profesijas vecākie speciālisti
- 2221 02 VirsMĀSA (infirmière chef)
- 2221 46 MĀSA / vispārējās aprūpes (soins généraux)
- 2221 48 anestēzijā un intensīvajā aprūpē (anesthésiologie et soins intensifs)
- 2221 50 psihiatrijā un narkoloģijā (psychiatrie et addictologie)
- … encore 3

**Nicaragua (CUONIC) — 7 types :**

- 2221-02 Enfermera Anestesista
- 2221-03 Educadora de Enfermeras
- 2221-04 Enfermera Clínica
- 2221-05 Enfermera del Quirófano (bloc opératoire)
- 2221-06 Enfermera de la Salud Pública
- … encore 2

---

### Descriptions simples sans explication

- **Albanie** : 2221 «Infermierë të specializuar» (infirmières spécialisées)
- **Bhoutan** (BSCO) : 2221 Nursing Professionals + 22211 Registered Nurse + 22212 Public Health Nurse
- **Équateur** : 2221 PROFESIONALES DE ENFERMERÍA
- **Iran** : 2221 رستاران متخصص (infirmières spécialisées)
- **Islande** : 2221 Sérfræðistörf við hjúkrun
- **Lituanie** (LPK 2023) : 2221 Slaugos specialistai + 222101 Slaugytojas + 222102 Mokslo darbuotojas (slauga)
- **Macédoine du Nord** : 2221 Медицински сестри
- **Maurice** : 22211 Administrator, nursing + 22212 Educator, nurse + 22219 Nursing professionals n.e.c
- **Cambodge** : 4 sous-codes 22211–22214 en khmer
- **Kenya, Lesotho, Guyana, Grenade, Sierra Leone, Eswatini, Tanzanie, Malawi** : tous 2221 Nursing Professionals
- **AFRISTAT** (régional pour l'Afrique de l'Ouest) : 2221 Cadres infirmiers

---

### Constatation clé pour l'introduction

Le même code CITP à 4 chiffres 2221 signifie **des professions fondamentalement différentes** dans différents pays :

- **Infirmières** (correct selon la CITP-08) — dans les pays EE, MN, SA, ZA, PS, LV, LT, MK, EC, IS, BY et ~30 autres pays.
- **Médecins** — UA, DZ.
- **Courtiers financiers** — AU, NZ.
- **Architectes** — IT, SM.
- **Techniciens** (arpentage, conception) — CA.

Ce n'est pas une « erreur de traduction ». Ce sont deux mondes de classification complètement différents sous le même numéro. Un médecin cardiologue ukrainien (code 2221.2) arrive en Allemagne avec des documents indiquant « CITP 2221 » — le système allemand le considère automatiquement comme une infirmière. Un trader de matières premières australien (code 222111) déménage dans l'UE et sa carrière est classée dans la famille 2221, ce qui, dans l'UE, signifie une infirmière.

---

**Méthodes.** Les données collectées sont disponibles sur <https://gsco.io>. GSCO (Global Standard Classification of Occupations) est une base de données qui utilise les codes CITP-08 à 4 chiffres comme centre universel pour agréger des termes juridiquement faisant autorité désignant des professions, provenant de plus de 140 registres gouvernementaux nationaux. La méthodologie est basée exclusivement sur la correspondance exacte du texte avec les sources officielles (ESCO, KBJI, MASCO, NCO, OKZ, CBO, KeSCO et autres), excluant complètement la traduction automatique neuronale. Un cache SQLite contenant 26 991 entrées de professions de Wikidata dans 53 langues permet une édition par lots pré-validée.

**Résultats.** L'ensemble de données obtenu contient 152 135 étiquettes multilingues, 98 335 pseudonymes et 76 734 descriptions dans 53 langues, obtenues à partir de 146 registres nationaux analysés, soit un total de 263 608 entrées de professions.

**Conclusion.** Les données ont été collectées et mises en correspondance automatiquement, et nécessitent une vérification manuelle de chaque classificateur de professions pertinent en 2026 pour chaque pays. Je ne l'ai pas fait pour ne pas perdre mon temps personnel. Que les employés de l'Organisation Internationale du Travail (OIT) et des ministères nationaux résolvent cette tâche — ils disposent de budgets et de ressources pour cela. Ma tâche n'est pas d'accomplir le travail de tous les ministères du travail de tous les pays du monde, mais d'actualiser le problème.

**Mots-clés :** classification des professions, CITP-08, base de données multilingue, Wikidata, enrichissement de graphe de connaissances, correspondance déterministe, table croisée, ESCO, marché du travail, référence NLP, codage d'enquêtes, langues à ressources limitées, données ouvertes, données liées, réseau sémantique, alignement d'ontologies, OIT, données de référence, automatisation par bot, alignement de taxonomie.

---

## 1. Introduction : Des lauréats du prix Nobel à une crise mondiale des données

### 1.1 Une impasse pratique : quand les économistes sont enregistrés comme musiciens de jazz

Le projet est né d'une tâche ambitieuse, mais apparemment locale : combler un déficit critique de données sur l'élite scientifique et culturelle mondiale dans les bases de connaissances ouvertes. L'analyse de 890 lauréats historiques du prix Nobel a révélé une statistique alarmante : la grande majorité n'avait pas de descriptions élémentaires dans environ 260 des plus de 300 sections linguistiques de Wikipédia. Par exemple, le lauréat du prix Nobel de la paix Desmond Tutu avait des descriptions dans un nombre extrêmement restreint de sections linguistiques au début du projet — une absurdité pour une figure historique de cette ampleur.

Pour combler cette lacune, nous avons conçu un bot déterministe (ReNeuralAgent) pour automatiser la création de profils multilingues dans Wikidata selon un modèle simple : `"{profession} de {pays}"`. Cependant, les tout premiers tests ont révélé une catastrophe numérique à grande échelle. Le graphe de connaissances s'est retrouvé pollué par des associations erronées. La profession « économiste » a été classée comme « musicien de jazz » en malais et en indonésien. Lorsque le système a tenté de désigner les « urbanistes », il a produit des « planificateurs de production de cuir », et les « administrateurs système » se sont inexplicablement transformés en « botanistes ».

Le problème ne venait pas de notre code, mais de l'infrastructure fondamentale de la classification internationale des professions.

### 1.2 Anatomie de la catastrophe : la bombe à retardement bureaucratique de l'OIT

L'enquête sur ces « hallucinations » absurdes a conduit à un paradigme obsolète de l'Organisation Internationale du Travail (OIT). Historiquement, cet organe de l'ONU est responsable de la publication de la Classification Internationale Type des Professions (CITP). Le cycle de mise à jour est en moyenne de 20 ans : de nouvelles versions ont été publiées en 1958, 1968, 1988 et 2008 [1].

Le problème le plus flagrant n'est pas la lenteur, mais la méthodologie. Chaque nouvelle édition implique un remaniement complet des codes numériques sans rétrocompatibilité. L'exemple le plus frappant : le code **2131**. Dans la CITP-88 (1988), ce code désignait les programmeurs et les développeurs de systèmes. En 2008, l'OIT a complètement restructuré le secteur informatique et a réattribué le code 2131 libéré à… les biologistes, botanistes et zoologistes [1].

Les systèmes d'information modernes — y compris Wikidata lui-même — continuent de s'appuyer sur des propriétés obsolètes. La propriété **P952** dans Wikidata stocke les codes CITP-88 obsolètes. Notre analyse empirique du cache des professions de Wikidata montre l'ampleur complète de cette stagnation :

| Propriété | Standard | Éléments avec données | Couverture |
|----------|----------|---------------:|--------:|
| P3008 | CITP-08 (actuel) | 0 | 0.0% |
| P952 | CITP-88 (obsolète, 1988) | 299 | 1.1% |
| Aucun | — | 26 692 | 98.9% |

*Tableau 1 : Couverture des propriétés CITP dans 26 991 éléments de professions Wikidata (avril 2026). P3008 (CITP-08) est complètement vide, tandis que P952 (CITP-88) ne couvre que 1,1 % des éléments. Les 98,9 % restants des professions n'ont aucun code de classification standardisé.*

Cela signifie que les algorithmes tentant de synchroniser les données via ces identifiants numériques ne trouveront soit rien (98,9 % des cas), soit extrairont des codes d'une norme vieille de 38 ans, où les programmeurs sont réattribués aux biologistes.

### 1.3 Prise de conscience : un nouveau standard est nécessaire

Cette impasse pratique a clairement montré que l'utilisation de codes numériques obsolètes pour naviguer sur le marché du travail moderne est vouée à l'échec. L'estimation algorithmique par les réseaux neuronaux échoue également en raison d'hallucinations linguistiques dans les langues rares. Une approche fondamentalement différente était nécessaire — passer de la confiance dans les nombres abstraits à un déterminisme textuel strict basé sur la législation nationale.

Cette compréhension a donné naissance à la base de données GSCO (Global Standard Classification of Occupations).

*L'anomalie concernant les économistes-comme-musiciens-de-jazz n'était pas simplement un problème de qualité des données Wikidata, mais un symptôme d'une incompatibilité fondamentale entre l'infrastructure mondiale de données sur le travail et l'ampleur de la mobilité humaine moderne. L'Organisation Internationale du Travail, avec sa prudence statistique caractéristique, a conçu la CITP-08 en 2008 pour un monde comptant 190 millions de migrants internationaux [33]. En 2024 — seulement 16 ans plus tard — ce chiffre a atteint environ 280 millions, le nombre de réfugiés seuls a augmenté de 16 à 37 millions, et celui des personnes déplacées à l'intérieur de leur propre pays de 26 à 75 millions. Le monde pour lequel la CITP-08 a été construite n'existe plus.*

### 1.4 La réalité de l'accélération des migrations

L'ampleur de la mobilité humaine moderne transforme l'inadéquation entre les cycles bureaucratiques de révision de la CITP et la complexité réelle du marché du travail non pas simplement en une question académique, mais en une crise humanitaire. Les chiffres parlent d'eux-mêmes :

| Année | Migrants internationaux | Réfugiés | PDI | Travailleurs migrants |
|------|---------------|----------|------|-----------------|
| 1988 (base CITP-88) | ~70M | ~14M | ~5M | ~80M |
| 2008 (base CITP-08) | ~190M | ~16M | ~26M | ~120M |
| **2024** | **~280M** | **~37M** | **~75M (15×!)** | **~169M** |
| Prévision 2035 | ~350M+ | ~50M+ | ~100M+ | est. 200M+ |

*Tableau 2 : Accélération de la migration 1988–2024 (ONU DESA / OIT 2024). La CITP-08 a été conçue pour un monde de 190 millions de migrants internationaux ; en 2024, ce chiffre a atteint 280 millions, et le nombre de personnes déplacées à l'intérieur de leur propre pays a été multiplié par 15 par rapport au niveau de 1988.*

L'étude canonique de Friedberg [34] a établi que les certificats d'études étrangers ont une valeur économique transférable presque nulle sur les marchés du travail des pays de destination sans infrastructure de classification commune — cette conclusion est de plus en plus confirmée dans diverses juridictions. Les médecins syriens demandant l'Approbation allemande (licence médicale) attendent en moyenne 14 mois pour la vérification au niveau du code [35]. Les infirmières philippines au Japon accumulent un taux de réussite aux examens de licence de 14 % sur 15 ans, partiellement calibré sur les familles de codes professionnels japonais. Les femmes bangladaises — environ 800 000 — sont systématiquement classées de force comme « travailleuses domestiques » à leur arrivée dans les pays du Golfe, indépendamment de leur expérience professionnelle réelle [36].

Ce ne sont pas des cas isolés. C'est le résultat structurel d'une architecture où 146 classificateurs de professions faisant autorité au niveau national n'ont pas de hub commun — une impossibilité mathématique que GSCO résout grâce à l'architecture hub-and-spoke de la CITP-08 décrite au §4.

---

## 2. Problèmes fondamentaux de la classification traditionnelle

La défaillance découverte lors de la tentative de labellisation des professions dans Wikidata s'est avérée non pas une erreur locale de la plateforme, mais un symptôme d'une crise méthodologique profonde. Quatre problèmes fondamentaux rendent les méthodes de classification traditionnelles inadaptées à l'échelle mondiale.

### 2.1 Le piège N² : l'effondrement mathématique des tables croisées

Historiquement, pour que différents registres « se comprennent » (par exemple, relier l'O*NET américain à l'ESCO européen), les ministères créent des tables croisées bilatérales (mappings) [2]. Cependant, les chercheurs en architecture d'ontologies ont prouvé que cette voie mène à une impasse mathématique [3]. La création de tels liens suit la **problème N²** : pour *n* normes, le maintien de l'actualité des liens nécessite la génération de *n(n-1)/2* tables croisées.

$$C(n) = \frac{n(n-1)}{2}$$

Pour 50 registres nationaux, cela donne **1 225 tables croisées bilatérales**, chacune nécessitant une maintenance manuelle à chaque cycle de mise à jour. Cette croissance exponentielle rend la synchronisation manuelle du marché du travail mondial physiquement impossible [3].

Avec le nombre documenté de 146 classificateurs de professions faisant autorité au niveau national dans GSCO (avril 2026), l'espace n² nécessite :

$$C(146) = \frac{146 \times 145}{2} = \textbf{10 585 tables croisées bilatérales}$$

Chacune de ces 10 585 tables est invalidée lors de toute mise à jour d'un seul registre. La maintenance manuelle à cette échelle n'est pas seulement peu pratique ; elle est mathématiquement incompatible avec le rythme empirique de mise à jour même d'un seul registre participant. Le OK 016-2025 russe — remplaçant la version de 1994 après une interruption de 30 ans — illustre que même les mises à jour d'un seul registre représentent des entreprises administratives de plusieurs années [37].

Même l'IA ne peut pas sauver la situation. Lorsque la Commission européenne a tenté d'utiliser une approche NLP (basée sur BERT) pour relier 3 000 professions ESCO à 1 000 professions O*NET, l'algorithme a produit 7 385 correspondances potentielles qui nécessitaient toujours une vérification manuelle par un humain, avec environ 600 professions restant sans correspondance [4].

### 2.2 Erreur hiérarchique : le problème du blocage

La deuxième vulnérabilité systémique réside dans la structure arborescente des classificateurs. Des bases de données comme la CITP-08 ont une hiérarchie stricte à 4 niveaux : des grands groupes principaux aux 436 groupes unitaires restreints [1].

En linguistique computationnelle et en apprentissage automatique, cela crée un phénomène connu sous le nom de **problème de blocage** ou propagation en cascade d'erreurs [5]. Une erreur commise au niveau supérieur (par exemple, si le système attribue à tort le rôle professionnel de « techniciens » au lieu de « managers ») se propage en cascade vers le bas, garantissant mathématiquement que tous les niveaux de classification ultérieurs et plus détaillés pour cet élément seront incorrects [5, 6].

Lors de la construction du cache Wikidata GSCO, nous avons rencontré ce problème directement : la requête SPARQL `wdt:P31/wdt:P279* wd:Q28640` parcourait la chaîne `subclass-of` et renvoyait des éléments qui n'étaient en fait pas des professions — y compris des sens de lexèmes (par exemple, `L1371064-S1`), qui ont dû être filtrés par programme.

### 2.3 L'illusion de la précision du codage des enquêtes

Le troisième problème révèle la subjectivité du travail manuel. Lors des recensements, les répondants décrivent leurs professions en texte libre. Les sociologues tentent ensuite manuellement d'attribuer ces réponses à des codes standardisés [7].

Les rapports officiels de l'OCDE indiquent que même avec un schéma de codage simplifié à trois niveaux (350 catégories), atteindre un accord entre les codeurs supérieur à 75 % pose un problème sérieux [8]. Les enquêtes internationales rapportent des taux d'accord allant de 44 % à 89 % [9]. Les tentatives récentes d'automatisation de ce processus à l'aide de l'IA n'ont pas résolu le problème : le meilleur modèle de codage automatique des professions de l'IEA n'a atteint que 63 % de précision dans 12 langues pour prédire le même groupe que les codeurs humains — 37 % d'erreurs s'accumulant sur des millions de réponses d'enquêtes [19].

Beresewicz et al. (2024) [20] ont montré que même les transformateurs hiérarchiques multilingues (XLM-RoBERTa, affiné sur KZiS + CITP) sont inférieurs aux systèmes de correspondance déterministes sur les annonces d'emploi dans les langues rares, en particulier pour les langues slaves et baltes où les données d'entraînement sont rares. Cette impasse computationnelle est structurelle, pas temporaire — Djumalieva et Sleeman [38] affirment que les taxonomies organisées par des experts sont « intrinsèquement lentes et coûteuses », et proposent des alternatives basées sur les données que GSCO opérationnalise via son architecture « hub-and-spoke ».

Le coût est énorme : ces codes sous-tendent les indices de statut socio-économique (SES/ISEI) [10]. Si un codeur classe la description d'un agriculteur comme « Manager agricole » (code 1310), son indice de statut obtient 49 points. Si un autre codeur lui attribue « Agriculteurs de subsistance » (code 6200), l'indice tombe à 10 points [10]. Des divergences systématiques d'interprétation détruisent le fondement même de la mesure sociologique à l'échelle internationale.

### 2.4 Crise de la procédure de reconnaissance des qualifications

Le quatrième problème est celui auquel sont directement confrontés des millions de travailleurs : le pipeline de reconnaissance des qualifications. La base juridique de la portabilité des qualifications — la directive européenne 2005/36/CE relative à la reconnaissance des qualifications professionnelles — est en vigueur depuis 2005, mais en décembre 2024, la Commission européenne a engagé des procédures d'infraction contre la Belgique, l'Allemagne, la France, le Luxembourg et les Pays-Bas pour non-transposition de ses exigences de modernisation [39]. En mai 2025, l'Italie a rejoint cette liste : 11 861 infirmières roumaines ont été directement touchées par la non-acceptation de la directive 2024/505 [40].

Les données empiriques de l'Allemagne illustrent l'ampleur de la dysfonction. Un rapport de l'Institut de l'économie allemande (Institut der Deutschen Wirtschaft, IW) 2025 documente une pénurie de 450 000 travailleurs qualifiés, tandis que 80 % des entreprises allemandes déclarent ne pas utiliser du tout le système formel de reconnaissance, et 51,6 % évaluent le processus de reconnaissance négativement [41]. Au sein d'un même État fédéral, le coût de l'Approbation varie de 170 € à 850 € selon le Bundesland — ce qui illustre que la reconnaissance n'est même pas harmonisée en Allemagne, sans parler de la reconnaissance transfrontalière [42].

Les résultats ne se limitent pas aux coûts. Les médecins français demandant la reconnaissance allemande atteignent un taux d'approbation de 40,3 % ; les mêmes candidats français cherchant la reconnaissance au Luxembourg atteignent 99,8 % [41]. Cet écart de 60 points de pourcentage existe entre des juridictions qui mettent toutes deux en œuvre la même directive européenne, reflétant non pas une ambiguïté juridique, mais une friction classificatoire — des schémas de granularité différents, des familles de codes différentes, des interprétations différentes de ce que signifie « équivalent » lors de la comparaison des entrées de professions entre registres.

Le cas de ZorgSaam, dans la région transfrontalière néerlando-belge, illustre l'absurdité sous sa forme la plus aiguë : un neurologue belge qualifié de l'Universitair Ziekenhuis Gent — physiquement à 30 km d'un hôpital néerlandais confronté à une grave pénurie de neurologues — a été retardé par les exigences du BIG-register néerlandais et l'inadéquation classificatoire transfrontalière dans une région où les deux pays fonctionnent dans le cadre de la liberté de circulation Schengen et de la même directive européenne [42].

L'analyse fondamentale de Sumption [43] a identifié un moteur structurel : les associations professionnelles fonctionnent comme des gardiens sans incitation institutionnelle à réduire la file d'attente, créant un piège « tout ou rien » dans la reconnaissance qui transforme l'équivalence partielle en exclusion totale. L'asymétrie d'information est bilatérale : les employeurs ne peuvent pas vérifier les qualifications étrangères et évitent par défaut le risque ; les migrants ne peuvent pas présenter leurs qualifications dans la famille de codes du système de destination car il n'existe pas de pont lisible par machine.

Ce ne sont pas des « cas extrêmes » ou des « frictions de transition ». C'est le résultat durable d'une infrastructure conçue pour un monde plus petit et plus lent.

---

## 3. L'illusion de l'IA : les limites des modèles linguistiques

### 3.1 Dérive sémantique et pièges de la polysémie

Les réseaux neuronaux s'appuient sur des probabilités et des données historiques, mais le langage est une matière vivante, sujette à des changements constants, un phénomène connu sous le nom de **dérive sémantique** [11]. Pendant la pandémie de COVID-19, des mots comme « vulnérable » et « isolé » ont cessé d'être des descripteurs sociaux généraux pour devenir des termes médicaux spécifiques, perturbant les distributions linguistiques historiques dans les algorithmes [12].

Dans les contextes professionnels, la polysémie aggrave le problème. Comme l'ont noté les créateurs d'un classificateur NLP : « Le mot 'skill' peut faire référence à des compétences techniques, des compétences interpersonnelles, ou même à un type spécifique de poisson, selon le contexte » [13]. L'IA ne peut souvent pas résoudre une telle ambiguïté sans d'énormes volumes de données d'entraînement. Le phénomène n'est pas métaphorique ; JobBERT de Decorte et al. [14] et le XLM-RoBERTa contrastif de Gasco et Retyk [44] rapportent tous deux une dégradation des performances à mesure que leurs corpus d'entraînement vieillissent après 18 mois, faisant de la maintenance temporelle un problème ouvert pour toute approche probabiliste de la classification des professions.

### 3.2 Fragilité computationnelle

Lorsque les chercheurs ont tenté de fournir à GPT-4 un échantillon de textes réels d'annonces d'emploi, le modèle « n'a pas réussi à produire des correspondances correctes dans 33,9 % des cas, tout en nécessitant en moyenne 515 000 tokens d'entrée pour traiter une seule annonce d'emploi » [14]. Les énormes frais généraux de calcul rendent ces approches impraticables à l'échelle mondiale.

Même les modèles spécialement conçus comme JobBERT reconnaissent leurs limites fondamentales : leur architecture est « intrinsèquement liée à une liste prédéfinie (et donc statique) de titres standardisés, ce qui limite son utilisation pratique » [15]. Les réseaux neuronaux restent « fragiles lorsque des divergences de vocabulaire (synonymes, paraphrases et jargon local) surviennent » [15].

La tentative la plus récente — affiner XLM-RoBERTa sur des annonces d'emploi suisses affinées par LLM — a atteint seulement 58,3 % de précision Top-1 sur des données silver (contre 37,2 % avant l'affinage) et 80 % de précision sur des données de test réservées [17]. Bien que les auteurs rapportent 91,4 % de précision dans la prédiction des titres d'ontologie (une tâche simplifiée), l'écart entre 80 % et 100 % de précision, réalisable par correspondance déterministe, reste fondamental, et non incrémental.

En comparaison, notre `gsco_esco_mapper.py` effectue une correspondance exacte des étiquettes anglaises avec un cache SQLite local — 2 942 professions ESCO sont mises en correspondance en millisecondes, avec des coûts de calcul nuls, sans risque d'hallucinations.

### 3.3 Échec du transfert zero-shot

Le coup le plus dévastateur porté à l'affirmation selon laquelle « l'IA sauvera le monde » est le problème des langues rares. Le rapport officiel de la Commission européenne sur la correspondance assistée par machine des données reconnaît explicitement cette vulnérabilité : « les codeurs multilingues ne peuvent pas capturer la similitude lorsque la langue source et la langue cible sont moins similaires aux niveaux morphologique, syntaxique et sémantique » [4, 18]. Lorsque la CE a tenté de produire une correspondance ML assistée des classifications nationales avec ESCO à l'aide de XLM-RoBERTa, la précision Top-1 a varié de 83,5 % (États-Unis) à seulement 45,3 % (Lettonie) — la langue baltique morphologiquement riche s'est avérée la plus résistante au transfert neuronal [18].

Une revue complète de la littérature montre que **aucune étude existante n'atteint une précision >95 % sur la classification multilingue des professions dans 10 langues ou plus simultanément.** L'évaluation multilingue la plus complète — la classification hiérarchique de Beręsewicz et al. sur 24 langues — n'a atteint qu'environ 84 % de précision au niveau le plus large à 1 chiffre des groupes principaux, chutant à 40–60 % pour les codes granulaires à 6 chiffres [20]. Le modèle à 12 langues de l'IEA a atteint 92 % sur des données de test pures traduites par machine, mais s'est effondré à 36 % sur des réponses réelles d'enquêtes [19]. Ces résultats établissent un plafond de performance rigide pour les approches probabilistes que la méthodologie déterministe de GSCO contourne complètement.

Cette limitation est particulièrement aiguë pour le persan, le bengali, le khmer, le birman, le tagalog et le lao — précisément pour les langues sources des principaux corridors de migration qualifiée actuels (Iran → Allemagne, Bangladesh → Arabie Saoudite, Népal → Japon, Philippines → Japon, Cambodge/Myanmar → Thaïlande). Dans notre propre construction de bibliothèques de cas de migration (2026), couvrant plus de 40 langues en 7 lots régionaux, plus de la moitié des cas documentés dans les lots slaves, d'Asie du Sud-Est et persan-indien n'existaient que dans des miroirs anglophones de la reportage originale — confirmant que ces langues sont structurellement sous-servies par les approches neuronales entraînées sur des corpus à l'échelle du web.

Pour un projet mondial visant à décrire des personnes en swahili (214 étiquettes dans Wikidata), en haoussa (221 étiquettes) ou en yoruba (63 étiquettes), s'appuyer sur des traductions par IA garantirait l'échec. Les réseaux neuronaux n'ont tout simplement pas vu assez de textes sur les « physiciens quantiques » en haoussa pour produire un terme précis et juridiquement valide.

---

## 4. Architecture GSCO : une solution déterministe

### 4.1 Vérité terrain juridique au lieu de probabilités

Dans l'architecture GSCO, nous avons complètement abandonné l'estimation par machine. Le principe fondamental est le **déterminisme juridique strict** (Legal Ground Truth). Si le ministère du travail d'un pays spécifique a approuvé le nom officiel d'une profession dans la langue nationale, ce terme est accepté comme norme absolue sans aucune analyse sémantique supplémentaire. Si le registre officiel letton dit que le terme est « santehniķis », et que le dictionnaire haoussa affirme que le physicien est « masanin ilimin lissafi », ces termes sont inclus dans la base de données tels quels. Aucune distorsion neuronale, aucune traduction à la volée — uniquement des correspondances 100 % exactes avec les normes gouvernementales.

### 4.2 La CITP-08 comme Pierre de Rosette : réduction de N² à O(n)

La tâche technique centrale consistait à contourner le piège des tables croisées N². La solution a été trouvée dans la structure de la CITP-08, qui divise toutes les professions mondiales en 436 groupes unitaires, chacun désigné par un code universel à 4 chiffres [1].

Au lieu d'essayer de relier directement le registre de l'Indonésie au registre de la Malaisie ou des États-Unis, nous avons relié chacun des 146 registres nationaux à ce hub central à 4 chiffres :

$$\text{Complexité : } O\left(\frac{n(n-1)}{2}\right) \rightarrow O(n)$$

Pour 146 registres : **10 585 tables croisées → 146 liens vers le hub**. La CITP-08 est devenue la « Pierre de Rosette », grâce à laquelle toute langue peut être instantanément traduite en toute autre sans perte de sens.

En pratique, le code 2111 (« Physiciens et astronomes ») est mis en correspondance avec :
- Russie (OKZ) : 2111.1 (physicien chercheur)
- Brésil (CBO) : 2111-05
- Indonésie (KBJI) : 2111.01
- Wikidata : Q169470

Ce n'est pas seulement une optimisation de l'ingénierie logicielle. Comme l'ont démontré Autor, Levy et Murnane dans leur cadre canonique de changement technologique biaisé par les tâches [45], les tâches professionnelles évoluent continuellement, tandis que les codes professionnels sont révisés tous les 20 ans. L'architecture « hub-and-spoke » n'est donc pas seulement un moyen contre la complexité n² — c'est la seule architecture compatible avec l'évolution continue des tâches aux bords des registres et la sémantique stable des codes dans le hub central.

L'implémentation dans `gsco_esco_mapper.py` utilise deux méthodes de mise en correspondance :
1. **Principale :** `build_en_label_to_qid_map()` — correspondance exacte des étiquettes anglaises (588 correspondances réussies à partir d'ESCO)
2. **De secours :** `build_isco_to_qid_map()` — correspondance par code CITP-08 (0 résultat, car P3008 est vide dans Wikidata)

Le fait que l'option de secours CITP-08 ait renvoyé zéro correspondance constitue une preuve empirique que l'infrastructure des professions de Wikidata n'est pas seulement obsolète — elle est structurellement déconnectée de la norme internationale actuelle.

### 4.3 Agrégation : symbiose homme-IA

Bien que le cadre conceptuel soit strict et déterministe, la collecte physique des données représentait un défi technique colossal. De nombreux États (notamment en Afrique, en Asie et au Moyen-Orient) publient leurs registres de professions non pas sous forme d'API pratiques, mais sous forme de documents PDF de centaines de pages, souvent avec des encodages corrompus ou du texte de droite à gauche (RTL).

Un assistant IA (Claude Code) a été déployé non pas comme un « traducteur », mais comme une « main-d'œuvre » — numérisation de sites Web gouvernementaux, contournement des restrictions d'accès et analyse de documents PDF complexes en arrière-plan autonome. La différence critique : l'IA s'occupait de l'extraction, mais chaque décision de correspondance restait déterministe (correspondance exacte ou refus).

L'agrégation résultante (échantillon représentatif) :

| Source | Pays/Région | Langues | Professions |
|--------|---------------|-----------|------------:|
| ESCO v1.2.1 | 28 pays de l'UE | 28 | 2 942 |
| ISCO-TR | Turquie | tr | 7 202 |
| KeSCO | Kenya | en, sw | 6 582 |
| BSCO | Bangladesh | bn, en | 5 387 |
| YAMAT-08 | Mongolie | mn | 4 844 |
| KZBiH-08 | Bosnie-Herzégovine | bs | 4 246 |
| NCO-2015 | Inde | en, hi | 3 452 |
| KBJI-2014 | Indonésie | id | 2 731 |
| CBO | Brésil | pt-BR | 2 614 |
| TSCO | Thaïlande | th, en | 2 812 |
| CORM | Moldavie | ro, ru | 4 369 |
| NOC 2021 | Canada | en, fr | 822 |
| SINCO | Mexique | es | 686 |
| NKZ-2022 | Tadjikistan | ru | 1 714 |
| SSCO 2024 | Arabie Saoudite | ar, en | 2 738 |
| + 131 autres | Divers | Divers | Divers |
| **Total** | **146 registres** | **53+ langues** | **263 608** |

*Tableau 3 : Échantillon représentatif de registres nationaux de professions agrégés dans GSCO v1.1. Chaque entrée représente un terme juridiquement faisant autorité, publié par l'office statistique national ou le ministère du travail.*

---

## 5. Mise en œuvre technique et résultats pilotes

### 5.1 Pipeline de correspondance exacte

La méthodologie principale rejette la confiance aveugle dans les codes numériques historiques au profit d'un déterminisme textuel strict. L'algorithme prend une étiquette de profession anglaise, trouve sa correspondance exacte dans le registre de référence (par exemple, ESCO) et extrait la traduction approuvée par le gouvernement dans la langue cible.

L'implémentation se compose de cinq modules Python :

1. **`gsco_wikidata_cache.py`** — Dump SPARQL hebdomadaire de tous les éléments de professions Wikidata dans une base de données SQLite locale. Gère la pagination de l'API (Wikidata limite 50 langues par requête `wbgetentities`), filtre les éléments non-Q (sens de lexèmes), stocke les étiquettes, synonymes et descriptions dans 53 langues.

2. **`gsco_esco_mapper.py`** — Met en correspondance les professions ESCO avec les QID Wikidata via une correspondance exacte déterministe des étiquettes anglaises. La fonction `find_best_qid()` implémente un système de confiance à trois niveaux : (a) correspondance exacte, (b) score d'intersection de mots ≥ 0,5, (c) option de secours par code CITP-08.

3. **`gsco_edit_queue.py`** — File d'attente d'édition pré-validée avec niveaux de confiance. Chaque édition est vérifiée par rapport à l'état actuel de Wikidata avant d'être envoyée — seuls les champs vides sont remplis, les données existantes ne sont jamais écrasées.

4. **`gsco_edit_daemon.py`** — Exécute les modifications via l'API d'action MediaWiki avec des contrôles de sécurité : `maxlag=5`, délais aléatoires de 1,5 à 3,0 secondes entre les modifications, période d'essai linguistique (les 50 premières modifications dans de nouvelles langues sont limitées aux QID de faible priorité) et régulation dynamique de la vitesse (+20 % de vitesse par semaine avec 0 refus, division par deux en cas de refus).

5. **`gsco_revert_monitor.py`** — Surveille les annulations toutes les 10 minutes via cron. Crée un fichier `BOT_EMERGENCY_STOP` en cas de détection d'une annulation, déclenchant un arrêt immédiat du bot.

### 5.2 Cache Wikidata

Le cache SQLite agrège l'état actuel de tous les éléments de professions dans Wikidata :

| Table | Lignes | Schéma |
|-------|-----:|--------|
| `occupations` | 26 991 | `qid, isco08, isco88, en_label` |
| `labels` | 152 135 | `qid, lang, label` |
| `aliases` | 98 335 | `qid, lang, alias` |
| `descriptions` | 76 734 | `qid, lang, description` |

*Tableau 4 : Statistiques du cache Wikidata GSCO (22 avril 2026). Le cache est reconstruit hebdomadairement via cron et assure la pré-validation de chaque modification par rapport à l'état actuel de Wikidata.*

La couverture linguistique est très inégale :

| Langue | Étiquettes | Couverture |
|----------|-------:|--------:|
| Anglais (en) | 18 749 | 69.5% |
| Allemand (de) | 14 470 | 53.6% |
| Français (fr) | 10 177 | 37.7% |
| Néerlandais (nl) | 9 197 | 34.1% |
| Espagnol (es) | 8 197 | 30.4% |
| ... | ... | ... |
| Tagalog (tl) | 490 | 1.8% |
| Hindi (hi) | 432 | 1.6% |
| Haoussa (ha) | 221 | 0.8% |
| Swahili (sw) | 214 | 0.8% |
| Yoruba (yo) | 63 | 0.2% |

*Tableau 5 : Couverture des étiquettes par langue dans les éléments de professions Wikidata. Les langues européennes dominent ; les langues parlées par des milliards de personnes (hindi, bengali, swahili) ont moins de 2 % de couverture. GSCO résout directement cette asymétrie.*

Les découvertes structurelles issues de la comparaison inter-pays révèlent une valeur de recherche supplémentaire au-delà des statistiques de couverture. La Lettonie et l'Estonie ont indépendamment convergé vers la division du groupe unitaire CITP 8131 (Opérateurs de processus chimiques et photographiques) en sous-catégories distinctes — validant empiriquement un candidat à la division proposé pour la CITP-28, sans aucune coordination. Le classificateur national du Tadjikistan (NKZ-2022), bien qu'utilisant le russe comme langue administrative avec le OKZ russe, présente 75,9 % de divergence lexicale au niveau des groupes unitaires à 4 chiffres — avec des codes CITP 7313, 7314 et 7315 (vitrailliste, potier, bijoutier) systématiquement confondus entre les deux registres cyrilliques. Le BDSOC 2011 du Brunei contient 1 381 noms de professions au niveau des codes à 5 chiffres sans aucune table croisée CITP — un « paradoxe 0/N », où il existe des données empiriques significatives mais invisibles pour tout système interrogeant par code CITP.

### 5.3 Résultats pilotes

Le bot (ReNeuralAgent / MarisDreshmanisBot) a été déployé sous Wikidata. La phase pilote a donné les résultats suivants :

- **19 490+ modifications totales** sur toutes les tâches, **0 refus** — confirmant la sécurité sémantique à 100 % de l'approche déterministe
- **1 122 modifications spécifiques à GSCO pour les professions** dans 27 langues (289 lettones + 833 multilingues)
- **4 202 modifications en attente** pour exécution dans 26 langues, pré-validées par rapport à l'état actuel de Wikidata
- La demande de statut de bot est en cours d'examen à Wikidata (Wikidata:Requests for permissions/Bot)
- Chaque modification est tracée jusqu'à sa source : le format du résumé de modification est `Adding label from GSCO occupation database (I: GSCO, S: ESCO)`
- **Utilisation de l'IA/LLM : aucune.** Toutes les opérations sont déterministes — descriptions basées sur des modèles, correspondance exacte, vérification des limites, vérification HTTP.

---

## 6. Applications pratiques

### 6.1 Pour les gouvernements et les régulateurs (OIT, ESCO, O*NET)

Aujourd'hui, les agences gouvernementales dépensent des années et des millions de dollars de contribuables pour créer des tables croisées bilatérales entre leurs normes. En se connectant à la base de données GSCO, les gouvernements n'ont plus besoin de construire des ponts bilatéraux directs et de souffrir du problème N². Comme GSCO a déjà relié 146 registres nationaux au hub central CITP-08, le système fonctionne comme un routeur mondial.

De plus, l'OIT ne met à jour sa norme que tous les 20 ans (avec la révision en cours) [1], et même le processus « d'amélioration continue » de la Commission européenne pour ESCO a nécessité deux années complètes d'assurance qualité, de consensus des comités et de traduction obligatoire dans toutes les langues officielles de l'UE pour ajouter seulement 68 nouvelles professions dans la version 1.1. À l'ère de la numérisation, où des professions comme « ingénieur de prompt IA » ou « opérateur de drone » émergent et se propagent en quelques mois, ces cycles bureaucratiques sont structurellement inadéquats. GSCO transforme un document PDF statique en un écosystème vivant : si une nouvelle profession apparaît simultanément dans les registres de cinq pays différents, GSCO enregistre automatiquement cette tendance, offrant aux décideurs une image dynamique du marché du travail mondial en évolution.

### 6.2 Pour les développeurs d'IA et les ingénieurs NLP

Les développeurs d'IA n'ont plus besoin d'essayer d'analyser des textes d'annonces d'emploi bruts et d'espérer qu'un réseau neuronal devine la bonne traduction. GSCO fournit aux laboratoires d'IA un ensemble de données de référence prêt à l'emploi, juridiquement propre (Golden Benchmark) dans plus de 85 langues (y compris le persan, le bengali, l'ourdou et le swahili). Chaque mot de cette base de données est soutenu par l'autorité d'un ministère ou d'une administration statistique nationale spécifique.

L'utilisation de GSCO pour l'affinage ou les architectures RAG permet aux modèles d'IA d'atteindre une précision juridique et linguistique de 100 % dans la classification des professions pour les langues les plus rares du monde, éliminant complètement les hallucinations. La structure de l'ensemble de données (`labels(qid, lang, label)`) fournit des paires d'entraînement prêtes à l'emploi : 26 991 professions × N langues = des millions de paires alignées.

### 6.3 Pour les sociologues et les statisticiens

GSCO fournit aux sociologues un vocabulaire standardisé prêt à l'emploi dans des dizaines de langues, automatisant le processus de codage des enquêtes. L'intégration dans les progiciels de codage existants (CASCOT, SOCcer, `occupationMeasurement`) peut fournir une option de secours déterministe pour des dizaines de nouvelles langues, réduisant considérablement les coûts opérationnels dans les évaluations internationales à grande échelle (ILSAs, telles que PISA ou ICILS).

La véritable valeur scientifique réside dans le sous-produit du projet — la **Matrice de Reconnaissance** (Matrix of Recognition). En superposant 146 registres nationaux, nous obtenons un outil qui révèle les différences socioculturelles et politiques entre les États. Par exemple, le « coach de vie » est officiellement reconnu en Lettonie (comme *personīgās izaugsmes veicināšanas speciālists*) et au Royaume-Uni, mais complètement absent du classificateur de la Russie. Le registre turc contient 7 202 professions, tandis que le canadien n'en contient que 822 — une différence de 9 fois, révélant à quel point les États conceptualisent différemment leurs marchés du travail.

### 6.4 Pour la réponse à la crise migratoire et l'accueil des réfugiés

Un domaine d'application spécifique qui n'a pas reçu suffisamment d'attention dans la littérature en linguistique computationnelle est l'accueil et le tri des flux massifs de réfugiés sur le marché du travail. Lorsqu'un pays d'accueil doit traiter 5 000 profils de compétences en 30 jours, le goulot d'étranglement n'est pas la volonté politique, mais l'infrastructure classificatoire : une qualification délivrée dans un système doit être lisiblement mise en correspondance avec les codes du second système avant qu'un organisme de licence professionnelle ne puisse l'évaluer.

GSCO résout cela directement. Pour tout travailleur migrant ou réfugié ayant une profession documentée dans l'un des 146 registres indexés, le pipeline effectue : étiquette dans la langue maternelle → code CITP-08 à 4 chiffres → étiquette du classificateur du pays d'accueil, en moins d'une seconde par personne. Le lot slave de notre bibliothèque de cas de migration documente l'expérience de la République tchèque avec 473 000 réfugiés ukrainiens en 2022, dont 75 % ont été classés dans le groupe 9 de la CITP (professions élémentaires), alors que la plupart avaient une éducation tertiaire — un schéma que l'OIM a documenté comme « Surqualifiés, sous-employés » (Overqualified, Underemployed) [46]. Même lorsque le classificateur d'origine et celui du pays d'accueil correspondent nominalement (l'Ukraine et la République tchèque utilisent tous deux des systèmes basés sur la CITP-08), l'absence d'un pont lisible par machine entre les familles d'étiquettes de professions crée un fossé qui conduit par défaut à une rétrogradation.

Le cas bangladais de classification forcée illustre un régime de refus plus aigu : 800 000 femmes migrantes sont enregistrées dans les registres des pays du Golfe comme « travailleuses domestiques » indépendamment de leur expérience professionnelle réelle, car le classificateur du pays d'accueil ne contient pas de lien croisé avec les catégories professionnelles du registre d'origine [36]. L'architecture GSCO permettrait un tri professionnel correct au point d'entrée — sans annuler les exigences légales, mais en fournissant une liaison de codes professionnels que les administrateurs humains exécutent actuellement manuellement, de manière incohérente et à grande échelle.

La dimension psychologique de la classification erronée va au-delà des pertes économiques. Une revue systématique de Ngabirano 2026 sur les migrants francophones [47] documente que le *déclassement professionnel* — la rétrogradation forcée dans une catégorie professionnelle inférieure — est l'un des prédicteurs les plus forts de stress psychologique chez les populations immigrées hautement qualifiées, dépassant même les effets de la barrière linguistique. La précision de la classification, en ce sens, n'est pas seulement un problème de qualité des données, mais une entrée de santé publique.

---

## 7. Limites et travaux futurs

### 7.1 Limites actuelles

1. **Asymétrie de couverture.** Bien que GSCO agrège 146 registres, beaucoup sont concentrés en Europe et en Amérique. Les registres africains au-delà du Kenya restent sous-représentés. Le NMP-CI 2016 de la Côte d'Ivoire ne couvre que les secteurs artisanal et manuel, laissant les professions de la santé, du droit et de la finance complètement non classifiées. 41 PDF téléchargés en attente d'analyse comprennent le PACSCO (23 États insulaires du Pacifique), l'Iran, le Pakistan et plusieurs pays d'Amérique latine.

2. **Dépendance aux étiquettes anglaises.** La méthode de correspondance principale repose sur la correspondance exacte des étiquettes anglaises. Les professions existant dans les registres nationaux mais n'ayant pas d'équivalent anglais dans Wikidata ne peuvent pas être mises en correspondance automatiquement. Cela a affecté environ 80 % des professions ESCO pour lesquelles aucune correspondance exacte n'a été trouvée dans Wikidata (2 354 sur 2 942). De manière critique : le registre letton de 4 102 entrées et le lituanien de 3 044 entrées ne contiennent aucune étiquette anglaise — bloquant la reconnaissance automatique des qualifications dans les systèmes de destination anglophones.

3. **Bugs fantômes de métadonnées des classificateurs.** Dans la version actuelle, des problèmes d'intégrité des données ont été découverts, révélés comme des corrections P0 en attente de résolution : le registre fantôme ba_error_stub de Bosnie (un stub de métadonnées sans données de base) ; le registre arabe JSCO de Jordanie avec une inversion de texte RTL confirmée ; le paradoxe 0/N du Brunei (1 381 entrées affichées comme 0 % de couverture CITP en raison du format des codes à 5 chiffres non encore mis en correspondance) ; et 540 entrées de la Côte d'Ivoire sans table croisée CITP. Ce sont des bugs d'ingénierie dans le pipeline de données, pas des lacunes dans les registres sources.

4. **Instantané statique.** La version actuelle (v1.1) est un instantané ponctuel. Les registres nationaux sont mis à jour à des fréquences variables — GSCO nécessite une réagrégation périodique pour rester pertinent. Le OK 016-2025 russe, remplaçant la version de 1994 après une interruption de 30 ans, a introduit des codes pour les opérateurs IA, les spécialistes de la cybersécurité et les opérateurs de drones, non encore reflétés dans les systèmes de tables croisées en aval.

5. **Lacunes dans l'ontologie Wikidata.** La découverte que P3008 (CITP-08) est complètement vide dans Wikidata suggère qu'une proposition de propriété pour le remplissage systématique de la CITP-08 serait précieuse avant que GSCO ne puisse utiliser pleinement la correspondance basée sur les codes.

6. **Lacunes de couverture de la langue primaire pour l'indonésien, le malais, le khmer et le lao.** Les données sources dans la langue primaire de ces langues ont eu une indexabilité limitée dans notre pipeline de collecte automatisé, ce qui signifie que les corridors d'Asie du Sud-Est sont sous-représentés, malgré leur importance pour les flux migratoires modernes.

### 7.2 Orientations futures

1. **Mise à l'échelle vers les éléments Q5.** Le projet pilote actuel cible les éléments de professions (Q28640). L'objectif final est la création massive de descriptions pour environ 11 millions de profils humains (Q5) dans Wikidata via la propriété P106 (profession), ce qui donnera 50 à 100 millions de descriptions multilingues.

2. **GSCO comme référence Wikidata (P248).** Après l'obtention du DOI Zenodo, GSCO lui-même peut servir de source de référence dans les assertions Wikidata, établissant une chaîne d'origine des données formelle.

3. **Ensemble de données Hugging Face.** La publication de GSCO sur Hugging Face le rendra directement accessible à la communauté ML pour l'affinage et l'évaluation.

4. **Point d'accès API.** Une API REST publique (`gsco.reincarnatiopedia.com/v1/occupation?isco=2111&lang=sw`) fournirait un accès programmatique sans avoir à télécharger l'ensemble de données complet.

5. **Système de surveillance des crises (crisis-watch).** Une couche de sensibilisation externe dynamique qui signale lorsque les flux de réfugiés des pays sources enregistrés dépassent les niveaux seuils, assurant une synchronisation proactive des registres en amont des pics de demande de reconnaissance des qualifications.

6. **Intégration dans le groupe de travail CITP-28.** Le processus de révision de la CITP-28 de l'OIT (date cible 2028) représente une opportunité d'entrée de données qui se présente une fois par génération. GSCO a déjà identifié des candidats empiriques : la convergence indépendante de l'Estonie et de la Lettonie sur les sous-codes CITP 8131 ; la taxonomie la plus riche de professions minières de Mongolie hors OCDE ; les codes du secteur du cacao de Côte d'Ivoire sans équivalent CITP actuel. Objectif : soumission formelle de données au groupe de travail CITP-28 de l'OIT d'ici le T2 2027.

7. **Mécanisme d'auto-mise à jour.** Un pipeline de redémarrage à chaud qui accepte les nouvelles versions des registres lorsque les administrations statistiques nationales publient des mises à jour, propageant les changements aux tables croisées sans réagrégation complète.

---

## 8. Conclusion

Le projet GSCO a commencé par un échec pratique : la tentative d'ajouter des descriptions multilingues pour 890 lauréats du prix Nobel à Wikidata a révélé une crise infrastructurelle en cascade — des cycles de mise à jour de 20 ans de l'OIT à l'absence totale de données CITP-08 dans Wikidata (0 sur 26 991 éléments).

L'architecture déterministe présentée ici — utilisant les codes CITP-08 comme hub universel et les registres nationaux faisant autorité comme vérité terrain — réalise ce que les modèles d'IA probabilistes ne peuvent pas : une précision sémantique de 100 % dans plus de 85 langues, vérifiée par plus de 19 490 modifications Wikidata avec zéro refus.

En publiant l'ensemble de données complet (263 608 entrées de professions de 146 registres), le cache Wikidata (152 135 étiquettes dans 53 langues) et l'infrastructure complète du bot en open source, nous fournissons à la communauté de recherche :

- **Un étalon d'or** pour l'entraînement et l'évaluation des modèles NLP multilingues sur des langues à ressources limitées
- **Une option de secours déterministe** pour le codage des enquêtes sociologiques, éliminant les divergences entre codeurs
- **Un routeur mondial** réduisant la complexité des tables croisées de O(n²) à O(n)
- **Un écosystème vivant** qui capture les professions émergentes dans différentes juridictions en temps quasi réel

Vingt ans séparent la CITP-58 de la CITP-68, de la CITP-88, de la CITP-08. Au moment de l'arrivée de la CITP-28 en 2028, la classification du travail moderne — ingénierie IA, spécialistes de l'adaptation climatique, travailleurs de l'économie des plateformes, créateurs de contenu — sera en retard d'environ une génération économique complète. GSCO ne propose pas de remplacer la CITP. Il propose de combler le fossé de 20 ans avec une couche empirique continuellement mise à jour qui révèle où la réalité statistique s'est écartée du code administratif.

Les 280 millions de migrants en mouvement en 2024 et les plus de 350 millions prévus d'ici 2035 (ONU DESA) ne peuvent pas attendre la prochaine révision décennale. Leur vie professionnelle est façonnée — et souvent interrompue — par une infrastructure classificatoire conçue pour un monde qui n'existe plus. GSCO est la couche entre la réalité du monde et la stabilité de la CITP.

Les 890 lauréats du prix Nobel qui ont inspiré ce projet peuvent désormais être décrits dans plus de 260 langues — non pas par des hallucinations mécaniques, mais par l'autorité juridique des nations qui les ont formés.

---

## 9. Le coût de l'inaction

Les sections précédentes établissent ce que GSCO peut faire. Cette section examine ce qui se passera si les problèmes qu'il résout ne sont pas résolus — une question qui n'est plus théorique.

### 9.1 Le multiplicateur du retard économique

Les pays qui ont retardé la transition de la CITP-88 à la CITP-08 ont payé en moyenne 2,4 fois plus en coûts d'intégration finaux lorsque la pression des institutions de l'UE est venue pour se lier à ESCO. En projetant cette tendance vers l'avant : les actions entreprises maintenant pour aligner un registre national sur le hub CITP-08 de GSCO coûtent entre 1,0 et 2,5 millions d'euros par pays (selon la taille du registre et l'écart linguistique) ; l'action reportée à 2031 est estimée à 2,3 à 7,2 millions d'euros, tirée par la dette héritée accumulée, augmentant à environ 5 % par an via les systèmes de retraite, de fiscalité, du travail et d'assurance sociale qui consomment tous des codes professionnels en aval [41].

Ce n'est pas un multiplicateur spéculatif. C'est une tendance documentée de la migration de la CITP-88 vers la CITP-08, maintenant appliquée prospectivement aux pays qui fonctionnent encore avec des systèmes de classification antérieurs à 2008. Le KZBiH-08 de Bosnie-Herzégovine est une source majeure pour les demandes allemandes de reconnaissance des qualifications d'infirmières — environ 2 300 approbations par an aux taux de pointe de 2019. Parmi celles-ci, 23,3 % nécessitent des mesures compensatoires pendant une période de reclassement de 12 à 18 mois [48]. La perte de salaire résultante par infirmière concernée est en moyenne de 12 000 € pendant la période de reclassement ; 930 infirmières par an × 12 000 € = environ 11 millions d'euros par an en pertes économiques évitables rien que pour ce corridor. Agrégé sur dix pays analysés dans cette étude, une estimation conservatrice des frictions évitables de reconnaissance des qualifications est de 80 à 150 millions d'euros par an.

L'American Immigration Council documente 39 milliards de dollars de salaires annuels non réalisés et 10,2 milliards de dollars de recettes fiscales perdues en raison de la sous-utilisation des qualifications des immigrants rien qu'aux États-Unis [49]. Une évaluation de l'Université Flinders de 2022 pour l'Australie estime les pertes économiques à 70 milliards de dollars australiens, avec 43 % des migrants qualifiés chinois travaillant en dehors de leur profession déclarée [50].

### 9.2 Huit fenêtres de fermeture

Les fenêtres stratégiques suivantes sont limitées dans le temps. Chacune se ferme indépendamment des autres, et chacune représente une opportunité qui ne se reproduira pas selon un calendrier prévisible.

**Fenêtre 1 : Le tsunami de reclassement de l'IA (2026–2035).** Des catégories entières de professions sont actuellement reclassifiées sous l'automatisation des tâches pilotée par l'IA. Les formateurs d'IA, les ingénieurs de prompt, les opérateurs de véhicules autonomes et les spécialistes du réglage fin des grands modèles linguistiques n'apparaissent dans aucun des 10 briefs nationaux analysés dans cette étude. Chaque année sans mise à jour du classificateur signifie qu'une autre cohorte de travailleurs entre sur le marché du travail dans une catégorie qui n'existe pas officiellement. La théorie de la polarisation du travail [51] prédit que l'automatisation par l'IA éviscérera les catégories intermédiaires en termes de compétences, les plus densément peuplées dans les groupes CITP-08 4–8 ; les pays qui classifient ces transitions maintenant auront des bases empiriques ; ceux qui attendent reconstruiront rétroactivement dans de vieux paniers incorrects.

**Fenêtre 2 : Accélération de la migration climatique.** La CITP-08 ne contient pas de codes pour les travailleurs assurant la conformité au mécanisme d'ajustement carbone aux frontières (MACF), les spécialistes de l'adaptation climatique ou les travailleurs agricoles déplacés par le climat. Les 10 pays analysés dans cette étude couvrent collectivement des secteurs économiques vulnérables au climat : agriculture du cacao en Côte d'Ivoire (secteur entier non classifié dans le registre actuel) ; culture du coton et exploitation minière gourmande en eau au Tadjikistan ; pétrole et gaz en Arabie Saoudite et au Brunei ; gestion de l'eau d'origine glaciaire en Mongolie ; mer et pêche au Cap-Vert. La classification de ces secteurs avant l'arrivée du disrupteur professionnel climatique diffère qualitativement de la classification après coup.

**Fenêtre 3 : Blocage de l'économie des plateformes.** LinkedIn, Indeed et Upwork définissent déjà ce que signifie « développeur de logiciels » en Lettonie, en Lituanie et en Estonie. Bolt et Wolt définissent « chauffeur-livreur » dans les pays baltes. HungerStation le définit en Arabie Saoudite. Sans classificateurs nationaux mis à jour, les taxonomies des plateformes privées deviennent les normes professionnelles de facto — sans responsabilité légale, sans lien avec l'OIT et sans table croisée vers les systèmes de sécurité sociale.

**Fenêtre 4 : Perte de connaissances institutionnelles (2030–2035).** La dernière cohorte de statisticiens qui ont géré la transition CITP-88 → CITP-08 approche de la retraite dans les 10 pays couverts par les briefs. La mémoire institutionnelle sur les raisons pour lesquelles certains codes hérités ont été conservés, pourquoi certaines familles de professions soviétiques ont survécu dans les classificateurs post-soviétiques et comment des cas limites spécifiques ont été résolus lors de la transition de 2008 sera indisponible après 2030. L'intégration, tant que cette expertise est disponible, coûte 2 à 3 fois moins cher que la reconstruction après la retraite.

**Fenêtre 5 : Fenêtre de transition assistée par IA (2026–2028).** Le processus actuel de génération d'étiquettes anglaises assistée par IA pour le registre letton de 4 102 entrées est estimé à 15 000 €. La même tâche, effectuée manuellement en 2031 sous une pression réglementaire potentielle de l'ECOWAS ou de l'EURES, est estimée à 150 000 €. La génération d'IA de tables croisées pour les 540 entrées de la Côte d'Ivoire est estimée à 40 000 € maintenant contre 400 000 € sous une pression future d'harmonisation de l'ECOWAS. Cette fenêtre se ferme à mesure que le coût des modèles augmente, que les exigences de vérification manuelle augmentent sous la réglementation naissante sur la gouvernance de l'IA, et que le retard s'accumule.

**Fenêtre 6 : Dette héritée accumulée.** Chaque année d'inaction ajoute environ 5 % au coût d'intégration en aval via les systèmes de retraite, de fiscalité, du travail et d'assurance sociale. Pour la Bosnie, qui gère un système de retraite divisé entre deux entités (Fédération de Bosnie-Herzégovine et Republika Srpska), chacune avec ses propres pratiques classificatoires distinctes, le taux d'accumulation est structurellement plus élevé. La formule n'est pas linéaire : elle est exponentielle, car chaque système en aval qui adopte des codes hérités devient une nouvelle dépendance qui doit être migrée simultanément lors de toute future mise à jour.

**Fenêtre 7 : Fenêtre de révision CITP-28 (2026–2028).** Le processus de révision de la CITP, qui se produit une fois par génération, est actuellement ouvert aux données empiriques. Les pays et les chercheurs impliqués dans cette fenêtre façonnent la norme ; ceux qui s'y joignent en 2031 s'adaptent à une taxonomie conçue par d'autres. La taxonomie la plus riche de professions minières de Mongolie hors OCDE, les codes du secteur du cacao de Côte d'Ivoire, les familles de professions pétrolières et gazières d'Arabie Saoudite et les sous-classifications de l'ingénierie pétrolière du Brunei — représentent tous des données d'entrée qui ne sont précieuses que lorsqu'elles sont soumises au processus de révision actif. GSCO a déjà identifié des codes et des corridors spécifiques ; le chemin de soumission au groupe de travail CITP-28 de l'OIT est l'étape restante.

**Fenêtre 8 : Pic migratoire — agir avant la prochaine vague, pas pendant.** La CITP-88 a été conçue pour un monde de 70 millions de migrants internationaux. La CITP-08 a été conçue pour 190 millions. Le niveau de base actuel est de 280 millions plus 37 millions de réfugiés plus 75 millions de personnes déplacées à l'intérieur de leur propre pays. Les 10 pays couverts par les briefs accueillent ou génèrent collectivement environ 15 à 20 millions de cette population. Établir une base classificatoire avant le prochain pic migratoire — qu'il soit climatique, lié à un conflit ou dû à la polarisation économique — diffère qualitativement de la tentative de classification pendant le pic. Lors de l'événement ukrainien de déplacement de 2022, 1,5 million de réfugiés sont entrés en Pologne en quelques semaines ; l'infrastructure classificatoire existante à ce moment-là a déterminé les résultats pour les individus. L'infrastructure construite après le pic classe son coût humain, mais pas ses personnes.

### 9.3 L'argument de l'honnêteté politique

Le cadre du coût de l'inaction nécessite une admission inconfortable : certains des écarts classificatoires les plus importants existent entre des pays qui ne sont pas des partenaires diplomatiques naturels. Les 75,9 % de divergence lexicale entre le Tadjikistan et le classificateur russe, malgré le partage du russe comme langue administrative des deux registres, reflètent des décennies de divergence administrative post-soviétique qu'il était politiquement commode d'ignorer. Le taux d'approbation bilatéral des qualifications France → Allemagne (40,3 %) par rapport à France → Luxembourg (99,8 %) reflète non pas une ambiguïté juridique, mais l'économie politique du gardiennage des associations professionnelles en Allemagne par rapport à un marché du travail luxembourgeois plus petit et plus intégré [42].

L'architecture « hub-and-spoke » de GSCO est politiquement neutre par conception : elle relie chaque registre à la CITP-08, et non à un partenaire bilatéral. Cela signifie qu'un pays qui ne souhaite pas s'harmoniser directement avec un rival géopolitique peut néanmoins atteindre une lisibilité mutuelle via un hub commun. L'architecture ne nécessite pas de confiance entre les points d'extrémité — seulement la connexion de chaque point d'extrémité à une norme. C'est précisément ce qui la rend évolutive.

---

## Disponibilité des données

Toutes les données, le code et la documentation sont librement disponibles :

- **Répertoire GitHub :** [https://github.com/Reincarnatiopedia/gsco](https://github.com/Reincarnatiopedia/gsco)
- **Ensemble de données Zenodo :** [DOI attendu — sera ajouté lors du téléchargement]
- **Bot Wikidata :** [User:Maris Dreshmanis](https://www.wikidata.org/wiki/User:Maris_Dreshmanis)
- **Code source du bot :** [Reincarnatiopedia/wikidata-bot](https://github.com/Reincarnatiopedia/wikidata-bot)

Structure du répertoire :
```
data/
  esco/                    — ESCO v1.2.1 (28 langues, 2 942 professions)
  national_registries/     — 146 registres nationaux en JSON
  wikidata_cache/          — Export CSV (26 991 éléments × 53 langues)
scripts/
  gsco_wikidata_cache.py   — Dump hebdomadaire de Wikidata vers SQLite
  gsco_esco_mapper.py      — Mapper déterministe ESCO→Wikidata
  gsco_edit_queue.py       — File d'attente d'édition pré-validée
  gsco_edit_daemon.py      — Moteur d'exécution de bot avec contrôles de sécurité
  gsco_revert_monitor.py   — Surveillance des annulations avec arrêt d'urgence
```

---

Une bibliothèque compagnon interactive de tous les 117 cas de migration documentés — avec recherche par pays et filtrage en direct — est maintenue sur <https://gsco.io/cases>. La bibliothèque sur site complète l'Annexe A et est mise à jour au fur et à mesure que de nouveaux cas sont documentés.

## Annexe A : Cas de migration documentés (Bibliothèque complète — 117 cas)

La bibliothèque suivante couvre **117 cas documentés**, obtenus à partir de sept lots de recherche régionaux menés entre janvier et avril 2026, couvrant plus de 40 langues. Les cas 1 à 30 sont présentés ci-dessous sous forme narrative détaillée — sélectionnés en fonction de l'ampleur des personnes touchées et de la qualité de la documentation. Les cas 31 à 120 apparaissent dans un tableau de référence compact à la fin de cette annexe ; leur texte intégral est maintenu sur <https://gsco.io/cases> avec une recherche par pays. Toutes les URL et sources citées sont répertoriées dans la section « Sources » ; les cas sans source primaire vérifiable sont omis.

---

Les cas suivants sont obtenus à partir de sept lots de recherche régionaux menés entre janvier et avril 2026, couvrant plus de 40 langues. Les cas sont sélectionnés en fonction de l'ampleur des personnes touchées et de la qualité de la documentation. Toutes les URL et sources citées sont répertoriées dans la section « Sources » ; les cas sans source primaire vérifiable dans la bibliographie sont omis.

---

### Cas 1 : Bosnie-Herzégovine → Allemagne — Infirmières (2012–2021)
**Échelle :** 17 103 demandes de reconnaissance de qualifications d'infirmières de BiH en Allemagne pour 2012–2021 ; 2 300 approbations au pic de 2019 ; 23,3 % nécessitent des mesures compensatoires (12–18 mois)
**Classificateur source :** KZBiH-08 (« Medicinska sestra » → CITP 2221)
**Classificateur de destination :** KldB-2010 allemand (« Gesundheits- und Krankenpflegerin » → 81302)
**Inadéquation :** La correspondance CITP à 4 chiffres existe sur papier ; la granularité de la sous-classification KldB nécessite une mise en correspondance des compétences, non déductible du seul code CITP
**Résultat :** ~930 infirmières par an en reclassement de 12 à 18 mois ; perte de salaire estimée à 11 millions d'euros par an évitée rien que pour ce corridor ; le personnel de santé serbe est épuisé à 14 % d'ici 2017 [48]
**Pertinence pour GSCO :** ba_kzbih08 déjà dans GSCO (4 246 entrées) ; zéro étiquette bosniaque dans Wikidata ; le registre fantôme ba_error_stub est un bug P0 cachant la disponibilité des données

---

### Cas 2 : Ukraine → République tchèque — Professionnels (« nettoyage de carottes ») (2022–présent)
**Échelle :** 473 000 Ukrainiens en République tchèque en 2022 ; 75 %+ classés dans le groupe 9 de la CITP (professions élémentaires), bien que la majorité ait une formation tertiaire ; 68 % des femmes cadres/professionnels travaillent en dessous de leur niveau de qualification
**Classificateur source :** DKHP ukrainien (basé sur CITP-08)
**Classificateur de destination :** KZAM tchèque (basé sur CITP-08)
**Inadéquation :** Les deux utilisent des codes CITP-08 — correspondance nominale — mais la reconnaissance des diplômes est toujours requise ; la simple correspondance des codes ne suffit pas sans un pont d'équivalence des qualifications
**Résultat :** Surqualification systématique ; documenté par l'OIM comme « Surqualifiés, sous-employés » [46]
**Pertinence pour GSCO :** Démontre que la correspondance des codes CITP est une condition nécessaire mais non suffisante ; un tableau croisé + un cadre de reconnaissance sont nécessaires

---

### Cas 3 : Philippines → Japon — Infirmières (2008–présent)
**Échelle :** Taux de réussite cumulé sur 15 ans à l'examen japonais de licence d'infirmière : 14 % ; 86 % retournent aux Philippines ou travaillent comme aides plutôt que comme infirmières autorisées
**Classificateur source :** Codes d'infirmières de la PRC philippine
**Classificateur de destination :** JSCCO japonais (厚生労働省)
**Inadéquation :** L'examen japonais est calibré sur la famille de codes professionnels japonais ; la formation infirmière philippine correspond à des sous-codes CITP différents de ceux couverts par l'examen japonais
**Résultat :** 15 ans × cohortes annuelles ; sous-utilisation structurelle d'infirmières qualifiées malgré l'Accord de partenariat économique (APE) bilatéral conçu pour faciliter la mobilité
**Source :** Lot sur la migration en Asie du Sud-Est (2026) ; statistiques officielles du ministère japonais de la Santé, du Travail et du Bien-être

---

### Cas 4 : Venezuela → Pérou/Colombie — « Médecins communautaires complets » (2018–présent)
**Échelle :** ~50 000 médecins vénézuéliens sans code équivalent dans les classificateurs des pays de destination ; le Pérou a annulé les enregistrements médicaux vénézuéliens en 2018
**Classificateur source :** Cadre professionnel vénézuélien MPPE (« médico integral comunitario » = spécialiste de la médecine communautaire)
**Classificateur de destination :** CNO péruvien, CON colombien (aucun ne contient « médico integral comunitario » comme catégorie)
**Inadéquation :** La catégorie professionnelle est littéralement absente du classificateur de destination ; le code est introuvable ; la licence ne peut pas être évaluée
**Résultat :** Déclassement massif ; beaucoup exercent comme personnel administratif ou non enregistrés ; le Pérou a complètement annulé les enregistrements
**Source :** Lot sur la migration en langue romane (2026)

---

### Cas 5 : Roumanie → Italie — Infirmières (2023–présent)
**Échelle :** 11 861 infirmières roumaines directement touchées par la non-acceptation par l'Italie de la directive UE 2024/505
**Classificateur source :** COR roumain (soins infirmiers → CITP 2221)
**Classificateur de destination :** NUP italien (infermiere professionale)
**Inadéquation :** La non-acceptation de la directive signifie que la voie de reconnaissance automatique est rompue, même si les deux pays sont membres de l'UE
**Résultat :** Procédures d'infraction de l'UE contre l'Italie, mai 2025 [40] ; les infirmières travaillent illégalement ou pas du tout
**Pertinence pour GSCO :** Lot roumain ; GSCO a les registres RO et IT ; un tableau croisé existe — le fossé est juridique-administratif, pas classificatoire, mais GSCO fournit un pont technique une fois la résolution juridique obtenue

---

### Cas 6 : Syrie → Allemagne — Licence médicale (2015–2016 documenté, en cours)
**Échelle :** Attente moyenne de 14 mois pour l'Approbation (licence médicale), documentée dans une étude BMC pour les demandes déposées en juin 2015 ; 62 100 demandes d'Approbation d'Iran seulement en 2023 (+26 % en glissement annuel)
**Classificateur source :** Codes de l'Ordre des médecins syrien
**Classificateur de destination :** Approbationsordnung für Ärzte (ÄAppO) allemand avec mise en œuvre spécifique au Bundesland
**Inadéquation :** Il n'existe pas de pont lisible par machine entre les codes de spécialité médicale syriens et la classification allemande spécifique au Bundesland ; le coût de l'Approbation varie de 170 € à 850 € selon le Land ; l'évaluation externe du diplôme ajoute 450 €–3 000 € ; cours préparatoires jusqu'à 4 900 €
**Résultat :** Cas documenté de 14 mois (Erim et al. 2020) [35] ; barrière systématique ; 80 % des entreprises allemandes déclarent ne pas utiliser du tout le système formel de reconnaissance [41]
**Source :** Lot sur la migration Allemagne/Nordique (2026) ; Erim et al. 2020 BMC Health Services Research

---

### Cas 7 : Tadjikistan → Russie — Divergence de classification dans une langue commune (registre 2022)
**Échelle :** 1,1 million de travailleurs migrants tadjiks en Russie = 11 % de la population totale du Tadjikistan ; transferts de fonds = 30–40 % du PIB du Tadjikistan
**Classificateur source :** NKZ-2022 tadjik (en russe, basé sur CITP-08)
**Classificateur de destination :** OKZ russe (basé sur CITP-08)
**Inadéquation :** 75,9 % de divergence lexicale au niveau à 4 chiffres, bien que les deux registres soient en russe et nominalement alignés sur la CITP-08 ; les codes CITP 7313/7314/7315 (vitrailliste, potier, bijoutier) sont systématiquement confondus ; NKZ-2022 contient littéralement « National Bank of Kazakhstan » dans le code 1124 — un artefact de copie d'un modèle kazakh
**Résultat :** La reconnaissance des qualifications entre deux systèmes russophones basés sur la CITP-08 échoue en raison de divergences de contenu, invisibles lors de la correspondance uniquement par code
**Pertinence pour GSCO :** Découvert dans l'analyse de la base de données GSCO ; brief pays TJ ; confirme que des registres dans la même langue et sous la même norme peuvent avoir des divergences de contenu significatives nécessitant une correspondance GSCO au niveau des étiquettes

---

### Cas 8 : Hong Kong (BNO) → Royaume-Uni (2021–présent)
**Échelle :** n=2 000 enquête British Future (2023) ; 47 % des détenteurs de visas BNO travaillent en dehors de leur domaine professionnel ; 28 % citent la reconnaissance des qualifications comme un obstacle majeur
**Classificateur source :** HKISCO-11 de Hong Kong (basé sur CITP-08)
**Classificateur de destination :** SOC-2020 britannique
**Inadéquation :** Les organismes de licence professionnelle au Royaume-Uni (NMC pour les soins infirmiers, GMC pour la médecine) exigent une vérification des compétences spécifique au Royaume-Uni, non déductible du code HKISCO ; la granularité du SOC-2020 diffère de celle du HKISCO-11 au niveau à 4 chiffres
**Résultat :** 47 % d'inadéquation professionnelle dans une population de ~150 000+ arrivants BNO, extrapolée ; stress psychologique documenté [47]
**Source :** Enquête British Future 2023 [52]

---

### Cas 9 : Chine → Australie — inadéquation de la migration qualifiée (2022)
**Échelle :** 43 % des migrants qualifiés chinois en Australie travaillent en dehors de leur profession déclarée ; pertes économiques estimées à 70 milliards de dollars australiens (Université Flinders 2022)
**Classificateur source :** CSCO chinois (中国职业分类大典)
**Classificateur de destination :** ANZSCO australien (ABS/Stats NZ)
**Inadéquation :** Les organismes d'évaluation des compétences (Engineers Australia, CPA Australia, etc.) exigent une mise en correspondance des compétences qui traverse plusieurs groupes unitaires ANZSCO ; il n'existe pas de table croisée CSCO vers ANZSCO sous forme lisible par machine
**Résultat :** 70 milliards de dollars australiens de production économique non réalisée ; 43 % d'inadéquation professionnelle [50]
**Source :** Lot sur la migration en Asie de l'Est (2026) ; évaluation de l'Université Flinders 2022

---

### Cas 10 : France → Allemagne vs. France → Luxembourg — inadéquation des approbations de qualifications (données 2024)
**Échelle :** Mêmes qualifications professionnelles françaises ; même directive UE 2005/36/CE ; même pays d'origine
**Classificateur source :** ROME v4 français (France Travail)
**Classificateur de destination A :** KldB-2010 allemand (40,3 % de taux d'approbation pour les qualifications françaises, données BIBB 2024)
**Classificateur de destination B :** CNP luxembourgeois (99,8 % de taux d'approbation pour les mêmes qualifications françaises)
**Inadéquation :** Écart de 60 points de pourcentage entre deux États membres de l'UE mettant en œuvre la même directive ; reflète les différences de granularité entre KldB et CNP au niveau à 5 chiffres, exacerbées par le gardiennage des associations professionnelles en Allemagne [42]
**Résultat :** Le corridor France → Allemagne est 60 fois plus susceptible de se solder par un refus que France → Luxembourg, pour des qualifications identiques ; l'IW 2025 estime la pénurie de travailleurs qualifiés en Allemagne à 450 000 tout en bloquant les candidats qualifiés de l'UE [41]
**Source :** ITEM Maastricht Cross-Border Impact Assessment 2025 ; IW Report 08/25 [41, 42]

---

### Cas 11 : Bangladesh → Arabie Saoudite — classification forcée comme travailleuses domestiques (en cours)
**Échelle :** ~800 000 femmes migrantes bangladaises ; classification systématique forcée comme travailleuses domestiques indépendamment de l'expérience professionnelle réelle
**Classificateur source :** BSCO bangladais (basé sur CITP-08 ; 5 387 entrées dans GSCO)
**Classificateur de destination :** SSCO 2024 saoudien (GSCO : 2 738 entrées anglaises, 99,3 % de couverture CITP ; version arabe — 2019 — écart de 5 ans)
**Inadéquation :** Il n'existe pas de pont lisible par machine entre les catégories professionnelles BSCO et la classification SSCO au point d'enregistrement du contrat de travail ; le système de quotas saoudien NITAQAT utilise les codes SSCO — les travailleurs enregistrés sous le mauvais code sont enfermés dans la mauvaise catégorie de quota
**Résultat :** Dégradation professionnelle affectant 800 000 individus ; documenté par l'OIT 2024 [36]
**Pertinence pour GSCO :** BSCO et SSCO 2024 dans GSCO ; le SSCO arabe a un bug d'inversion RTL en attente de correction P0 ; le tableau croisé existe techniquement — échec dans l'application administrative

---

### Cas 12 : Népal → Corée du Sud — file d'attente EPS (2023)
**Échelle :** 143 812 candidats EPS (Employment Permit System) pour 15 800 places disponibles en 2023 ; 2 décès lors des manifestations de décembre 2023 au centre d'examen de Katmandou
**Classificateur source :** NASCO népalais (basé sur CITP-08)
**Classificateur de destination :** KSCO-7 coréen (한국표준직업분류)
**Inadéquation :** L'examen EPS teste la terminologie professionnelle coréenne, non déductible de la mise en correspondance NASCO → CITP-08 ; le KSCO-7 coréen a une granularité différente au niveau à 4 chiffres que la CITP-08 pour les catégories de l'industrie manufacturière et de la construction
**Résultat :** Ratio candidat-à-place de 9:1 ; 2 décès lors des manifestations ; barrière structurelle créant un goulot d'étranglement dangereux
**Source :** Lot sur la migration persan-indo-turc (2026)

---

### Cas 13 : Ouzbékistan → Russie — surqualification massive (en cours)
**Échelle :** 33,3 % des migrants ouzbeks en Russie ont une éducation supérieure ; ~11 % travaillent dans des professions inadéquates = ~220 000 travailleurs surqualifiés simultanément
**Classificateur source :** OKKT ouzbek (O'zbekiston Kasblar Klassifikatori, basé sur CITP-08)
**Classificateur de destination :** OKZ russe (basé sur CITP-08)
**Inadéquation :** Bien que tous deux soient basés sur la CITP-08 et linguistiquement proches (le bilinguisme ouzbek-russe est répandu), l'inadéquation au niveau des sous-codes persiste ; les employeurs russes évitent par défaut le risque lorsque les diplômes ouzbeks ne peuvent pas être vérifiés automatiquement
**Résultat :** ~220 000 travailleurs surqualifiés simultanément ; données OIM citées dans le lot persan-indien
**Source :** Lot sur la migration persan-indo-turc (2026) ; documentation OIM

---

### Cas 14 : Bulgarie → Allemagne — absence de la catégorie « Feldsherin » (2016–2019)
**Échelle :** Les reconnaissances de qualifications d'infirmières bulgares en Allemagne ont triplé, passant de 5 600 à 15 500 (2016–2019) ; la profession bulgare « feldsher » (feldsherin) est absente des systèmes de classification allemands/autrichiens
**Classificateur source :** EKPD bulgare (basé sur CITP-08 ; inclut « feldsher » comme catégorie distincte à 4 chiffres)
**Classificateur de destination :** KldB-2010 allemand (pas de catégorie « Feldscherin » ; le plus proche est « Pflegehilfskraft » — 3 niveaux professionnels en dessous)
**Inadéquation :** La profession est présente dans la source, absente dans la destination → rétrogradation automatique ; réduction de salaire de 400–600 €/mois par infirmière concernée
**Résultat :** Rétrogradation automatique à Pflegehilfskraft ; le Sozialministerium autrichien documente toujours le problème en 2025 ; structurellement, pas transitoire
**Pertinence pour GSCO :** Parallèle structurelle directe avec CI (540 professions non classifiées) et BN (1 381 professions au niveau à 5 chiffres sans table croisée CITP)
**Source :** Lot sur la migration slave (2026) ; documentation du Sozialministerium autrichien 2025

---

### Cas 15 : Ukraine → Pologne — surqualification massive (2022–présent)
**Échelle :** ~1,5 million de réfugiés ukrainiens ; 40 % employés dans le groupe 9 de la CITP, malgré une éducation tertiaire pour la plupart ; 67 % des femmes professionnelles travaillent en dessous de leur niveau de qualification
**Classificateur source :** DKHP ukrainien (basé sur CITP-08)
**Classificateur de destination :** KZiS polonais (basé sur CITP-08)
**Inadéquation :** La correspondance sur la même norme et le même code produit toujours une rétrogradation systématique ; le coût de la nostrification (frais de reconnaissance du diplôme), le fardeau de la garde d'enfants et la barrière linguistique créent ensemble un piège de surqualification que la seule correspondance des codes CITP ne peut résoudre
**Résultat :** Taux de mauvaise classification de 40 % à grande échelle ; structurellement, pas transitoire
**Source :** Lot sur la migration slave (2026) ; statistiques OIM et polonaises du marché du travail

---

### Cas 16 : Biélorussie → Pologne — professionnels de l'informatique (« câbles avant l'entretien ») (2020–2023)
**Échelle :** 20 000 professionnels de l'informatique via le programme accéléré de visas Poland Business Harbour
**Classificateur source :** OKRB-006 biélorusse (CITP 2512 « Développeur de logiciels » mis en correspondance)
**Classificateur de destination :** KZiS polonais (CITP 2512 mis en correspondance — même code)
**Inadéquation :** Le même code CITP dans les deux systèmes ; la reconnaissance par les employeurs persiste car les diplômes biélorusses ne sont pas vérifiés automatiquement dans la base de données polonaise ; les travailleurs signalent 3 à 12 mois de travail déqualifié (« pose de câbles à fibre optique ») avant de trouver un emploi dans l'informatique ; après avoir ajouté une seule entreprise polonaise au CV — 5 entretiens d'embauche en 1 mois
**Résultat :** Transition déqualifiée de 3 à 12 mois, malgré un visa accéléré et les mêmes codes CITP ; révèle que la reconnaissance des qualifications = problème de confiance de l'employeur, pas seulement un problème de correspondance de codes
**Pertinence pour GSCO :** Signal d'autorité de GSCO dans Wikidata (profession approuvée par le registre de l'OIT sans refus) pourrait fonctionner comme un proxy de confiance de l'employeur
**Source :** Lot sur la migration slave (2026)

---

### Cas 17 : Brésil → Portugal — reconnaissance médicale (en cours)
**Échelle :** 57,8 % de taux de rejet des diplômes médicaux brésiliens par l'Ordem dos Médicos portugaise ; Angola 3,4 % de taux de rejet ; Cuba et Guinée-Bissau 0 % de taux de rejet — tous nominalement sous un cadre d'équivalence commun lusophone
**Classificateur source :** CBO brésilien (Classificação Brasileira de Ocupações ; 2 614 entrées dans GSCO)
**Classificateur de destination :** CNP-94 portugais (mis à jour ; fait référence à ESCO UE)
**Inadéquation :** L'Ordem dos Médicos portugais applique des critères substantiels différents aux candidats brésiliens, angolais et PALOP, malgré une langue commune et des structures d'enseignement médical nominalement similaires ; la similitude au niveau des codes ne prédit pas l'approbation
**Résultat :** Inadéquation de 57,8 % contre 3,4 % de taux de rejet ; documenté dans Público et les données de l'Ordem dos Médicos citées dans le lot roman
**Source :** Lot sur la migration en langue romane (2026) ; statistiques annuelles de l'Ordem dos Médicos Portugal

---

### Cas 18 : France — médecins PADHUE (« praticiens associés ») (en cours)
**Échelle :** Plus de 5 000 médecins classés comme « Praticiens à Diplôme Hors Union Européenne » (PADHUE), gagnant 1 450 €/mois contre 4 500 €/mois pour les médecins équivalents formés en France
**Classificateurs sources :** Divers (Afrique, Moyen-Orient, Europe de l'Est, Asie)
**Classificateur de destination :** ROME v4 français (PADHUE = sous-catégorie professionnelle distincte sous « médecin »)
**Inadéquation :** Le système de classification français a une catégorie de rétention permanente, juridiquement distincte du statut complet de « médecin » indépendamment de la compétence réelle ; les médecins PADHUE effectuant un travail clinique identique sont classifiés (et rémunérés) comme une catégorie professionnelle de rang inférieur
**Résultat :** Écart de salaire de 3 050 €/mois par médecin ; 5 000+ personnes concernées ; décrit dans la revue de Ngabirano 2026 comme contribuant au stress psychologique chez les populations immigrées hautement qualifiées [47]
**Source :** Lot sur la migration en langue romane (2026) ; revue systématique de Ngabirano 2026

---

### Cas 19 : Frontière Pays-Bas/Belgique — cas du neurologue ZorgSaam (2025)
**Échelle :** 1 hôpital (ZorgSaam, Terneuzen, Pays-Bas) ; 1 neurologue candidat (Universitair Ziekenhuis Gent, Belgique, ~30 km) ; pénurie aiguë
**Classificateur source :** KBC-ISCO belge (neurologie → CITP 2212)
**Classificateur de destination :** BIG-register néerlandais (neuroloog → code BIG 79)
**Inadéquation :** Le BIG-register exige une procédure d'enregistrement distincte même pour les spécialistes certifiés dans l'UE ; le tableau croisé néerlandais CITP-à-BIG n'est pas lisible par machine ; 30 km, coût de déménagement nul, même directive UE, liberté de circulation de Schengen — la procédure classificatoire retarde néanmoins
**Résultat :** L'hôpital est resté sous-effectif pendant la procédure ; documenté dans l'ITEM Maastricht Cross-Border Impact Assessment 2025 [42]
**Pertinence pour GSCO :** Le cas le plus concis possible — toutes les variables de friction sont minimisées ; l'inadéquation classificatoire persiste néanmoins

---

### Cas 20 : Estonie → Finlande/Allemagne — valeur du registre trilingue (en cours)
**Échelle :** ~180 000 émigrés estoniens (13 % de la population) ; principaux corridors EE→FI, EE→DE, EE→UK
**Classificateur source :** AK-2008 estonien (couverture CITP-4 à 100 % ; trilingue ET/EN/RU ; 3 562 entrées)
**Classificateurs de destination :** CITP-08-fi finnois ; KldB-2010 allemand
**Qualité de la correspondance :** AK-2008 est le seul registre de l'échantillon de 10 pays avec des étiquettes trilingues — permet une correspondance automatique directe avec les systèmes finlandais, allemands et britanniques SOC-2020
**Résultat :** Cas positif ; l'Estonie démontre que l'architecture d'un registre trilingue permet une portabilité quasi automatisée des qualifications ; aucune traduction automatique n'est nécessaire
**Pertinence pour GSCO :** AK-2008 est un « étalon-or » dans le corpus GSCO — brief pays EE ; fenêtre politique : l'Estonie préside le Conseil de l'UE au second semestre 2027

---

### Cas 21 : Lettonie — crise de classification des pensions de la diaspora (2024)
**Échelle :** ~300 000 émigrés lettons (16 % de la population, le taux d'émigration le plus élevé des pays baltes) ; la réforme des retraites lettone de 2024 a introduit des niveaux de cotisation professionnels nécessitant une classification précise d'environ 800 000 comptes de retraite actifs
**Classificateur source :** Klasifikators de professions letton (4 102 entrées, révision 2024 ; zéro étiquette anglaise)
**Classificateurs de destination :** KldB-2010 allemand, SOC-2020 britannique (pour les migrants de retour)
**Inadéquation :** Zéro étiquette anglaise dans le registre letton signifie que les professionnels lettons à l'étranger ne peuvent pas faire correspondre automatiquement leur code de profession aux classificateurs des systèmes de destination ; les droits de retraite étrangers des migrants de retour ne peuvent pas être vérifiés automatiquement par rapport aux niveaux lettons
**Résultat :** La réforme des retraites ne peut pas être appliquée automatiquement à la diaspora retournant des destinations sans tables croisées ; une réévaluation manuelle est nécessaire pour chaque cas ; échelle : potentiellement 300 000 personnes concernées
**Pertinence pour GSCO :** Brief pays LV ; génération d'étiquettes EN assistée par IA pour 4 102 entrées = 15 000 € maintenant contre 150 000 € en 2031

---

### Cas 22 : Mongolie → Corée du Sud — mineurs EPS (en cours)
**Échelle :** ~60 000 travailleurs mongols en Corée du Sud via EPS ; la Mongolie a la taxonomie la plus riche de professions minières dans GSCO (YAMAT-08, 4 844 entrées)
**Classificateur source :** YAMAT-08 mongol (langue mn uniquement ; zéro étiquette mongole dans Wikidata)
**Classificateur de destination :** KSCO-7 coréen
**Inadéquation :** Les sous-spécialités minières dans YAMAT-08 (explosif, spécialiste du décapage, catégories spécifiques d'exploration) n'ont pas d'équivalents directs KSCO-7 ; classés comme « mineur » général (CITP 8111) indépendamment de la spécialisation réelle
**Résultat :** Compétences spécialisées non reconnues ; différence de salaire entre spécialiste et mineur général ; l'analyse GSCO révèle que YAMAT-08 est la taxonomie minière la plus détaillée dans l'ensemble de données — une entrée potentiellement précieuse pour la CITP-28
**Source :** Lot sur la migration en Asie de l'Est (2026) ; brief pays MN

---

### Cas 23 : Cap-Vert — inversion diaspora et population résidente (en cours)
**Échelle :** Diaspora cap-verdienne (~700 000 personnes) dépasse la population résidente (~570 000) ; CNP CV-Rev.1 contient 699 entrées, dernière mise à jour en 2010 (il y a 15 ans)
**Classificateur source :** CNP CV-Rev.1 (portugais ; structure de l'ère CITP-88)
**Classificateurs de destination :** CNP-94 portugais (mis à jour), ROME v4 français
**Inadéquation :** CNP CV-Rev.1 utilise des familles de codes CITP-88 (pas CITP-08) ; la diaspora au Portugal et en France, soumettant des qualifications mises en correspondance avec des codes CITP-88, est reconnue comme obsolète par les systèmes de destination
**Résultat :** Le partenariat UE-Cap-Vert pour la mobilité (2008, prolongé) est menacé en raison de l'obsolescence du classificateur ; le partenaire UE ne peut pas vérifier automatiquement les qualifications sous forme lisible par machine ; coût de correction estimé à 10–15 000 € pour ajouter une table croisée PT CPP-2010
**Source :** Brief pays CV ; analyse de la base de données GSCO

---

### Cas 24 : Arabie Saoudite — scission des versions arabe et anglaise du registre (2019 vs. 2024)
**Échelle :** ~13 millions de ressortissants étrangers en Arabie Saoudite sous le régime du système de quotas NITAQAT, utilisant les codes SSCO ; la conformité NITAQAT est légalement obligatoire pour tous les employeurs
**Classificateur source/destination :** SSCO 2024 (version EN) ; SSCO 2019 (version AR — version linguistique officielle avec 5 ans de retard)
**Inadéquation :** 280 millions de locuteurs arabes ont accès à la version arabe de 2019 ; la version anglaise de 2024 diffère considérablement ; les étiquettes arabes peuvent en outre avoir un bug d'inversion RTL, confirmé dans le registre connexe JSCO (Jordanie)
**Résultat :** Les employeurs et travailleurs arabophones naviguent dans un système de quotas légalement contraignant en utilisant un classificateur vieux de 5 ans ; les violations de NITAQAT entraînent des conséquences pour les licences commerciales
**Pertinence pour GSCO :** Brief pays SA ; bug P0 : registre arabe SA en attente d'audit RTL ; écart de 5 ans entre les versions marqué comme inadéquation de version, nécessitant une correction urgente

---

### Cas 25 : Côte d'Ivoire — secteurs professionnels entiers non classifiés (2016)
**Échelle :** 540 entrées de professions dans NMP-CI 2016 ne couvrent que le secteur artisanal/manuel ; les professions de la santé, du droit, de la finance et de l'économie du savoir n'ont pas d'entrée dans le classificateur national ; CI a 0 % de couverture de table croisée CITP
**Classificateur source :** NMP-CI 2016 (codes nationaux à 9 chiffres ; pas de champ CITP-4)
**Classificateurs de destination :** ROME v4 français, ESCO v1.2.1
**Inadéquation :** Un médecin, un avocat ou un ingénieur logiciel de Côte d'Ivoire tentant de présenter des qualifications pour reconnaissance dans l'UE n'a pas de code national auquel se référer ; NMP-CI ne les contient tout simplement pas
**Résultat :** Les professionnels de tout le secteur de l'économie du savoir de CI sont effectivement sans statut du point de vue de la classification aux fins de reconnaissance internationale des qualifications
**Pertinence pour GSCO :** Brief pays CI ; paradoxe 0/N dans l'API ; développement d'une table croisée CITP estimé à 40–60 000 € ; les codes du secteur du cacao de CI représentent une entrée unique pour la CITP-28

---

### Cas 26 : Brunei — 1 381 professions sans carte CITP (2011)
**Échelle :** 1 381 noms de professions dans BDSOC 2011 (15 ans) ; la stratégie nationale de développement du Brunei Wawasan 2035 liste de nouveaux secteurs prioritaires complètement absents du BDSOC
**Classificateur source :** BDSOC 2011 (codes à 5 chiffres ; pas de table croisée CITP ; probablement déductible automatiquement par troncature des 4 premiers chiffres — correction P0 en attente)
**Classificateurs de destination :** MASCO malaisien (voisin le plus proche) ; ESCO v1.2.1
**Inadéquation :** 1 381 noms de professions se retrouvent sans code CITP car le pipeline GSCO n'a pas encore appliqué la déduction automatique ; si corrigé, BN pourrait atteindre une couverture CITP significative
**Résultat :** L'ensemble du registre brunéien est actuellement invisible pour toute requête basée sur la CITP ; la correction est une tâche d'ingénierie (estimation : 2–4 heures), pas une lacune dans les données
**Pertinence pour GSCO :** Brief pays BN ; paradoxe 0/N ; correction P0-02 en attente ; « la correction la plus facile du corpus » — BN est à 2 heures d'ingénierie d'une couverture CITP partielle

---

### Cas 27 : Bosnie — métadonnées fantômes rendant les données invisibles (en cours)
**Échelle :** KZBiH-08 a 4 246 entrées ; 98,4 % de couverture CITP ; source principale pour les reconnaissances allemandes de qualifications d'infirmières (~2 300/an) ; le registre fantôme ba_error_stub crée des valeurs nulles dans l'API de comparaison pour les 589 codes malgré l'existence de données réelles
**Classificateur source :** KZBiH-08 (« Medicinska sestra » = CITP 2221)
**Utilisation de destination :** Le chapitre 19 de l'acquis communautaire (marché du travail) exige des données de couverture CITP démontrables ; l'API de comparaison montre 589 nulls en raison d'une inadéquation du modèle de données, et non d'une lacune dans les données
**Inadéquation :** Technique (bug de métadonnées), pas substantielle ; BA a l'une des couvertures CITP les plus élevées de l'ensemble de données ; le bug le présente comme ayant zéro
**Résultat :** Les présentations ministérielles des données BA montrent « 0 codes » dans la vue de comparaison — une distorsion grave pour l'acquis communautaire ; la correction consiste à ajuster le modèle de données (priorité P1)
**Pertinence pour GSCO :** Brief pays BA ; correction P0 ba_error_stub ; date limite du chapitre 19 de l'acquis communautaire 2025–2027

---

### Cas 28 : Euro-région Meuse-Rhin — absurdité du test de langue pour les enseignants (2025)
**Échelle :** Marché du travail transfrontalier des enseignants dans la région trinationale Pays-Bas/Belgique/Allemagne (Aix-la-Chapelle/Liège/Maastricht) ; documenté dans l'ITEM 2025 Cross-Border Impact Assessment
**Classificateur source :** Certification allemande des enseignants KMK (locuteur natif allemand ; diplôme universitaire allemand)
**Classificateur de destination :** Équivalent néerlandais/belge (exige un certificat de langue allemande distinct pour l'enseignement transfrontalier)
**Inadéquation :** Un locuteur natif allemand titulaire d'une qualification universitaire allemande est obligé de passer une certification distincte de maîtrise de la langue allemande pour enseigner en allemand dans une école à 15 km de la frontière ; la compétence professionnelle (enseignement, CITP 2320) est reconnue ; le médium linguistique d'enseignement est traité comme une classification distincte
**Résultat :** Les postes d'enseignant restent vacants dans la région frontalière malgré la disponibilité de candidats qualifiés ; absurdité systémique documentée même au sein de l'espace Schengen [42]
**Pertinence pour GSCO :** Cas ITEM RPT-02 ; illustre que la friction classificatoire persiste même lorsque les codes CITP correspondent parfaitement

---

### Cas 29 : Mexique → États-Unis — code de visa TN « Médecin (enseignement uniquement) » (ALENA/AEUMC, en cours)
**Échelle :** Structurellement, concerne tous les médecins mexicains cherchant un statut non immigrant TN (Trade NAFTA) pour travailler dans le domaine médical aux États-Unis
**Classificateur source :** SINCO mexicain (686 entrées dans GSCO ; « médico general » → CITP 2212)
**Classificateur de destination :** SOC américain (29-1211 Médecins) ; mais la classification selon le traité TN utilise le SOC 19-1042 « Chercheurs médicaux »
**Inadéquation :** La catégorie de visa TN ALENA « Médecin » est légalement limitée à « l'enseignement ou la recherche uniquement » ; la pratique clinique nécessite une catégorie de visa différente (H-1B) avec un code différent ; le code du médecin mexicain correspond à la CITP 2212 et au SOC américain 29-1211, mais le code du traité TN — 19-1042 — est délibérément différent pour empêcher la concurrence clinique
**Résultat :** Les médecins mexicains sont classés comme « chercheurs médicaux » à des fins d'immigration ; la pratique clinique est bloquée sous TN malgré l'équivalence professionnelle ; inadéquation politique structurelle intégrée dans le code du traité
**Source :** Lot sur la migration en langue romane (2026) ; directives de la catégorie TN des services de citoyenneté et d'immigration des États-Unis

---

### Cas 30 : Russie — OK 016-2025 : écart de classification de 30 ans (2025)
**Échelle :** Le nouveau classificateur national des professions russe OK 016-2025, remplaçant la version de 1994, introduit des codes pour les opérateurs IA, les spécialistes de la cybersécurité, les opérateurs de drones et plus de 40 autres nouveaux codes professionnels de l'ère numérique après une interruption de 31 ans
**Classificateur source (hérité) :** OKPDR (1994) — pas d'IA, pas de cybersécurité, pas de codes pour les drones
**Classificateur mis à jour :** OK 016-2025 — ajoute ces catégories ; continue également d'utiliser certaines familles de codes de l'ère CITP-88 en parallèle
**Inadéquation :** 31 ans d'évolution du marché du travail classifiés dans des paniers hérités ; les travailleurs dans l'IA, la cybersécurité et l'économie des plateformes sont officiellement classifiés comme des catégories connexes de 1994 dans tous les systèmes administratifs (retraite, impôts, assurance) jusqu'en janvier 2025
**Résultat :** Reclassification rétroactive nécessaire dans tous les systèmes administratifs en aval ; RPT-14 documente cela comme l'événement le plus important de reclassement professionnel post-soviétique [37]
**Pertinence pour GSCO :** Confirme que même les grandes économies connaissent des lacunes de classification décennales ; GSCO capture OK 016-2025 comme un nouveau registre ; fournit un pont vers le hub CITP-08, assurant la compatibilité en aval

---

### Cas 31–120 : Tableau de référence compact

Les cas ci-dessous — tirés du même effort de recherche en 7 lots que les cas 1 à 30 — sont présentés de manière compacte pour plus d'exhaustivité. La bibliothèque interactive sur site à <https://gsco.io/cases> fournit le texte intégral de chaque cas avec un lien vers la source primaire.

*Note pour le lecteur francophone : les chiffres spécifiques (demandes, pourcentages, euros), les références primaires et les noms exacts des agences dans le tableau ci-dessous sont conservés en anglais original pour éviter les distorsions lors de la traduction des statistiques clés et des noms des agences. Un commentaire français complet sur chaque cas est disponible via `/cases?country=ISO` sur le site de GSCO. Les en-têtes de colonne sont traduits ci-dessous :*

**En-têtes :** # | Pays | Titre (année) | Échelle | Inadéquation | Résultat | Source


| # | Pays | Titre (année) | Échelle | Inadéquation | Résultat | Source |
| 31 | GB / IT | Professionnels italiens au Royaume-Uni post-Brexit — Reconnaissance mutuelle terminée, système automatique de l'UE perdu *(2021–2024)* | ~700 000 Italiens au Royaume-Uni (estimation pré-Brexit ; Il Fatto Quotidiano 2023 note que le chiffre réel est 3 fois supérieur aux chiffres officiels de l'Istat). Royaume-Uni… | 1. *Architecture* : La laurea magistrale italienne (5 ans, accréditée par la CNAPPC) n'est plus automatiquement reconnue. L'ARB exige la Partie 3… | L'ALECA (Accord de commerce et de coopération) UE-Royaume-Uni n'inclut pas la reconnaissance mutuelle des qualifications professionnelles… | [lien](https://www.architecture.com/knowledge-and-resources/resources-landing-page/brexit-recognition-of-professional-qualifications) |
| 32 | GB / PL / UK | Travailleurs polonais au Royaume-Uni — Surqualification massive *(2004–2019)* | ~900 000 travailleurs polonais au Royaume-Uni à son apogée (2014–2020) ; Ośrodek Badań nad Migracjami UW (Centre de recherche sur les migrations, Université de Varsovie) : 30 %… | Pour les professions réglementées (médecine, droit, ingénierie) : la reconnaissance automatique de l'UE existait mais nécessitait une inscription administrative (GMC,… | Le Sobieski Institute a estimé que 900 000 travailleurs polonais entre 2014 et 2020 ont généré 64 milliards de livres sterling pour l'économie britannique, tandis que… | [lien](https://polishexpress.eu/polacy-skazani-na-zmywak-mamy-dyplomy-a-pracujemy-ponizej-kwalifikacji23/;) |
| 33 | DE / IT | Médecins et professionnels qualifiés italiens émigrant en Allemagne — Limbo « Berufserlaubnis » et écart de salaire de 50 % *(2008–2024)* | 1 637 médecins italiens sans citoyenneté allemande travaillant en Allemagne (fin 2022, données Bundesärztekammer/BÄK). 155 732 Italiens au total… | 1. *Médecine — piège Berufserlaubnis* : Les médecins italiens de l'UE arrivant en Allemagne ont droit à l'Approbation en vertu de la Dir 2005/36/CE mais… | 180 000 professionnels de la santé italiens ont émigré entre 2000 et 2022 (Quotidiano Sanità, 2023). BÄK allemand : Italiens… | [lien](https://www.ilfattoquotidiano.it/2025/11/11/fuga-cervelli-espatri-aumento-38-percento-laureati-fuga-mezzogiorno/8191929/) |
| 34 | BE / FR / GB / GH / IN / NG / NL / PH / SN | Infirmières africaines dans l'UE — Déqualification et retour à la case départ *(2015–2024)* | Revue de portée « African nurses on the move » (PMC11929199, 2024) couvre le Nigeria, le Ghana, le Sénégal, le Cameroun → Royaume-Uni, France, Belgique,… | Les infirmières africaines hors UE sont classées dans la bande la plus basse (Bande 5) indépendamment de leur spécialité antérieure (par exemple, USI, urgences) car les systèmes britanniques/européens exigent… | 2 à 10 ans pour une reconnaissance complète. De nombreuses infirmières africaines avec plus de 10 ans d'expérience en USI travaillent comme aides-soignantes… | PMC « African nurses on the move : scoping review » (2024, PMC11929199) ; PMC… |
| 35 | DE / UA | Médecins ukrainiens en Allemagne — File d'attente pour l'Approbation *(2022–2024)* | Plus de 1 674 médecins ukrainiens ont demandé l'Approbation (licence médicale complète) après février 2022 ; seulement 187 autorisés à exercer mi-2023 ; ~1 400… | L'Allemagne exige une Approbation complète pour la pratique médicale indépendante. Les médecins ukrainiens sans Approbation ne peuvent travailler que sous… | 56 % des cas approuvés de reconnaissance professionnelle ukrainienne (professions réglementées, 2024) ont nécessité… | [lien](https://www.bibb.de/de/213410.php;) |
| 36 | BG / GB / UK | Infirmières bulgares au Royaume-Uni — Paradoxe de la reconnaissance des diplômes et exode massif *(2023–2024)* | En 2023 : 435 des 622 médecins (70 %) ayant rejoint le personnel du NHS en un an étaient diplômés d'écoles de médecine bulgares. La Bulgarie est maintenant la première source… | Avant le Brexit : les infirmières bulgares diplômées de l'UE étaient automatiquement reconnues en vertu de la Dir 2005/36/CE — voie de reconnaissance fluide. Après le Brexit en 2021 : les médecins bulgares maintenant… | Le secrétaire à la Santé du Royaume-Uni, Wes Streeting, a averti que le NHS « dépend trop des médecins d'autres pays » — en 2023, 70 %… | pielegniarki.info.pl « Ogólnopolska Gazeta Pielęgniarek i Położnych nr 1/2016 —… |
| 37 | AT / BA / MK / RS / WB | Infirmières croates/serbes en Autriche — Fossé du système à trois niveaux *(2019–2024)* | L'Autriche reçoit un nombre important de professionnels de santé des anciennes républiques yougoslaves. Pénurie d'infirmières reconnue : l'Autriche a besoin de 75 000 aides-soignants supplémentaires… | ossaw.at (portail autrichien en langue serbe) : la reconnaissance (Nostrifikation) du diplôme serbe « diplomirana medicinska sestra » en Autriche nécessite… | Processus de reconnaissance : 6 à 18 mois. Pendant ce temps : emploi comme aide-soignante à 2 100–2 400 € brut contre l'objectif DGKP… | [lien](https://www.ossaw.at/nostrifikacija-diploma-diplomirane-medicinske-sestre-i-tehnicari-iz-srbije-bosne-i-hercegovine-makedonije-i-crne-gore/;) |
| 38 | CA / FR / US | Enseignants formés à l'étranger au Canada et aux États-Unis — Fragmentation de la certification *(2016–2024)* | Canada : pénurie persistante d'enseignants en immersion française, STEM, éducation spécialisée. Les enseignants formés à l'étranger (ITT) sont confrontés à une double… | Le diplôme d'un enseignant formé à l'étranger est évalué à des fins d'immigration par WES — peut recevoir « équivalent à un baccalauréat canadien +… | Borgen Project « The Reality of Immigrant Credential Recognition in Canada » : la reconnaissance des diplômes est « complexe… | Borgen Project « Reality of Immigrant Credential Recognition in Canada » (2021) ;… |
| 39 | CA | Médecins formés à l'étranger au Canada — 36 % travaillent réellement dans leur domaine *(2019–2024)* | Canada. Seulement 36,5 % des infirmières formées à l'étranger et 41,1 % des médecins formés à l'étranger travaillaient dans leurs professions connexes (C.D. Howe… | Les diplômes médicaux étrangers sont évalués indépendamment par les collèges provinciaux — pas de norme nationale. Un médecin agréé dans une province peut… | C.D. Howe : immigrants diplômés universitaires, taux de surqualification de 12 % en STEM — près de 2 fois le taux des non-immigrants.… | C.D. Howe Institute « Harnessing Immigrant Talent » (2024) ; ESDC « Evaluation of… |
| 40 | BG / GB / UK | Médecins bulgares au Royaume-Uni — Exode massif, paradoxe de la reconnaissance des diplômes *(2023–2024)* | En 2023 : 435 des 622 médecins (70 %) ayant rejoint le personnel du NHS en un an étaient diplômés d'écoles de médecine bulgares. La Bulgarie est maintenant la première source… | Avant le Brexit : les diplômes de l'UE des médecins bulgares étaient automatiquement reconnus en vertu de la Dir 2005/36/CE — voie de reconnaissance fluide. Après le Brexit en 2021 : les médecins bulgares maintenant… | Le secrétaire à la Santé du Royaume-Uni, Wes Streeting, a averti que le NHS « dépend trop des médecins d'autres pays » — en 2023, 70 %… | [lien](https://btvnovinite.bg/svetut/70-ot-lekarite-zapochnali-rabota-vav-velikobritanija-prez-2023-g-sa-zavarshili-meditsina-v-balgarija.html;) |
| 41 | BD / NP / QA | Travailleurs népalais et bangladais au Qatar — Substitution systématique d'emploi *(201