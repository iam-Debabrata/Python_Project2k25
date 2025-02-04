# Calculator with if elif statement

operator = input("Enter an operator (+ - * /) : ")
num1 = float(input("Enter 1st number : "))
num2 = float(input("Enter 2nd number : "))

if operator == '+':
    print(f"Summation of two number is : {num1+num2}")
elif operator == '-':
    print(f"Substraction of two number is : {num1-num2}")
elif operator == '*':
    print(f"Multiplication of two number is : {num1*num2}")
elif operator == '/':
    print(f"Division of two number is : {num1/num2}")
else:
    print(f"{operator} is invalid operator to perform operation")
