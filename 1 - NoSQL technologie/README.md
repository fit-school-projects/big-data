# MongoDB

### Obecné chování

NoSQL databázy boli vyvinuté koncom 21. storočia so zameraním na škálovanie, rýchle dotazy, umožňujúce časté zmeny v aplikácií a zjednodušenie programovania pre vývojárov.
MongoDB, Redis, Apache Cassandra a Neo4j sú všetky NoSQL databázy, no líšia sa v základných štruktúrach dat, které používajú a v použiteľnosti pre rôzne typy aplikácií.

V porovnaní s SQL databázami, NoSQL databázy obvykle nepoužívajú pevne definované schémy a niesú závislé na štruktúrach tabuliek s pevne definovanými vzťahmi (cudzie kľúče atď.). To ich robí flexibilnejšími pre aplikácie s neštrukturovanými alebo pološtruktoravanými datami.

Sú ľahko škálovateľné, čo umožňuje efektívnejšiu správu veľkého objemu dat rozprestrených po veľkom množstve serverov.

Často taktiež podporujú modely programovania špecifické pre konkrétny typ dát (dokumenty, kľúč-hodnota, grafy...), čo môže uľahčiť vývoj aplikácií v konkrétnych doménach.

### Základní principy

MongoDB je NoSQL **dokumentovo orientovaná databáza**, čo znamená, že dáta ukladá vo formáte podobnom JSON (JavaScript Object Notation) resp. BSON (Binary JavaScript object notation). To umožňuje veľmi flexibilné schéma dát a je vhodné pre aplikáce, kde se často menia požiadavky na data a schéma.

Podporuje indexovanie, zložité dotazy, agregácie a geopriestorové indexy.
MongoDB podporuje horizontálne škálovanie pomocou techniky nazývanej "**sharding**", ktorá umožňuje rozdelenie dátových súborov medzi viaceré servery. Sharding je účinný spôsob, ako zvládnuť veľké objemy dát a zároveň udržiavať dobrý výkon pri vysokej záťaži.

Pre replikáciu dát MongoDB používa replikačné sady na zabezpečenie vysokej dostupnosti a odolnosti voči zlyhaniu. Replikačná sada obsahuje viaceré kópie dát, pričom jedna z nich je označená ako primárny uzol (primary), ktorý spracúva všetky zápisy. Ostatné uzly (secondary), udržiavajú kópie dát a môžu byť použité na čítanie dát, aby sa znížilo zaťaženie primárneho uzla.

V porovnaní s inými NoSQL databázami, ako sú Redis (kľúč-hodnota), Apache Cassandra (stĺpcová) a Neo4j (grafová), MongoDB poskytuje lepšie možnosti pre komplexné dotazy a agregácie, vďaka svojej dokumentovo orientovanej štruktúre.

MongoDB tiež podporuje geopriestorové indexy a full-textové vyhľadávanie, čo rozširuje možnosti použitia na rôzne typy aplikácií, od lokalizačných služieb po vyhľadávanie v obsahu.

### CAP teorém

MongoDB ako zvolená NoSql databáza je navrhnutá tak, aby poskytovala vysokú dostupnosť a konzistenciu dát v rámci viacerých serverov, čo umožňuje systému efektívne riešiť výzvy spojené s teóriou CAP (konzistencia, dostupnosť, tolerancia delenia/particionálnych chýb). V kontexte CAP teorému sa MongoDB zameriava skôr na **konzistenciu (C)** a **toleranciu na particionálne chyby (P)**, čo znamená, že v prípade výpadku siete alebo rozdelenia clusteru sa snaží udržať konzistenciu dát na úkor okamžitej dostupnosti všetkých operácií. MongoDB teda používa replikačné sady na zabezpečenie vysokého stupňa odolnosti a konzistencie, čo umožňuje systému efektívne zotaviť sa z jednotlivých serverových alebo sietových zlyhaní. V prípade zlyhania jedného uzla môže systém automaticky prepnúť na sekundárne uzly, čím zabezpečí nepretržité fungovanie služby bez straty dát.

### Architektura

**Ako vyzerá architektúra vášho riešenia a prečo?**
Moje riešenie pozostáva z jednoduchej MongoDB databázy behajúcej v Docker kontajneri. Toto riešenie som zvolil kvôli jeho jednoduchosti, lepšiu demonštráciu dat a nízkym nárokom na údržbu, čo je ideálne pre malé projekty, ako je tento s 500 záznamami hráčov NHL. Pri väčšom množstve dat by som už zvážil použitie shardingu na rozloženie záťaže.

**Ako sa prípadne líši od doporučeného používania a prečo?**
Odporúčané použitie MongoDB zahŕňa funkcie ako sharding a replikácia pre zabezpečenie vysokej dostupnosti a škálovateľnosti. V tomto projekte som tieto funkcie neimplementoval kvôli obmedzenej veľkosti a rozsahu dát, čo zjednodušuje celkovú infraštruktúru.

**Aký cluster pre vaše riešenie ste vytvorili a prečo?**
Vytvoril som jednoduchý cluster s jedným uzlom (single-node cluster), ktorý je vhodný na spracovanie mojich dát bez potreby škálovania alebo replikácie.

**Koľko uzlov pre vaše riešenie používate a prečo?**
Používam jeden uzol, pretože to postačuje pre množstvo a typ operácií, ktoré sú v mojom projekte potrebné. Väčší počet uzlov by znamenal zbytočne komplexnejšiu správu a vyššie náklady.

**Ako využívate pre vaše riešenie replikáciu a prečo?**
Replikáciu v mojom riešení nevyužívam, pretože dáta nie sú kritické a aplikácia nevyžaduje vysokú dostupnosť alebo odolnosť voči chybám, ktoré by replikácia poskytla.

**Využívate sharding a ako jej pre vaše riešenie využívate a prečo? Pripadne pokud jej nevyužívate, tak prečo nie?**
Sharding nevyužívam, pretože množstvo a komplexnosť dát nie je dostatočne veľká na to, aby ospravedlnila zložitosť a náklady spojené s implementáciou shardingu.

**S akými typmi dát vaša databáza pracuje, akého sú formátu a ako s nimi databáza nakladá?**
Databáza pracuje s dátami hráčov uloženými vo formáte JSON. Tento formát je vhodný pre dokumentovo orientované databázy ako MongoDB, pretože umožňuje flexibilné a dynamické spracovanie štruktúrovaných i neštruktúrovaných dát.

**Prečo ste nezvolili ďalšie možné dátové štruktúry pre vašu databázu?**
Nezvolil som iné dátové štruktúry, ako sú relačné databázy alebo key-value store, pretože JSON dokonale vyhovuje potrebám aplikácie vzhľadom na flexibilitu a jednoduchosť manipulácie s dátami, čo je výhodné pre dynamické zmeny a rýchly vývoj.

**S koľkými dátami vaša databáza bude pracovať?**
Databáza bude pracovať s približne 500 záznamami, čo sú vygenerované dáta hráčov NHL.

**Odkiaľ sú dáta generovaná?**
Dáta sú generovaná pomocou skriptu v jazyku Python, ktorý je napísaný na mieru pre moje potreby. Využíva knižnicu Faker na tvorbu náhodne generovaných profilov hráčov a používa reálne názvy NHL tímov pre lepšiu predstavu.

### Perzistence

V mojom riešení je perzistencia dát zabezpečená uložením na pevný disk pomocou volume v Docker compose, ktorý mapuje lokálny adresár do kontajnera s MongoDB. Toto umožňuje trvalé uloženie dát medzi reštartami kontajnera. Tento prístup je vhodný pre základné ukladanie dát bez potreby rýchleho prístupu k sekundárnej pamäti alebo sofistikovaných techník ukladania dát ako je cachovanie.

### Zabezpečení

Možnosti zabezpečenia MongoDB zahŕňajú autentifikáciu, autorizáciu, šifrovanie dát v pokoji aj v prenose. Vo svojom riešení som implementoval základnú autentifikáciu pomocou užívateľského mena a hesla, ktoré sú definované v environment premenných v Docker compose súbore. Tento spôsob je efektívny pre základné zabezpečenie databázy v prostredí, kde nie sú vyžadované vysoké bezpečnostné opatrenia.

### Výhody a nevýhody

Medzi hlavné výhody môjho riešenia patrí jeho jednoduchosť a nízke náklady na údržbu, vďaka čomu je ideálny pre malé projekty ako je tento. Vďaka použitiu JSON dátového formátu je tiež možné ľahko manipulovať s dátami. Hlavnou nevýhodou je obmedzená škálovateľnosť a nižšia odolnosť proti chybám, čo by v prípade rozšírenia projektu mohlo predstavovať problém.

### Případy užití

Zvolil som si MongoDB kvôli flexibilite a jednoduchosti, ktoré sú ideálne pre dynamické spracovanie a ukladanie dokumentov vo formáte JSON. Tento typ databáze je vhodný pre projekty, kde je potrebná rýchla iterácia a zmeny schémy. Nezvolil som inú NoSQL databázu ako napríklad Cassandra alebo Redis, pretože MongoDB poskytuje lepšie nástroje pre prácu s komplexnými dokumentmi a nevyžaduje prísne definované schémy. MongoDB je vhodná pre malé až stredne veľké projekty, ale môže byť nevhodná pre aplikácie, ktoré vyžadujú veľmi vysokú konzistenciu dát alebo kde je potrebná komplexná transakčná podpora.

## Popis vlastního datasetu

Vygenerovaný dataset obsahuje simulované dáta hokejistov, hrajúcich v NHL. Je vytvorený pomocou knižnice `Faker` na generovanie náhodných mien a ďalších atribútov hráčov. Každý hráč v datasete má nasledujúce atribúty:

1. **Meno (name)**: Náhodne generované celé meno.
2. **Vek (age)**: Náhodne generovaný vek hráča medzi 18 a 40 rokmi.
3. **Tím (team)**: Jeden z 30 tímov NHL, medzi ktoré patrí napríklad Montreal Canadiens, Boston Bruins, Seattle Kraken...
4. **Pozícia (position)**: Hráčova pozícia na ľade, ktorá môže byť útočník (Forward), obranca (Defense), alebo brankár (Goalie).
5. **Body (points)**, **Góly (goals)**, **Asistencie (assists)**: Štatistiky vypočítané náhodne s určenými rozsahmi pre body, góly a asistencie.
6. **Trestné minúty (penalty_minutes)**: Náhodne generovaný počet trestných minút.
7. **Odohrané zápasy (games_played)**: Počet odohraných zápasov v sezóne, náhodne generovaný medzi 0 a 82.
8. **Plus/mínus hodnotenie (plus_minus)**: Statistika udávajúca rozdiel v počte gólov kedy hráč bol na ľade, náhodne generované medzi -30 a 30.
9. **Strely na bránu (shots_on_goal)**: Náhodne generovaný počet striel na bránu, v rozmedzí od 50 do 300.
10. **Zranenia (injuries)**: Zoznam náhodne generovaných zranení s dátumom ich vzniku, kde zranenie môže byť napríklad zranenie kolena alebo ramena.
11. **Národnosť (nationality)**: Krajina pôvodu hráča, vybraná náhodne z možností ako Kanada, USA, Rusko, a ďalšie.
12. **Draftové kolo (draft_round)**: Kolo, v ktorom bol hráč draftovaný, náhodne medzi 1 a 7.
13. **Sezóna (season)**: Sezóna, pre ktorú sú hráčove štatistiky uvádzané, v tomto prípade "2023-2024".

Tento dataset bol uložený do súboru JSON s názvom `nhl_players.json`, a obsahuje celkovo 500 hráčových profilov. Každý profil obsahuje detailné štatistické údaje a osobné informácie, ktoré môžu byť použité pre analýzy výkonnosti, simulácie sezón, alebo pre vývoj manažérskych stratégií pre fantasy hokejové ligy.

## Zdroje

-   https://www.mongodb.com/docs/
-   https://courses.fit.cvut.cz/BI-BIG/@master/prednasky/03/P3.pdf
-   https://www.scaler.com/topics/cap-theorem-mongodb/
-   https://github.com/minhhungit/mongodb-cluster-docker-compose/blob/master/docker-compose.yml
