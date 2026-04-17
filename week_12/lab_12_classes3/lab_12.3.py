import math

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __eq__(self, numer):
        if self.a == numer.a and self.b == numer.b:
            return True
        else:
            return False
    def __str__(self):
        return f"{self.a} + {self.b}i"

number1 = ComplexNumber(1,2)
number2 = ComplexNumber(1,2)

print(number1.__eq__(number2))