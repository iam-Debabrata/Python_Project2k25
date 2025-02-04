# Logical Operators  =  Evaluate multiple conditions (or, and, not)
#                       or = at least one conditions must be true
#                       and = both conditions must be true
#                       not - inverts the condition (not True, not False)

temp = 25
is_raining = False
is_sunny = True

if temp < 25 or temp > 0 or is_raining == True or is_sunny == True:
    print("Is Raining and rainbow may appear")
else:
    print("Its sunny today")

if temp < 25 and temp > 0 and is_raining == True and is_sunny == True:
    print("Is Raining and rainbow may appear")
else:
    print("Its sunny today")