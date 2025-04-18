price = float(input("Enter the price: "))
bf = input("Is it black friday [y/n]: ")
if bf == "y":
    price = price - (price * 0.4)
elif bf == "n":
    price = price

coupon = input("Do you have a coupon [y/n]: ")
if coupon == "y":
    price = price - (price * 0.05)
elif coupon == "n":
    price = price

employee = input("Do you have an employee discount [y/n]: ")
if employee == "y":
    price = price - (price * 0.2)
elif employee == "n":
    price = price

print(f"The final price is: ${price:.2f}")