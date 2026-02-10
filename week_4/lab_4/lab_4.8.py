flag = True
total = 0
while flag == True:
    integer = int(input("Give me an integer: "))
    if integer < 0:
        break
    else:
        total += integer

print(total)