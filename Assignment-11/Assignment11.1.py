# 1. Write a program which accepts one number and checks whether it is prime or not.
#Input : 11
#Output: Prime Number

# Function to check whether number is prime or not
def CheckPrime(Value):
    # Assume number is prime initially
    Flag = True

    # Prime numbers are greater than 1
    if Value <= 1:
        Flag = False
    else:
        # Check divisibility from 2 to Value-1
        for i in range(2, Value):
            # If number is divisible by i, it is not prime
            if Value % i == 0:
                Flag = False
                break

    # Return result
    return Flag

# Main function to accept input and display result
def main():
    # Accept number from user
    No = int(input("Enter Number : "))

    # Call CheckPrime function and store returned value
    Ret = CheckPrime(No)

    # Display result based on returned value
    if Ret == True:
        print("Prime Number")
    else:
        print("Not Prime Number")

# Program execution starts from here
if __name__ == "__main__":
    main()