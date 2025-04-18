import matplotlib.pyplot as plt

menu = "1. Student grade\n2. Assignment statistics\n3. Assignment graph"

print(menu)
choice = input('Enter your selection: ')

if choice == '1':
    username = input("What is the student's name: ")
    file = open("/Users/andrewho/PycharmProjects/SchoolProject/data/students.txt", "r")

    for line in file:
        new_line = line[3:]
        if username in new_line:
            print(new_line)

    print("Student not found")

# elif choice == '2':
#
# elif choice == '3':
