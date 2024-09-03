#Write the Python code of a program that reads two numbers from the user. The program should then print "First is greater" if the first number is greater, "Second is greater" if the second number is greater, and "The numbers are equal" otherwise.

num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
if num1==num2:
    print("The numbers are equal!!")
elif num1>num2:
    print("First is Greater!")
else:
    print("Second is greater!!")