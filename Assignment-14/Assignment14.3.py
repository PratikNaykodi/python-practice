# 3. Write a lambda function which accepts two number and returns Maximum number.
#
# Input : 5 10
# Output: 10

# Lambda function to find maximum of two numbers
# Take two numbers. If the first number is greater, return the first number; otherwise return the second number
Maximum = lambda Value1, Value2: Value1 if Value1 > Value2 else Value2

# Main function to accept input and display result
def main():
    # Accept first number from user
    No1 = int(input("Enter First Number : "))
    # Accept second number from user
    No2 = int(input("Enter Second Number : "))

    # Call lambda function and store returned value
    Ret = Maximum(No1, No2)

    # Print maximum number
    print("Maximum Number is :", Ret)

# Program execution starts from here
if __name__ == "__main__":
    main()