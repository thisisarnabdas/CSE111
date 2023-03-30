class Triangle:
    def __init__(self, base, height):
        self.__base = base
        self.__height = height

    def getBase(self):
        return self.__base

    def setBase(self, base):
        self.__base = base

    def getHeight(self):
        return self.__height

    def setHeight(self, height):
        self.__height = height

    def area(self):
        return 0.5 * self.__base * self.__height
t1 = Triangle(10, 5)
print("First Triangle Base:" , t1.getBase())
print("First Triangle Height:" , t1.getHeight())
print("First Triangle area:" ,t1.area())

t2 = Triangle(5, 3)
print("Second Triangle Base:" , t2.getBase())
print("Second Triangle Height:" , t2.getHeight())
print("Second Triangle area:" ,t2.area())
