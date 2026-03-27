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

def optimal_isogram(word):
    seen = ""
    for letter in word:
        if letter in seen:
            return("Not Isogram")
            break
        seen += letter
    return("Is Isogram")

is_isogram("algorithm")
is_isogram("password")
is_isogram("consecutive")
print(optimal_isogram("racecar"))

