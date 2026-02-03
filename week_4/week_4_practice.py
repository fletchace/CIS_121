def count_letters(word, test_letter):
    count = 0
    for letter in word:
        if letter == test_letter:
            count += 1
    print(f"the number of {test_letter}'s in {word} is {count}.")
word1 = "well watermelon tastes swell"
count_letters(word1, 'l')
word2 = "taco tuesday"
count_letters(word2, 't')
flag = 0
def count_even(lower_bound, upper_bound):
    for number in range(lower_bound, upper_bound+1):
        if number %2 == 0:
            if flag %2 == 1:
                flag += 1
                print(number)

count_even(2, 10)
count_even(3, 15)
count_even(7,20)