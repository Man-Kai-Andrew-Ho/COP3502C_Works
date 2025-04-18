h = int(input("Height: "))

for i in range(1, h + 1):
    print(" " * (h - i), end = "")
    for j in range(1, i + 1):
        print(j, end="")
    print()