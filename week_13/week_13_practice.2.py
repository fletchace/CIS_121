number_file = open("week_13\\numbers.txt")

data = number_file.readlines()

total = 0
count = 0

for number in data:
    #print(number.strip())
    total += int(number.strip())
    count += 1

average = total / count

print(average)


family_file = open("week_13\\family.csv",'r')

for line in family_file.readlines()[1:]:
    line_data = line.split(',')
    first_name = line_data[0]
    last_name = line_data[1]
    age = int(line_data[2])
    count += 1
    total += age

mean = total / count
print(mean)
