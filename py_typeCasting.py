#typecasting = The process of Converting variable from one datatype to another datatype
#              str(), int(), float(), bool()

name = "Jaxx"
age = 29
gpa = 4.78
is_student = False
print(type(name))
print(f"Round of Percentage of {name} is {int(gpa)}")
print(f"age in float {float(age)}")

name = bool(name)
print(name)