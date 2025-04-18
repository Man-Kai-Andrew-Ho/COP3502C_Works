from pakudex import *

menu = """
Pakudex Main Menu
-----------------
1. List Pakuri
2. Show Pakuri
3. Add Pakuri
4. Evolve Pakuri
5. Sort Pakuri
6. Exit
"""

if __name__ == "__main__":
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    while True:
        max_cap = input("Enter max capacity of the Pakudex: ")
        count = 0
        if max_cap.isnumeric():
            max_cap = int(max_cap)
            pakudex = Pakudex(max_cap)
            print(f"The Pakudex can hold {max_cap} species of Pakuri.")
            while True:
                print(menu)
                option = input("What would you like to do? ")

                if option == "1":
                    species_list = pakudex.get_species_array()
                    if not species_list:
                        print("No Pakuri in Pakudex yet!")
                    else:
                        print("Pakuri In Pakudex:")
                        for i, species in enumerate(species_list, 1):
                            print(f"{i}. {species}")

                elif option == "2":
                    species = input("Enter the name of the species to display: ")
                    stats = pakudex.get_stats(species)
                    if stats:
                        print(f"Species: {species}")
                        print(f"Attack: {stats[0]}")
                        print(f"Defense: {stats[1]}")
                        print(f"Speed: {stats[2]}")
                    else:
                        print("Error: No such Pakuri!")

                elif option == "3":
                    if count == max_cap:
                        print("Error: Pakudex is full!")
                        continue
                    else:
                        species = input("Enter the name of the species to add: ")
                        if pakudex.add_pakuri(species):
                            print(f"Pakuri species {species} successfully added!")
                            count += 1
                        else:
                            if species in pakudex.get_species_array():
                                print("Error: Pakudex already contains this species!")
                            else:
                                print("Error: Pakudex is full!")

                elif option == "4":
                    species = input("Enter the name of the species to evolve: ")
                    if pakudex.evolve_species(species):
                        print(f"{species} has evolved!")
                    else:
                        print("Error: No such Pakuri!")

                elif option == "5":
                    pakudex.sort_pakuri()
                    print("Pakuri have been sorted!")

                elif option == "6":
                    print("Thanks for using Pakudex! Bye!")
                    exit()

                else:
                    print("Unrecognized menu selection!")
                    continue
        else:
            print("Please enter a valid size.")
            continue
