# 2. Write a program which accepts one number and prints count of digits in that number.
#Input : 7521
#Output: 4

# Function to count digits of a number
def CountDigits(Value):
    # Initialize digit count
    Count = 0

    # Handle zero separately
    if Value == 0:
        return 1

    # Remove digits one by one
    while Value > 0:
        # Remove last digit
        Value = Value // 10

        # Increment digit count
        Count = Count + 1

    # Return total digit count
    return Count

# Main function to accept input and display result
def main():
    # Accept number from user
    No = int(input("Enter Number : "))

    # Call CountDigits function and store returned value
    Ret = CountDigits(No)

    # Print count of digits
    print(Ret)

# Program execution starts from here
if __name__ == "__main__":
    main()