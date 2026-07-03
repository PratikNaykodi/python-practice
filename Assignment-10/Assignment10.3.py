# 3. Write a program which accepts one number and prints factorial of that numbers .
#Input : 5
#Output: 120

# Function to calculate factorial of a number
def Factorial(Value):
    # Initialize factorial variable
    Fact = 1

    # Multiply numbers from 1 to N
    for i in range(1, Value + 1):
        Fact = Fact * i

    # Return factorial value
    return Fact

# Main function to accept input and display result
def main():
    # Accept number from user
    No = int(input("Enter Number : "))

    # Call Factorial function and store returned value
    Ret = Factorial(No)

    # Print factorial of the number
    print(Ret)

# Program execution starts from here
if __name__ == "__main__":
    main()