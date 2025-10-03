# Elastic Stack

Data pre spracovanie pochádzajú všetky z jedného zdroja, konkrétne z platformy [Kaggle](https://www.kaggle.com/), ktorá je považovaná za najväčší zdroj otvorených dát od výmyslu sveta. Vybral som si datasety, ktoré spadajú pod tému životného štýlu a miest, kde sa ľudia môžu ísť najesť, ísť na rande, stráviť čas s rodinou, alebo sa zrelaxovať pri dobrej káve po práci či cvičení. Hlavným cieľom týchto dát je nájsť zaujímavé korelácie a vizualizácie medzi počtom pobočiek McDonald's a Starbucks na celom svete a následne porovnať najznámejšie veľkomestá a ich údaje, ako sú obezita, cena vody, alebo počet miest, kde sa ľudia môžu stretnúť a dať si niečo dobré.

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
