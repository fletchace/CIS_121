def is_isogram(word):
    dict_check = {}
    for letter in word:
        if letter in dict_check:
            return "False"
        else:
            dict_check[letter] = 1
    return "True"

print(is_isogram("algorism")) # → True
print(is_isogram("password")) # → False