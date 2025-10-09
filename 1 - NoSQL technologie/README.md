# MongoDB - NoSQL Databáza

Tento projekt demonštruje prácu s MongoDB - dokumentovo orientovanou NoSQL databázou na príklade datasetu hráčov NHL.

## 🎯 Cieľ projektu

- Demonštrácia NoSQL databázy MongoDB
- Komplexné dotazy a agregácie
- Analýza športových dát
- Porovnanie s relačnými databázami

## 🏗 Architektúra

### Technológie
- **MongoDB** - dokumentovo orientovaná databáza
- **Docker** - kontajnerizácia
- **Mongo Express** - webové rozhranie pre správu DB
- **Python** - generovanie dát

### Štruktúra riešenia
```
MongoDB (single-node cluster)
├── Database: nhl
├── Collection: players
└── 500 dokumentov hráčov NHL
```

## 📊 Dataset

### NHL Players Dataset
- **Počet záznamov**: 500 hráčov
- **Formát**: JSON/BSON
- **Zdroj**: Vygenerované pomocou Python + Faker

### Štruktúra dokumentu
```json
{
  "name": "John Doe",
  "age": 25,
  "team": "Boston Bruins",
  "position": "Forward",
  "goals": 15,
  "assists": 20,
  "points": 35,
  "penalty_minutes": 12,
  "games_played": 65,
  "plus_minus": 8,
  "shots_on_goal": 120,
  "injuries": [
    {"injury": "Knee", "date": "2023-01-15"}
  ],
  "nationality": "Canada",
  "draft_round": 2,
  "season": "2023-2024"
}
```

## 🚀 Spustenie

### 1. Spustenie kontajnerov
```bash
docker compose up -d
```

### 2. Import dát
```bash
# Kopírovanie súboru do kontajnera
docker cp mongo/nhl_players.json mongo:/home

# Import do databázy
docker exec -it mongo bash
mongoimport --username user --password pass --authenticationDatabase admin --db nhl --collection players --file /home/nhl_players.json
```

### 3. Pripojenie k databáze
```bash
# Pripojenie cez mongosh
docker exec -it mongo bash
mongosh
use admin
db.auth("user", "pass")
use nhl
```

### 4. Webové rozhranie
- **Mongo Express**: http://localhost:8081
- **MongoDB**: mongodb://localhost:27017

## 📝 Dotazy a analýzy

### Základné dotazy (Find)
- Hráči s najvyšším počtom gólov
- Filtrovanie podľa národnosti a draftového kola
- Vyhľadávanie podľa regex vzorov

### Komplexné agregácie
- Najproduktívnejší hráč v každom tíme
- Štatistiky zranení podľa tímov
- Priemerný vek hráčov v tímoch
- Analýza streleckej presnosti

### Pokročilé analýzy
- Hráči s nadpriemernou úspešnosťou
- Rizikoví hráči (vysoká produktivita + zranenia)
- Kandidáti na reprezentáciu

**Celkovo**: 13 rôznych dotazov a agregácií

## 🔧 Konfigurácia

### Docker Compose
- **MongoDB**: Port 27017
- **Mongo Express**: Port 8081
- **Autentifikácia**: user/pass
- **Perzistencia**: Volume mapping

### Zabezpečenie
- Základná autentifikácia
- Environment premenné
- Izolované kontajnery

## 📈 Výsledky

### Kľúčové zistenia
- Analýza výkonnosti hráčov
- Korelácie medzi zraneniami a produktivitou
- Štatistiky tímov a národností
- Identifikácia talentov

### Technické výsledky
- Úspešná implementácia MongoDB
- Komplexné dotazy a agregácie
- Efektívne spracovanie JSON dát
- Demonštrácia NoSQL výhod

## 📚 Dokumentácia

- **HOWTO.md** - Detailné inštrukcie
- **queries.md** - Všetky dotazy s vysvetlením
- **mongo/** - Generátory dát

## 🔗 Odkazy

- [MongoDB dokumentácia](https://www.mongodb.com/docs/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Mongo Express](https://github.com/mongo-express/mongo-express)

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
