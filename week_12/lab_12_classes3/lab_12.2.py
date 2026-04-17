import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other_vector):
        if self.x == other_vector.x and self.y == other_vector.y:
            return True
        else:
            return False
    def distance_apart(self, other_vector):
        distance = math.sqrt((self.x-other_vector.x)**2 + (self.y-other_vector.y)**2)
        return distance
    def __str__(self):
        return f"({self.x}, {self.y})"

vector1 = Vector(3,4)
vector2 = Vector(0,0)

print(vector1.__eq__(vector2))
print(vector1.distance_apart(vector2))
print(vector1.__str__())
print(vector2.__str__())