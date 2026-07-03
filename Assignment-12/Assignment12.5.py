# 5. Program: Accept one numbers and prints that many numbers in reverse order. 
#
# Input : 5
# Output: 5 4 3 2 1

# Function to print numbers in reverse order
def PrintReverseNumbers(Value):
    # Loop from Value to 1
    for i in range(Value, 0, -1):
        # Print number
        print(i, end=" ")

# Main function to accept input and display result
def main():
    # Accept number from user
    No = int(input("Enter Number : "))
    # Call PrintReverseNumbers function
    PrintReverseNumbers(No)

# Program execution starts from here
if __name__ == "__main__":
    main()