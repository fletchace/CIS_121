coinage = int(input("How many knuts: "))
galleon = ''
sickle = ''
knuts = ''
if coinage >= 493:
    galleon = int(coinage/493)
    coinage -= int(galleon) * 493
elif coinage >=29:
    sickle = int(coinage/29)
    coinage -= int(sickle) * 29
else:
    knuts = coinage
print(f"{galleon} galleons {sickle} sickles {knuts} knuts")