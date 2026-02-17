def add_lists(list1, list2):
    lyst = []
    for spot in range(len(list1)):
        lyst.append(list1[spot]+list2[spot])
    print(lyst)

add_lists([1, 3, 3, 1], [4, 3, 6, 1])
add_lists([1, 8, 5, 0, -7], [0, -7, 4, 2, -6])
add_lists([1, 2], [-1, 1])