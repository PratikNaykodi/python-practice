# 5. Write a lambda function which accepts one number and returns True if number is even otherwise False.
#
# Input : 4
# Output: True

# Lambda function to check whether number is even
Even = lambda Value: Value % 2 == 0

# Main function to accept input and display result
def main():
    # Accept number from user
    No = int(input("Enter Number : "))

    # Call lambda function and store returned value
    Ret = Even(No)
    if(Ret):
        # Print result
        print("Is Number Even :", Ret)
    else:
        print("Is Number Even :", Ret)

# Program execution starts from here
if __name__ == "__main__":
    main()