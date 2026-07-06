# 5. Write a program which accept N numbers from user and store it into List. Return addition of all prime numbers from that List. Main python file accepts N numbers from user and pass each number to ChkPrime() function which is part of our user defined module named as MarvellousNum. Name of the function from main python file should be ListPrime().
# Input: Number of elements : 11
# Input Elements : 13 5 45 7 4 56 10 34 2 5 8
# Output: 32

# Import user-defined module
import MarvellousNum

# Function to calculate addition of prime numbers
def ListPrime(Data):
    Sum = 0

    for No in Data:
        if MarvellousNum.ChkPrime(No):
            Sum = Sum + No

    return Sum

# Main function
def main():
    Size = int(input("Enter Number of Elements : "))

    Numbers = []

    for i in range(Size):
        No = int(input("Enter Number : "))
        Numbers.append(No)

    Ret = ListPrime(Numbers)

    print("Addition of Prime Numbers is :", Ret)

# Program execution starts from here
if __name__ == "__main__":
    main()