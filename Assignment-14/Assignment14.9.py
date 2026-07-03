# 9. Write a lambda function which accepts two number and returns Multiplication.
#
# Input : 2 5
# Output: 7

# Lambda function to perform multiplication of two numbers
Multiplication = lambda Value1, Value2: Value1 * Value2

# Main function to accept input and display result
def main():
    # Accept first number from user
    No1 = int(input("Enter First Number : "))
    # Accept second number from user
    No2 = int(input("Enter Second Number : "))

    # Call lambda function and store returned value
    Ret = Multiplication(No1, No2)

    # Print Multiplication result
    print("Multiplication is :", Ret)

# Program execution starts from here
if __name__ == "__main__":
    main()