students = ["Tommy", "Carter", "Landon", "Connor", "Aiden"]
subjects = ["Math", "English", "History", "Science", "Gym"]
grades = [97, 41, 85, 76, 64]
attendance = [95, 100, 97, 67, 81]
for student, subject, grade, attendance in zip(students, subjects, grades, attendance):
    print(f"{student} - {subject} - Grade: {grade} - Attendance: {attendance}%")
    if grade >= 90:
        print(f"{student}, thats outstanding!")
    elif grade >= 75:
        print(f"{student}, thats passing.")
    else:
        print(f"{student} needs improvement.")
    if attendance < 80:
        print(f"{student}, this is an attendance warning.")
student_amount = (len(students))
highest_grade = (max(grades))
average_grade = (sum(grades)/len(grades))
print(student_amount)
print(highest_grade)
print(average_grade)