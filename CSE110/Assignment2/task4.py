#Write the Python code of a program that reads two numbers, subtracts the smaller number from the larger one, and prints the result.
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
if num1>num2:
    print(num1-num2)
else:
    print(num2-num1)