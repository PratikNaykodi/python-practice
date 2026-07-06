# 2. Write a program which contains one function named as ChkNum() which accept one
# parameter as number. If number is even then it should display "Even number" otherwise
# display "Odd number" on console.
# Input: 11
# Output: Odd number
# Input: 8
# Output: Even number
# Function to check whether a number is even or odd
def ChkNum(No):
    if No % 2 == 0:
        return "Even number"
    else:
        return "Odd number"

# Main function
def main():
    Number = int(input("Enter Number : "))

    Ret = ChkNum(Number)

    print(f"{Number} is {Ret}")

# Program execution starts from here
if __name__ == "__main__":
    main()