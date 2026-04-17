import math

class Vector:
    def __init__(self, a, b):
        self._a = a
        self._b = b
    
    def __eq__(self, other_vector):
        if self._a == other_vector._a and self._b == other_vector._b:
            return True
        else:
            return False
    
    def __str__(self):
        return f"({self._a}, {self._b})"
    
vector1 = Vector(6, 7)
vector2 = Vector(6, 7)

if vector1 == vector2:
    print("They are the same")
else:
    print("They are different")