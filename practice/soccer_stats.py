players = ["Messi", "Ronaldo", "Neymar", "Yamal", "Modric"]
goals = [6, 2, 7, 4, 3]
assists = [2, 1, 3, 2, 4]
def performance(goal, assist):
    if goal + assist >= 8:
        return "Elite"
    elif goal + assist >= 5:
        return "Good"
    else:
        return "Needs improvement"
def total_contributions(player, goal, assist):
    return f"{player} - Goals: {goal}, Assists: {assist} - Total: {goal + assist} - {performance(goal, assist)}"
for player, goal, assist in zip(players, goals, assists):
    print(total_contributions(player, goal, assist))
print(len(players))
print(max(goals))
print(sum(assists)/len(assists))