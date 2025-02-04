# Weight converter Kg to lb and vice versa
weight = float(input("Enter your weight : "))
converter = input("Select your converter (Like 'kg' or 'lb') : ")

if converter == 'kg':
    weight *= 2.205
    unit = "lb."
    print(f"Your weight in {unit} is {weight}")
elif converter == 'lb':
    weight /= 2.205
    unit = "kg."
else:
    print("Select valid converter for weight convertion")