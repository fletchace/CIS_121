def output_odd(first, last):
    lysp = []
    for numer in range(first, last+1):
        if numer % 2 == 1:
            lysp.append(numer)
    print(lysp)

output_odd(37, 110)
output_odd(1,200)
output_odd(50,199)