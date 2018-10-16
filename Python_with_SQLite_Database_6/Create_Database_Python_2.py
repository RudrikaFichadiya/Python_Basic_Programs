import sqlite3
db = sqlite3.connect("Empolyees.sqlite")
print("Opened database successfully...!!!")

db.execute('''CREATE TABLE IF NOT EXISTS Employees 
            (empid INTEGER PRIMARY KEY NOT NULL, name TEXT NOT NULL, age INTEGER, email TEXT, salary REAL)''')
print("Database Created Successfully...!!!")
db.commit()
db.close()
