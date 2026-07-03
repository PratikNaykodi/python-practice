# 6. Write a lambda function using reduce() which accepts a list of numbers and returns minimum element.
#
# Input : [10, 25, 15, 5]
# Output: 5

# Import reduce function from functools module
from functools import reduce

# Lambda function to find Minimum of two numbers
Minimum = lambda Value1, Value2: Value1 if Value1 < Value2 else Value2

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
    Result = reduce(Minimum, Numbers)

    # Print Minimum number
    print("Minimum Number is :", Result)

# Program execution starts from here
if __name__ == "__main__":
    main()

# Dry Run
# Input List:
# Numbers = [10, 25, 15, 5]

# Lambda Function:
# Minimum = lambda Value1, Value2: Value1 if Value1 < Value2 else Value2

# Step 1:
# Value1 = 10
# Value2 = 25
# 10 < 25 ? Yes
# Return = 10

# Step 2:
# Value1 = 10
# Value2 = 15
# 10 < 15 ? Yes
# Return = 10

# Step 3:
# Value1 = 10
# Value2 = 5
# 10 < 5 ? No
# Return = 5

# Final Result:
# Minimum Number = 5