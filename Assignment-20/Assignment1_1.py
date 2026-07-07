# 1. Design a Python application that creates two separate threads named Even and Odd.

# The Even thread should display the first 10 even numbers.
# The Odd thread should display the first 10 odd numbers.
# Both threads should execute independently using the threading module.
# Ensure proper thread creation and execution.

# Import threading module
import threading

# Global variables
EvenNumbers = []
OddNumbers = []

# Function to generate even numbers
def Even(Count):
    Result = []

    for Number in range(1, Count + 1):
        Result.append(Number * 2)

    return Result

# Function to generate odd numbers
def Odd(Count):
    Result = []

    for Number in range(1, Count + 1):
        Result.append((Number * 2) - 1)

    return Result

# Thread function for even numbers
def EvenThread(Count):
    global EvenNumbers
    EvenNumbers = Even(Count)

# Thread function for odd numbers
def OddThread(Count):
    global OddNumbers
    OddNumbers = Odd(Count)

# Main function
def main():
    # Accept how many numbers to display
    Count = int(input("How many numbers do you want to display : "))

    # Create threads
    tObj1 = threading.Thread(target=EvenThread, args=(Count,))
    tObj2 = threading.Thread(target=OddThread, args=(Count,))

    # Start threads
    tObj1.start()
    tObj2.start()

    # Wait for both threads to complete
    tObj1.join()
    tObj2.join()

    # Display results
    print("Even Numbers are :", EvenNumbers)
    print("Odd Numbers are :", OddNumbers)

# Program execution starts from here
if __name__ == "__main__":
    main()