class Bird:
    def fly(self):
        print("Bird can fly")

class Mammal:
    def run(self):
        print("Mammal can run")

class Bat(Bird, Mammal):
    def run(self):
        print("Bat can fly and run")

b = Bat()
b.run()