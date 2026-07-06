# 4. Write a program which accept one number form user and return addition of its factors.
# Input: 12
# Output: 16   (1+2+4+6)

# Function to calculate addition of factors
def AddFactors(No):
    Sum = 0

    for i in range(1, No):
        if No % i == 0:
            Sum = Sum + i

    return Sum

# Main function
def main():
    Number = int(input("Enter Number : "))

    Ret = AddFactors(Number)

    print(f"Addition of factors of {Number} is : {Ret}")
    
# Program execution starts from here
if __name__ == "__main__":
    main()