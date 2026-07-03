# 9. Write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements.
#
# Input : [1, 2, 3, 4, 5]
# Output: 120

# Import reduce function from functools module
from functools import reduce

# Lambda function to multiply two numbers
Product = lambda Value1, Value2: Value1 * Value2

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
    Result = reduce(Product, Numbers)

    # Print product of all elements
    print("Product of all Numbers :", Result)

# Program execution starts from here
if __name__ == "__main__":
    main()

# Dry Run
# Input List:
# Numbers = [1, 2, 3, 4, 5]

# Lambda Function:
# Product = lambda Value1, Value2: Value1 * Value2

# Step 1:
# Value1 = 1
# Value2 = 2
# 1 * 2 = 2

# Step 2:
# Value1 = 2
# Value2 = 3
# 2 * 3 = 6

# Step 3:
# Value1 = 6
# Value2 = 4
# 6 * 4 = 24

# Step 4:
# Value1 = 24
# Value2 = 5
# 24 * 5 = 120

# Final Result:
# Product of all Numbers = 120