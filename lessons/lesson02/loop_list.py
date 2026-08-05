fruits = ["Apple", "Banana", "Orange", "Mango"]
# for fruit in fruits:
#     print(fruit)

# index = 0
# while index < len(fruits):
#     print(fruits[index])
#     index += 1

for index, fruit in enumerate(fruits):
    print(f"{index + 1}: {fruit}")


mock_user_data = [
    {"id": 1, "name": "Alice Smith", "role": "Admin", "active": True, "score": 92.5},
    {"id": 2, "name": "Bob Jones", "role": "User", "active": False, "score": 45.0},
    {"id": 3, "name": "Charlie Brown", "role": "User", "active": True, "score": 78.2},
    {"id": 4, "name": "Diana Prince", "role": "Manager", "active": True, "score": 88.0},
    {"id": 5, "name": "Evan Wright", "role": "User", "active": True, "score": 61.4},
    {
        "id": 6,
        "name": "Fiona Gallagher",
        "role": "User",
        "active": False,
        "score": 23.1,
    },
    {"id": 7, "name": "George Clark", "role": "Admin", "active": True, "score": 95.0},
    {"id": 8, "name": "Hannah Abbott", "role": "User", "active": True, "score": 74.6},
    {"id": 9, "name": "Ian Malcolm", "role": "Manager", "active": False, "score": 50.5},
    {"id": 10, "name": "Julia Roberts", "role": "User", "active": True, "score": 83.9},
    {"id": 11, "name": "Kevin Bacon", "role": "User", "active": True, "score": 69.1},
    {"id": 12, "name": "Laura Croft", "role": "Admin", "active": True, "score": 98.7},
    {
        "id": 13,
        "name": "Michael Scott",
        "role": "Manager",
        "active": False,
        "score": 41.2,
    },
    {"id": 14, "name": "Nina Simone", "role": "User", "active": True, "score": 87.3},
    {"id": 15, "name": "Oscar Wilde", "role": "User", "active": True, "score": 55.8},
    {"id": 16, "name": "Penelope Cruz", "role": "User", "active": False, "score": 66.4},
    {"id": 17, "name": "Quinn Fabray", "role": "User", "active": True, "score": 71.2},
    {"id": 18, "name": "Ray Charles", "role": "Admin", "active": True, "score": 91.0},
    {
        "id": 19,
        "name": "Sarah Connor",
        "role": "Manager",
        "active": True,
        "score": 89.4,
    },
    {"id": 20, "name": "Tom Hardy", "role": "User", "active": False, "score": 33.5},
    {
        "id": 21,
        "name": "Ursula Dittmeyer",
        "role": "User",
        "active": True,
        "score": 77.1,
    },
    {
        "id": 22,
        "name": "Victor Frankenstein",
        "role": "User",
        "active": True,
        "score": 60.0,
    },
    {
        "id": 23,
        "name": "Wendy Darling",
        "role": "Admin",
        "active": False,
        "score": 84.2,
    },
    {
        "id": 24,
        "name": "Xavier Hernandez",
        "role": "User",
        "active": True,
        "score": 79.9,
    },
    {"id": 25, "name": "Yolanda Adams", "role": "User", "active": True, "score": 65.3},
    {
        "id": 26,
        "name": "Zachary Levi",
        "role": "Manager",
        "active": True,
        "score": 82.1,
    },
    {"id": 27, "name": "Amy Farrah", "role": "User", "active": False, "score": 48.7},
    {"id": 28, "name": "Bruce Wayne", "role": "Admin", "active": True, "score": 99.9},
    {"id": 29, "name": "Clark Kent", "role": "User", "active": True, "score": 90.1},
    {
        "id": 30,
        "name": "David Tennant",
        "role": "Manager",
        "active": False,
        "score": 73.4,
    },
    {"id": 31, "name": "Emma Watson", "role": "User", "active": True, "score": 85.6},
    {
        "id": 32,
        "name": "Freddie Mercury",
        "role": "User",
        "active": True,
        "score": 94.2,
    },
    {"id": 33, "name": "Gina Linetti", "role": "User", "active": False, "score": 15.5},
    {"id": 34, "name": "Harry Potter", "role": "Admin", "active": True, "score": 81.3},
    {"id": 35, "name": "Iris West", "role": "User", "active": True, "score": 70.8},
    {"id": 36, "name": "John Doe", "role": "User", "active": False, "score": 50.0},
    {"id": 37, "name": "Kate Austen", "role": "Manager", "active": True, "score": 76.4},
    {"id": 38, "name": "Luke Skywalker", "role": "User", "active": True, "score": 93.1},
    {"id": 39, "name": "Mary Jane", "role": "User", "active": True, "score": 68.5},
    {"id": 40, "name": "Ned Stark", "role": "Admin", "active": False, "score": 52.3},
    {
        "id": 41,
        "name": "Oliver Queen",
        "role": "Manager",
        "active": True,
        "score": 86.7,
    },
    {"id": 42, "name": "Peter Parker", "role": "User", "active": True, "score": 88.9},
    {
        "id": 43,
        "name": "Quentin Tarantino",
        "role": "User",
        "active": False,
        "score": 44.1,
    },
    {"id": 44, "name": "Rachel Green", "role": "User", "active": True, "score": 63.2},
    {"id": 45, "name": "Steve Rogers", "role": "Admin", "active": True, "score": 97.2},
    {"id": 46, "name": "Tony Stark", "role": "Manager", "active": True, "score": 99.1},
    {"id": 47, "name": "Uma Thurman", "role": "User", "active": False, "score": 58.4},
    {"id": 48, "name": "Valerie Perez", "role": "User", "active": True, "score": 72.0},
    {"id": 49, "name": "Wanda Maximoff", "role": "User", "active": True, "score": 91.6},
    {"id": 50, "name": "Xena Warrior", "role": "Admin", "active": True, "score": 89.8},
    {
        "id": 51,
        "name": "Yanni Chryssomallis",
        "role": "User",
        "active": False,
        "score": 39.5,
    },
    {"id": 52, "name": "Zane Grey", "role": "User", "active": True, "score": 62.1},
    {"id": 53, "name": "Arthur Dent", "role": "User", "active": True, "score": 42.0},
    {"id": 54, "name": "Barry Allen", "role": "Manager", "active": True, "score": 94.7},
    {"id": 55, "name": "Carol Danvers", "role": "Admin", "active": True, "score": 96.3},
    {"id": 56, "name": "Danny Rand", "role": "User", "active": False, "score": 51.2},
    {
        "id": 57,
        "name": "Ellen Ripley",
        "role": "Manager",
        "active": True,
        "score": 92.9,
    },
    {"id": 58, "name": "Ford Prefect", "role": "User", "active": True, "score": 73.0},
    {"id": 59, "name": "Gwen Stacy", "role": "User", "active": True, "score": 80.5},
    {"id": 60, "name": "Hank Pym", "role": "Admin", "active": False, "score": 67.8},
]

for index, user in enumerate(mock_user_data[10:20]):
    serial_number = index + 1
    print(f"{serial_number}: {user['name']}")
