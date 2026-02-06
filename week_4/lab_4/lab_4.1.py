num1 = int(input("Give me number: "))
num2 = int(input("Give me number: "))
maximum = max(num1,num2)
minimum = min(num1,num2)
count = 0
fletcher = maximum
while fletcher > minimum:
    fletcher = maximum // 2
    if fletcher > minimum:
        count += 1
print(count)