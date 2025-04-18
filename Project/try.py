
def string_to_rle(rle_string):
    string = ""
    runs = rle_string.split(':')

    for run in runs:
        string += run

    return string_to_data(string)

def string_to_data(data_string):
    list = []

    for i in range(len(data_string)):
        if data_string[i] == "a":
            list.append(10)
        elif data_string[i] == "b":
            list.append(11)
        elif data_string[i] == "c":
            list.append(12)
        elif data_string[i] == "d":
            list.append(13)
        elif data_string[i] == "e":
            list.append(14)
        elif data_string[i] == "f":
            list.append(15)
        else:
            list.append(int(data_string[i]))

    return list

def decode_rle(rle_data):
    list = []

    for i in range(0, len(rle_data), 2):
        check = rle_data[i]
        for j in range(check):
            list.append(rle_data[i + 1])

    return list

print(decode_rle(string_to_rle("19:14:151:151:61")))