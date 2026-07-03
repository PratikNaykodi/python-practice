# 10. Write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers.
#
# Input : [1, 2, 3, 4, 5, 6]
# Output: 3

# Lambda function to check even number
Even = lambda Value: Value % 2 == 0

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

    # Filter even numbers using lambda function
    EvenNumbers = list(filter(Even, Numbers))

    print(EvenNumbers)
    # Count total even numbers
    Count = len(EvenNumbers)

    # Print count of even numbers
    print("Count of Even Numbers :", Count)

# Program execution starts from here
if __name__ == "__main__":
    main()
