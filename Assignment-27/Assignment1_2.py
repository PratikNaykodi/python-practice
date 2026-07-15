# 2: Write a Python program to implement a class named BankAccount with the following
# requirements:
#     The class should contain two instance variables:
#         Name (Account holder name)
#         Amount (Account balance)
#     The class should contain one class variable:
#         ROI (Rate of Interest), initialized to 10.5

#     Define a constructor (__init__) that accepts Name and initial Amount.

#     Implement the following instance methods:
#         Display() -displays account holder name and current balance
#         Deposit() - accepts an amount from the user and adds it to balance
#         Withdraw() - accepts an amount from the user and subtracts it from balance
#         (Ensure withdrawal is allowed only if sufficient balance exists)
#         CalculateInterest() - calculates and returns interest using formula:
#             Interest = (Amount * ROI) / 100
#     Create multiple objects and demonstrate all methods.

class BankAccount:

    # Class variable
    ROI = 10.5

    # Constructor
    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    # Display account details
    def Display(self):
        print("\nAccount Holder :", self.Name)
        print("Current Balance :", self.Amount)

    # Deposit money
    def Deposit(self):
        try:
            DepositAmount = float(input("Enter amount to deposit: "))

            if DepositAmount <= 0:
                print("Deposit amount must be greater than zero.")
                return

            self.Amount += DepositAmount
            print("Amount deposited successfully.")

        except ValueError:
            print("Invalid amount.")

    # Withdraw money
    def Withdraw(self):
        try:
            WithdrawAmount = float(input("Enter amount to withdraw: "))

            if WithdrawAmount <= 0:
                print("Withdrawal amount must be greater than zero.")
            elif WithdrawAmount > self.Amount:
                print("Insufficient balance.")
            else:
                self.Amount -= WithdrawAmount
                print("Amount withdrawn successfully.")

        except ValueError:
            print("Invalid amount.")

    # Calculate Interest
    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest

# First Account
Obj1 = BankAccount("Pratik", 10000)

Obj1.Display()
Obj1.Deposit()
Obj1.Display()
Obj1.Withdraw()
Obj1.Display()
print("Interest :", Obj1.CalculateInterest())

print("-"*50)

# Second Account
Obj2 = BankAccount("Rahul", 5000)

Obj2.Display()
Obj2.Deposit()
Obj2.Withdraw()
Obj2.Display()
print("Interest :", Obj2.CalculateInterest())