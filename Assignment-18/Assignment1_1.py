# 1. Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.
# Input: Number of elements : 6
# Input Elements : 13 5 45 7 4 56
# Output: 130

# Function to calculate addition of all elements
def Addition(Data):
    Sum = 0

    for No in Data:
        Sum = Sum + No

    return Sum

# Main function
def main():
    Size = int(input("Enter Number of Elements : "))

    Numbers = []

    for i in range(Size):
        No = int(input("Enter Number : "))
        Numbers.append(No)

    Ret = Addition(Numbers)

    print("Addition of all elements is :", Ret)

# Program execution starts from here
if __name__ == "__main__":
    main()