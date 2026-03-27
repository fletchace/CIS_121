def find_youngest(people):
    youngest_age = 100
    youngest_bih = ''
    for person, age in people.items():
        if age < youngest_age:
            youngest_age = age
            youngest_bih = person
    print(youngest_bih)

find_youngest({"Emma": 71, "Jack": 45, "Olivia": 82, "Liam": 39})  # → "Liam"
find_youngest({"Sophia": 50, "Mason": 68, "Ava": 67, "Noah": 33})  # → "Noah"
find_youngest({"Ethan": 25, "Lucas": 30, "Mia": 29})  # → "Ethan"