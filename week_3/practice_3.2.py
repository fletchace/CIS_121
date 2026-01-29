for number in range(5,100+1):
    if number %2 == 0:
        print(number)

for number in range(6, 100+1, 2):
    print(number)

total=0
for number in range(2,7):
    if number %2 == 1:
        total += number
print(f"total = {total}")

number_to_add = 0
total_added = 0
while number_to_add != 'stop':
    number_to_add=input("Give me a number: ")
    if number_to_add != 'stop': 
        total_added += int(number_to_add)
print(f"total = {total_added}")