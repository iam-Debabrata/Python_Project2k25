# Exercise 2 : Shopping cart program

items = input("What item would you like to buy ?  ")
price = float(input("What is the price of the item ?  "))
quantity = int(input("How many would you like to take ?  "))
total_Purchase = price * quantity

print(f"You have bought {quantity} * {items}/s")
print(f"Your total is ${total_Purchase}")
print("Thank you !!! Purchase again")