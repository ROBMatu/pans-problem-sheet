# squareRoot.py
# Author: Robert O'Brien-Monk
# input of positive floating-point number
# output approximate square root using newton square root formula
# sources:
# https://tutorialsinhand.com/Articles/python-program-to-find-square-root-of-a-number-using-newton-square-root-formula.aspx
# https://stackoverflow.com/questions/28733759/python-square-function-using-newtons-algorithm

# function for calculating square root of a number
def sqrt (num):
    number = num
    guess = 0.5 * num
    for i in range(50):
        square_root = 0.5 * (guess + (number/guess)) 
    return number,square_root

# main program

# input from user converted to a float
num = float(input("enter a number: "))

# accepts tuple of values from sqrt() and assigns the elements to the variables
number, square_root = sqrt(num)

print(f"The square root of {number} is approx. {square_root}")