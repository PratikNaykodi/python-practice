# 4. Write a program which accepts one number and prints cube of that number.
#Input : 5
#Output: 125

# Function to calculate cube of a number
def CalculateCube(Value1):
     # Return multiplication of number three times
    return Value1 * Value1 * Value1

# Main function to accept input and display result
def main():
    # Accept number from user
    No1 = int(input("Enter Number : "))

    # Call CalculateSquare function and store returned value
    Ret = CalculateCube(No1)
    # Print cube of the number
    print(Ret)

# Program execution starts from here
if __name__ == "__main__":
    main()