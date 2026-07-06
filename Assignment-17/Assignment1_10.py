# 10. Write a program which accept number from user and return addition of digits in that number.
# Input: 5187934
# Output: 37

# Function to calculate addition of digits
def AddDigits(No):
    Sum = 0

    while No > 0:
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10 # // use for Drops the decimal

    return Sum

# Main function
def main():
    Number = int(input("Enter Number : "))

    Ret = AddDigits(Number)

    print(f"Addition of digits in {Number} is : {Ret}")

# Program execution starts from here
if __name__ == "__main__":
    main()