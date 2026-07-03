# 5. Write a program which accepts one number and prints all odd numbers till that number.
#Input : 10
#Output: 1 3 5 7 9

# Function to print odd numbers till given number
def OddNumbers(Value):
    # Loop from 1 to Value
    for i in range(1, Value + 1):
        # Check if number is odd
        if i % 2 == 1:
            # Print odd number
            print(i, end=" ")

# Main function to accept input and display result
def main():
    # Accept number from user
    No = int(input("Enter Number : "))

    # Call OddNumbers function
    OddNumbers(No)

# Program execution starts from here
if __name__ == "__main__":
    main()