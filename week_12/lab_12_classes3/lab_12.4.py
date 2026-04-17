class LinearEquation:
    def __init__(self, m, b):
        self.m = m
        self.b = b

    def __add__(self, equation_2):
        # update slope and y-intercept
        new_m = self.m + equation_2.m
        new_b = self.b + equation_2.b

        # save new numbers to an equation
        third_equation = LinearEquation(new_m, new_b)

        return third_equation
    
    def __str__(self):
        # prints in the format y = mx + b
        return f"y = {self.m}x + {self.b}"
    
eq1 = LinearEquation(2,3)
eq2 = LinearEquation(-1,5)
eq3 = eq1 + eq2

print(eq3)
