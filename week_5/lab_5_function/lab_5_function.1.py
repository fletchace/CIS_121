def reverse_until(word, stop):
    reverse = ''
    for letter in word:
        while letter != stop:
            reverse = letter + reverse
    print(reverse)
reverse_until("programming","m")