import console_gfx
import P2_B



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
            image_data = P2_B.decode_rle(P2_B.string_to_rle(input_data))
        elif option == 4:
            input_data = input("Enter an RLE Hex string to be decoded: ")
            image_data = P2_B.decode_rle(P2_B.string_to_data(input_data))
        elif option == 6:
            console_gfx.display_image(image_data)
        elif option == 7:
            input_data = P2_B.to_rle_string(P2_B.encode_rle((image_data)))
            print(f"RLE representation: {input_data}")
        elif option == 8:
            input_data = P2_B.to_hex_string(P2_B.encode_rle(image_data))
            print(f"RLE hex values: {input_data}")
        elif option == 9:
            input_data = P2_B.flat_string(image_data)
            print(f"Flat hex values: {input_data}")
        else:
            print("Error! Invalid input.")

if __name__ == "__main__":
    main()
