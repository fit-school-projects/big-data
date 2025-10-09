# Big Data - Semestrálna práca

Tento projekt predstavuje komplexnú analýzu Big Data pomocou moderných technológií. Projekt je rozdelený do dvoch hlavných častí:

## 📊 Časti projektu

### 1. NoSQL technológie (MongoDB)
- **Lokalizácia**: `1 - NoSQL technologie/`
- **Technológie**: MongoDB, Docker, Python
- **Dataset**: 500 vygenerovaných hráčov NHL
- **Cieľ**: Demonštrácia NoSQL databázy, komplexné dotazy a agregácie

### 2. Elastic Stack (ELK)
- **Lokalizácia**: `2 - Elastic Stack/`
- **Technológie**: Elasticsearch, Logstash, Kibana, Docker
- **Datasety**: McDonald's, Starbucks, Healthy Lifestyle
- **Cieľ**: Analýza a vizualizácia geografických a lifestyle dát

### 3. Generátory dát
- **Lokalizácia**: `nhl-players-generator/`
- **Technológie**: Python, Faker
- **Cieľ**: Generovanie a čistenie dát pre oba projekty

## 🚀 Rýchly štart

### MongoDB (NoSQL)
```bash
cd "1 - NoSQL technologie"
docker compose up -d
# Import dát a spustenie dotazov podľa HOWTO.md
```

### Elastic Stack
```bash
cd "2 - Elastic Stack"
docker compose up -d
# Spustenie Logstash pipeline pre import dát
```

## 📈 Výsledky

- **MongoDB**: 13 komplexných dotazov a agregácií
- **Elastic Stack**: 8 vizualizácií v Kibane
- **Datasety**: 16,000+ Starbucks pobočiek, 40,000+ McDonald's pobočiek, lifestyle dáta 44 miest

## 🛠 Technológie

- **Databázy**: MongoDB, Elasticsearch
- **Vizualizácia**: Kibana, Mongo Express
- **Infraštruktúra**: Docker, Docker Compose
- **Jazyky**: Python, MongoDB Query Language
- **Dáta**: JSON, CSV, NDJSON

## 📁 Štruktúra projektu

```
big-data/
├── 1 - NoSQL technologie/     # MongoDB projekt
├── 2 - Elastic Stack/         # ELK stack projekt  
├── nhl-players-generator/     # Generátory dát
└── README.md                  # Tento súbor
```

Každý podadresár obsahuje vlastné README s detailnými inštrukciami.
