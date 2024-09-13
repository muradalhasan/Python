class Student:
    def __init__(self,name,cgpa,credit=None,dept=None):
        self.name=name
        self.cgpa=cgpa
        self.credit=credit
        self.dept=dept
        self.scolar=None
    def  checkScholarshipEligibility(self):
        if self.cgpa>=3.5 and self.credit>10:
            print(" {self.name} eligible for scholarship. ")
            self.scolar="eligible for scholarship."
        elif self.cgpa>=3.5 and self.cgpa<3.7:
            self.scolar="Need-based scholarship."
            print(f"{self.name} is eligible for Need-based scholarship.")
        elif self.cgpa>=3.7:
            self.scolar="Merit based scholarship"
            print(f"{self.name} is eligible for Merit based scholarship")
        else:
            self.scolar="No scholarship"
            print(f"{self.name} is not eligible for scholarship. ")
    def showDetails(self):
        print(f"Name: {self.name}\nDepartment: {self.cgpa}\nCGPA: {self.cgpa}\nNumber of Credits: {self.credit}\nScholarship Status: {self.scolar}")
print('------------------:--------')
std1 = Student("Alif", 3.99, 12)
print('--------------------------')
std1.checkScholarshipEligibility()
print('--------------------------')
std1.showDetails()
print('--------------------------')
std2 = Student("Mim", 3.4)
std3 = Student("Henry", 3.5, 15,"BBA")
print('--------------------------')
std2.checkScholarshipEligibility()
print('--------------------------')
std3.checkScholarshipEligibility()
print('--------------------------')
std2.showDetails()
print('--------------------------')
std3.showDetails()
print('--------------------------')
std4 = Student("Bob", 4.0, 6, "CSE")
print('--------------------------')
std4.checkScholarshipEligibility()
print('--------------------------')
std4.showDetails()
