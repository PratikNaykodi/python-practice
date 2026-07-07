# 2. Write a program which contains one lambda function which accepts two parameters and return its multiplication.
# Input : 4 3   Output: 12
# Input : 6 3   Output: 18

Multiplication = lambda Value1, Value2 : Value1*Value2

def main():
    No1 = int(input("Enter First Number : "))
    No2 = int(input("Enter Second Number : "))

    Ret = Multiplication(No1, No2)

    print(f"Multiplication of two number: {Ret}")

if __name__ == "__main__":
    main()