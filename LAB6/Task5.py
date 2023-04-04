class Employee:
    def __init__(self,name,exp):
        self.name=name
        self.workingPeriod=exp
    @classmethod
    def employeeByJoiningYear(cls,name,year):
        return cls(name,2023-year)
    @staticmethod
    def experienceCheck(exp,gender):
        if exp<3:
            if gender=="male":
                return "He is not experienced"
            else:
                return "She is not experienced"
        else:
            if gender=="male":
                return "He is experienced"
            else:
                return "She is experienced"
employee1 = Employee('Dororo', 3)
employee2 = Employee.employeeByJoiningYear('Harry', 2016)
print(employee1.workingPeriod)
print(employee2.workingPeriod)
print(employee1.name)
print(employee2.name)
print(Employee.experienceCheck(2, "male"))
print(Employee.experienceCheck(3, "female"))