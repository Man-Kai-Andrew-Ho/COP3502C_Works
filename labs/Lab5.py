menu = """Decoding Menu
-------------
1. Decode hexadecimal
2. Decode binary
3. Convert binary to hexadecimal
4. Quit
"""

def hex_char_decode(digit):
    new_list = []
    res = 0
    count = 0
    for char in digit:
        new_list.append(int(char))
    for num in new_list:
        res = res + (num * (16 ** count))
        count += 1
    return res

def hex_string_decode(hex):
    new_hex_str = hex[::-1]
    new_list = []
    for char in new_hex_str:
        new_list.append(char)
    for i in range(0, len(new_list)):
        if new_list[i] == "A" or new_list[i] == "a":
            new_list[i] = "10"
        elif new_list[i] == "B" or new_list[i] == "b":
            new_list[i] = "11"
        elif new_list[i] == "C" or new_list[i] == "c":
            new_list[i] = "12"
        elif new_list[i] == "D" or new_list[i] == "d":
            new_list[i] = "13"
        elif new_list[i] == "E" or new_list[i] == "e":
            new_list[i] = "14"
        elif new_list[i] == "F" or new_list[i] == "f":
            new_list[i] = "15"
    return hex_char_decode(new_list)

def binary_string_decode(binary):
    new_binary = str(binary)[::-1]
    new_list = []
    res = 0
    count = 0
    for char in new_binary:
        new_list.append(int(char))
    for num in new_list:
        res = res + (num * (2 ** count))
        count += 1
    return res

def binary_to_hex(binary):
    new_binary = str(binary)[::-1]
    new_list = []
    for char in new_binary:
        new_list.append(char)

    result = []

    for i in range(0, len(new_list), 4):
        sublist = new_list[i:i + 4]
        result.append(sublist)

    output = []

    for m in range(0, len(result)):
        res = 0
        count = 0
        for num in result[m]:
            num = int(num)
            res = res + (num * (2 ** count))
            count += 1
        output.append(str(res))

    for i in range(0, len(output)):
        if output[i] == "10":
            output[i] = "A"
        elif output[i] == "11":
            output[i] = "B"
        elif output[i] == "12":
            output[i] = "C"
        elif output[i] == "13":
            output[i] = "D"
        elif output[i] == "14":
            output[i] = "E"
        elif output[i] == "15":
            output[i] = "F"

    output = output[::-1]

    return "".join(output)

if __name__ == "__main__":
    option = 0
    while option != 4:
        print(menu)
        option = int(input("Please enter an option: "))
        if option == 1:
            result = input("Please enter the numeric string to convert: ")
            res_list = []
            for char in result:
                res_list.append(char)
            if res_list[0] == "0":
                res_list.pop(0)
            if res_list[0] == "x":
                res_list.pop(0)
            result = "".join(res_list)
            result = hex_string_decode(result)
            print(f"Result: {result}")
        elif option == 2:
            result = input("Please enter the numeric string to convert: ")
            res_list = []
            for char in result:
                res_list.append(char)
            if res_list[0] == "0":
                res_list.pop(0)
            if res_list[0] == "b":
                res_list.pop(0)
            result = "".join(res_list)
            result = binary_string_decode(result)
            print(f"Result: {result}")
        elif option == 3:
            result = binary_to_hex(input("Please enter the numeric string to convert: "))
            print(f"Result: {result}")

    print("Goodbye!")