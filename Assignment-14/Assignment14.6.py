# 6. Write a lambda function which accepts one number and returns True if number is odd otherwise False.
#
# Input : 4
# Output: True

# Lambda function to check whether number is odd
Odd = lambda Value: Value % 2 == 1

# Main function to accept input and display result
def main():
    # Accept number from user
    No = int(input("Enter Number : "))

    # Call lambda function and store returned value
    Ret = Odd(No)
    if(Ret):
        # Print result
        print("Is Number Odd :", Ret)
    else:
        # Print result
        print("Is Number Odd :", Ret)

# Program execution starts from here
if __name__ == "__main__":
    main()