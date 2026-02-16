def output_even(first, last):
    lysp = []
    for numer in range(first, last):
        if numer % 2 == 0:
            lysp += numer
    print(lysp)

output_even(37, 1050)
output_even(1,2000)