# 4. Write a program which accepts one number and prints reverse of that number.
#Input : 123
#Output: 321

# Function to reverse a number
def ReverseNumber(Value):
    # Initialize reverse variable
    Rev = 0

    # Extract digits one by one
    while Value > 0:
        # Get last digit of number
        Digit = Value % 10

        # Add digit to reverse number
        Rev = (Rev * 10) + Digit

        # Remove last digit from original number
        Value = Value // 10

    # Return reversed number
    return Rev

# Main function to accept input and display result
def main():
    # Accept number from user
    No = int(input("Enter Number : "))

    # Call ReverseNumber function and store returned value
    Ret = ReverseNumber(No)

    # Print reverse of number
    print(Ret)

# Program execution starts from here
if __name__ == "__main__":
    main()