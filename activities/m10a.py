class Pakuri:
    def __init__(self, name):
        self.name = name

    def attack(self, attack_name):
        self.attack_name = attack_name
        pakuri_name = self.name
        print(f"{pakuri_name} used {attack_name}!")

    def speak(self):
        pakuri_name = self.name
        print(f"{pakuri_name}, {pakuri_name}!")

class BankAccount:
    def __init__(self):
        self.money = 0

    def deposit(self, amount):
        if amount < 0:
            print(f"Invalid amount.")
        else:
            self.money += amount
            print(f"Deposited ${amount}")

    def withdraw(self, amount):
        if amount < 0:
            print(f"Invalid amount.")
        elif amount > self.money:
            print(f"You don't have enough money :(")
        else:
            self.money -= amount
            print(f"Withdrew ${amount}")

    def display(self):
        balance = self.money
        print(f"Current balance: ${balance}")

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Coordinate):
            return self.x == other.x and self.y == other.y

    def __add__(self, other):
        if isinstance(other, Coordinate):
            return self.x + other.x, self.y + other.y

    def __str__(self):
        return f"({self.x}, {self.y})"


