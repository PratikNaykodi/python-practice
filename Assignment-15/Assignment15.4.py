# 4. Write a lambda function using reduce() which accepts a list of numbers and returns addition of all element.
#
# Input : [1, 2, 3, 4, 5]
# Output: 15

# Import reduce function from functools module
from functools import reduce

# Lambda function to add two numbers
Addition = lambda Value1, Value2: Value1 + Value2

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

    # Apply lambda function using reduce()
    Result = reduce(Addition, Numbers)

    # Print addition of all elements
    print("Addition of all Numbers :", Result)

# Program execution starts from here
if __name__ == "__main__":
    main()

# Dry Run
# Input List:
# Numbers = [1, 2, 3, 4, 5]

# Lambda Function:
# Addition = lambda Value1, Value2: Value1 + Value2

# Step 1:
# Value1 = 1
# Value2 = 2
# 1 + 2 = 3

# Step 2:
# Value1 = 3
# Value2 = 3
# 3 + 3 = 6

# Step 3:
# Value1 = 6
# Value2 = 4
# 6 + 4 = 10

# Step 4:
# Value1 = 10
# Value2 = 5
# 10 + 5 = 15

# Final Result:
# Addition of all Numbers = 15