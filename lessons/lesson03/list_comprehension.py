# Traditional for loop
numbers = [10, 20, 30, 40, 50, 60]
double = []
for num in numbers:
    double.append(num * 2)
print(double)

# list comprehension loop
multiplied_by_two = [numb * 2 for numb in numbers]
print(f"multiplied_by_two: {multiplied_by_two}")

# names = ["srikanth", "sonu", "anu", "deep"]
# capital = []
# for name in names:
#     capital.append(name.upper())
# print(capital)

# upper_case_letters = [name.upper() for name in names]
# print(f"Transforming Characters to uppercase: {upper_case_letters}")


fruits = ["Apple", "Banana", "Orange", "Kiwi"]
fruits_length_above_five = [fruit for fruit in fruits if len(fruit) > 5]
print(fruits_length_above_five)

marks = [45, 67, 89, 34, 92, 76, 58, 81]
squared_marks = [mark**2 for mark in marks]
print(squared_marks)
passed_members = [mark for mark in marks if mark >= 35]
print(f"Total Marks: {len(marks)}")
print(f"Passed Marks: {len(passed_members)}")
distinction = [mark for mark in marks if mark >= 75]
print(f"Distinction: {len(distinction)}")

names = ["ram", "john", "sam", "alex", "robert"]
names_with_more_than_Three_chars = [name.upper() for name in names if len(name) > 3]
print(names_with_more_than_Three_chars)


numbers = [1, 2, 3, 4, 5]

result = [number * 10 for number in numbers if number % 2 != 0]

print(result)

numbers = [1, 2, 3, 4, 5]

result = [number * 5 for number in numbers if number > 2]
print(result)

student = {"name": "Srikanth", "age": 28, "course": "Python AI"}

print(student)
print(type(student))

print(student["name"])
print(student["age"])
print(student["course"])

employee = {
    "id": 101,
    "name": "Srikanth",
    "role": "Software Engineer",
    "salary": 1500000,
    "experience": 7.2,
}
employee["salary"] = 150000
employee["experience"] = 7.2

# print(employee["name"])
# print(employee["salary"])
# print(employee)

# print(employee)
for key, value in employee.items():
    print(f"{key} : {value}")
