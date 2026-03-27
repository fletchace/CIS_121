def count_duplicates(num1 = 0, num2 = 0, num3 = 0):
    lyst = [num1, num2, num3]
    dictionary = {}
    most = 0
    for number in lyst:
        if number in dictionary:
            dictionary[number] += 1
        else:
            dictionary[number] = 1
    for how_many in dictionary.values():
        if how_many > most:
            most = how_many
    if most == 1:
        print("Each number is unique")
    else:
        print(f"There are {most} of the same number")

count_duplicates(2, 3, 2) # "There are 2 of the same number"
count_duplicates(4, 4, 4) # "There are 3 of the same number"
count_duplicates(1, 2, 3) # "Each number is unique"
count_duplicates(1) # "There are 2 of the same number"
count_duplicates(0) # "There are 3 of the same number"