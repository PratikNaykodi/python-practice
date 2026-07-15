# 3: Write a Python program to implement a class named Arithmetic with the following
# characteristics:
#     The class should contain two instance variables: Value1 and Value2.
#     Define a constructor (__init__) that initialize all instance varibales to 0.0.
    
#     Implement the following instance methods:
#         Accept () - accepts values for Value1 and Value2 from the user.
#         Addition( ) -returns the addition of Value1 and Value2.
#         Subtraction() - returns the subtraction of Value1 and Value2.
#         Multiplication() -returns the multiplication of Value1 and Value2.
#         Division() -returns the division of Value1 and Value2 (handle division by zero properly).

# Create multiple objects of the Arithmetic class and invoke all the instance methods.

class Arithmetic:
    # Constructor
    def __init__(self):
        self.Value1 = 0.0
        self.Value2 = 0.0

    # Accept values from user
    def Accept(self):
        while True:
            try:
                self.Value1 = float(input("Enter first value: "))
                self.Value2 = float(input("Enter second value: "))
                break
            except ValueError:
                print("Error: Please enter valid numeric values.")

    # Addition
    def Addition(self):
        return self.Value1 + self.Value2

    # Subtraction
    def Subtraction(self):
        return self.Value1 - self.Value2

    # Multiplication
    def Multiplication(self):
        return self.Value1 * self.Value2

    # Division
    def Division(self):
        try:
            return self.Value1 / self.Value2
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."

# First Object
Obj1 = Arithmetic()
Obj1.Accept()

print("Addition :", Obj1.Addition())
print("Subtraction :", Obj1.Subtraction())
print("Multiplication :", Obj1.Multiplication())
print("Division :", Obj1.Division())

print("-"*50)

# Second Object
Obj2 = Arithmetic()
Obj2.Accept()

print("Addition :", Obj2.Addition())
print("Subtraction :", Obj2.Subtraction())
print("Multiplication :", Obj2.Multiplication())
print("Division :", Obj2.Division())