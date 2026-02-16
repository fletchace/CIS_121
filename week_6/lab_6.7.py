def ascending_order(num1, num2, num3):
    lyst = []
    if num1 <= num2 <= num3:
        lyst.append(num1, num2, num3)
    elif num1 <= num3 <= num2:
        lyst.append(num1, num3, num2)
    elif num2 <= num1 <= num3:
        lyst.append(num2, num1, num3)
    elif num2 <= num3 <= num1:
        lyst.append(num2, num3, num1)
    elif num3 <= num2 <= num1:
        lyst.append(num3, num2, num1)
    elif num3 <= num1 <= num2:
        lyst.append(num3, num1, num2)
    print(lyst)

ascending_order(3,2,1)
ascending_order(10,1,25)
ascending_order(2,45,4)