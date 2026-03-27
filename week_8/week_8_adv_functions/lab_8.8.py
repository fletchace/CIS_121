def descending_order(num1, num2 = 15, num3 = 5):
    if num1 >= num2 >= num3:
        print(num1, num2, num3)
    elif num1 >= num3 >= num2:
        print(num1, num3, num2)
    elif num2 >= num1 >= num3:
        print(num2, num1, num3)
    elif num2 >= num3 >= num1:
        print(num2, num3, num1)
    elif num3 >= num2 >= num1:
        print(num3, num2, num1)
    elif num3 >= num1 >= num2:
        print(num3, num1, num2)

descending_order(2, 3, 1) # [3, 2, 1]
descending_order(10) # [15, 10, 5]
descending_order(2, 45) # [45, 5, 2]