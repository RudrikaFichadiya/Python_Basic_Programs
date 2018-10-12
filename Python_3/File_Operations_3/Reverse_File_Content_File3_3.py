#12 - October - 2018
#program to reverse content of a .txt file
filename=input("Enter file name: ")
for line in reversed(list(open(filename))):
    print(line.rstrip())