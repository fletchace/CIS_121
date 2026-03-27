def return_unique(numbers):
    seen = {}
    unique = []
    for numer in numbers:
        if numer in seen:
            seen[numer] += 1
        else:
            seen[numer] = 1
    for number, how_many in seen.items():
        if how_many == 1:
            unique.append(number)
    print(unique)

return_unique([1, 9, 8, 8, 7, 6, 1, 6]) # [9, 7],
return_unique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]) # [2, 1],
return_unique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]) # [5, 6]