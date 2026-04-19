players = ["Messi", "Ronaldo", "Neymar"]
goals = [7, 4, 2]

for player, goal in zip(players, goals):
    if goal >= 5:
        print(f"{player} - Elite")
    elif goal >= 3:
        print(f"{player} - Good")
    else:
        print(f"{player} - Needs improvement")