# Calculate the hypotenuse of the triangle
import math

measurement = input("Enter the measurement type ? Like : cm/inc/m/ft.  ")
a_height = float(input("Enter the side a : "))
b_base = float(input("Enter the side b : "))
c_hypotenuse = math.sqrt(pow(a_height,2) + pow(b_base,2))

print(f"Hypotenuse of the triangle is {c_hypotenuse}{measurement}")