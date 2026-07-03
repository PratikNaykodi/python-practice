# 3. Write a program which accepts one numbers and prints square of that number.
#Input : 5
#Output: 25

# Function to calculate square of a number
def CalculateSquare(Value1):
    # Return multiplication of number by itself
    return Value1 * Value1

# Main function to accept input and display result
def main():
    # Accept number from user
    No1 = int(input("Enter Number : "))

    # Call CalculateSquare function and store returned value
    Ret = CalculateSquare(No1)
    # Print square of the number
    print(Ret)

# Program execution starts from here
if __name__ == "__main__":
    main()