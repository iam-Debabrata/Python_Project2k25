# Conditional Expression = A one-line shortcut for the if-else statement (ternary Operator)
#                            print or assign one of two values based on a condition
#                            x if condition else y
#Global variable
num = -4.0
a = 6
b = 8
age = 25
temp = -5

#1
print("Positive" if num > 0 else "Negative")

#2
even_odd = "EVEN" if num % 2 == 0 else "ODD"
print(f"{num} is {even_odd}")

#3
max_num = a if a > b else b
print(f"Maximum number is {max_num}")
min_num = a if a < b else b
print(f"Minimum number is {min_num}")

#4
age = "ADULT" if age >=18 else "CHILD"
print(age)

#5
temp_status = "COOLER" if temp <=5 else "HOTTER"
print(temp_status)