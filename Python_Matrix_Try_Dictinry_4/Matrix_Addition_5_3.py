# 12 - October -2018
# Program to add two matrices using nested loop

mat1 = [[1,2,3],
    [4,5,6],
    [7,8,9]]

mat2 = [[10,9,8],
    [7,6,5],
    [4,3,2]]

resultmat = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(mat1)):
   # iterate through columns
   for j in range(len(mat1[0])):
       resultmat[i][j] = mat1[i][j] + mat2[i][j]

for r in resultmat:
   print(r)