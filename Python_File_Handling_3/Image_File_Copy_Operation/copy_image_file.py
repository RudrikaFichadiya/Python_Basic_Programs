print("_______________________________________________________________________")
print("\t\t\t\t\t\tOperations on the Image File")
print("_______________________________________________________________________")
rf = open('pythn.png', 'rb')
wf = open('pythn_copy.png', 'wb')
for line in rf:
    wf.write(line)
rf.close()
wf.close()

