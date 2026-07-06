# 3. Write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers.
# Input: 11 5
# Output: 16

# Function to add two numbers
def Add(Value1, Value2):
    return Value1 + Value2

# Main function
def main():
    No1 = int(input("Enter First Number : "))
    No2 = int(input("Enter Second Number : "))

    Ret = Add(No1, No2)

    print(f"Addition of {No1} & {No2} is {Ret}")

# Program execution starts from here
if __name__ == "__main__":
    main()