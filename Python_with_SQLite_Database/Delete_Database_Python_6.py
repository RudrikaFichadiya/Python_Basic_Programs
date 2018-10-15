import sqlite3

db = sqlite3.connect("Employees.sqlite")
print ("Opened database successfully")

db.execute("DELETE FROM Employees WHERE empid = 4")
db.commit()
print("Total number of rows deleted :", db.total_changes)

cursor = db.execute("SELECT empid, name, age, email, salary FROM Employees")
for row in cursor:
    print("EMPID = ", row[0])
    print("NAME = ", row[1])
    print("AGE = ", row[2])
    print("EMAIL = ",row[3])
    print("SALARY = ", row[4])
    print("-" * 20)
print()
print("Operation done successfully...!")
db.close()