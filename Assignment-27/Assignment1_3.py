# 3: Write a Python program to implement a class named Numbers with the following
# specifications:
#     The class should contain one instance variable:
#         Value
#     Define a constructor (__init__) that accept a number  from user and initializes Value.
#     Implement the following instance methods:
#         ChkPrime() -returns True if the number is prime, otherwise returns False
#         ChkPerfect() -returns True if the number is perfect, otherwise returns False
#         Factors() -displays all factors of the number
#         SumFactors() -returns the sum of all factors
#     Create multiple objects and call all methods.

class Numbers:
    # Constructor
    def __init__(self):
        self.Value = 0

    # Accept value from user
    def Accept(self):
        while True:
            try:
                self.Value = int(input("Enter a number: "))
                if self.Value <= 0:
                    print("Please enter a positive number.")
                    continue
                break
            except ValueError:
                print("Invalid input! Please enter a valid integer.")

    # Check Prime
    def ChkPrime(self):
        if self.Value < 2:
            return False

        # Check whether Value is prime
        # Value ** 0.5 gives the square root of the number.
        # We check only up to the square root because checking beyond it is unnecessary.
        for i in range(2, int(self.Value ** 0.5) + 1):
            if self.Value % i == 0:
                return False

        return True

    # Check Perfect Number
    def ChkPerfect(self):
        Sum = 0

        for i in range(1, self.Value):
            if self.Value % i == 0:
                Sum += i

        return Sum == self.Value

    # Display Factors
    def Factors(self):
        print("Factors are:")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    # Sum of Factors
    def SumFactors(self):
        Sum = 0

        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                Sum += i

        return Sum

# First Object
Obj1 = Numbers()
Obj1.Accept()

print("Prime :", Obj1.ChkPrime())
print("Perfect :", Obj1.ChkPerfect())
Obj1.Factors()
print("Sum of Factors :", Obj1.SumFactors())

print("-"*50)

# Second Object
Obj2 = Numbers()
Obj2.Accept()

print("Prime :", Obj2.ChkPrime())
print("Perfect :", Obj2.ChkPerfect())
Obj2.Factors()
print("Sum of Factors :", Obj2.SumFactors())