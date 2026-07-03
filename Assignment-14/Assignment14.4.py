# 4. Write a lambda function which accepts two number and returns Minimum number.
#
# Input : 5 10
# Output: 5

# Lambda function to find minimum of two numbers
# Take two numbers. If the first number is less, return the first number; otherwise return the second number
Minimum = lambda Value1, Value2: Value1 if Value1 < Value2 else Value2

# Main function to accept input and display result
def main():
    # Accept first number from user
    No1 = int(input("Enter First Number : "))
    # Accept second number from user
    No2 = int(input("Enter Second Number : "))

    # Call lambda function and store returned value
    Ret = Minimum(No1, No2)

    # Print minimum number
    print("Minimum Number is :", Ret)

# Program execution starts from here
if __name__ == "__main__":
    main()