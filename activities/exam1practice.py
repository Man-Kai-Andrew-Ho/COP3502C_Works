def fourbonacci(n):
    a, b, c, d = 1, 4, 7, 8
    e = 0
    for _ in range(n-1):
        e = 4*a + 3*b + 2*c + d
        a, b, c, d = b, c, d, e
    return a


def check_square(n):
    num = int(n**0.5)
    return num**2 == n

def odd_squares(n):
    i = 1
    num = 1
    while i <= n:
        if num % 2 != 0 and check_square(num):
            print(num)
            i += 1
            num += 1
        elif num % 2 == 0:
            num += 1
        else:
            num += 1


def diamond(n):
    for i in range(n):
        space = abs(i - n//2)
        for _ in range(space):
            print(" ", end="")
        for j in range(n - space * 2):
            print(j+1, end="")
        print()


