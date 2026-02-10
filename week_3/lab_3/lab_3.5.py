first_number = int(input("Give me a number: "))
second_number = int(input("Give me a number: "))
third_number = int(input("Give me a number: "))
if first_number < second_number and first_number < third_number:
    print(f"The smallest number is {first_number}.")
elif second_number < first_number and second_number < third_number:
    print(f"The smallest number is {second_number}.")
elif third_number < second_number and third_number < first_number:
    print(f"The smallest number is {third_number}.")
