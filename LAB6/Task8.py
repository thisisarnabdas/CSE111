import math

class Cylinder:
    radius = 5
    height = 18
    
    def __init__(self, radius, height):
        print(f"Default radius={Cylinder.radius} and height={Cylinder.height}")
        self.radius = radius
        self.height = height
        Cylinder.radius=self.radius
        Cylinder.height=self.height
        print(f"Updated radius={Cylinder.radius} and height={Cylinder.height}")
        
    @staticmethod
    def area(radius,height):
        print("Area: ", 2 * math.pi * radius * (radius + height))
        
    @staticmethod
    def volume(radius,height):
        print("Volume: ", math.pi * (radius ** 2) * height)
        
    @classmethod
    def swap(cls, height, radius):
        return cls(radius, height)
    
    @classmethod
    def changeFormat(cls, info):
        radius, height = map(float, info.split("-"))
        return cls(radius, height)
c1 = Cylinder(0,0)
Cylinder.area(c1.radius,c1.height)
Cylinder.volume(c1.radius,c1.height)
print("===============================")
c2 = Cylinder.swap(8,3)
c2.area(c2.radius,c2.height)
c2.volume(c2.radius,c2.height)
print("===============================")
c3 = Cylinder.changeFormat("7-13")
c3.area(c3.radius,c3.height)
c3.volume(c3.radius,c3.height)
print("===============================")
Cylinder(0.3,5.56).area(Cylinder.radius,Cylinder.height)
print("===============================")
Cylinder(3,5).volume(Cylinder.radius,Cylinder.height)
