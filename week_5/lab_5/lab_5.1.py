def reverse_string(word):
    back = ''
    for letter in word:
        back = letter + back
    print(back)

reverse_string("programming")
reverse_string("python")
reverse_string("hello")