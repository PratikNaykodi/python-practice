# 4. Write a program which accepts one number and prints binary equivalent.
#
# Input : 10
# Output: 1010

# Function to convert decimal number into binary
def Binary(Value):
    # Initialize binary string
    Result = ""

    # Convert number into binary
    while Value > 0:
        # Get remainder (0 or 1)
        Digit = Value % 2

        # Add digit at beginning of binary string
        Result = str(Digit) + Result

        # Divide number by 2
        Value = Value // 2

    # Return binary equivalent
    return Result

# Main function to accept input and display result
def main():
    # Accept number from user
    No = int(input("Enter Number : "))

    # Call Binary function and store returned value
    Ret = Binary(No)

    # Print binary equivalent
    print("Binary Equivalent :", Ret)

# Program execution starts from here
if __name__ == "__main__":
    main()