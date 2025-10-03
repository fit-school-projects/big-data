# Vizualizace dat - prezentace výsledků

Vďaka vizualizačnému nástroju Kibana môžeme pekným spôsobom zobraziť korelácie a zaujímavé pozorovania v datasetoch týkajúcich sa pobočiek McDonald's, Starbucks a životného štýlu veľkomiest. V tejto sekcii sa pozrieme na 8 rôznych vizualizácií a výsledkov danej dátovej analýzy.

## Vizualizace 1

![Vizualizacia 1](assets/mcs_starbies_US_map.png?raw=true "Vizualizacia 1")

Ako prvá vizualizácia je ukážka pobočiek jednotlivých McDonald's a Starbucks v Spojených štátoch a ich zaujímavé rozprestrenie s veľkej časti hlavne na východnom pobreží. Pri tvorbe tejto mapy sme jednotlivé výsledky odčlenili farbami, kde modrá značí McDonald's a zelená Starbucks. Ďalej sme dáta z datasetov vyfiltrovali na základe atribútu `country` = `United States`, aby sme zamedzili zobrazeniu aj nežiaducich dát.

## Vizualizace 2

![Vizualizacia 2](assets/mcs_vs_starbucks_graph_US_cities.png?raw=true "Vizualizacia 2")

Na tomto grafe môžeme vidieť počet pobočiek McDonald's v porovnaní so Starbucks v jednotlivých mestách USA. Graf slúži k lepšej predstave a ako pomôcka k prvému grafu, kde sú práve tieto pobočky zobrazené na mape. Modrá farba udáva počet McDonald's a zelená počet Starbucks, pričom na x-ovej osi je názov mesta a na y-ovej osi je počet.

## Vizualizace 3

![Vizualizacia 3](assets/food_vs_sport_facilities_top_cities_world.png?raw=true "Vizualizacia 3")

Porovnanie počtu podnikov McDonald's a Starbucks vo veľkých známych mestách s priemernou cenou mesačného predplatného do fitness centier a počtom voľnočasových outdoorových aktivít ukazuje, že mestá s menším počtom pobočiek fast food reťazca McDonald's alebo kaviarní Starbucks majú oveľa viac outdoorových aktivít. Z toho môžeme predpokladať, že reťazce s rýchlym občerstvením majú v mestách s veľa možnosťami na trávenie času vonku menšiu šancu na úspech a obyvatelia ich nevyhľadávajú.

## Vizualizace 4

![Vizualizacia 4](assets/takeout_places_top_5_US_cities.png?raw=true "Vizualizacia 4")

Na tomto grafe vidíme porovnanie počtu všetkých možných takeout miest, kde si ľudia môžu vyraziť a dať niečo rýchle, s reálnym počtom McDonald's a Starbucks v danom meste. Vidíme, že aj napriek veľkému počtu týchto populárnych reťazcov s rýchlym občerstvením obyvatelia miest ako New York alebo LA majú oveľa viac v obľube iné reťazce. Y-ová os označuje počet miest a x-ová top 5 US miest, na ktorých bola daná analýza vytvorená. Bol použitý filter podľa názvu mesta (`city`).

## Vizualizace 5

![Vizualizacia 5](assets/heatmap_mcs_slovakia.png?raw=true "Vizualizacia 5")

Vizualizácia opisuje počet a lokalitu pobočiek McDonald's na Slovensku, spolu s údajmi ako otváracie hodiny, služby, ktoré sú ponúkané na danej lokalite, a adresy, kde sa daná pobočka nachádza. McDonaldy sú zobrazené pomocou heatmapy, kde najintenzívnejšia zelená farba označuje oblasti s najvyšším počtom pobočiek. Zároveň je každá pobočka označená modro-čiernym tooltipom, ktorý poskytuje ďalšie informácie. Táto mapa umožňuje rýchly prehľad o rozložení a dostupnosti služieb tohoto reťazca v rôznych častiach krajiny.

## Vizualizace 6

![Vizualizacia 6](assets/mcs_slovakia_location_table.png?raw=true "Vizualizacia 6")

Táto tabuľka slúži ako pomocná tabuľka údajov všetkých pobočiek McDonald's na Slovensku, spolu s konkrétnou nadmorskou výškou a šírkou pre lepší prehľad a vyhľadávanie. Dáta boli rovnako filtrované podľa krajiny (`country equals Slovakia`).

## Vizualizace 7

![Vizualizacia 7](assets/cities_happiness_vs_workinghours.png?raw=true "Vizualizacia 7")

Na tomto kruhovom grafe môžeme vidieť koreláciu medzi priemerným počtom odpracovaných hodín ročne obyvateľstvom miest na pravej strane a úrovňou šťastia. Vidíme, že mestá, kde obyvatelia menej pracujú, sú oveľa šťastnejší. Dáta pochádzajú z datasetu o životnom štýle, z ktorého bolo náhodne vyfiltrovaných 10 miest, aby mal graf aj nejakú výpovednú hodnotu.

## Vizualizace 8

![Vizualizacia 8](assets/avg_takeout_places_number.png?raw=true "Vizualizacia 8")

Priemerný počet miest na rýchle občerstvenie v najpopulárnejších mestách sveta, kde je úroveň obezity v krajine medzi 20 a 30 %. Na získanie týchto údajov bolo použité filtrovanie podľa úrovne obezity (`obesity level`) v rozsahu 20 až 30 % a výsledné čísla boli zaokrúhlené na celé čísla. Údaje pochádzajú z datasetu o zdravom životnom štýle.
