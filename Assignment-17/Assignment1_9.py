# 9. Write a program which accept number from user and return number of digits in that number.
# Input: 5187934
# Output: 7

# Function to count digits
def CountDigits(No):
    Count = 0

    while No > 0:
        Count = Count + 1
        No = No // 10  #// is use for Drops the decimal

    return Count

# Main function
def main():
    Number = int(input("Enter Number : "))

    Ret = CountDigits(Number)

    print(f"Number of digits in {Number} is : {Ret}")

# Program execution starts from here
if __name__ == "__main__":
    main()