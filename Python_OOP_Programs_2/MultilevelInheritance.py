# 11 - October - 2018
print()
print("Program to Implement Multilevel Inheritance")
class MusicalInstruments:
    numberofNotes = 10
class StringInstrument(MusicalInstruments):
    materialtoMake = "Walnut"
class Santoor(StringInstrument):
    def __init__(self):
        self.numberofStrings = 100
        print("Santoor Consists of \"{}\" number of strings. It is mostly made of \"{}\" and it includes \"{}\" number of total notes.".format(self.numberofStrings, self.materialtoMake, self.numberofNotes))

santoor = Santoor()

