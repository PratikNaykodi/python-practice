# 3. Design a Python application that creates two threads named EvenList and OddList.

# Both threads should accept a list of integers as input.
# The EvenList thread should:
# Extract all even elements from the list.
# Calculate and display their sum.

# The OddList thread should:
# Extract all odd elements from the list.
# Calculate and display their sum.

# Threads should run concurrently.

# Import threading module
import threading

# Global variables
EvenSum = 0
OddSum = 0

# Function to calculate sum of even numbers
def EvenList(Numbers):
    Sum = 0

    print("Even Numbers are :", end=" ")

    for Number in Numbers:
        if Number % 2 == 0:
            print(Number, end=" ")
            Sum = Sum + Number

    print()
    return Sum

# Function to calculate sum of odd numbers
def OddList(Numbers):
    Sum = 0

    print("Odd Numbers are :", end=" ")

    for Number in Numbers:
        if Number % 2 != 0:
            print(Number, end=" ")
            Sum = Sum + Number

    print()
    return Sum

# Thread function for even numbers
def EvenListThread(Numbers):
    global EvenSum
    EvenSum = EvenList(Numbers)

# Thread function for odd numbers
def OddListThread(Numbers):
    global OddSum
    OddSum = OddList(Numbers)

# Main function
def main():
    # Accept number of elements
    Size = int(input("Enter Number of Elements : "))

    # Create an empty list
    Numbers = []

    # Accept numbers from user
    for Index in range(Size):
        Number = int(input("Enter Number : "))
        Numbers.append(Number)

    # Create threads
    t1 = threading.Thread(target=EvenListThread, args=(Numbers,))
    t2 = threading.Thread(target=OddListThread, args=(Numbers,))

    # Start threads
    t1.start()
    t2.start()

    # Wait for both threads to complete
    t1.join()
    t2.join()

    # Display results
    print("Addition of Even Numbers :", EvenSum)
    print("Addition of Odd Numbers :", OddSum)

    print("Exit from main")

# Program execution starts from here
if __name__ == "__main__":
    main()