class Student:
    counter=1
    def __init__(self,name,dept,age,cg):
        self.name=name
        self.dept=dept
        self.age=age
        self.cg=cg
        self.stid=Student.counter
        Student.counter+=1
    def showDetails(self):
        print(f"ID: {self.stid}\nName: {self.name}\nDepartment:{self.dept}\nAge: {self.age}\nCGPA: {self.cg}")
    @classmethod
    def from_String(cls,info):
        name,dept,age,cg=info.split("-")
        return cls(name,dept,age,cg)
s1 = Student("Samin", "CSE", 21, 3.91)
s1.showDetails()
print("-----------------------")
s2 = Student("Fahim", "ECE", 21, 3.85)
s2.showDetails()
print("-----------------------")
s3 = Student("Tahura", "EEE", 22, 3.01)
s3.showDetails() 
print("-----------------------")
s4 = Student.from_String("Sumaiya-BBA-23-3.96")
s4.showDetails()
print("A class variable is a variable that is shared among all instances of a class. It is defined at the class level and can be accessed by calling it with the class name . On the other hand, an instance variable is a variable whose value is specific to each instance of a class. It is defined within methods and can have different values across different objects ")
print("An instance method is a method that operates on an instance of a class and has access to its instance variables . On the other hand, a class method is a method that operates on the class itself and does not have access to a particular instance’s variables unless an instance is passed in as a parameter ")
