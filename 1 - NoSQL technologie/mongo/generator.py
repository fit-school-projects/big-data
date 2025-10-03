from faker import Faker
import json
import random
import uuid

fake = Faker()

def generate_player():
    positions = ['Forward', 'Defense', 'Goalie']
    teams = [
        'Montreal Canadiens',
        'Toronto Maple Leafs',
        'Boston Bruins',
        'New York Rangers',
        'Chicago Blackhawks',
        'Detroit Red Wings',
        'Philadelphia Flyers',
        'Pittsburgh Penguins',
        'Los Angeles Kings',
        'Vancouver Canucks',
        'Washington Capitals',
        'St. Louis Blues',
        'Buffalo Sabres',
        'Calgary Flames',
        'Colorado Avalanche',
        'Dallas Stars',
        'Edmonton Oilers',
        'Florida Panthers',
        'Minnesota Wild',
        'Nashville Predators',
        'New Jersey Devils',
        'New York Islanders',
        'Ottawa Senators',
        'San Jose Sharks',
        'Tampa Bay Lightning',
        'Arizona Coyotes',
        'Carolina Hurricanes',
        'Winnipeg Jets',
        'Vegas Golden Knights',
        'Seattle Kraken'
    ]
    injuries = ['Concussion', 'Knee', 'Shoulder', 'Groin', 'Hip', 'Ankle', 'Back', 'Neck', 'Wrist', 'Hand', 'Foot']
    country = ['Canada', 'USA', 'Russia', 'Sweden', 'Finland', 'Czech Republic', 'Slovakia', 'Germany', 'Switzerland']

    player = {
        "_id": str(uuid.uuid4()),
        "name": fake.name(),
        "age": random.randint(18, 40),
        "team": random.choice(teams),
        "position": random.choice(positions),
        "points": random.randint(0, 100),
        "goals": random.randint(0, 50),
        "assists": random.randint(0, 50),
        "penalty_minutes": random.randint(0, 100),
        "games_played": random.randint(0, 82),
        "plus_minus": random.randint(-30, 30),
        "shots_on_goal": random.randint(50, 300),
        "injuries": [{"injury": random.choice(injuries), "date": fake.date_this_year().isoformat()} for _ in
                     range(random.randint(0, 3))],
        "nationality": random.choice(country),
        "draft_round": random.randint(1, 7),
        "season": f"2023-2024"
    }
    return player


def create_players(num_players):
    return [generate_player() for _ in range(num_players)]


# Generate 100 players
players = create_players(500)

# Write to JSON file
with open('nhl_players.json', 'w') as file:
    for player in players:
        file.write(json.dumps(player) + "\n")

print("Dataset was successfully generated and saved as 'nhl_players.json'.")
