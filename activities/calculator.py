operation = input("Enter the operation: ")
first = float(input("Enter the first operand: "))
second = float(input("Enter the second operand: "))

result = 0
if operation == "add":
    result = first + second
elif operation == "sub":
    result = first - second
elif operation == "mul":
    result = first * second
elif operation == "div":
    result = first / second

print(f"Result is {round(result, 2)}")