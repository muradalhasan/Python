num1=int(input("Enter the first number: "))

if num1%2==0 and num1%5==0:
    print("Multiple of 2 and 5 both")
elif num1%2==0 or num1%5==0:
    print(num1)
else:
    print("Not a multiple we want")