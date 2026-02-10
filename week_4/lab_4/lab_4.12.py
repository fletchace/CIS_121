int1 = int(input("Enter Integer: "))
int2 = int(input("Enter Integer: "))

for number in range(1,int1+1):
    for number2 in range(1,int2+1):
        print(f"{number*number2:3}", end = ' ')
    print()