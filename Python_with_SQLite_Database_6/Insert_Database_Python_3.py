import sqlite3

db = sqlite3.connect("Employees.sqlite")
print("Opened database successfully")

db.execute('CREATE TABLE IF NOT EXISTS Employees (empid INTEGER PRIMARY KEY NOT NULL, name TEXT NOT NULL, age INTEGER, email TEXT, salary INTEGER)')
db.execute("INSERT INTO Employees (empid, name, age, email, salary) VALUES(001,'ABC', 27, 'abc@email.com', 25000)")
db.execute("INSERT INTO Employees VALUES(002,'XYZ', 26, 'xyz@email.com', 31500)")
db.execute("INSERT INTO Employees VALUES(003,'PQR', 28, 'pqr@email.com', 30000)")
db.execute("INSERT INTO Employees VALUES(004,'STU', 23, 'stu@email.com', 29000)")
db.execute("INSERT INTO Employees VALUES(005,'MNO', 20, 'mno@email.com', 45000)")
db.execute("INSERT INTO Employees VALUES(006,'KLM', 29, 'klm@email.com', 37000)")
db.execute("INSERT INTO Employees VALUES(007,'EFG', 30, 'efg@email.com', 43000)")
db.commit()
print("Records created successfully")
db.close()