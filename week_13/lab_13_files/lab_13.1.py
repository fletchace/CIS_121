import random
quiz_ints = open("week_13\\lab_13_files\\QuizInts.txt", "w")

for numbers in range(100):
    number = random.randint(50,200)
    quiz_ints.write(str(number) + "\n")

quiz_ints.close()