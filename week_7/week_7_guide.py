# How to Iterate through a dictionary ?

# First if we create a dictionary , key is the Star ID an

# {Key = Star ID : Value = Name}
studentDict = {"Z26767Z" : "Rousslang Rebecca" ,
               "AB4261I" : "Matt Priem" ,
               "OP1242I" : "Shane Zimmerman"}

# This just gets the values (name)
for name in studentDict.values():
    print(name)

# This just gets the keys (techId)
for techId in studentDict.keys():
    print(techId)

# We can access Star ID and Name this way:
for techid in studentDict:
    # This iterates Tech ID and gets the name
    name = studentDict[techid]
    print(name)

# This also works, gets key and value at the same time !
for techid, name in studentDict.items():
    print(techid)
    print(name)