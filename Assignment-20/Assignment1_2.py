# 2. Design a Python application that creates two threads named EvenFactor and OddFactor.

# Both threads should accept one integer number as a parameter.
# The EvenFactor thread should:
# Identify all even factors of the given number.
# Calculate and display the sum of even factors.

# The OddFactor thread should:
# Identify all odd factors of the given number.
# Calculate and display the sum of odd factors.
# After both threads complete execution, the main thread should display the message: "Exit from main"

# Import threading module
import threading

# Global variables
EvenFactorSum = 0
OddFactorSum = 0

# Function to calculate sum of even factors
def EvenFactor(Number):
    Sum = 0

    print("Even Factors are :", end=" ")

    for Index in range(1, Number + 1):
        if Number % Index == 0 and Index % 2 == 0:
            print(Index, end=" ")
            Sum = Sum + Index

    print()
    return Sum

# Function to calculate sum of odd factors
def OddFactor(Number):
    Sum = 0

    print("Odd Factors are :", end=" ")

    for Index in range(1, Number + 1):
        if Number % Index == 0 and Index % 2 != 0:
            print(Index, end=" ")
            Sum = Sum + Index

    print()
    return Sum

# Thread function for even factors
def EvenFactorThread(Number):
    global EvenFactorSum
    EvenFactorSum = EvenFactor(Number)

# Thread function for odd factors
def OddFactorThread(Number):
    global OddFactorSum
    OddFactorSum = OddFactor(Number)

# Main function
def main():
    # Accept number from user
    Number = int(input("Enter Number : "))

    # Create threads
    t1 = threading.Thread(target=EvenFactorThread, args=(Number,))
    t2 = threading.Thread(target=OddFactorThread, args=(Number,))

    # Start threads
    t1.start()
    t2.start()

    # Wait for both threads to complete
    t1.join()
    t2.join()

    # Display results
    print("Addition of Even Factors :", EvenFactorSum)
    print("Addition of Odd Factors :", OddFactorSum)

    print("Exit from main")

# Program execution starts from here
if __name__ == "__main__":
    main()