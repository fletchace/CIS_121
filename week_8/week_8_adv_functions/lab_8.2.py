from random import randint
def guess(thing = "even"):
    value = randint(0,9) #picks a random integer between 0-9 inclusive
    if thing == "even":
        if value % 2 == 0:
            print("I suppose thats right")
        else:
            print("You're diddled, sorry, it was me")
    if thing == "odd":
        if value % 2 == 1:
            print("I suppose thats right")
        else:
            print("You're diddled, sorry, it was Jeffrey")

guess() # "Correct!" (if random value is even) or "Incorrect!" (if random value is odd)
guess("odd") # "Correct!" (if random value is odd) or "Incorrect!" (if random value is even)
guess("even") # "Correct!" (if random value is even) or "Incorrect!" (if random value is odd)