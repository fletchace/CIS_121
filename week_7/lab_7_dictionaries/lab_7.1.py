def oldest_bih(people):
    oldest_peep = ''
    peep_age = 0
    for peep in people:
        if people[peep] > peep_age:
            oldest_peep = peep
            peep_age = people[peep]
    print(oldest_peep)
    

oldest_bih({"Emma": 71,"Jack": 45,"Olivia": 82,"Liam": 39}) #Olivia
oldest_bih({"Sophia": 50,"Mason": 68,"Ava": 67,"Noah": 33}) 
oldest_bih({"Ethan": 25,"Lucas": 30,"Mia": 29})