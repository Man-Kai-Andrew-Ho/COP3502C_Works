from base_classes import *

class SecureAccount(Account):
    def __init__(self, password):
        super().__init__()
        self.password = password

    def get_balance(self, password):
        if password != self.password:
            print("Incorrect password")
        else:
            return super().get_balance()

    def deposit(self, amount, password):
        if password != self.password:
            print("Incorrect password")
        else:
            super().deposit(amount)

    def withdraw(self, amount, password):
        if password != self.password:
            print("Incorrect password")
        else:
            super().withdraw(amount)

class MemoryCalculator(Calculator):
    def __init__(self):
        super().__init__()
        self.answer = 0

    def add(self, x, y):
        if x == "RESULT" and y == "RESULT":
            self.answer = super().add(self.answer, self.answer)
            return self.answer
        elif y == "RESULT":
            self.answer = super().add(x, self.answer)
            return self.answer
        elif x == "RESULT":
            self.answer = super().add(self.answer, y)
            return self.answer
        else:
            self.answer = super().add(x, y)
            return self.answer


    def sub(self, x, y):
        if x == "RESULT" and y == "RESULT":
            self.answer = super().sub(self.answer, self.answer)
            return self.answer
        elif y == "RESULT":
            self.answer = super().sub(x, self.answer)
            return self.answer
        elif x == "RESULT":
            self.answer = super().sub(self.answer, y)
            return self.answer
        else:
            self.answer = super().sub(x, y)
            return self.answer

class ImprovedFraction(Fraction):
    def add(self, other):
        if isinstance(other, int):
            other = ImprovedFraction(other, 1)
        return super().add(other)

    def multiply(self, other):
        if isinstance(other, int):
            other = ImprovedFraction(other, 1)
        return super().multiply(other)

    def __add__(self, other):
        return self.add(other)

    def __mul__(self, other):
        return self.multiply(other)

    def __str__(self):
        return f"{self.get_numerator()}/{self.get_denominator()}"






