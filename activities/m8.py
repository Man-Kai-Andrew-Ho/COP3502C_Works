def flatten(nested_list):
    total = []
    for inside in nested_list:
        if isinstance(inside, list):
            total += flatten(inside)
        else:
            total.append(inside)
    return total

# def mystery1(n):
#     def inner(n, a, b, c, d, e):
#         if n <= 0:
#             return a
#         return inner(n - 1, b, c, d, e, a-c+e)
#     return inner(n, 1, 2, 3, 4, 5)

def mystery1(n):
    a, b, c, d, e = 1, 2, 3, 4, 5
    for i in range(n):
        a, b, c, d, e = b, c, d, e, (a-c+e)
    return a

# def mystery2(number):
#     total = 0
#     while number > 0:
#         digit = number % 10
#         total += digit
#         number //= 10
#     return total

def mystery2(number):
    if number < 10:
        return number
    else:
        return mystery2(number//10) + number % 10

def collatz_sequence(num):
    print(int(num), end=" ")
    if num == 1:
        print()
        return
    elif num % 2 == 0:
        collatz_sequence(num / 2)
    else:
        collatz_sequence(num * 3 + 1)

