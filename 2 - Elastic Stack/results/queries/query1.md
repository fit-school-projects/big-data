# Dotaz 1

#### Starbucks v US obsahujúce New v názve mesta

Chceme získať zoznam pobočiek Starbucks v USA, ktoré sú vo veľkých mestách, konkrétne tie, ktoré obsahujú "New" v názve mesta, a zároveň chceme zoradiť výsledky podľa časového pásma

```
GET starbucks/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "country": "United States"
          }
        },
        {
          "wildcard": {
            "city": "*New*"
          }
        }
      ]
    }
  },
  "sort": [
    {
      "timezone": {
        "order": "asc"
      }
    }
  ],
  "size": 10,
  "_source": ["store name", "city", "state/province", "phone number", "timezone"]
}
```

1. **Filtrovanie**: Dotaz používa bool a match klauzuly na filtrovanie pobočiek Starbucks tak, že country musí byť USA. To zaisťuje, že výsledky budú obsahovať len pobočky umiestnené v USA. Taktiež používame wildcard na filtrovanie miest, kde musí názov mesta obsahovať "New" (napríklad New York, New Jersey atď.).
2. **Triedenie**: Výsledky sú zoradené podľa časového pásma (timezone), použitím keyword na presné zhodnotenie, a to v vzostupnom poradí (asc).
3. **Wildcard vyhľadávanie**: Používa sa na filtrovanie miest podľa názvu mesta pomocou wildcard klauzuly, ktorá umožňuje nájsť všetky mestá, ktorých názvy obsahujú reťazec "New".
4. **Projekcia**: Klauzula `_source` je použitá na určenie, ktoré polia sa majú zobraziť v odpovedi. Týmto spôsobom získame prehľadný výstup obsahujúci názov obchodu, mesto, štát/provinciu, telefónne číslo a časové pásmo.
