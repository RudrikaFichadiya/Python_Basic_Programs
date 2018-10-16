# 12 - October - 2018
#program to implement dictionaries in python
#where dictionary includes Key:Value pair data

students = {"Stud1":13,"Stud2":16,"Stud3":12,"Stud4":15,"Stud5":17,"Stud6":19,"Stud7":16}

print("Student1 Age=",students["Stud1"]) # returns value acording to entered key
# Enter key and get value
print("------------------------------------------------------------------------------------------")
print("Now we will \"Update\" Dictionary data")
print()
print("Age of Student4 Before updating, is= ", students["Stud4"])
students["Stud4"] = 20 # changed value from 15 to 20
print("New age of Student4 after updating, is= ", students["Stud4"])
print("******************************************************************************************")

print("Age of Student7 Before updating, is= ", students["Stud7"])
students["Stud7"] = 27 # changed value from 16 to 27
print("New age of Student7 after updating, is= ", students["Stud7"])
print("------------------------------------------------------------------------------------------")
print("Now we will \"Delete\" Dictionary data")
print()
print("Length of the \"Student\" dictionary before delete operation ",len(students))

del students["Stud5"]
# student deleted
print("Length of the \"Student\" dictionary is ",len(students))

