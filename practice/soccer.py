players = ["Messi", "Ronaldo", "Neymar", "Pulisic", "Yamal"]
teams = ["Inter Miami", "Al-Nassr", "Santos", "AC Milan", "Barcelona"]
goals = [4, 2, 3, 1, 4]
for player, team, goal in zip(players, teams, goals):
    print(f"{player} plays for {team} and he scored {goal} goals last game.")
players.append("Pedri")
teams.append("Barcelona")
goals.append(2)
total_players = len(players)
for player, team, goal in zip(players, teams, goals):
    print(f"{player} plays for {team} and he scored {goal} goals last game.")
total_goals = sum(goals)
print(f"My database has {total_players} players. The total goals scored is {total_goals}.")