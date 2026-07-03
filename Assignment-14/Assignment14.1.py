# 1. Write a lambda function which accepts one number and returns square of that number.
#
# Input : 5
# Output: 25

# Lambda function to calculate square of a number
Square = lambda Value: Value * Value

# Main function to accept input and display result
def main():
    # Accept number from user
    No = int(input("Enter Number : "))

    # Call lambda function and store returned value
    Ret = Square(No)

    # Print square of number
    print("Square of Number is :", Ret)

# Program execution starts from here
if __name__ == "__main__":
    main()