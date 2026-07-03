# 3. Program: Accept two numbers and print Addition, Subtraction,
# Multiplication and Division
#
# Input : 12 4
# Output:
# Addition: 16
# Subtraction: 8
# Multiplication: 48
# Division: 3.0

# Function to perform addition
def Addition(Value1, Value2):
    # Return addition of two numbers
    return Value1 + Value2

# Function to perform subtraction
def Subtraction(Value1, Value2):
    # Return subtraction of two numbers
    return Value1 - Value2

# Function to perform multiplication
def Multiplication(Value1, Value2):
    # Return multiplication of two numbers
    return Value1 * Value2

# Function to perform division
def Division(Value1, Value2):
    # Check division by zero
    if Value2 == 0:
        return "Division not possible"

    # Return division of two numbers
    return Value1 / Value2

# Main function to accept input and display result
def main():
    # Accept first number from user
    No1 = int(input("Enter First Number : "))
    # Accept second number from user
    No2 = int(input("Enter Second Number : "))

    # Call Addition function
    Ret = Addition(No1, No2)
    print("Addition :", Ret)

    # Call Subtraction function
    Ret = Subtraction(No1, No2)
    print("Subtraction :", Ret)

    # Call Multiplication function
    Ret = Multiplication(No1, No2)
    print("Multiplication :", Ret)

    # Call Division function
    Ret = Division(No1, No2)
    print("Division :", Ret)

# Program execution starts from here
if __name__ == "__main__":
    main()