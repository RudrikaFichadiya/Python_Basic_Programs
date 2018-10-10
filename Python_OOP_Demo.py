class Person: #class
    def getName(self): # class member function, self refers to current object or instance
        print("ABC_Person_Name")
    def getAge(self):
        print("20")

p = Person() # object  p of Person class
p.getName() # calling member functions using object of class
p.getAge()
print("_____________________________________________________________________")

class PersonDetails:
    def __init__(self,name,age): # init function allows us to create object of a class with specific properties/ attributes
        self.name = name
        self.age = age
    def getPersonName(self):
        print("Your name is=" + self.name)
    def getPersonAge(self):
        print("Your Age is=" +self.age)
pobj = PersonDetails("RHF", "20")
pobj.getPersonAge()
pobj.getPersonName()
