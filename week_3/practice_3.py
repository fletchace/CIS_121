
num = 1
total = 0

while num <= 6:
    if num %2 == 1:
        total += num
    num += 1

print(f"total = {total}")

purchased=int(input("How many units were purchased?: "))
max_number_of_units = 0
budget = 400

while purchased <= 10000:
    if purchased <= 100:
        price = 3.99
    else:
        if purchased <= 300:
            price = 2.99
        else:
            price = 1.99
    total_cost = price * purchased
    print(f"The cost of {purchased} is {round(total_cost,2)}")
    if total_cost < budget and purchased > max_number_of_units:
        max_number_of_units = purchased
    purchased = purchased + 1

print(f"The max number of units for $400 is {max_number_of_units}")


num = 1
total = 0

while num <= 6:
    if num %2 == 1:
        total += num
    num += 1

print(f"total = {total}")