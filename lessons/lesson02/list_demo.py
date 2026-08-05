fruits = ["Apple", "Banana", "Orange"]

print(fruits[0])
print(fruits[1])
print(fruits[2])
fruits.append("Grapes")
print(fruits)
print(fruits[-1])
print(fruits[-2])
print(fruits[-3])

print(type(fruits))
fruits.insert(0, "Berry")
print(fruits)
fruits.sort()
print(fruits)
print(len(fruits))
print(fruits.pop())
print(fruits)
print(fruits.pop(0))
print(fruits)


numbers = [10, 20, 30, 40, 50, 60]
print(numbers[0:3])
print(numbers[2:5])
print(numbers[:4])
print(numbers[3:])
print(numbers[-3:])

print(numbers[1:-1])  # 20, 30, 40, 50
print(numbers[:-2])  # 10, 20, 30, 40
print(numbers[-4:-1])  # 30, 40, 50
