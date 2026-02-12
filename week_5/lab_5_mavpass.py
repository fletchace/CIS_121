

def decode_rle(string):
    final = ''
    pattern = ''
    how_many = ''
    how_many_number = 0
    count = 0
    for char in string:
        if count > 0:
            how_many_number = int(how_many)
            final = final + (pattern * how_many)
        if char != '0' and char != '1' and char != '2' and char != '3' and char != '4' \
            and char != '5' and char != '6' and char != '7' and char != '8' and char != '9':
            pattern = ''
            how_many = ''
            how_many_number = 0
            pattern += char
            count += 1
        else:
            how_many += char
    print(final)

decode_rle("a3b1c12")