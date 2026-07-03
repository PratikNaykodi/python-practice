# 5. Write a program which accepts one character and checks whether it is Vowel or Consonant.
#Input : a
#Output: Vowel

# Function to reverse a number
def ReverseNumber(Value):
    # Initialize reverse variable
    Rev = 0

    # Store digits one by one
    while Value > 0:
        # Get last digit of number
        Digit = Value % 10

        # Build reverse number
        Rev = (Rev * 10) + Digit

        # Remove last digit from original number
        Value = Value // 10

    # Return reversed number
    return Rev

# Function to check palindrome
def CheckPalindrome(Value):
    # Store original number
    Original = Value

    # Call ReverseNumber function
    Reverse = ReverseNumber(Value)

    # Compare original number with reverse number
    if Original == Reverse:
        return True
    else:
        return False

# Main function to accept input and display result
def main():
    # Accept number from user
    No = int(input("Enter Number : "))

    # Call CheckPalindrome function
    Ret = CheckPalindrome(No)

    # Display result
    if Ret:
        print("Palindrome")
    else:
        print("Not Palindrome")

# Program execution starts from here
if __name__ == "__main__":
    main()