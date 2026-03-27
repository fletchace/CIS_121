import math
class Star:
    def __init__(self, name):
        self._name = name
    
    def get_name(self):
        return self._name
    def __str__(self):
        msg = f"hello from star {self.get_name()}"
        return msg
class Planet:
    def __init__(self, name, radius, mass, distance):
        self._name = name
        self._radius = radius
        self._mass = mass
        self._distance = distance
    
    def get_name(self):
        return self._name
    def get_radius(self):
        return self._radius
    def get_mass(self):
        return self._mass
    def get_distance(self):
        return self._distance
    def get_volume(self):
        volume = 4/3 * math.pi * self._radius ** 3
    def get_density(self):
        return self._mass / self.get_volume()
    def set_name(self, new_name):
        self._name = new_name
    def __str__(self):
        msg = f"hello from planet {self.get_name()}"
        return msg

planet1 = Planet("x25", 45, 198, 1000)
planet2 = Planet("Gornar", 12, 23, 456)
star1 = Star("poop")

print(planet1)
print(planet2)
print(star1)

#print(planet1.get_name())
#change = input("Wanna change name? yes/no ")
#if change == "yes":
#    change_name = input("What would you like to name the new planet? ")
#    planet1.set_name(change_name)
#print(planet1.get_name())

#print(planet2.get_name())