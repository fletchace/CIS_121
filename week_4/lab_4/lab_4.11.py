width = int(input("Enter width: "))
length = int(input("Enter length: "))
pattern = input("Enter pattern: ")

print("Your rug is: ")
for len in range(length+1):
    print(width*pattern, end = " ")
    print()