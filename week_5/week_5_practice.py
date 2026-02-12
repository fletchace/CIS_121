'''
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

lisp = ['a', 'apple', 7, 12.1, True, 456]

print(lisp[1:4+1])

for thang in lisp[1:4+1]:
    print(thang)

for numer in range(len(lisp)):
    print(numer)
'''
'''
sentence = "I gotta get out of here and go eat some food at the cafeteria and after that I am going to go to the CSU and do some homework for my calculus class."
for letter in sentence:
    word_lyst = []
    count = 1
    if count != 0:
        print(letter, end = '')
    if letter == ' ':
        count = 0
        print()

sentence = "I gotta get out of here and go eat some food at the cafeteria and after that I am going to go to the CSU and do some homework for my calculus class."
word_lyst = []
new_word = ''
for letter in sentence:
    if letter != ' ':
        new_word += letter
    if letter == ' ':
        word_lyst.append(new_word)
        new_word = ''
word_lyst.append(new_word)
for element in word_lyst:
    print(element)

def sentence_to_words(sent):
    word_lyst = []
    found_word = ''
    for letter in sent:
        if letter == " ":
            word_lyst.append(found_word)
        else:
            fount_word += letter
    return word_lyst

sample_sentence = "I gotta get out of here and go eat some food at the cafeteria and after that I am going to go to the CSU and do some homework for my calculus class."
words = sentence_to_words (sample_sentence)
for word in words:
    print(words)
'''
sentence = "I gotta get out of here and go eat some food at the cafeteria and after that I am going to go to the CSU and do some homework for my calculus class."
words = sentence.split()

for word in words:
    print(word)