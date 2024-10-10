class Animal:
    def makeSound(self):
        print("Some Generic Sound")


class Dog(Animal):
    def makeSound(self):
        print("Bark")


animals = [Dog(), Animal()]

for animals in animals:
    animals.makeSound()