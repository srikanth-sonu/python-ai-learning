students = [
    {"id": 1, "name": "Srikanth", "marks": 89},
    {"id": 2, "name": "Rahul", "marks": 65},
    {"id": 3, "name": "Anjali", "marks": 92},
    {"id": 4, "name": "Kiran", "marks": 34},
]
for student in students:
    for key, value in student.items():
        print(f"{key} : {value}")
    print("-" * 20)

passed_students = [student for student in students if student["marks"] >= 35]
print("Passed Students and their marks\n")
for student in passed_students:
    print(f"{student['name']} - {student['marks']}")
print("-" * 20)
distinction_students = [student for student in students if student["marks"] > 75]
print("Distinction Students and their marks\n")
for student in distinction_students:
    print(f"{student['name']} - {student['marks']}")
print("-" * 20)
failed_students = [student for student in students if student["marks"] < 35]
print("Failed Students and thier marks\n")
for student in failed_students:
    print(f"{student['name']} - {student['marks']}")
print("-" * 20)

print(f"Total Students  : {len(students)}")
print(f"Passed          : {len(passed_students)}")
print(f"Failed          : {len(failed_students)}")
print(f"Distinction     : {len(distinction_students)}")
print("-" * 20)
