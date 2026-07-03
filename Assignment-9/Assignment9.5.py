# 5. Write a program which accepts one number and check whether it is divisible by 3 and 5.
#Input : 15
#Output: Divisible by 3 and 5

# Function to check divisibility by 3 and 5
def Divisible(Value1):
    # Check if number is divisible by both 3 and 5
    if Value1 % 3 == 0 and Value1 % 5 == 0:
        return True
    # Return False if number is not divisible by both
    else:
        return False

# Main function to accept input and display result
def main():
    # Accept number from user
    No1 = int(input("Enter Number : "))

    # Call Divisible function and store returned value
    Ret = Divisible(No1)

    # Check returned result and print output
    if Ret:
        print("Divisible by 3 and 5")
    else:
        print("Not Divisible by 3 and 5")

# Program execution starts from here
if __name__ == "__main__":
    main()