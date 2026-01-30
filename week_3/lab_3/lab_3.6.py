from random import randint
value = randint(0,1) #picks a random integer. Either 0 or 1.
guess = input("Guess heads or tails: ")
if guess == "heads":
    if value == 0:
        print("Correct!!!")
    else:
        print("*LOUD INCORRECT BUZZER SOUND*")
if guess == "tails":
    if value == 1:
        print("Correct")
    else:
        print("*LOUD INCORRECT BUZZER SOUND*")