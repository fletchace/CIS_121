def find_factors(numer):
    lyst = []
    for num in range(1,numer+1):
        if numer % num == 0:
            lyst.append(num)
    print(lyst)

find_factors(12)
find_factors(17)
find_factors(36)