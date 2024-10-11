class A:
    def display(self):
        print("A")

class B:
    def display(self):
        print("B")


class Demo(A, B):
    def show(self):
        print("C")

d = Demo()
d.display() # Output: C
print(Demo.mro()) # Output: [<class '__ma in__.Demo'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]