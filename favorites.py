sports = ["Soccer", "Golf", "Football", "Baseball", "Skiing"]
print(len(sports))
print(sports[0], sports[-1])
sports.append("Basketball")
sports.remove("Baseball")
print(sports)
print(f"My favorite sport is {sports[0]} and I have {len(sports)} sports in my list!")