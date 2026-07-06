# 4. Write a program which accept N numbers from user and store it into List. Accept one another number from user and return frequency of that number from List.
# Input: Number of elements : 11
# Input Elements : 13 5 45 7 4 56 5 34 2 5 65
# Element to search : 5
# Output: 3

# Function to count frequency of a number
def Frequency(Data, No):
    Count = 0

    for Value in Data:
        if Value == No:
            Count = Count + 1

    return Count

# Main function
def main():
    Size = int(input("Enter Number of Elements : "))

    Numbers = []

    for i in range(Size):
        Value = int(input("Enter Number : "))
        Numbers.append(Value)

    Search = int(input("Enter Element to Search : "))

    Ret = Frequency(Numbers, Search)

    print(f"Frequency of {Search} is : {Ret}")

# Program execution starts from here
if __name__ == "__main__":
    main()