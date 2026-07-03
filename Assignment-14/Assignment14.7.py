# 7. Write a lambda function which accepts one number and returns True if divisible by 5 otherwise False.
#
# Input : 25
# Output: True

# Lambda function to check whether number is divisible by 5
DivisibleBy5 = lambda Value: Value % 5 == 0

# Main function to accept input and display result
def main():
    # Accept number from user
    No = int(input("Enter Number : "))
    # Call lambda function and store returned value
    Ret = DivisibleBy5(No)

    # Print result
    print("Is Number Divisible by 5 :", Ret)

# Program execution starts from here
if __name__ == "__main__":
    main()