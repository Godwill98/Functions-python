# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def MakeSound(self):
#         print("Some sound")

# class Dog(Animal):
#     def MakeSound(self):
#         print("Bark")

# Dog1 = Dog("Simba").MakeSound() # Output: Bark

class Shape:
    def calculate_area(self):
        pass
class Rectangle(Shape):
    def __init__(self,h,w):
        self.h = h
        self.w = w
    def calculate_area(self):
        return self.h*self.w
    
   
rect1 = Rectangle(5,10)
print(rect1.calculate_area()) # Output
