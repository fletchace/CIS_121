def flip_flop(word):
    if len(word) % 2 == 0:
        length = int(len(word))
        half_int = int(length/2)
        first_half = word[:half_int]
        second_half = word[half_int:]
        print(f"{second_half}{first_half}")
    if len(word) % 2 == 1:
        length = int(len(word))
        half_int = int(length/2)
        first_half = word[:half_int]
        middle_letter = word[half_int]
        second_half = word[half_int+1:]
        print(f"{second_half}{middle_letter}{first_half}")

flip_flop("python")
flip_flop("programming")