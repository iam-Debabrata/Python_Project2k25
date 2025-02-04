# Temperature Conversion Program

unit = input("Is this temperature in Celsius or Fahrenheit (Select C/F) : ")
temp = float(input("Enter the temperature : "))

if unit == 'C':
    temp = (temp * (9/5)) + 32
    print(f"The temperature in Fahrenheit is {round(temp, 2)}F.")
elif unit == 'F':
    temp = (temp - 32) * (5/9)
    print(f"The temperature in Celsius is {round(temp, 2)}C.")
else:
    print(f"{unit} is an invalid unit of measurement.")