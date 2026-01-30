starting_coinage = int(input("How many knuts: "))
coinage = starting_coinage
galleon = ''
sickle = ''
knuts = ''
if coinage >= 493:
    galleon = int(coinage/493)
    coinage -= int(galleon) * 493
    print(coinage)
if coinage >=29:
    sickle = int(coinage/29)
    coinage -= int(sickle) * 29
    print(coinage)
if coinage < 29:
    knuts = coinage
print(f"Given {starting_coinage} knuts you get,{galleon} galleon {sickle} sickles {knuts} knuts")