import math
def area_circumference_generator(r):
    area=(math.pi)*(r**2)
    circum=2*(math.pi)*r
    print((area,circum))
    print(f"Area of the circle is {area} and circumference is {circum}")
area_circumference_generator(1)