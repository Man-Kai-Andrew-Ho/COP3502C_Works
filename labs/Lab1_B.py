# This gets the input and changes it to float
price = float(input("Enter the price of the item: "))
tax = float(input("Enter the sales tax percentage: "))
# This calculates the total from price and tax
total = price * tax / 100 + price
# This prints the total price
print(f"Your total is ${total:.2f}")