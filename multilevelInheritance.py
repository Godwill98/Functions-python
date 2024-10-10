class Dog:
    def makeSound(self):
        print("Bark")
class Cat:
    def makeSound(self):
        print("Meow")
class Bird:
    def makeSound(self):
        print("Chirp")


def let_them_speak(animal):
    return animal.makeSound()       

d = Dog()
c = Cat()
b = Bird()

print(let_them_speak(d)) # Output: Bark
let_them_speak(c) # Output: Meow
let_them_speak(b) # Output: Chirp