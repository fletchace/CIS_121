def reverse_until(word, stop):
    reverse = ''
    for letter in word:
        if (letter != stop):
            reverse = letter + reverse
        else:
            break
    print(reverse)
reverse_until("programming","m")