def total_calories(fruits):
    calories = {"apple":95,"banana":105,"orange":62,"grape":3,"pear":102}
    total = 0
    for frut in fruits:
        total += calories[frut]
    print(total)


total_calories([ "apple", "banana", "orange"]) #262 (since 95 + 105 + 62 = 262)
total_calories([ "grape", "grape", "grape", "grape", "grape"]) #15
total_calories([ "banana", "pear", "apple"]) #302