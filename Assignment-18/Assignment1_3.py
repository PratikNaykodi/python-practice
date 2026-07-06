# 3. Write a program which accept N numbers from user and store it into List. Return Minimum number from that List.
# Input: Number of elements : 4
# Input Elements : 13 5 45 7
# Output: 5

# Import reduce function from functools module
from functools import reduce

# Lambda function to find minimum
Minimum = lambda Value1, Value2: Value1 if Value1 < Value2 else Value2

# Function to return minimum number
def MinNumber(Data):
    return reduce(Minimum, Data)

# Main function
def main():
    Size = int(input("Enter Number of Elements : "))

    Numbers = []

    for i in range(Size):
        No = int(input("Enter Number : "))
        Numbers.append(No)

    Ret = MinNumber(Numbers)

    print("Minimum Number is :", Ret)

# Program execution starts from here
if __name__ == "__main__":
    main()