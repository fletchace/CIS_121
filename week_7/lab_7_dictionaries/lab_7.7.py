def find_unique(numbers):
    seen = {}
    for numer in numbers:
        if numer in seen:
            seen[numer] += 1
        else:
            seen[numer] = 1
    for number, how_many in seen.items():
        if how_many == 1:
            return number

print(find_unique([1, 2, 2, 3, 3, 4, 4])) # 1
print(find_unique([7, 8, 8, 9, 9, 10, 10])) # 7
print(find_unique([5, 6, 6, 7, 7, 8, 8, 5, 9])) # 9