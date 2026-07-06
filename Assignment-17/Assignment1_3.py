# 3. Write a program which accept one number from user and return its factorial.
# Input: 5
# Output: 120

# Function to calculate factorial
def Factorial(No):
    Fact = 1

    for i in range(1, No + 1):
        Fact = Fact * i

    return Fact

# Main function
def main():
    Number = int(input("Enter Number : "))

    Ret = Factorial(Number)

    print(f"Factorial of {Number} is : {Ret}")

# Program execution starts from here
if __name__ == "__main__":
    main()