def first_letters(sentence):
    count = 0
    for letter in sentence:
        if count == 0:
            print(letter, end = '')
        if letter == ' ':
            count = 0
        else:
            count += 1
    print()

first_letters("wingardium leviosa makes objects float")
first_letters("expecto patronum repels dementors")
first_letters("the magic is within you")