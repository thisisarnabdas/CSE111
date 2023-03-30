class Student:
    def __init__(self,name,stid,dept,email=None,password=None,login_status=None):
        print("Student object is created!")
        self.name=name
        self.stid=stid
        self.dept=dept
        self.email=email
        self.password=password
        self.login_status=login_status
        self.advised_courses=""
class Usis:
    def __init__(self):
        print("USIS is ready to use!")
    def login(self,student):
        condition=(student.email==None,student.password==None)
        if all(condition):
            print("Email and password need to be set.")
        else:
            print("Login successful!")
            student.login_status=1
    def advising(self,student,*clist):
        if student.login_status==1 and 0<len(clist)<=3:
            student.advised_courses=",".join(clist)
            print("Advising Successful!")
        elif student.login_status!=1:
            print("Please login to advise courses!")
        elif len(clist)==0:
            print("You haven't selected any courses.")
        else:
            print("You need special approval to take more than 3 courses.")
    def individualDetails(self,student):
        return f"Name: {student.name}\nID: {student.stid}\nDepartment: {student.dept}\nAdvised courses: {student.advised_courses}"

rakib = Student("Rakib", 12301455, "CSE")
print("1***********************")
usis_obj = Usis()
print("2***********************")
usis_obj.login(rakib)
print("3***********************")
usis_obj.advising(rakib)
print("4***********************")
rakib.email = "rakib@hotmail.com"
rakib.password = "1234"
print("5***********************")
usis_obj.login(rakib)
print("6***********************")
usis_obj.advising(rakib)
print("7***********************")
usis_obj.advising(rakib, "CSE110", "PHY111", "MAT110", "CSE260")
print("8***********************")
usis_obj.advising(rakib, "CSE110", "PHY111", "MAT110")
print("9***********************")
print(usis_obj.individualDetails(rakib))
