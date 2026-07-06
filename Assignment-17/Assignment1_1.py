# 1. Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() for subtraction, Mult() for multiplication and Div() for division. All functions accepts two parameters as number and perform the operation. Write on python program which call all the functions from Arithmetic module by accepting the parameters from user.
# Input: 
# Enter First Number : 6
# Enter Second Number : 5
# Output:
# Addition : 11
# Subtraction : 1
# Multiplication : 30
# Division : 1.2

# Import Arithmetic module
import Arithmetic

# Main function
def main():
    No1 = int(input("Enter First Number : "))
    No2 = int(input("Enter Second Number : "))

    print("Addition :", Arithmetic.Add(No1, No2))
    print("Subtraction :", Arithmetic.Sub(No1, No2))
    print("Multiplication :", Arithmetic.Mult(No1, No2))
    print("Division :", Arithmetic.Div(No1, No2))

# Program execution starts from here
if __name__ == "__main__":
    main()