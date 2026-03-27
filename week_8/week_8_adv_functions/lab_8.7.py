def ascending_order(num1, num2 = 5, num3 = 25):
    if num1 <= num2 <= num3:
        print(num1, num2, num3)
    elif num1 <= num3 <= num2:
        print(num1, num3, num2)
    elif num2 <= num1 <= num3:
        print(num2, num1, num3)
    elif num2 <= num3 <= num1:
        print(num2, num3, num1)
    elif num3 <= num2 <= num1:
        print(num3, num2, num1)
    elif num3 <= num1 <= num2:
        print(num3, num1, num2)


ascending_order(2, 3, 1) # → [1, 2, 3]
ascending_order(10, 1) # → [1, 10, 25]
ascending_order(50) # → [5, 25, 50]