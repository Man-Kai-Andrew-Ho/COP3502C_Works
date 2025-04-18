def fibonacci(n):
    list = [0,1]
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        while len(list) < n:
            num_ex = list[len(list)-2] + list[len(list)-1]
            list.append(num_ex)
        return list[len(list)-1]

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_prime_factors(n):

    if is_prime(n):
        print(f"{n} = {n}")
    else:
        temp = n
        output = f"{temp} ="
        count = 0
        while temp > 1:
            if temp % 2 == 0:
                if count == 0:
                    output += " 2"
                else:
                    output += " * 2"
                temp = temp // 2
            elif temp % 3 == 0:
                if count == 0:
                    output += " 3"
                else:
                    output += " * 3"
                temp = temp // 3
            elif temp % 5 == 0:
                if count == 0:
                    output += " 5"
                else:
                    output += " * 5"
                temp = temp // 5
            else:
                if count == 0:
                    output += f" {temp} "
                else:
                    output += f" * {temp} "
                break
            count = 1

        return print(output)
