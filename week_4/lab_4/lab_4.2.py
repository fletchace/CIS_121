word = input("")
count = 1
for letter in word:
    if count %2 == 0:
        print(letter)
    count += 1