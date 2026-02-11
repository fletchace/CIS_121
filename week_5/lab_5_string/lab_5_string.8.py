def last_letters(sentence):
    count = 0
    last_letter = ''
    for letter in sentence:
        if letter == ' ':
            count = 0
        if count == 0:
            print(last_letter, end = '')
        count += 1
        last_letter = letter
    print(sentence[-1], end = '')
    print()

last_letters("wingardium leviosa makes objects float")
last_letters("expecto patronum repels dementors")
last_letters("the magic is within you")