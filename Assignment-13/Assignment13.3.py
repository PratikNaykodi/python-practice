# 3. Write a program which accepts one number and checks whether it is perfect number or not.
#
# Input : 6
# Output: Perfect Number

# Example: 6 → Factors: 1, 2, 3
# 1 + 2 + 3 = 6

# Function to check whether number is perfect or not
def CheckPerfect(Value):
    # Initialize sum of factors
    Sum = 0

    # Find factors from 1 to Value-1
    for i in range(1, Value):
        # Check if i is a factor of number
        if Value % i == 0:
            # Add factor to sum
            Sum = Sum + i

    # Check sum of factors equals original number
    if Sum == Value:
        return True
    else:
        return False

# Main function to accept input and display result
def main():
    # Accept number from user
    No = int(input("Enter Number : "))

    # Call CheckPerfect function
    Ret = CheckPerfect(No)

    # Display result
    if Ret:
        print("Perfect Number")
    else:
        print("Not Perfect Number")

# Program execution starts from here
if __name__ == "__main__":
    main()