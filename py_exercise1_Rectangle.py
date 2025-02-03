# Exercise 1 : Calculating the area of Rectangle based on user input
measurement = input("Enter the measurement type ? Like : cm/inc/m/ft.  ")
length = float(input("Enter the length of the rectangle ?  "))
width = float(input("Enter the width of the rectangle ?  "))

#area calculation
area = length * width
print(f"Area of the Rectanlge is {area}{measurement}^2")