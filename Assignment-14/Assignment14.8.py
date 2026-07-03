# 8. Write a lambda function which accepts two number and returns Addition.
#
# Input : 2 5
# Output: 7


# Lambda function to perform addition of two numbers
Addition = lambda Value1, Value2: Value1 + Value2

# Main function to accept input and display result
def main():
    # Accept first number from user
    No1 = int(input("Enter First Number : "))
    # Accept second number from user
    No2 = int(input("Enter Second Number : "))

    # Call lambda function and store returned value
    Ret = Addition(No1, No2)

    # Print addition result
    print("Addition is :", Ret)

# Program execution starts from here
if __name__ == "__main__":
    main()