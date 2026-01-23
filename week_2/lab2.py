import math

#Question 1
pig_legs=int(input("How many pigs do you have?: "))*4
chicken_legs=int(input("How many chickens do you have?: "))*2
cow_legs=int(input("How many cows do you have?: "))*4
total_legs=pig_legs+chicken_legs+cow_legs
print(f"The total amount of legs on your farm is {total_legs}.")

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
cylindar_radius = int(input("Gimmie da radius boi: "))
cylindar_height = int(input("Gimmie dur height: "))
cylindar_volume = (math.pi*(cylindar_radius ** 2) * cylindar_height)
print(f"Tha cindar volum is {cylindar_volume}.")

#Question 6
sphere_radius = int(input("give me the sphere radius: "))
sphere_volume = (4/3) * math.pi * (sphere_radius ** 3)
print(f"The sphere volume is {sphere_volume}.")

#Question 7
cone_radius = int(input("Give me the radius: "))
cone_height = int(input("Give me the height: "))
cone_volume = math.pi * (((cone_radius ** 2) * cone_height) / 3)
print(f"The cone volume is {cone_volume}.")

#Question 8
semi_radius = int(input("Give me the radius: "))
semi_area = (1/2) * math.pi * (semi_radius ** 2)
print(semi_area)