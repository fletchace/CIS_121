def hailstone_seq(numer = 40):
    workin_wid_it = numer
    print(workin_wid_it)
    while workin_wid_it != 1:
        if workin_wid_it % 2 == 0:
            workin_wid_it /= 2
            print(workin_wid_it)
        elif workin_wid_it % 2 == 1:
            workin_wid_it = (3 * workin_wid_it) + 1
            print(workin_wid_it)

hailstone_seq(25) # → 25, 76, 38, 19, 58, ..., 8, 4, 2, 1
hailstone_seq(40) # → 40, 20, 10, 5, 16, 8, 4, 2, 1
hailstone_seq() # → 40, 20, 10, 5, 16, 8, 4, 2, 1