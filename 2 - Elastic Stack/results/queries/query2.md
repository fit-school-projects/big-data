# Dotaz 2

#### Vyhľadávanie pobočiek McDonald's v Košiciach bez služby McDrive

Tento dotaz je navrhnutý na vyhľadávanie pobočiek reťazca McDonald's v mojom rodnom meste Košice, ktoré nesmú ponúkať službu McDrive. Ulohou je overenie si mojich poznatkov o tomto raťazci s datasetom, ktorý mám k dispozícii.

```
GET mcdonalds/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "term": {
            "city": "Košice"
          }
        },
        {
          "term": {
            "country": "Slovakia"
          }
        }
      ],
      "must_not": [
        {
          "wildcard": {
            "services": "*McDrive*"
          }
        }
      ]
    }
  },
  "size": 10,
  "_source": ["name", "address", "city", "services", "country", "runhours"]
}
```

1. **Filtrácia podľa mesta a krajiny**: Používame term dotazy na presné filtrovanie záznamov tak, aby odpovedali len mestu Košice a krajine Slovensko.
2. **Vylúčenie služieb McDrive (wildcard)**: S pomocou wildcard dotazu vylučujeme všetky pobočky, ktoré vo svojom popise služieb obsahujú "McDrive". Toto je realizované cez klauzulu `must_not`, ktorá zabezpečuje, že žiadne z vrátených pobočiek tieto služby neponúkajú.
3. **Projekcia**: V odpovedi sa zobrazujú polia ako názov pobočky, adresa, mesto, ponúkané služby, krajina a prevádzkové hodiny, čo umožňuje lepší prehľad o každej konkrétnej lokalite.
