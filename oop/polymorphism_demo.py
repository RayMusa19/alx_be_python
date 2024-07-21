import math

class Shape:
    def area(self):
        raise NotImplementedError("Derived classes need to override this method")

    def __str__(self):
        return f"{self.area}"

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        self.Area = self.length * self.width
        return self.Area
        
    def __str__(self):
        return f"{self.Area}"
    
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        self.Area = math.pi * (self.radius ** 2)
        return self.Area

    def __str__(self):
        return f"{self.Area}"
