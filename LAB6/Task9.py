class Student:
    total_students=0
    bracu_students=0
    other_students=0
    def __init__(self,name,dept,uni="BRAC University"):
        self.name=name
        self.dept=dept
        self.uni=uni
        Student.total_students+=1
        if self.uni=="BRAC University":
            Student.bracu_students+=1
        else:
            Student.other_students+=1
    def individualDetail(self):
        print(f"Name: {self.name}\nDepartment: {self.dept}\nInstitution: {self.uni}")
    @classmethod
    def printDetails(cls):
        print(f"Total Student(s): {cls.total_students}\nBRAC University Student(s): {cls.bracu_students}\nOther Institution Student(s): {cls.other_students}")
    @classmethod
    def createStudent(cls,name,dept,uni="BRAC University"):
        return cls(name,dept,uni)
        

Student.printDetails()
print('#########################')

mikasa = Student('Mikasa Ackerman', "CSE")
mikasa.individualDetail()
print('------------------------------------------')
Student.printDetails()

print('========================')

harry = Student.createStudent('Harry Potter', "Defence Against Dark Arts", "Hogwarts School")
harry.individualDetail()
print('-------------------------------------------')
Student.printDetails()

print('=========================')

levi = Student.createStudent("Levi Ackerman", "CSE")
levi.individualDetail()
print('--------------------------------------------')
Student.printDetails()

