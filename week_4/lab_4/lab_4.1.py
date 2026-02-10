larger = int(input("Larger number: "))
smaller = int(input("Smaller number: "))
count = 0
fletcher = larger
while fletcher > smaller:
    fletcher = fletcher // 2
    count += 1
print(count)