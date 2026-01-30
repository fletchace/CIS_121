first_number = int(input("Give me a number: "))
second_number = int(input("Give me a number: "))
third_number = int(input("Give me a number: "))
smallest = ''
middle = '' 
largest = ''
if first_number < second_number and first_number < third_number:
    smallest = first_number
elif second_number < first_number and second_number < third_number:
    smallest = second_number
elif third_number < second_number and third_number < first_number:
    smallest = third_number
else:
    pass

if first_number > second_number and first_number > third_number:
    largest = first_number
elif second_number > first_number and second_number > third_number:
    largest = second_number
elif third_number > second_number and third_number > first_number:
    largest = third_number
else:
    pass

if int(smallest) == first_number and int(largest) == second_number:
    middle = third_number
elif int(smallest) == first_number and int(largest) == third_number:
    middle = second_number
elif int(smallest) == third_number and int(largest) == second_number:
    middle = first_number
elif int(smallest) == second_number and int(largest) == first_number:
    middle = third_number
elif int(smallest) == third_number and int(largest) == first_number:
    middle = second_number
elif int(smallest) == second_number and int(largest) == third_number:
    middle = first_number

print(smallest, middle, largest)