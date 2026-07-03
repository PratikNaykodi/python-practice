# 2. Write a program which accepts one number and prints sum of first N natural numbers .
#Input : 5
#Output: 15

# Function to calculate sum of first N natural numbers
def SumNaturalNumbers(Value):
    # Initialize sum variable
    Sum = 0
    # Add numbers from 1 to N
    for i in range(1, Value + 1):
        Sum = Sum + i

    # Return total sum
    return Sum

# Main function to accept input and display result
def main():
    # Accept number from user
    No = int(input("Enter Number : "))

    # Call SumNaturalNumbers function and store returned value
    Ret = SumNaturalNumbers(No)

    # Print sum of first N natural numbers
    print(Ret)

# Program execution starts from here
if __name__ == "__main__":
    main()