subjects = ["Math", "English", "History", "Science", "Gym"]
grades = [100, 84, 82, 97, 100]
print(len(subjects))
for subject, grade in zip(subjects, grades):
    print(f"{subject}: {grade}")
subjects.append("Art")
grades.append(98)
print(f"I am taking {len(subjects)} subjects this year.")