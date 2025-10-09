# Elastic Stack (ELK) - Analýza a vizualizácia dát

Tento projekt demonštruje kompletný ELK stack (Elasticsearch, Logstash, Kibana) na analýze geografických a lifestyle dát z celého sveta.

## 🎯 Cieľ projektu

- Analýza pobočiek McDonald's a Starbucks po celom svete
- Korelácie medzi fast food reťazcami a lifestyle indikátormi
- Geografické vizualizácie a mapy
- Business intelligence a market research

## 🏗 Architektúra

### ELK Stack
- **Elasticsearch 7.10.0** - vyhľadávací engine a databáza
- **Logstash 7.10.0** - spracovanie a transformácia dát
- **Kibana 7.10.0** - vizualizácia a dashboarding

### Infraštruktúra
- **Docker Compose** - kontajnerizácia
- **Networking** - izolovaná sieť pre ELK
- **Volumes** - perzistencia dát a konfigurácie

## 📊 Datasety

### 1. Starbucks Stores
- **Zdroj**: [Kaggle](https://www.kaggle.com/datasets/starbucks/store-locations)
- **Počet záznamov**: 16,000+ pobočiek
- **Pokrytie**: Celosvetové
- **Kľúčové polia**: city, country, latitude, longitude, timezone

### 2. McDonald's Stores  
- **Zdroj**: [Kaggle](https://www.kaggle.com/datasets/forveryou/mcdonalds-stores-data)
- **Počet záznamov**: 40,000+ pobočiek
- **Pokrytie**: 90 krajín
- **Kľúčové polia**: city, country, address, services, runhours

### 3. Healthy Lifestyle Cities
- **Zdroj**: [Kaggle](https://www.kaggle.com/datasets/pawarmukesh/healthy-life-style-city-2021)
- **Počet záznamov**: 44 najväčších miest
- **Kľúčové polia**: city, happiness, obesity, working hours, gym costs

## 🚀 Spustenie

### 1. Spustenie ELK stacku
```bash
docker compose up -d
```

### 2. Import dát cez Logstash
```bash
# Spustenie pipeline pre každý dataset
docker exec -it logstash bash
# Pipelines sa spustia automaticky
```

### 3. Prístup k službám
- **Kibana**: http://localhost:5601
- **Elasticsearch**: http://localhost:9200
- **Logstash**: http://localhost:9600

## 📈 Vizualizácie v Kibane

### 1. Geografické mapy
- **McDonald's vs Starbucks v USA** - porovnanie rozloženia
- **Heatmapa McDonald's na Slovensku** - koncentrácia pobočiek
- **Celosvetové rozloženie** - globálne pokrytie

### 2. Analytické grafy
- **Počet pobočiek v mestách** - porovnanie konkurencie
- **Lifestyle korelácie** - vzťah medzi fast food a zdravím
- **Working hours vs Happiness** - work-life balance analýza

### 3. Business intelligence
- **Top 5 US cities** - najlepšie trhy
- **Takeout places analysis** - trhové príležitosti
- **Obesity vs Fast Food** - zdravotné korelácie

**Celkovo**: 8 komplexných vizualizácií

## 🔧 Konfigurácia

### Elasticsearch
- **Port**: 9200, 9300
- **Memory**: 1GB heap
- **Health checks**: Automatické monitorovanie

### Logstash
- **Pipelines**: 3 samostatné pipeline pre každý dataset
- **Templates**: Index templates pre správne mapovanie
- **Data processing**: CSV parsing, geo_point creation

### Kibana
- **Port**: 5601
- **Index patterns**: Automatické vytvorenie
- **Dashboards**: Predpripravené vizualizácie

## 📊 Výsledky analýzy

### Kľúčové zistenia
- **Geografické koncentrácie**: Fast food reťazce sa sústredia v urbanizovaných oblastiach
- **Lifestyle korelácie**: Mestá s viac outdoor aktivitami majú menej fast food pobočiek
- **Market opportunities**: Identifikované nedostatočne pokryté trhy
- **Health correlations**: Korelácia medzi fast food a obezitou

### Business insights
- **Expansion opportunities**: Potenciálne lokality pre nové pobočky
- **Competition analysis**: Porovnanie McDonald's vs Starbucks
- **Market saturation**: Analýza preplnenosti trhov
- **Consumer behavior**: Vzťah medzi lifestyle a spotrebou

## 📁 Štruktúra projektu

```
2 - Elastic Stack/
├── docker-compose.yml          # ELK stack konfigurácia
├── elasticsearch/config/       # Elasticsearch nastavenia
├── logstash/
│   ├── config/                # Logstash konfigurácia
│   ├── pipeline/              # Data processing pipelines
│   ├── template/              # Index templates
│   └── data/                  # CSV datasety
├── kibana/config/             # Kibana nastavenia
├── results/                   # Exportované vizualizácie
│   ├── assets/               # Screenshots grafov
│   └── queries/              # Kibana queries
└── README.md                 # Tento súbor
```

## 📚 Dokumentácia

- **HOWTO.md** - Detailné inštrukcie
- **results/README.md** - Popis všetkých vizualizácií
- **results/queries/** - Kibana queries a analýzy

## 🔗 Odkazy

- [Elasticsearch dokumentácia](https://www.elastic.co/guide/en/elasticsearch/reference/7.10/)
- [Kibana dokumentácia](https://www.elastic.co/guide/en/kibana/7.10/)
- [Logstash dokumentácia](https://www.elastic.co/guide/en/logstash/7.10/)
- [Kaggle datasety](https://www.kaggle.com/)

## Starbucks stores dataset

### Popis datasetu

Dáta o pobočkách Starbucks pochádzajú zo zdroja Kaggle a sú uložené v CSV formáte, ktorý obsahuje viac ako 16 000 záznamov o pobočkách tejto kaviarenskej siete rozmiestnených po celom svete.

Pôvodný dataset obsahoval množstvo záznamov s chýbajúcimi alebo nezmyselnými údajmi, ako napríklad názov mesta alebo geografické súradnice. Preto bola najprv uskutočnená dôkladná čistka dát pomocou Python skriptu, ktorý načítal všetky dáta a odstraňoval tie, ktoré boli neúplné. Okrem toho boli upravené názvy krajín, ako napríklad zmena skratky 'US' na plný názov 'United States', čo zjednodušuje filtrovanie a vizualizáciu dát.

Dataset obsahuje stĺpce ako `city` (mesto), ktorý slúži ako hlavný identifikátor všetkých troch datasetov a umožňuje korelácie a vizualizácie naprieč všetkými dátami. Dáta o polohe sú označené stĺpcami `latitude` a `longitude`, `timezone` (časová zóna, v ktorej sa daný Starbucks nachádza) a `country` (krajina, pre lepšie filtrovanie a vizualizáciu pobočiek, napríklad v Spojených štátoch). Sú tu tiež údaje o vlastníkovi pobočky, ako `brand`, `store number`, `store name`, `ownership type`, `phone number`, a adresné údaje ako `street address`, `state/province`, `postcode`.

Údaje v CSV súbore sú oddelené bodkočiarkou `(;)` pre lepšiu orientáciu a mapovanie. Pokiaľ ide o typy údajov, všetky sú mapované ako keyword pre jednoduchšiu manipuláciu a mapovanie. Ako posledný údaj bol vytvorený atribút `location`, ktorý je dátového typu `geo_point` a je vytvorený z `latitude` a `longitude`. Tento atribút sa využíva pre vizualizácie v Kibane na mapách.

## Mcdonalds stores dataset

### Popis datasetu

Dáta o pobočkách McDonald's pochádzajú z najväčšej rýchloobčerstvovacej siete na svete, ktorá denne obsluhuje viac ako 69 miliónov zákazníkov vo viac ako 40 000 pobočkách rozmiestnených v 90 krajinách, ako bolo zaznamenané v roku 2022. Tento dataset zahŕňa záznam o každej pobočke McDonald's aktuálne k septembru 2023.

Dáta boli získané z webstránky pre vyhľadávanie pobočiek McDonald's každej krajiny pomocou Python skriptu, ktorý automatizovane scrapoval informácie. Dataset je uložený v CSV formáte a pred spracovaním bol podrobený dôkladnej čistke. Následne som tento upravený dataset prebral zo stránky kaggle a urobil som druhé čistenie dát aby zodpovedali mojim potrebám.

Pôvodný dataset obsahoval stĺpec `store_id`, ktorý bol odstránený, keďže spoločným identifikátorom pre všetky tri datasety je stĺpec `city`. Okrem toho bolo veľa hodnôt v datasete označených ako ???, ktoré boli tiež odstránené, aby sa zabezpečila kvalita a presnosť dát.

Dataset obsahuje nasledujúce stĺpce city (Mesto, kde sa pobočka nachádza, slúži ako hlavný identifikátor), `name` (Názov pobočky), `country` (Krajina, v ktorej sa pobočka nachádza),`subdivision` (Regionálne rozdelenie krajin,napríklad štát alebo provincia), `address` (Kompletná adresa pobočky), `postcode` (Poštový kód lokality), `telephone` (Telefónne číslo pobočky), `runhours` (Prevádzkové hodiny),`latitude` a `longitude` (Zemepisné súradnice pobočky, na základe ktorých je vytvorený atribút `location` pre geografické mapovanie) `services` (Popis služieb ponúkaných pobočkou ako mcdrive alebo mccafe).

Údaje sú v CSV súbore oddelené bodkočiarkou `(;)` a všetky textové polia sú spracované tak, aby poskytovali maximálnu možnú mieru presnosti a relevancie pre analýzy a vizualizácie v aplikáciách ako Kibana, čo umožňuje efektívne vyhľadávanie a filtrovanie podľa rôznych atribútov.

## Healthylifestyle dataset

Dataset zdravého životného štýlu v mestách

### Popis datasetu

Tento dataset obsahuje informácie o 44 najväčších a najznámejších mestách na svete, ktoré sú známe svojím zdravým životným štýlom. Údaje boli získané z platformy Kaggle a sú určené pre klastrovanie miest podľa zdravého životného štýlu v roku 2021, ako aj pre zlepšenie štatistických analýz. Dataset slúžil ako doplnkový dataset k datasetom Starbucks a McDonald's pre lepšie vizualizácie

Údaje boli pôvodne získané zo zdroja Kaggle a boli upravené pre odstránenie znakov libry (£) z hodnôt v atribútoch cost of a bottle of water (City) a cost of a monthly gym membership (City), aby bolo možné dáta správne indexovať a vizualizovať v Kibane. Tieto úpravy zabezpečili, že všetky numerické údaje sú korektne formátované a pripravené pre analytické účely.

Dataset sa skladá z `city` co je názov mesta a slúži ako identifikátor záznamu v datasete. Tento atribút je typu `keyword`, čo umožňuje efektívne vyhľadávanie podľa názvu mesta. `rank` uvádza hodnotenie zdravého životného štýlu priradené mestu a je typu `integer`.
`sunshine hours (City)` predstavuje počet slnečných hodín v meste a je typu `integer`. `cost of a bottle of water (City)` označuje cenu fľaše vody v meste a je typu `float`. `obesity levels (Country)` ukazuje úroveň obezity v danej krajine a je typu `float`. `life expectancy (years) (Country)` informuje o priemernej dĺžke života v krajine a je typu `float`.
`pollution (Index score) (City)` uvádza index znečistenia v meste a je typu `float`. `annual avg. hours worked` predstavuje priemerný počet odpracovaných hodín za rok a je typu `integer`. `happiness levels (Country)` označuje úroveň šťastia v krajine a je typu `float`. `outdoor activities (City)` uvádza počet vonkajších aktivít dostupných v meste a je typu `integer`. `number of take out places (City)` informuje o počte miest na jedlo s sebou v meste a je typu `integer`. `cost of a monthly gym membership (City)` označuje cenu mesačného členstva v posilovni v meste a je typu `float`.

### Zdroje

-   [starbucks](https://www.kaggle.com/datasets/starbucks/store-locations?select=directory.csv)
-   [mcdonalds](https://www.kaggle.com/datasets/forveryou/mcdonalds-stores-data)
-   [healthylifestyle_data](https://www.kaggle.com/datasets/pawarmukesh/healthy-life-style-city-2021)

## Závěr

Z nájdených dát môžeme vytvoriť zmysluplné vizualizácie týkajúce sa polohy jednotlivých pobočiek McDonald's a Starbucks v rôznych krajinách a mestách. Tieto vizualizácie nám umožnia vyhodnotiť, kde by bolo najlepšie rozbehnúť novú pobočku alebo kde je najmenšia konkurencia. Súčasne, vďaka dátam o životnom štýle, môžeme preskúmať, aký vplyv má počet týchto pobočiek v jednotlivých veľkomestách na faktory ako obezita, úroveň šťastia obyvateľov alebo cenu mesačného predplatného do fitness centier.

Tieto analýzy nám môžu poskytnúť hlbší vhľad do toho, ako lokalizácia rýchloobčerstvovacích reťazcov ovplyvňuje mestské prostredie a životný štýl jeho obyvateľov. Môžu tiež napomôcť mestským plánovačom a podnikateľom v rozhodovaní o strategických umiestneniach nových pobočiek na základe existujúcej konkurencie a preferencií spotrebiteľov. Okrem toho, porozumenie vzťahom medzi prítomnosťou fast foodov a indikátormi verejného zdravia môže pomôcť formovať verejné zdravotné iniciatívy a marketingové stratégie zamerané na zlepšenie životného štýlu obyvateľov.
