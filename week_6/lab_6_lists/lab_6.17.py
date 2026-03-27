def war_of_numbers(armys):
    odds = 0
    evens = 0
    for number in armys:
        if number % 2 == 0:
            evens += number
        elif number % 2 == 1:
            odds += number
    if odds > evens:
        print("Odds")
    elif evens > odds:
        print("Evens")
    else:
        print("Tie?")
war_of_numbers([2, 8, 7, 5])
war_of_numbers([12, 90, 75, 1, 1])
war_of_numbers([2, 10, 22, 243])
war_of_numbers([5, 2, 10, 243])