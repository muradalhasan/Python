def calculate_tax(age,salary,designation):
    if age<18 or designation=="president" or salary<10000:
        tax= 0
    elif salary >=10000 and salary<=20000:
        tax=(salary*5)/100
    elif salary >20000:
        tax=tax=(salary*10)/100
    return tax
age=int(input())
salary=int(input())
desig=input()
print(calculate_tax(age,salary,desig))
    