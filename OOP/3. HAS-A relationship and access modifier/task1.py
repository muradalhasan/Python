class Student:
    def __init__(self,name,id,cg):
        self.name=name
        self.__id=id
        self.__cgpa=cg
    def getId(self):
        return self.__id
    def getCGPA(self):
        return self.__cgpa
    def setId(self,id):
        self.__id=id
class Department:
    def __init__(self,name):
        self.Dname=name
        self.student=[]
    def addStudent(self,*a):
        for i in a:
            flag=True
            for s in self.student:
                if i.getId()==s.getId():
                    flag=False               
                    print("Student with the same ID already exists, Please try with another ID")
            if flag==True:
                self.student.append(i)
                print(f"Welcome to CSE department, {i.name}")        
    def findStudent(self,id):
        flag=False
        for i in self.student:
            if i.getId()==id:
                print(f"Student info:\nStudent Name:{i.name}\nID: {i.getId()}\nCGPA: {i.getCGPA()}")
                flag=True
        if flag==False:
            print(f"Student with this ID doesn't exist, Please give a valid ID")
    def details(self):
        print(f"Department Name: {self.Dname}")
        print(f"Number of student: {len(self.student)}\nDetails of the students: ")
        for i in self.student:
            print(f"Student name: {i.name} ,ID: {i.getId()} ,CGPA: {i.getCGPA()}")
            
s1 = Student("Akib", 22301010, 3.29)
s2 = Student("Reza", 22101010, 3.45)
s3 = Student("Ruhan", 23101934, 4.00)
print("1==================================")
cse = Department("CSE")
cse.findStudent(22112233)
print("2==================================")
cse.addStudent(s1,s2,s3)
print("3==================================")
cse.details()
print("4==================================")
cse.findStudent(22301010)
print("5==================================")
s4 = Student("Nakib",22301010,3.22)
cse.addStudent(s4)
print("6==================================")
s4.setId(21201220)
cse.addStudent(s4)
print("7==================================")
cse.details()
print("8==================================")
s5 = Student("Sakib",22201010,2.29)
cse.addStudent(s5)
print("9==================================")
cse.details()
