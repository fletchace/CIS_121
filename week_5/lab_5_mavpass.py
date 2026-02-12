

def decode_rle(string):
    final = ''
    pattern = ''
    how_many = ''
    how_many_number = 0
    count = 0
    flag = 0
    for char in string:
        if char != '0' and char != '1' and char != '2' and char != '3' and char != '4' \
            and char != '5' and char != '6' and char != '7' and char != '8' and char != '9':
            pattern += char
            count = 0
            flag += 1
        else:
            how_many += char
            count += 1
        if count == 0 and flag != 1:
            how_many_number = int(how_many)
            final = final + (pattern * how_many_number)
            pattern = ''
            how_many = ''
            how_many_number = 0
            count += 1
    print(final)

decode_rle("a3b1c12")