#Write the Python code of a program that reads the radius of a circle and prints its circumference and area.
import math
radius=int(input("Enter the radius: "))
print(f"Area is {math.pi*(radius*radius)}\nCircumference is {2*math.pi*radius}")