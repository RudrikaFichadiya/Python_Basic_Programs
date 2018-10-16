print("This is the demo program to implement Inheritance")
class Parent:
    def __init__(self):
        print("This is the parent class")
    def parentFunction(self):
        print("This is the Parent Class Member Function")
p = Parent()
p.parentFunction()

class Child(Parent): #to implement inheritance parent is written inside the child class brackets
    def __init__(self):
        super().__init__()
        print("This is child class")
    def childFunction(self):
        print("Child class member function")
p2 = Child()
p2.parentFunction()
p2.childFunction()