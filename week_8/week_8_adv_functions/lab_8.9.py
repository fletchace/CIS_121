def get_indices(lysp, value = 0):
    lyst = []
    count = 0
    for numer in lysp:
        if numer == value:
            lyst.append(count)
            count += 1
        else:
            count += 1
    print(lyst)


get_indices([1, 0, 5, 0, 7]) # [1, 3]
get_indices([1, 5, 5, 2, 7], 7) # [4]
get_indices([1, 5, 5, 2, 7]) # []
get_indices([1, 5, 5, 2, 7], 5) # [1, 2]
get_indices([1, 5, 5, 2, 7], 8) # []
get_indices(["a", "a", "b", "a", "b", "a"], "a") # [0, 1, 3, 5]