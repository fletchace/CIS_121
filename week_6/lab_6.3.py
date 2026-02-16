def output_even(first, last):
    lysp = []
    for numer in range(first, last+1):
        if numer % 2 == 0:
            lysp.append(numer)
    print(lysp)

output_even(37, 1050)
output_even(1,2000)