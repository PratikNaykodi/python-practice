# 4. Program: Accept one numbers and prints that many numbers starting from . 
#
# Input : 5
# Output: 1 2 3 4 5

# Function to print numbers from 1 to Value
def PrintNumbers(Value):
    # Loop from 1 to Value
    for i in range(1, Value + 1):
        # Print number
        print(i, end=" ")

# Main function to accept input and display result
def main():
    # Accept number from user
    No = int(input("Enter Number : "))
    # Call PrintNumbers function
    PrintNumbers(No)

# Program execution starts from here
if __name__ == "__main__":
    main()