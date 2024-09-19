# Parent class: Employee
class Employee:
    def __init__(self, name, emp_id, department):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.salary = 30000  # Default basic salary for regular employees
    
    def employeeDetails(self):
        print(f"Name: {self.name}, Dept {self.department}")
        print(f"Employee id: {self.emp_id}, Salary: {self.salary}")
    
    def workDistribution(self, department):
        if department == "Human Resource":
            print("Collect work distribution details from the manager.")
        else:
            print("Collect work distribution loads from the HR department.")
    
    def increment(self):
        self.salary += self.salary * 0.10  

# Child class: Foreign Employee
class Foreign_employee(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id, department)
        self.salary = 30000  # Foreign employees start with the same basic salary
    
    def employeeDetails(self):
        super().employeeDetails()
        print("Employee Type: Foreign")
    
    def increment(self):
        self.salary += self.salary * 0.15  # Foreign employee gets 15% increment
        print("Employee Type: Foreign")


# Child class: Part-time Employee
class Part_time_employee(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id, department)
        self.salary = 15000  # Part-time employees start with a lower basic salary
    
    def employeeDetails(self):
        print(f"Name: {self.name}, Dept {self.department}")
        print(f"Employee id: {self.emp_id}, Salary: {self.salary}")
        print("Employee Type: Part Time")
    
    def workDistribution(self, department):
        print("Collect work distribution loads from the HR department.")
    
    def increment(self):
        print("Sadly, there is no increment for the part time employees!!")


# Driver Code to produce the required output
print("1------------------------------------------")
emp1 = Employee("Nawaz Ali", 102, "Marketing")
print("2------------------------------------------")
emp1.employeeDetails()
print("3------------------------------------------")
emp1.workDistribution("Marketing")
print("4------------------------------------------")
emp1.increment()
emp1.employeeDetails()
print("5------------------------------------------")
f_emp = Foreign_employee("Nadvi", 311, "Human Resource")
f_emp.employeeDetails()
print("6------------------------------------------")
f_emp.workDistribution("Human Resource")
print("7------------------------------------------")
f_emp.increment()
f_emp.employeeDetails()
print("8------------------------------------------")
p1_emp = Part_time_employee("Asif", 210, "Sales")
p2_emp = Part_time_employee("Olive", 223, "Accounts")
print("9------------------------------------------")
p1_emp.employeeDetails()
print("10------------------------------------------")
p1_emp.workDistribution("Sales")
print("11------------------------------------------")
p2_emp.increment()
print("12------------------------------------------")
p2_emp.employeeDetails()
