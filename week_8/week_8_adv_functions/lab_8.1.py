from random import randint
def toss_coin(guess = 0):
    value = randint(0,1) #picks a random integer. Either 0 or 1.
    if guess == value:
        print("Correct!")
    else:
        print("YOU HAVE BEEN SENT TO the_littlest_jeffrey's PRIVATE ISLAND TO BE DIDDLED")

toss_coin() # "Correct!" (if the random value is 0) or "Incorrect!" (if the random value is 1)
toss_coin(0) # "Correct!" (if the random value is 0) or "Incorrect!" (if the random value is 1)
toss_coin(1) # "Correct!" (if the random value is 1) or "Incorrect!" (if the random value is 0)