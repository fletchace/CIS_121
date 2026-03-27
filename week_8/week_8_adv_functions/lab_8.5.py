def find_relation(name = "Plop"):
    if name == "Darth Vader":
        print("Father")
    elif name == "R2D2":
        print("Droid")
    elif name == "Leia":
        print("Sister")
    elif name == "Han":
        print("Brother in Law")
    else:
        print("Unknown")

find_relation("Darth Vader") #"Father",
find_relation("R2D2") #"Droid",
find_relation("Jabba the Hutt") #"Unknown"
find_relation( ) #"Unknown"