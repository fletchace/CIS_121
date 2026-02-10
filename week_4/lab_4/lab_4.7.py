word = ''
flag = True
while flag == True:
    letter = input("Give me a letter (or type 'done'): ")
    if letter == 'done':
        flag = False
    else:
        word += letter
print(word)