import random
number_file = open("week_13\\numbers.txt", "w")

for index in range(100):
    number = random.randint(300,750)
    number_file.write(str(number) + "\n")

number_file.close()


#str(3) = "3"
