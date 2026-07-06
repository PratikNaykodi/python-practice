# 6. Write a program which accept number from user and check whether that number is positive or negative or zero.
# Input : 11
# Output : Positive Number
# Input : -8
# Output : Negative Number
# Input : 0
# Output : Zero Number

# Function to check the number
def ChkNum(No):
    if No > 0:
        return "Positive Number"
    elif No < 0:
        return "Negative Number"
    else:
        return "Zero Number"

# Main function
def main():
    Number = int(input("Enter Number : "))

    Ret = ChkNum(Number)

    print(f"{Number} is : {Ret}")

# Program execution starts from here
if __name__ == "__main__":
    main()