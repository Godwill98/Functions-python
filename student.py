
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Create an instance of the Student class

student1 = Student("Alice", 20)
student1.display()  # Output: Name: Alice, Age: 20