def skip_letter(thang):
    lysp = []
    for character in range(0, len(thang), 2):
            lysp += thang[character]
    print(lysp)


skip_letter("counterattack")
skip_letter("banana sunday")