# 4. Write a program which accepts one number and prints all even numbers till that number.
#Input : 10
#Output: 2 4 6 8 10

# Function to print even numbers till given number
def EvenNumbers(Value):
    # Loop from 1 to Value
    for i in range(1, Value + 1):
        # Check if number is even
        if i % 2 == 0:
            # Print even number
            print(i, end=" ")

# Main function to accept input and display result
def main():
    # Accept number from user
    No = int(input("Enter Number : "))

    # Call EvenNumbers function
    EvenNumbers(No)

# Program execution starts from here
if __name__ == "__main__":
    main()