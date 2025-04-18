import math

menu = "Calculator Menu\n---------------\n0. Exit Program\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponentiation\n6. Logarithm\n7. Display Average\n"

pre_ans = 0
sum_calc = 0
num_calc = 0

print("Current Result: 0.0\n")
while True:
    print(menu)
    while True:
        selection = input("Enter Menu Selection: ")
        if selection == "0":
            print("Thanks for using this calculator. Goodbye!")
            exit()
        elif selection == "1":
            f = (input("Enter first operand: "))
            s = (input("Enter second operand: "))
            if f == "RESULT":
                f = pre_ans
            if s == "RESULT":
                s = pre_ans
            add = float(f)+float(s)
            print(f"Current Result: {add}\n")
            pre_ans = add
            sum_calc += add
            num_calc += 1
            break
        elif selection == "2":
            f = (input("Enter first operand: "))
            s = (input("Enter second operand: "))
            if f == "RESULT":
                f = pre_ans
            if s == "RESULT":
                s = pre_ans
            sub = float(f)-float(s)
            print(f"Current Result: {sub}\n")
            pre_ans = sub
            sum_calc += sub
            num_calc += 1
            break
        elif selection == "3":
            f = (input("Enter first operand: "))
            s = (input("Enter second operand: "))
            if f == "RESULT":
                f = pre_ans
            if s == "RESULT":
                s = pre_ans
            mul = float(f)*float(s)
            print(f"Current Result: {mul}\n")
            pre_ans = mul
            sum_calc += mul
            num_calc += 1
            break
        elif selection == "4":
            f = (input("Enter first operand: "))
            s = (input("Enter second operand: "))
            if f == "RESULT":
                f = pre_ans
            if s == "RESULT":
                s = pre_ans
            div = float(f)/float(s)
            print(f"Current Result: {div}\n")
            pre_ans = div
            sum_calc += div
            num_calc += 1
            break
        elif selection == "5":
            f = (input("Enter first operand: "))
            s = (input("Enter second operand: "))
            if f == "RESULT":
                f = pre_ans
            if s == "RESULT":
                s = pre_ans
            exp = float(f)**float(s)
            print(f"Current Result: {exp}\n")
            pre_ans = exp
            sum_calc += exp
            num_calc += 1
            break
        elif selection == "6":
            f = (input("Enter first operand: "))
            s = (input("Enter second operand: "))
            if f == "RESULT":
                f = pre_ans
            if s == "RESULT":
                s = pre_ans
            log = math.log(float(s), float(f))
            print(f"Current Result: {log}\n")
            pre_ans = log
            sum_calc += log
            num_calc += 1
            break
        elif selection == "7":
            if sum_calc == 0:
                print("Error: No calculations yet to average!\n")
            elif num_calc > 0:
                print(f"Sum of calculations: {sum_calc}")
                print(f"Number of calculations: {num_calc}")
                print(f"Average of calculations: {sum_calc/num_calc:.2f}\n")
        else:
            print("Error: Invalid selection!\n")