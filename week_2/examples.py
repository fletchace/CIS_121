import math

#Question 1
chicken_legs = int(input("How many chickens do you have? "))*2
cow_legs = int(input("How many cows do you have? "))*4
pig_legs = int(input("How many pigs do you have? "))*4
total_legs = chicken_legs + cow_legs + pig_legs
print(f"You have {total_legs} legs.")

#Question 2
two_pointers = int(input("How many 2 pointers? "))*2
three_pointers = int(input("How many 3 pionters? "))*3
total_points = two_pointers + three_pointers
print(f"You scored {total_points} points!")

#Question 3
height=int(input("Gimmie da height: "))
top_base=int(input("Gimmie da top: "))
base=int(input("Gimmie da base: "))
trapazoid_area = ((top_base + base)/2)*height
print(f"Yer area is {trapazoid_area} bruh. Duh")

#Question 4
tiangl_base = int(input("Gimmie da base boi: "))
tiangl_height = int(input("Gimmie dur height: "))
tiangl_volume = (((tiangl_base ** 2)*tiangl_height)/3)
print(f"Da volum is {tiangl_volume}.")

#Question 5
spere_radius = int(input("Gimmie da radius boi: "))
spere_height = int(input("Gimmie dur height: "))
spere_volume = (math.pi*(spere_radius ** 2) * spere_height)
print(f"Tha cindar volum is {spere_volume}.")