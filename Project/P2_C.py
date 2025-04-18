import console_gfx

def to_hex_string(data): #1
    new_list = []
    for i in range(len(data)):
        if data[i] == 10:
            new_list.append("a")
        elif data[i] == 11:
            new_list.append("b")
        elif data[i] == 12:
            new_list.append("c")
        elif data[i] == 13:
            new_list.append("d")
        elif data[i] == 14:
            new_list.append("e")
        elif data[i] == 15:
            new_list.append("f")
        else:
            new_list.append(str(data[i]))

    return "".join(new_list)

def count_runs(flat_data): #2
    runs = 1
    count = 1
    if not flat_data:
        return 0
    for i in range(1, len(flat_data)):
        if flat_data[i] == flat_data[i - 1]:
            count += 1
            if count == 16:
                runs += 1
                count = 1
        else:
            runs += 1
            count = 1

    return runs

def encode_rle(flat_data): #3
    new_list = []
    count = 1
    if not flat_data:
        return []
    for i in range(1, len(flat_data)):
        if flat_data[i] == flat_data[i - 1]:
            count += 1
            if count == 16:
                new_list.append(15)
                new_list.append(flat_data[i])
                count = 1
        else:
            new_list.append(count)
            new_list.append(flat_data[i - 1])
            count = 1
    new_list.append(count)
    new_list.append(flat_data[-1])

    return new_list

def get_decoded_length(rle_data): #4
    num = 0
    for i in range(len(rle_data)):
        if i % 2 == 0:
            num += rle_data[i]
    return num

def decode_rle(rle_data): #5
    new_list = []
    for i in range(len(rle_data)):
        if i % 2 == 0:
            for j in range(int(rle_data[i])):
                new_list.append(int(rle_data[i + 1]))
    return new_list

def string_to_data(data_string): #6
    my_list = list(data_string)
    new_list = []

    for i in range(0, len(my_list)):
        if my_list[i] == "A" or my_list[i] == "a":
            my_list[i] = "10"
        elif my_list[i] == "B" or my_list[i] == "b":
            my_list[i] = "11"
        elif my_list[i] == "C" or my_list[i] == "c":
            my_list[i] = "12"
        elif my_list[i] == "D" or my_list[i] == "d":
            my_list[i] = "13"
        elif my_list[i] == "E" or my_list[i] == "e":
            my_list[i] = "14"
        elif my_list[i] == "F" or my_list[i] == "f":
            my_list[i] = "15"

    for item in my_list:
        new_list.append(int(item))

    return new_list

def to_rle_string(rle_data): #7
    new_list = ""

    for i in range(0, len(rle_data)):
        if i % 2 != 0:
            if rle_data[i] == 10:
                new_list += "a:"
            elif rle_data[i] == 11:
                new_list += "b:"
            elif rle_data[i] == 12:
                new_list += "c:"
            elif rle_data[i] == 13:
                new_list += "d:"
            elif rle_data[i] == 14:
                new_list += "e:"
            elif rle_data[i] == 15:
                new_list += "f:"
            else:
                new_list += str(rle_data[i]) + ":"
        else:
            new_list += str(rle_data[i])

    return new_list[0:-1]

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

def flat_string(rle_data): #9
    new_list = []
    for i in rle_data:
        if i == 10:
            new_list.append("a")
        elif i == 11:
            new_list.append("b")
        elif i == 12:
            new_list.append("c")
        elif i == 13:
            new_list.append("d")
        elif i == 14:
            new_list.append("e")
        elif i == 15:
            new_list.append("f")
        else:
            new_list.append(str(i))
    return "".join(new_list)


def reverse_flat_string(rle_data):  # 10
    new_list = list(rle_data)
    new_new = []
    for inside in new_list:
        if inside == "A" or inside == "a":
            new_new.append(10)
        elif inside == "B" or inside == "b":
            new_new.append(11)
        elif inside == "C" or inside == "c":
            new_new.append(12)
        elif inside == "D" or inside == "d":
            new_new.append(13)
        elif inside == "E" or inside == "e":
            new_new.append(14)
        elif inside == "F" or inside == "f":
            new_new.append(15)
        else:
            new_new.append(int(inside))

    return new_new



def display_menu():
    print("\nRLE Menu\n"
          "--------\n"
          "0. Exit\n"
          "1. Load File\n"
          "2. Load Test Image\n"
          "3. Read RLE String\n"
          "4. Read RLE Hex String\n"
          "5. Read Data Hex String\n"
          "6. Display Image\n"
          "7. Display RLE String\n"
          "8. Display Hex RLE Data\n"
          "9. Display Hex Flat Data")

def main():
    print("Welcome to the RLE image encoder!\n")
    print("Displaying Spectrum Image:")
    console_gfx.display_image(console_gfx.test_rainbow)
    while True:
        display_menu()
        option = int(input("Select a Menu Option: "))
        if option == 0:
            break
        elif option == 1:
            file_name = input("Enter name of file to load: ")
            image_data = console_gfx.load_file(file_name)
        elif option == 2:
            image_data = console_gfx.test_image
            print("Test image data loaded.")
        elif option == 3:
            input_data = input("Enter an RLE string to be decoded: ")
            image_data = decode_rle(string_to_rle(input_data))
        elif option == 4:
            input_data = input("Enter the hex string holding RLE data: ")
            image_data = decode_rle(string_to_data(input_data))
        elif option == 5:
            input_data = input("Enter the hex string holding flat data: ")
            image_data = reverse_flat_string(input_data)
        elif option == 6:
            print("Displaying image...")
            console_gfx.display_image(image_data)
        elif option == 7:
            input_data = to_rle_string(encode_rle((image_data)))
            print(f"RLE representation: {input_data}")
        elif option == 8:
            input_data = to_hex_string(encode_rle(image_data))
            print(f"RLE hex values: {input_data}")
        elif option == 9:
            input_data = flat_string(image_data)
            print(f"Flat hex values: {input_data}")
        else:
            print("Error! Invalid input.")

if __name__ == "__main__":
    main()
