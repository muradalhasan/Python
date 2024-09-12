class Student:
    def __init__(self, name, cgpa, courses_taken):
        self.name = name
        self.cgpa = cgpa
        self.courses_taken = courses_taken
        self.student_status = self.get_student_status()
        self.advising_status = self.get_advising_status()

        # Print messages based on status and advising approval
        if self.student_status == "Probation":
            if self.advising_status == "Approved":
                print(f"Study hard this time, {self.name}.")
            else:
                print(f"Sorry, {self.name}, you are on probation and cannot take more than 2 courses.")
        elif self.student_status == "Regular":
            if self.advising_status == "Approved":
                print(f"All the best, {self.name}, for the upcoming semester.")
            else:
                print(f"Hello {self.name}, You are a regular student and have to take between 3 to 5 courses.")

    def get_student_status(self):
        """Determine if the student is under probation or regular based on their CGPA."""
        if self.cgpa < 2.00:
            return "Probation"
        else:
            return "Regular"

    def get_advising_status(self):
        """Determine the advising status based on the student type and courses taken."""
        if self.student_status == "Probation":
            # Probation students must take between 1 and 2 courses
            if 1 <= self.courses_taken <= 2:
                return "Approved"
            else:
                self.courses_taken = 0
                return "Denied"
        elif self.student_status == "Regular":
            # Regular students must take between 3 and 5 courses
            if 3 <= self.courses_taken <= 5:
                return "Approved"
            else:
                self.courses_taken = 0
                return "Denied"

            
s1 = Student("Clark", 3.45, 4)
print(f"Name: {s1.name}\nCGPA: {s1.cgpa}\nCourses Taken: {s1.courses_taken}")
print(f"Student Status: {s1.student_status}\nAdvising Status: {s1.advising_status}")
print("--------------------------------------------------------------------------------")
s2 = Student("Barry", 1.93, 2)
print(f"Name: {s2.name}")
print(f"Student Status: {s2.student_status}\nAdvising Status: {s2.advising_status}")
print("--------------------------------------------------------------------------------")
s3 = Student("Diana", 2.91, 2)
print(f"Advising Status: {s3.advising_status}\nCourses Taken: {s3.courses_taken}")
print("--------------------------------------------------------------------------------")
s4 = Student("Bruce", 1.52, 5)
print(f"Advising Status: {s4.advising_status}\nCourses Taken: {s4.courses_taken}")
