number = 1
largest = 0
while number > 0:
    number = int(input("Give me numer: "))
    if number > largest:
        if number % 2 == 0:
            largest = number
    if number == 1:
        largest = -1
print(largest)