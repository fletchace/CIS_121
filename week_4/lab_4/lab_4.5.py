number = int(input("Give me number: "))
for num in range(1, number):
    if number % num == 0:
        print(num)