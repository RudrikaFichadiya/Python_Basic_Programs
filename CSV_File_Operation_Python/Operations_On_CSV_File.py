# 11 - October - 2018
import csv
print("_______________________________________________________________________")
print("\t\t\t\t\t\tOperations on CSV File")
# CSV - Comma-Separated Values File
print("_______________________________________________________________________")
print()
with open('file2csvdemo.csv', 'r')as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line)

