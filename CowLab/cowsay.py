import sys
from heifer_generator import get_cows
from dragon import *
from ice_dragon import *

def list_cows(cows):
    cow_names = []
    for cow in cows:
        cow_names.append(cow.get_name())
    print("Cows available:", " ".join(cow_names))


def find_cow(name, cows):
    for cow in cows:
        if cow.get_name() == name:
            return cow
    return None

def main():
    cows = get_cows()

    if len(sys.argv) < 2:
        print("Usage: python3 cowsay.py [OPTIONS] MESSAGE")
        return

    if sys.argv[1] == "-l":
        list_cows(cows)
    elif sys.argv[1] == "-n":
        if len(sys.argv) < 4:
            print("Usage: python3 cowsay.py -n COW MESSAGE")
            return
        cow_name = sys.argv[2]
        message = " ".join(sys.argv[3:])
        cow = find_cow(cow_name, cows)
        if cow:
            print(message)
            print(cow.get_image())
            
            if isinstance(cow, Dragon):
                if cow.can_breath_fire():
                    print("This dragon can breathe fire.")
                else:
                    print("This dragon cannot breathe fire.")
        else:
            print(f"Could not find {cow_name} cow!")
    else:
        message = " ".join(sys.argv[1:])
        default_cow = cows[0]
        print(message)
        print(default_cow.get_image())


if __name__ == "__main__":
    main()
