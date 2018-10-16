# 12 - October - 2018
import csv
print("_____________________________________________________________________________________________")
print("\t\t\t\t\t\tStudent Grade History")
# CSV - Comma-Separated Values File
print("_____________________________________________________________________________________________")

print()
print("  No.    Student Id   Sub1  Sub2  Sub3   Sub4    Sub5      Emailid          Birthdate")
print("_____________________________________________________________________________________________")

with open('stud_data.csv', 'r')as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line)

