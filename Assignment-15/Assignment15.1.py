# 1. Write a lambda function using map() which accepts a list of numbers and returns a list of squeres of each number.
#
# Input : [1, 2, 3, 4, 5]
# Output: [1, 4, 9, 16, 25]

# Lambda function to calculate square of each number using map()
Square = lambda Value: Value * Value

# Main function
def main():
    # Accept list of numbers from user
    # Numbers = list(map(int, input("Enter Numbers : ").split()))
    # Accept count of numbers
    Size = int(input("How many numbers you want to enter : "))

    # Create empty list
    Numbers = []
    # Accept numbers from user
    for i in range(Size):
        No = int(input("Enter Number : "))
        Numbers.append(No)

    # Apply lambda function on each element using map()
    Result = list(map(Square, Numbers))

    # Print list of squares
    print("Square List :", Result)


# Program execution starts from here
if __name__ == "__main__":
    main()