# Dotaz 3

#### Zdravý životný štýl podľa počtu outdoorových aktivít a úrovne obezity

Dotaz, ktorý hľadá mestá s vysokým počtom vonkajších aktivít a nízkou úrovňou obezity, čo by mohlo poukazovať na zdravší životný štýl.

```
GET healthylifestyle/_search
{
  "query": {
    "bool": {
      "filter": [
        {
          "range": {
            "obesity levels(Country)": {
              "lte": 20
            }
          }
        },
        {
          "range": {
            "outdoor activities(City)": {
              "gte": 50
            }
          }
        }
      ]
    }
  },
  "aggs": {
    "average_gym_cost": {
      "avg": {
        "field": "cost of a monthly gym membership(City)"
      }
    },
    "average_life_expectancy": {
      "avg": {
        "field": "life expectancy(years) (Country)"
      }
    }
  },
  "size": 0,
  "_source": false
}
```

Tento dotaz je zameraný na identifikáciu mest a krajín s atribútmi, ktoré môžu poukazovať na zdravší životný štýl - nízke úrovne obezity a vysoký počet outdoorových aktivít. Okrem toho analyzuje priemerné náklady na posilňovňu a priemernú očakávanú dĺžku života.

1.  **Filtrácia a podmienky**:

    **Obezita**: Filtrujeme krajiny, kde je úroveň obezity 20% alebo nižšia.
    **Outdoorové aktivity**: Filtrujeme mestá s minimálne 50 outdoorovými aktivitami, čo naznačuje dobré možnosti pre aktívny životný štýl.

2.  **Agregácie**:

    **Priemerná cena za posilňovňu**: Vypočíta priemernú cenu mesačného členstva v posilňovni v mestách zahrnutých v dotaze.
    **Priemerná dĺžka života**: Vypočíta priemernú dĺžku života v krajine zahrnutých v dotaze.

**Výstup**: Dotaz nevracia detaily konkrétnych dokumentov, ale sústredí sa na agregované údaje a štatistiky, ktoré poskytujú prehľad o zdravotných a životných podmienkach v daných mestách
