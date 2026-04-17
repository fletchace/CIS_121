class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    def get_x(self):
        return self._x
    def get_y(self):
        return self._y
    def __str__(self):
        msg = f'({self._x},{self._y})'
        return msg
    def __add__(self, other):
        new_x = self._x + other.get_x()
        new_y = self._y + other.get_y()
        return Point(new_x,new_y)

p1 = Point(3,4)
p2 = Point(7,12)
p3 = p1 + p2
p4 = Point(1,1)
p5 = p3 + p4

print(p1)
print(p2)
print(p3)
print(p4)
print(p5)