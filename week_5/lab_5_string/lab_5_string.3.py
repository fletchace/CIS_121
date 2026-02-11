def is_boiling(temp):
    temperature = float(temp[:-1])
    system = temp[-1]
    if system == 'F':
        if float(temperature) >= 212:
            print("Is Boiling")
        else:
            print("No Boil")
    if system == 'C':
        if float(temperature) >= 100:
            print("Is Boiling")
        else:
            print("No Boil")
is_boiling("212F")
is_boiling("100C")
is_boiling("0F")