def greeting(name):
    print(f"Hello {name}. How are you?")

greeting("Fletcher")
greeting("Piece")

def add_three(number):
    number = number + 3
    return number

x = 10
print(x)
x = add_three(x)
print(x)

def max_of_three(n1,n2,n3):
    if n1 > n2:
        if n1 > n3:
            return n1
        return n3
    else:
        return n2

#take a word and determine if it has an x
count = 0
flag = 0
def x_in_word(word):
    for letter in word:
        if letter == "x":
            count += 1
        if letter == "y":
            flag += 1
    if count >= 1 and flag >= 1:
        return True
    return False

for num1 in range(1,5):
    for num2 in range(1,7):
        print(f'{num1*num2 :3.0f}', end = "")