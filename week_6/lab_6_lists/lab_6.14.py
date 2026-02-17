def list_of_multiples(num,length):
    lyst = []
    for numer in range(1, length + 1):
        lyst.append(numer*num)
    print(lyst)
list_of_multiples(7, 5)
list_of_multiples(12, 10)
list_of_multiples(17, 6)