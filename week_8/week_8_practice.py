def greeting(name:str, age = "unknown"):
    if age == "unknown":
        print(f"Erm Dur {name}. Gimmie ur age stoopid!")
    elif name == "unknown":
        print(f"You're {age}, but what is your name?")
    else:
        print(f"Howdy, {name}! Wait you are {age} years old. EYUCK!!!")

greeting("tyrone", 19)
greeting("abardolf linkler", 17)
greeting("sharquisha")
greeting("scary terry", 30)