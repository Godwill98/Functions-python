class Animal:
    def __init__(self, name):
        self.name = name
    def MakeSound(self):
        print("Some sound")

class Dog(Animal):
    def MakeSound(self):
        print("Bark")

Dog1 = Dog("Simba").MakeSound() # Output: Bark

Dog1.MakeSound() # Output: Bark