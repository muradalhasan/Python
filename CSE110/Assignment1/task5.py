#Write a Python program that reads two integers M and N respectively and finds the value of M^N (or MN) and prints the value exactly as shown in the examples below. Your code should work correctly for any other sample inputs.
num1=int(input("Please enter the number1: "))
num2=int(input("Please enter the number2: "))
res=num1**num2
print(f"{num1}^{num2}:{res}")