# NHL Players Generator

Tento adresár obsahuje nástroje pre generovanie a čistenie dát používaných v Big Data projekte.

## 🎯 Účel

- Generovanie realistických dát hráčov NHL
- Čistenie a príprava datasetov pre Elastic Stack
- Automatizácia procesu vytvárania testovacích dát

## 📁 Obsah adresára

### Generátory dát
- **`generator.py`** - Hlavný generátor NHL hráčov
- **`teams-generator.py`** - Generátor tímov NHL
- **`csv_datasets_for_elastic_script.py`** - Skript pre Elastic Stack datasety

### Čističe dát
- **`mcdonalds_cleaner.py`** - Čistenie McDonald's datasetu
- **`starbucks_cleaner.py`** - Čistenie Starbucks datasetu

### Výstupné súbory
- **`nhl_players.json`** - 500 vygenerovaných hráčov NHL
- **`nhl_teams.json`** - Zoznam NHL tímov
- **`data/`** - Čistené CSV datasety pre Elastic Stack

## 🚀 Použitie

### Generovanie NHL hráčov
```bash
python generator.py
```

### Generovanie tímov
```bash
python teams-generator.py
```

### Čistenie Elastic Stack dát
```bash
python mcdonalds_cleaner.py
python starbucks_cleaner.py
python csv_datasets_for_elastic_script.py
```

## 📊 Generované dáta

### NHL Players Dataset
- **Počet záznamov**: 500 hráčov
- **Formát**: JSON
- **Atribúty**: 
  - Osobné údaje (meno, vek, národnosť)
  - Športové štatistiky (góly, asistencie, body)
  - Tímové informácie (tím, pozícia, draft)
  - Zdravotné údaje (zranenia, odohrané zápasy)

### Čistené CSV datasety
- **McDonald's**: Vyčistené dáta pobočiek
- **Starbucks**: Vyčistené dáta pobočiek  
- **Healthy Lifestyle**: Dáta o lifestyle indikátoroch miest

## 🛠 Technológie

- **Python 3.x**
- **Faker** - generovanie realistických dát
- **Pandas** - manipulácia s dátami
- **JSON/CSV** - formáty výstupných súborov

## 📈 Výsledky

### NHL Players
- Realistické profily hráčov
- Rovnomerné rozloženie po tímoch
- Rôznorodé štatistiky a zranenia
- Kompatibilita s MongoDB

### Elastic Stack datasety
- Vyčistené a štandardizované dáta
- Správne formátovanie pre Logstash
- Geografické súradnice pre mapy
- Konzistentné názvy krajín a miest

## 🔧 Konfigurácia

### Požiadavky
```bash
pip install faker pandas
```

### Nastavenie
- Generátory používajú predvolené nastavenia
- Možnosť úpravy počtu generovaných záznamov
- Konfigurovateľné rozsahy pre štatistiky

## 📚 Dokumentácia

- **`generator.py`** - Komentáre v kóde
- **`teams-generator.py`** - Dokumentácia tímov
- **Čističe** - Popis čistiacich procesov

## 🔗 Súvisiace súbory

- **MongoDB projekt**: `../1 - NoSQL technologie/`
- **Elastic Stack**: `../2 - Elastic Stack/`
- **Root README**: `../README.md`
