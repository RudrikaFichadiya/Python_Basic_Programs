# 12 - october - 2018
# Program to implement polymorphism
class Square:
    def __init__(self, side):
        self.side = side

    # Overload the exponential operator
    def __pow__(numOne, numTwo):
        # Return side of squareOne to the power of side of squareTwo
        print()
        print(numOne.side , "^", numTwo.side)
        return numOne.side ** numTwo.side

numOne = Square(2)
numTwo = Square(6)
print("numOne to the power of numTwo = ", numOne ** numTwo)
