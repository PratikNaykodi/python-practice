# 3. Write a program which accepts one number and prints sum of digits.
#Input : 123
#Output: 6

# Function to calculate sum of digits
def SumDigits(Value):
    # Initialize sum variable
    Sum = 0

    # Add digits one by one
    while Value > 0:
        # Get last digit of number
        Digit = Value % 10

        # Add digit to sum
        Sum = Sum + Digit

        # Remove last digit from number
        Value = Value // 10

    # Return total sum of digits
    return Sum

# Main function to accept input and display result
def main():
    # Accept number from user
    No = int(input("Enter Number : "))

    # Call SumDigits function and store returned value
    Ret = SumDigits(No)

    # Print sum of digits
    print(Ret)

# Program execution starts from here
if __name__ == "__main__":
    main()