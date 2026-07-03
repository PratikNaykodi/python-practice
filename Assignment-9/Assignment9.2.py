# 2. Write a program which contains one funtion ChkGreater() that accepts two numbers and prints the greater
#Input : 10 20
#Output: 20 is greater

# Function to check which number is greater
def ChkGreater(Value1, Value2):
    # Return first number if it is greater
    if Value1 > Value2:
        return Value1
    # Return second number if it is greater
    elif Value2 > Value1:
        return Value2
    # Return None if both numbers are equal
    else:
        return None

# Main function to accept input and display result
def main():
    # Accept two numbers from user
    No1 = int(input("Enter First Number : "))
    No2 = int(input("Enter Second Number : "))

    # Store returned value
    Ret = ChkGreater(No1, No2)

    # Check if function returned None
    if Ret is None:
        print("Both are same")
    else:
        print(Ret, "is greater")

# Program execution starts from here
if __name__ == "__main__":
    main()