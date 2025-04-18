import console_gfx


def menu():
    print()
    print("RLE Menu")
    print("--------")
    print("0. Exit")
    print("1. Load File")
    print("2. Load Test Image")
    print("3. Read RLE String")
    print("4. Read RLE Hex String")
    print("5. Read Data Hex String")
    print("6. Display Image")
    print("7. Display RLE String")
    print("8. Display Hex RLE Data")
    print("9. Display Hex Flat Data")

def to_hex_string(data):
    string = ""
    for i in range(len(data)):
        if data[i] == 10:
            string += "a"
        elif data[i] == 11:
            string += "b"
        elif data[i] == 12:
            string += "c"
        elif data[i] == 13:
            string += "d"
        elif data[i] == 14:
            string += "e"
        elif data[i] == 15:
            string += "f"
        else:
            string += str(data[i])

    return string



def count_runs(flat_data):
    count = 1
    runcount = 1
    temp = flat_data[0]

    for i in flat_data:
        if temp == i and runcount < 15:
            runcount += 1
        else:
            count += 1
            runcount = 1
            temp = i

    return count

def encode_rle(flat_data):
    list = []
    count = 0
    temp = flat_data[0]
    runcount = 0

    for i in range(len(flat_data)):
        if temp == flat_data[i] and runcount < 14:
            count += 1
            runcount += 1
        else:
            list.append(count)
            list.append(temp)
            temp = flat_data[i]
            count = 1
            runcount = 0

    list.append(count)
    list.append(temp)

    return list



def get_decoded_length(rle_data):
    count = 0
    for i in range(0, len(rle_data), 2):
        count += rle_data[i]

    return count



def decode_rle(rle_data):
    list = []

    for i in range(0, len(rle_data), 2):
        check = rle_data[i]
        for j in range(check):
            list.append(rle_data[i + 1])

    return list



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


def to_rle_string(rle_data):
    rle_str = []

    for i in range(0, len(rle_data), 2):

        length = str(rle_data[i])
        value = hex(rle_data[i + 1])[2:]
        rle_str.append(length + value)

    return ':'.join(rle_str)



def string_to_rle(rle_string):
    string = ""
    runs = rle_string.split(':')

    for run in runs:
        string += run

    return string_to_data(string)



def main():

    print("Welcome to the RLE image encoder!\n")

    print("Displaying Spectrum Image:")
    console_gfx.display_image(console_gfx.test_rainbow)

    image_data = ""

    while True:
        menu()
        option = int(input("Select a Menu Option: "))
        if option == 0:
            break
        elif option == 1:
            file_name = input("Enter name of file to load: ")
            image_data = console_gfx.load_file(file_name)
        elif option == 2:
            image_data = console_gfx.test_image
            print(" Test image data loaded.")
        elif option == 3:
            input_data = input("Enter an RLE string to be decoded: ")
            image_data = decode_rle(string_to_rle(input_data))
        elif option == 4:
            input_data = input("Enter the hex string holding RLE data: ")
            image_data = decode_rle(string_to_data(input_data))
        elif option == 5:
            input_data = input("Enter the hex string holding flat data: ")
            image_data = string_to_data(input_data)
        elif option == 6:
            if image_data == "":
                print("Displaying image...")
                print("(no data)")
            else:
                print("Displaying image...")
                console_gfx.display_image(image_data)
        elif option == 7:
            if image_data == "":
                print("RLE representation: (no data)")
            else:
                image_data = encode_rle(image_data)
                image_data = to_rle_string(image_data)
                print("RLE representation: " + image_data)
        elif option == 8:
            if image_data == "":
                print("RLE hex values: (no data)")
            else:
                image_data = to_hex_string(encode_rle(image_data))
                print("RLE hex values: " + image_data)
        elif option == 9:
            if image_data == "":
                print(" Flat hex values: (no data)")
            else:
                image_data = to_hex_string(image_data)
                print("Flat hex values: " + image_data)
        else:
            print("Error! Invalid Input.")

if __name__ == "__main__":
    main()