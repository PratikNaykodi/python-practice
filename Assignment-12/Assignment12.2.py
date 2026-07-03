# 2. Write a program which accepts one number and prints its factors.
#Input : 12
#Output: 1 2 3 4 6 12

# Function to print factors of a number
def Factors(Value):
    # Loop from 1 to Value
    for i in range(1, Value + 1):
        # Check if number is completely divisible by i
        if Value % i == 0:
            # Print factor
            print(i, end=" ")


# Main function to accept input and display result
def main():
    # Accept number from user
    No = int(input("Enter Number : "))

    # Call Factors function
    Factors(No)

# Program execution starts from here
if __name__ == "__main__":
    main()