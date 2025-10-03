# Návod ke zprovoznění semestrální práce

1. **Naklonovanie repozitára**
   `git clone git@gitlab.fit.cvut.cz:BI-BIG/B232/BI/melisand.git`
2. **Prepnutie sa do zložky 1 - NoSQL technologie**
   `cd 1\ -\ NoSQL\ technologie`
3. **Spustenie docker-compose.yml**
   `docker compose up -d`
4. **Nahratie dat do mongoDB**
    - `docker cp mongo/nhl_players.json mongo:/home`
    - `docker exec -it mongo bash`
    - `mongoimport --username user --password pass --authenticationDatabase admin --db nhl --collection players --file /home/nhl_players.json`

### Prihlásenie sa do mongosh

1. `docker exec -it mongo bash`
2. `mongosh`
3. `use admin`
4. `db.auth("user", "pass");`
