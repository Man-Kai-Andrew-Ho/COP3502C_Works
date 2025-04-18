def sum(*args):
    if args == ():
        args = 0.0
        return args
    else:
        temp = 0.0
        for arg in args:
            temp = temp + arg
        return temp


def print_range(a, b):
    while a < b:
        print(a, end = ", ")
        a = a + 1
    print(b)


def sum_of_digits(a):
    sum_num = 0
    for digit in str(a):
        sum_num = sum_num + int(digit)
    return sum_num


