w_hour=int(input("Enter total working hour: "))
salary=0
if w_hour<=40:
    if w_hour<0:
        print(f"Hour cannot be negative")
    else:
      salary=w_hour*200
      print(f"Salary: {salary}")
else:
    if w_hour >168:
        print(f"Impossible to work more than 168 hours weekly")
    else:
        extra=w_hour-40
        salary=8000+(extra*300)
        print(f"Salary: {salary}")
 
