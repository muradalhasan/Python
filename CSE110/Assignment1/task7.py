#Write a Python program that reads 3 integers A, B, and C respectively, and then reads a floating point number D. After reading, the program should print the result (as int) using the given formula below.
#Formula110: A**C+B*A-D/3 
a=int(input())
b=int(input())
c=int(input())
d=float(input())
res=(a**c)+(b*a)-(d/3)
print(f"{int(res)}")