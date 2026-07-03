# 2. Write a lambda function which accepts one number and returns cube of that number.
#
# Input : 5
# Output: 125

# Lambda function to calculate cube of a number
Cube = lambda Value: Value * Value * Value

# Main function to accept input and display result
def main():
    # Accept number from user
    No = int(input("Enter Number : "))

    # Call lambda function and store returned value
    Ret = Cube(No)

    # Print Cube of number
    print("Cube of Number is :", Ret)

# Program execution starts from here
if __name__ == "__main__":
    main()