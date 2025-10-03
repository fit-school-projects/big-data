### Dotazy s Find

1. Hrac s najvacsim poctom golov v sezone 2023-2024 z Kanady, draftovany v prvom kole

```mongoDB
// alternativa 1
db.players.find({nationality: "Canada", draft_round: 1, season: "2023-2024"}).sort({"goals": -1}).limit(1);

// alternativa 2
db.players.find({nationality: "Canada", season: "2023-2024"}).sort({"draft_round": 1, "goals": -1}).limit(1);
```

2. Hraci, ktorych meno zacina na pismeno 'A', a ktori maju pocet plus-minus vacsi nez 10 a pocet odohranych zapasov aspon 40

```mongoDB
db.players.find({
    "name": { $regex: '^A', $options: 'i' },  // Mená začínajúce na 'A', nezávisle od veľkosti písmen
    "plus_minus": { $gt: 10 },  // Plus/mínus skóre je väčšie ako 10
    "games_played": { $gt: 40 }  // Odohraných viac ako 40 zápasov
}).sort({ "plus_minus": -1 })
```

### Agregacie

1. Najdi najproduktivnejsieho hraca v kazdom time a vypis jeho meno, goly, asistencie a narodnost.

```mongoDB
[
    {
        // Pridanie poľa pre celkové body (súčet gólov a asistencií)
        $addFields: {
            total_points: { $add: ["$goals", "$assists"] }
        }
    },
    {
        // Zoskupenie hráčov podľa tímu
        $group: {
            _id: "$team",
            players: {
                $push: {
                    name: "$name",
                    goals: "$goals",
                    assists: "$assists",
                    nationality: "$nationality",
                    total_points: "$total_points"
                }
            }
        }
    },
    {
        // Vytvorenie nového poľa s najproduktívnejším hráčom v každom tíme
        $project: {
            topScorer: {
                $arrayElemAt: [
                    {
                        $filter: {
                            input: "$players",
                            as: "player",
                            cond: {
                                $eq: ["$$player.total_points", { $max: "$players.total_points" }]
                            }
                        }
                    },
                    0  // Vráti prvý záznam, keďže môže byť viac hráčov s rovnakým počtom bodov
                ]
            }
        }
    },
    {
        // Projektovanie potrebných údajov
        $project: {
            _id: 0,
            team: "$_id",
            name: "$topScorer.name",
            goals: "$topScorer.goals",
            assists: "$topScorer.assists",
            nationality: "$topScorer.nationality"
        }
    }
]
```

2. Vypis 5 najcastejsie vylucovanych hracov v NHL (s najvacsim poctom trestnych minut)

```mongoDB
[
  {
    $sort: {
      penalty_minutes: -1
    }
	},
  {
    $limit: 5
  }
]
```

3. Tim v NHL, ktory ma najvacsi pocet hracov so zranenim, a hraca v tom time, ktory bol zraneny najviac krat a pocet zraneni

```mongoDB
[
    // Krok 1: Rozbalenie zranení každého hráča
    {
        $unwind: "$injuries"
    },
    // Krok 2: Zoskupenie hráčov podľa tímu a mena, počítanie zranení
    {
        $group: {
            _id: { team: "$team", name: "$name" },
            totalInjuries: { $sum: 1 },
            injuriesList: { $push: "$injuries.injury" }
        }
    },
    // Krok 3: Zoskupenie výsledkov podľa tímu
    {
        $group: {
            _id: "$_id.team",
            totalPlayersWithInjuries: { $sum: 1 },
            players: {
                $push: {
                    name: "$_id.name",
                    totalInjuries: "$totalInjuries",
                    injuriesList: "$injuriesList"
                }
            }
        }
    },
    // Krok 4: Nájdenie hráča s najväčším počtom zranení v každom tíme
    {
        $project: {
            totalPlayersWithInjuries: 1,
            playerWithMostInjuries: {
                $arrayElemAt: [
                    { $filter: {
                        input: "$players",
                        as: "player",
                        cond: { $eq: ["$$player.totalInjuries", { $max: "$players.totalInjuries" }] }
                    }},
                    0
                ]
            }
        }
    },
    // Krok 5: Zoradenie tímov podľa počtu hráčov so zraneniami
    {
        $sort: { totalPlayersWithInjuries: -1 }
    },
    // Krok 6: Výber tímu s najväčším počtom hráčov so zraneniami
    {
        $limit: 1
    }
]
```

4. Celkovy pocet bodov hracov v jednotlivych timoch usporiadane vzostupne

```mongoDB
[
  {
    $group: {
      _id: "$team",
      TotalPoints: { $sum: "$points" },
    },
  },
  {
    $sort: {
      TotalPoints: -1,
    },
  },
]
```

5. Tim s najvacsim poctom hracov draftovanych v prvom kole draftu mladsich ako 25 rokov, ich mena a vek.

```mongoDB
[
  {
    $match: {
      age: { $lt: 25 },
      draft_round: 1,
    },
  },
  {
    $group: {
      _id: { team: "$team", name: "$name" },
      points: { $first: "$points" },  // Zachovanie veku prvého výskytu hráča, pretože vek by mal byť konzistentný pre dané meno
    },
  },
  {
    $group: {
      _id: "$_id.team",  // Zoskupenie podľa tímu
      numOfPlayersDraftedInFirstRound: { $sum: 1 },  // Počítanie počtu hráčov
      playersDrafted: {
        $push: {
          $concat: [
            "$_id.name",  // Meno hráča
            " (",
            { $toString: "$points" },  // Konverzia veku na reťazec
            " rokov)"
          ],
        },  // Vytvorenie reťazca kombinujúceho meno a vek
      },
    },
  },
  {
    $sort: {
      numOfPlayersDraftedInFirstRound: -1,  // Zoradenie tímov podľa počtu hráčov
    },
  },
  {
    $limit: 1,  // Výber len jedného tímu s najväčším počtom hráčov
  },

]
```

6. Priemer veku hracov v kazdom time na 2 desatinne miesta, zoradene a vypis vsetkych hracov daneho timu a ich vek

```mongoDB
[
  {
    $lookup: {
      from: "teams",
      localField: "team",
      foreignField: "team_name",
      as: "team_info",
    },
  },
  {
    $unwind: {
      path: "$team_info",
      preserveNullAndEmptyArrays: true,
    },
  },
  {
    $group: {
      _id: "$team_info.team_name",
      average_age: {
        $avg: "$age",
      },
      total_players: {
        $sum: 1,
      },
      players_list: {
        $push: {
          $concat: [
            "$name",
            " (",
            { $toString: "$age" },
            " rokov)",
          ],
        },
      }, // vytvori zoznam hracov s ich vekom pre kazdy tim
    },
  },
  {
    $project: {
      _id: 0,
      team_name: "$_id",
      average_age: {
        $round: ["$average_age", 2],
      }, // zaokruhli na 2 desatinne miesta
      total_players: 1, // zahrn total_players vo vysledku
      players_list: 1, // zahrn players_list vo vysledku
    },
  },
  {
    $sort: {
      average_age: 1,
    },
  },
]
```

7. Pocet hracov so zranenim Shoulder alebo Hand , ktori hraju za Boston Bruins a rozsah odohranych zapasov hracmi s tymito zraneniami

```mongoDB
[
  // Krok 1: Filtrovanie hráčov z tímu "Boston Bruins"
  {
    $match: {
      team: "Boston Bruins",
    },
  },
  // Krok 2: Rozšírenie zranení
  {
    $unwind: "$injuries",
  },
  // Krok 3: Filtrovanie hráčov so zraneniami ramena alebo ruky
  {
    $match: {
      $or: [
        { "injuries.injury": "Shoulder" },
        { "injuries.injury": "Hand" },
      ],
    },
  },
  // Krok 4: Zoskupenie podľa typu zranenia
  {
    $group: {
      _id: "$injuries.injury",
      totalPlayers: { $sum: 1 }, // Počet hráčov s daným typom zranenia
      minGamesPlayed: { $min: "$games_played" }, // Minimum odohraných zápasov
      maxGamesPlayed: { $max: "$games_played" }, // Maximum odohraných zápasov
    },
  },
]
```

8. Hraci, ktori maju nadpriemernu uspesnost strelby v NHL

```mongoDB
[
  {
    $facet: {  // Rozdelenie agregačného pipeline na dve nezávislé cesty: "stats" pre štatistiky a "players" pre údaje o hráčoch
      stats: [
        {
          $group: {  // Zoskupenie všetkých dokumentov na výpočet celkových striel a gólov
            _id: null,  // Zoskupovací kľúč nie je nastavený, čo znamená globálne zoskupenie
            totalShots: {
              $sum: "$shots_on_goal",  // Súčet všetkých striel na bránu
            },
            totalGoals: { $sum: "$goals" },  // Súčet všetkých gólov
          },
        },
        {
          $project: {
            _id: 0,  // Odstránenie _id z výstupu
            averageShootingAccuracy: {
              $divide: [
                "$totalGoals",
                "$totalShots",
              ],  // Výpočet priemernej streleckej presnosti
            },
          },
        },
      ],
      players: [
        {
          $project: {
            name: 1,
            team: 1,
            shots_on_goal: 1,
            goals: 1,
            shootingAccuracy: {
              $round: [
                {
                  $divide: [
                    "$goals",
                    "$shots_on_goal",
                  ],
                },
                3  // Zaokrúhľovanie streleckej presnosti hráča na tri desatinné miesta
              ],
            },
          },
        },
      ],
    },
  },
  {
    $unwind: "$stats",  // Rozbalenie pole "stats" na jednotlivé dokumenty
  },
  {
    $unwind: "$players",  // Rozbalenie pole "players" na jednotlivé dokumenty
  },
  {
    $project: {  // Finálne projekcia polí pre zjednodušenie a určenie, či hráč prekročil priemernú presnosť a je high-volume strelec
      name: "$players.name",
      team: "$players.team",
      shotsOnGoal: "$players.shots_on_goal",
      shootingAccuracy: "$players.shootingAccuracy",
      exceedsAverage: {
        $gt: [
          "$players.shootingAccuracy",
          "$stats.averageShootingAccuracy",
        ],
      },
      highVolumeShooter: {
        $gt: ["$players.shots_on_goal", 150],
      },
    },
  },
  {
    $match: {
      exceedsAverage: true,  // Filtrovanie hráčov, ktorí majú lepšiu streleckú presnosť ako priemer
      highVolumeShooter: true,  // Filtrovanie hráčov, ktorí majú viac ako 150 striel na bránu
    },
  },
  {
    $sort: {
      shootingAccuracy: -1
    }
  }
]

```

9. Narodnost hracov s najvacsim zastupenim v NHL

```mongoDB
[
  {
    $group: {
      _id: "$nationality",
      count: { $sum: 1 },
    }, // spocitanie hracov zoskupenych podla narodnosti
  },
  {
    $sort: {
      count: -1, // od najvacsieho
    },
  },
  {
    $limit: 1, // prvy vysledok
  },
]
```

10. Timy s priemernym vekom hracov nad 30 rokov

```mongoDB
[
  {
    $group: {
      _id: "$team",
      averageAge: { $avg: "$age" }  // Výpočet priemerného veku pre každý tím
    }
  },
  {
    $project: {
      averageAge: { $round: ["$averageAge", 2] }  // Zaokrúhľovanie priemerného veku na dve desatinné miesta
    }
  },
  {
    $match: {
      averageAge: { $gt: 30 }  // Filtrovanie tímov, kde zaokrúhlený priemerný vek je väčší ako 30
    }
  }
]
```

11. Priemerny pocet golov hraca na zapas

```mongoDB
[
  {
    $project: {
      _id: 0,
      name: 1,
      goals: 1,
      games_played: 1,
      avgGoalsPerGame: {
        $round: [
          {
            $divide: ["$goals", "$games_played"]
          },
          3
        ]
      }
    }
  }
]
```

12. Hraci, ktori maju pocet golov vacsi ako priemer timu a boli aspon raz zraneni (tzv. rizikovy hraci, ktori oslabia vykonnost timu)

```mongoDB
[
  {
    $match: {
      injuries: { $exists: true, $not: {$size: 0} }  // Filtruje hráčov, ktorí majú aspoň jedno zaznamenané zranenie
    }
  },
  {
    $group: {
      _id: "$team",  // Zoskupuje dokumenty podľa tímu
      highRiskPlayers: {
        $push: {  // Vytvára pole hráčov pre každý tím
          name: "$name",  // Meno hráča
          gamesPlayed: "$games_played",  // Počet odohraných zápasov
          goals: "$goals",  // Počet gólov, ktoré hráč dosiahol
          averageInjuriesPerSeason: { $size: "$injuries" }  // Počet zranení, ktoré hráč mal
        }
      },
      teamAverageGoals: { $avg: "$goals" }  // Vypočíta priemerný počet gólov na tím
    }
  },
  {
    $project: {
      teamAverageGoals: 1,  // Zahrnutie priemerného počtu gólov tímu
      highRiskPlayers: {
        $filter: {  // Filtruje pole highRiskPlayers
          input: "$highRiskPlayers",  // Vstupné pole na filtráciu
          as: "player",  // Alias pre každý element v poli
          cond: { $gt: ["$$player.goals", "$teamAverageGoals"] }  // Podmienka, ktorá zahrnie len hráčov s počtom gólov vacsim ako je priemer tímu
        }
      }
    }
  }
]
```

13. Hraci z Ceska, ktori su pripraveni zahviezdit na MS v ladovom hokeji (tzn. hrac ktory nebol ani raz zraneny, bol draftovany v 1. - 3. kole draftu, a maju sucet golov a asistencii minimalne 40 a pocet trestnych minut je co najmensi. Vyber top 3.)

```mongoDB
[
    {
        $match: {
            nationality: "Czech Republic",  // Hráči z CZ
            age: { $lte: 25 },  // Vek do 25 rokov
            draft_round: { $lte: 3 }, // kolo draftu 1 alebo 2
          	injuries: { $eq: [] } // niesu aktualne zraneni
        }
    },
    {
        $project: {
            name: 1,
            team: 1,
            goals: 1,
            assists: 1,
            penalty_minutes: 1,
            points: { $add: ["$goals", "$assists"] },  // Súčet gólov a asistencií pre výpočet celkových bodov
            draft_round: 1
        }
    },
    {
        $sort: {
            points: -1,  // Zoradiť hráčov podľa celkového počtu bodov zostupne
            goals: -1,  // Zoradiť hráčov podľa počtu gólov zostupne
            assists: -1,  // Zoradiť hráčov podľa počtu asistencií zostupne
            penalty_minutes: 1  // Zoradiť hráčov podľa počtu trestných minút vzostupne (menej je lepšie)
        }
    },
    {
        $limit: 3  // Vrátiť len top 3 hráčov
    }
]
```
