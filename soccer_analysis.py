players = ["Messi", "Ronaldo", "Neymar", "Yamal", "Modric"]
goals = [6, 2, 7, 4, 3]
for player, goal in zip(players, goals):
    if goal >= 5:
        print(f"{player} - Elite performer with {goal} goals.")
    elif goal >= 3:
        print(f"{player} - Good performer with {goal} goals.")
    else:
        print(f"{player} - Needs improvement with {goal} goals.")
print(len(players))