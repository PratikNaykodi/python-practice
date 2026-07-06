# 5. Write a program which accept one number for user and check whether number is prime or not.
# Input: 5
# Output: It is Prime Number

# Function to check whether the number is prime
def ChkPrime(No):
    if No <= 1:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False

    return True

# Main function
def main():
    Number = int(input("Enter Number : "))

    Ret = ChkPrime(Number)

    if Ret:
        print(f"{Number} is a Prime Number.")
    else:
        print(f"{Number} is not a Prime Number.")

# Program execution starts from here
if __name__ == "__main__":
    main()