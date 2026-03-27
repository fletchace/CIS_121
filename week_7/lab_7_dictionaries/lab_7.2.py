def letter_count(word):
    word_letters = {}
    for letter in word:
        if letter in word_letters:
            word_letters[letter] += 1
        else:
            word_letters[letter] = 1
    print(word_letters)


letter_count("hello") #{"h":1,"e":1,"l":2,"o":1}
letter_count("mississippi") #{"m":1,"i":4,"s":4,"p":2}
letter_count("apple") #{"a":1,"p":2,"l":1,"e":1}