# 8. Write a lambda function using filter() which accepts a list of numbers and returns list of numbers divisible by both 3 and 5.
#
# Input : [10, 15, 20, 30, 45, 50]
# Output: [15, 30, 45]

# Lambda function to check number divisible by both 3 and 5
Divisible = lambda Value: Value % 3 == 0 and Value % 5 == 0

# Main function
def main():
    # Accept list of numbers from user
    # Numbers = list(map(int, input("Enter Numbers : ").split()))

    # Accept count of numbers
    Size = int(input("How many numbers you want to enter : "))

    # Create empty list
    Numbers = list()
    # Accept numbers from user
    for i in range(Size):
        No = int(input("Enter Number : "))
        Numbers.append(No)

    # Apply lambda function using filter()
    Result = list(filter(Divisible, Numbers))

    # Print numbers divisible by both 3 and 5
    print("Numbers divisible by 3 and 5 :", Result)

# Program execution starts from here
if __name__ == "__main__":
    main()
