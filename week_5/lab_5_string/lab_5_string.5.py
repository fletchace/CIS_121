def is_isogram(word):
    letter_count = 0
    for letter in word:
        for letters in word:
             if letters == letter:
                  letter_count += 1
    if letter_count > len(word):
        print("Not Isogram")
    else:
        print("Is Isogram")

is_isogram("algorithm")
is_isogram("password")
is_isogram("consecutive")
is_isogram("python")

def optimal_isogram(word):
    seen = ""
    for letter in word:
        if letter in seen:
            print("No Isogram")
        seen += letter
    print("Is Isogram")
