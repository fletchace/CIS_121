integer = int(input("Give me an integer: "))
while integer != 1:
    if integer % 2 == 0:
        integer = integer / 2
        print(integer)
    elif integer % 2 == 1:
        integer = 3*integer + 1
        print(integer)
    
print(int(integer))