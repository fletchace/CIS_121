def count_repetitions(lyst):
    new_dict = {}
    for thang in lyst:
        if thang in new_dict:
            new_dict[thang] += 1
        else:
            new_dict[thang] = 1
    ordered_dict = {}
    while new_dict:
        most = 0
        thing = ''
        for element, how_many in new_dict.items():
            if how_many > most:
                most = how_many
                thing = element
        ordered_dict[thing] = most
        del new_dict[thing]
    print(ordered_dict)
    

count_repetitions(["cat", "dog", "cat", "cow", "cow", "cow"]) 
# → {"cow": 3, "cat": 2, "dog": 1}
count_repetitions([1, 5, 5, 5, 12, 12, 0, 0, 0, 0, 0, 0])
# → {0: 6, 5: 3, 12: 2, 1: 1}
count_repetitions(["Infinity", "null", "Infinity", "null", "null"])
# → {"null": 3, "Infinity": 2}