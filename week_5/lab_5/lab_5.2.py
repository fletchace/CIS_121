def is_fever(temp):
    temperature = float(temp[:-1])
    system = temp[-1]
    if system == 'F':
        if float(temperature) > 98.6:
            print("Has fever :(")
        else:
            print("No fever :)")
    if system == 'C':
        if float(temperature) > 37:
            print("Has fever :(")
        else:
            print("No fever :)")
is_fever("99F")
is_fever("37C")
is_fever("98F")