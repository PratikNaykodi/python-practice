# 1. Write a program which contains one lambda function which accepts one parameter and return power of two.
# Input : 4   Output: 16
# Input : 6   Output: 36

def DisplayPower(No):
    return No ** 2

def main():
    No = int(input("Enter Number : "))

    Ret = DisplayPower(No)

    print(f"Power of two : {Ret}")

if __name__ == "__main__":
    main()