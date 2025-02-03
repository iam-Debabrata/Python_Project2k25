# Program, to calculate the circumference of the circle

import math
from math import floor

radius = float(input("Enter the radius of the circle : "))
circumference = 2 * math.pi * radius
print(f"The circumference of circle is {circumference}cm.")
#print(f"The circumference of circle is {round(circumference, 2)}")

# Program to calculate the area of the circle

radius = float(input("Enter the radius of the circle : "))
area = math.pi * pow(radius, 2)
print(f"The area of the circle is {area}")
print(f"The area of the circle is {round(area, 3)}cm^2.")
#print(f"The area of the circle is {math.floor(area)}")
#print(f"The area of the circle is {math.ceil(area)}")