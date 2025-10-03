import json
from faker import Faker

fake = Faker()

# List of NHL teams with some attributes
teams_data = [
    {"team_name": "Anaheim Ducks", "location": "Anaheim, California", "conference": "Western", "division": "Pacific", "established": 1993},
    {"team_name": "Arizona Coyotes", "location": "Glendale, Arizona", "conference": "Western", "division": "Pacific", "established": 1996},
    {"team_name": "Boston Bruins", "location": "Boston, Massachusetts", "conference": "Eastern", "division": "Atlantic", "established": 1924},
    {"team_name": "Buffalo Sabres", "location": "Buffalo, New York", "conference": "Eastern", "division": "Atlantic", "established": 1970},
    {"team_name": "Calgary Flames", "location": "Calgary, Alberta", "conference": "Western", "division": "Pacific", "established": 1980},
    {"team_name": "Carolina Hurricanes", "location": "Raleigh, North Carolina", "conference": "Eastern", "division": "Metropolitan", "established": 1972},
    {"team_name": "Chicago Blackhawks", "location": "Chicago, Illinois", "conference": "Western", "division": "Central", "established": 1926},
    {"team_name": "Colorado Avalanche", "location": "Denver, Colorado", "conference": "Western", "division": "Central", "established": 1972},
    {"team_name": "Columbus Blue Jackets", "location": "Columbus, Ohio", "conference": "Eastern", "division": "Metropolitan", "established": 2000},
    {"team_name": "Dallas Stars", "location": "Dallas, Texas", "conference": "Western", "division": "Central", "established": 1967},
    {"team_name": "Detroit Red Wings", "location": "Detroit, Michigan", "conference": "Eastern", "division": "Atlantic", "established": 1926},
    {"team_name": "Edmonton Oilers", "location": "Edmonton, Alberta", "conference": "Western", "division": "Pacific", "established": 1972},
    {"team_name": "Florida Panthers", "location": "Sunrise, Florida", "conference": "Eastern", "division": "Atlantic", "established": 1993},
    {"team_name": "Los Angeles Kings", "location": "Los Angeles, California", "conference": "Western", "division": "Pacific", "established": 1967},
    {"team_name": "Minnesota Wild", "location": "St. Paul, Minnesota", "conference": "Western", "division": "Central", "established": 2000},
    {"team_name": "Montreal Canadiens", "location": "Montreal, Quebec", "conference": "Eastern", "division": "Atlantic", "established": 1909},
    {"team_name": "Nashville Predators", "location": "Nashville, Tennessee", "conference": "Western", "division": "Central", "established": 1998},
    {"team_name": "New Jersey Devils", "location": "Newark, New Jersey", "conference": "Eastern", "division": "Metropolitan", "established": 1974},
    {"team_name": "New York Islanders", "location": "Uniondale, New York", "conference": "Eastern", "division": "Metropolitan", "established": 1972},
    {"team_name": "New York Rangers", "location": "New York, New York", "conference": "Eastern", "division": "Metropolitan", "established": 1926},
    {"team_name": "Ottawa Senators", "location": "Ottawa, Ontario", "conference": "Eastern", "division": "Atlantic", "established": 1992},
    {"team_name": "Philadelphia Flyers", "location": "Philadelphia, Pennsylvania", "conference": "Eastern", "division": "Metropolitan", "established": 1967},
    {"team_name": "Pittsburgh Penguins", "location": "Pittsburgh, Pennsylvania", "conference": "Eastern", "division": "Metropolitan", "established": 1967},
    {"team_name": "San Jose Sharks", "location": "San Jose, California", "conference": "Western", "division": "Pacific", "established": 1991},
    {"team_name": "Seattle Kraken", "location": "Seattle, Washington", "conference": "Western", "division": "Pacific", "established": 2021},
    {"team_name": "St. Louis Blues", "location": "St. Louis, Missouri", "conference": "Western", "division": "Central", "established": 1967},
    {"team_name": "Tampa Bay Lightning", "location": "Tampa, Florida", "conference": "Eastern", "division": "Atlantic", "established": 1992},
    {"team_name": "Toronto Maple Leafs", "location": "Toronto, Ontario", "conference": "Eastern", "division": "Atlantic", "established": 1917},
    {"team_name": "Vancouver Canucks", "location": "Vancouver, British Columbia", "conference": "Western", "division": "Pacific", "established": 1970},
    {"team_name": "Vegas Golden Knights", "location": "Las Vegas, Nevada", "conference": "Western", "division": "Pacific", "established": 2017},
    {"team_name": "Washington Capitals", "location": "Washington, D.C.", "conference": "Eastern", "division": "Metropolitan", "established": 1974},
    {"team_name": "Winnipeg Jets", "location": "Winnipeg, Manitoba", "conference": "Western", "division": "Central", "established": 2011}
]

# Add a random number of simulated staff members for each team
for team in teams_data:
    team["staff_members"] = [{'name': fake.name(), 'position': fake.job()} for _ in range(fake.random_int(min=5, max=15))]

# Write the data to a JSON file
with open('nhl_teams.json', 'w') as f:
    json.dump(teams_data, f, indent=4)

print("Generated NHL teams data saved to 'nhl_teams.json'.")
