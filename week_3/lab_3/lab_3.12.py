starting_coinage = int(input("How many knuts: "))
coinage = starting_coinage
galleon = 0
sickle = 0
knuts = 0
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

if galleon > 0:
    galleon_total = galleon, "galleons"
if sickle > 0:
    sickle_total = galleon, "galleons"
if knuts > 0:
    knuts_total = galleon, "galleons"
print(f"Given {starting_coinage} knuts you get,{galleon_total} {sickle_total} {knuts_total}")