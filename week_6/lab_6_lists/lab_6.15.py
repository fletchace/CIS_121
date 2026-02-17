def count_cards(cards):
    count = 0
    for card in cards:
        if card == 2 or card == 3 or card == 4 or card == 5 or card == 6:
            count += 1
        elif card == 10 or card == 'j' or card == 'q' or card == 'k' or card == 'a':
            count -= 1
    print(count)

count_cards([5, 9, 10, 3, 'j', 'a', 4, 8, 5])
count_cards([ 'a', 'a', 'k', 'q', 'q', 'j'])
count_cards([ 'a', 5, 5, 2, 6, 2, 3, 8, 9, 7])
