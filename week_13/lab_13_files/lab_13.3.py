my_name = open("week_13\\lab_13_files\\MyName.txt", "r")

name = my_name.read()

for letter in name:
    print(letter)

my_name.close()