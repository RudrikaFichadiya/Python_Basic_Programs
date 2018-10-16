# python does not force to add access specifiers into the syntax of our code
# if we want to use access specifiers we have to write some naming conventions
#11 - October - 2018
print()
print("Program to display how to use Access Specifiers in Python")
print()
class MusicalInstruments:
    notes = 10 # public attribute accessible by derived class and other classes as well
    _material = "Walnut" # protected attribute accessible within this class and derived class only
    __strings = 100 # private attribute accessible just within this class and no where else

class Santoor(MusicalInstruments): #derived class
    def __init__(self):
        print("Protected attribute value Notes=", self._material)

ms = MusicalInstruments() #object of parent class

santoor = Santoor() # creating object of the class Santoor
print("public attribute value Material=", santoor.notes)

print("Private attribute value Strings=",ms._MusicalInstruments__strings)



