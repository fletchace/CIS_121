def list_battle(list1, list2):
    sum_list1 = 0
    sum_list2 = 0
    for number in list1:
        sum_list1 += number
    for number in list2:
        sum_list2 += number
    if list1 > list2:
        print(list1)
    elif list1 < list2:
        print(list2)
    else:
        print(f"Tie? {list1}")

list_battle([1, 4, 7, 6, 4, 3, 65], [45, 2, 9, 10, 4, 3])