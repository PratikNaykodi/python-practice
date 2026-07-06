# 2. Write a program which accept N numbers from user and store it into List. Return Maximum number from that List.
# Input: Number of elements : 7
# Input Elements : 13 5 45 7 4 56 34
# Output: 56

from functools import reduce

# Lambda function to find maximum
Maximum = lambda Value1, Value2: Value1 if Value1 > Value2 else Value2

# Function to return maximum number
def MaxNumber(Data):
    return reduce(Maximum, Data)

# Main function
def main():
    Size = int(input("Enter Number of Elements : "))

    Numbers = []

    for i in range(Size):
        No = int(input("Enter Number : "))
        Numbers.append(No)

    Ret = MaxNumber(Numbers)

    print("Maximum Number is :", Ret)

# Program execution starts from here
if __name__ == "__main__":
    main()