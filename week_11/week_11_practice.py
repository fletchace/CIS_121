import math
class Star:
    def __init__(self, name):
        self._name = name
    
    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        self._name = new_name

    def __str__(self):
        return f"hello from star {self.get_name()}"

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
        return 4/3 * math.pi * self._radius ** 3
    
    def get_density(self):
        return self._mass / self.get_volume()
    
    def set_name(self, new_name):
        self._name = new_name
    
    def __str__(self):
        return f"hello from planet {self.get_name()}"

class PlanetarySystem:
    # A planetary system should have a single star and any amount of planets
    def __init__(self, name, star):
        self._name = name
        self._star = star
        self.planet_list = []

    def add_planet(self, planet):
        self.planet_list.append(planet)
    
    def show_planets(self):
        for planet in self.planet_list:
            print(planet)
    
    def change_star_name(self, new_name):
        self._star.set_name(new_name)

    def rename_planet(self, old_name, new_name):
        for planet in self.planet_list:
            if planet.get_name() == old_name:
                planet.set_name(new_name)

# ----- testing your code -----

sun = Star("Galactic Goober")
solar_system = PlanetarySystem("Solar System", sun)

solar_system.add_planet(Planet("x25", 45, 198, 1000))
solar_system.add_planet(Planet("Gornar", 12, 23, 456))

print("Before rename:")
solar_system.show_planets()

solar_system.rename_planet("x25", "x26")

print("\nAfter rename:")
solar_system.show_planets()

solar_system.change_star_name("Sol")
print("\nStar name:", sun.get_name())