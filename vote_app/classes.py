class NewClass:
    b = "Bence"
    c = 4

    def func(self):
        return "Hello!"

x = NewClass()

class Pet:
    kind = "Dog"

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

a = Pet("Sanyi")
b = Pet("Géza")

a.add_trick("jump")
b.add_trick("klif")

print(a.name + str(" és ") + b.name + str(" barátok."))
"""

"""
print(a.tricks)
print(b.tricks)

