name = "Tommy"
age = 14
height = 5.3
hobbies = ["golfing", "skiing", "coding", "soccer", "pushups"]
print(len(hobbies))
hobbies.append("math")
hobbies.remove("pushups")
for hobby in hobbies:
    print(f"I enjoy {hobby}")
print(f"My name is {name}, I am {age} years old, and I have {len(hobbies)} hobbies.")