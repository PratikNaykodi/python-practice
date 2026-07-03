# 10. Write a lambda function which accepts three number and returns largest number.
#
# Input : 10 25 15
# Output: 25

# Lambda function to find largest of three numbers
Largest = lambda Value1, Value2, Value3: Value1 if Value1 > Value2 and Value1 > Value3 else (Value2 if Value2 > Value3 else Value3)

# Main function to accept input and display result
def main():
    # Accept first number from user
    No1 = int(input("Enter First Number : "))
    # Accept second number from user
    No2 = int(input("Enter Second Number : "))
    # Accept third number from user
    No3 = int(input("Enter Third Number : "))

    # Call lambda function and store returned value
    Ret = Largest(No1, No2, No3)

    # Print largest number
    print("Largest Number is :", Ret)

# Program execution starts from here
if __name__ == "__main__":
    main()