import sqlite3

db = sqlite3.connect("Employees.sqlite")
print("Opened database successfully...!!!")

cursor = db.cursor()
cursor.execute("SELECT * FROM Employees")
for empid, name, age, email, salary in cursor:
    print("EMPID=", empid)
    print("NAME=", name)
    print("AGE=", age)
    print("EMAIL=", email)
    print("SALARY=", salary)
    print("-" * 20)
cursor.close()
db.commit()
db.close()