# 12 - october - 2018
# Program to implement polymorphism
class Square:
    def __init__(self, side):
        self.side = side

    # Overload the exponential operator
    def __pow__(numOne, numTwo):
        # Return side of squareOne to the power of side of squareTwo
        print(numOne.side , "^", numTwo.side)
        return numOne.side ** numTwo.side

numOne = Square(3)
numTwo = Square(4)
print("numOne to the power of numTwo = ", numOne ** numTwo)
