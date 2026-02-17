def hailstone_seq(numer):
    num = numer
    lysp = []
    while num != 1:
        lysp.append (num)
        if num % 2 == 0:
            num = num / 2
        elif num % 2 == 1:
            num = (3 * num) + 1
    print(lysp)

hailstone_seq(25)
hailstone_seq(40)