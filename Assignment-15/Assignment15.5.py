# 5. Write a lambda function using reduce() which accepts a list of numbers and returns maximum element.
#
# Input : [10, 25, 15, 5]
# Output: 25

# Import reduce function from functools module
from functools import reduce

# Lambda function to find maximum of two numbers
Maximum = lambda Value1, Value2: Value1 if Value1 > Value2 else Value2

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
    Result = reduce(Maximum, Numbers)

    # Print maximum number
    print("Maximum Number is :", Result)

# Program execution starts from here
if __name__ == "__main__":
    main()

# Dry Run
# Input List:
# Numbers = [10, 25, 15, 5]

# Lambda Function:
# Maximum = lambda Value1, Value2: Value1 if Value1 > Value2 else Value2

# Step 1:
# Value1 = 10
# Value2 = 25
# 10 > 25 ? No
# Return = 25

# Step 2:
# Value1 = 25
# Value2 = 15
# 25 > 15 ? Yes
# Return = 25

# Step 3:
# Value1 = 25
# Value2 = 5
# 25 > 5 ? Yes
# Return = 25

# Final Result:
# Maximum Number = 25