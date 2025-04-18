def string_to_rle(rle_string): #8
    new_string = rle_string.split(":")
    new_list = []

    for inside in new_string:
        if len(inside) == 3:
            new_list.append(int(inside[0] + inside[1]))
            if inside[-1] == "A" or inside[-1] == "a":
                new_list.append(10)
            elif inside[-1] == "B" or inside[-1] == "b":
                new_list.append(11)
            elif inside[-1] == "C" or inside[-1] == "c":
                new_list.append(12)
            elif inside[-1] == "D" or inside[-1] == "d":
                new_list.append(13)
            elif inside[-1] == "E" or inside[-1] == "e":
                new_list.append(14)
            elif inside[-1] == "F" or inside[-1] == "f":
                new_list.append(15)
            else:
                new_list.append(int(inside[-1]))
        else:
            new_list.append(int(inside[0]))
            new_list.append(int(inside[1]))


    return new_list

def decode_rle(rle_data): #5
    new_list = []
    for i in range(len(rle_data)):
        if i % 2 == 0:
            for j in range(int(rle_data[i])):
                new_list.append(int(rle_data[i + 1]))
    return new_list

print(decode_rle(string_to_rle("19:14:151:151:61")))