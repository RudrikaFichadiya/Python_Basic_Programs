# 12 - October - 2018
#program to implement try % except
print("Enter numberOne=")
numberOne=int(input())
print("Enter numberTwo=")
numberTwo=int(input())
if numberOne and numberTwo < 0:
    print("Minus numbers not allowed")
try:
    result = numberTwo/numberOne
except:
    print("0 is not allowed in division!!! Try again")
    