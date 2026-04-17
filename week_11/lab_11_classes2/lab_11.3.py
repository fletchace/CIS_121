class Droid:
    def __init__(self, designation, series):
        # Class Variables
        self._designation = designation
        self._series = series

    def get_series(self):
        return self._series

    def set_series(self, new_series):
        self._series = new_series

    def communicate(self):
        return "Bleep-Bloop-Blop"
    
    def __str__(self):
        return f"Droid designation: {self._designation} series: {self._series}"


class Starship:
    def __init__(self, name):
        self._starship_name = name
        self._starship_droids = []   # starts with NO droids

    def add_droid(self, droid):
        self._starship_droids.append(droid)

    def droids_communicate(self):
        for d in self._starship_droids:
            print(d.communicate())

    def __str__(self):
        return f"Starship: {self._starship_name} with {len(self._starship_droids)} droids"
    
# Create droids
d1 = Droid("R2-D2", "Astromech")
d2 = Droid("C-3PO", "Protocol")

# Create starship
falcon = Starship("Millennium Falcon")

# Add droids
falcon.add_droid(d1)
falcon.add_droid(d2)

# Make all droids communicate
falcon.droids_communicate()