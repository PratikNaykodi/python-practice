# 7. Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false.
# Input : 8
# Output : False
# Input : 25
# Output : True

# Function to check whether the number is divisible by 5
def ChkDivisible(No):
    if No % 5 == 0:
        return True
    else:
        return False

# Main function
def main():
    Number = int(input("Enter Number : "))

    Result = ChkDivisible(Number)

    print(Result)

# Program execution starts from here
if __name__ == "__main__":
    main()