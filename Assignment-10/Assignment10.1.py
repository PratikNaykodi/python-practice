# 1. Write a program which accepts one number and prints multiplication table of that number.
#Input : 4
#Output: 4 8 12 16 20 24 28 .... 40

# Function to print multiplication table
def MultiplicationTable(Value):
    # Loop from 1 to 10
    for i in range(1, 11):
        # Print multiplication result
        print(Value * i, end=" ")

# Main function to accept input and display result
def main():
    # Accept number from user
    No = int(input("Enter Number : "))

    # Call multiplication table function
    MultiplicationTable(No)

# Program execution starts from here
if __name__ == "__main__":
    main()