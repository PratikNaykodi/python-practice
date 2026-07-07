# 2. Design a Python application that creates two threads.

# Thread 1 should calculate and display the maximum element from an list.
# Thread 2 should calculate and display the minimum element from the same list.
# The list should be accepted from the user.

# Import threading and time module
import threading
import time

# Global variables
MaximumNumber = 0
MinimumNumber = 0

# Function to return maximum number
def Maximum(Numbers):
    Max = Numbers[0]

    for Number in Numbers:
        if Number > Max:
            Max = Number

    return Max

# Function to return minimum number
def Minimum(Numbers):
    Min = Numbers[0]

    for Number in Numbers:
        if Number < Min:
            Min = Number

    return Min

# Wrapper function for Maximum thread
def MaximumThreadFunction(Numbers):
    global MaximumNumber

    MaximumNumber = Maximum(Numbers)

# Wrapper function for Minimum thread
def MinimumThreadFunction(Numbers):
    global MinimumNumber

    MinimumNumber = Minimum(Numbers)

# Main function
def main():
    # Accept number of elements from user
    Size = int(input("Enter Number of Elements : "))

    # Create an empty list
    Numbers = []

    # Accept numbers from user
    for Index in range(Size):
        Number = int(input("Enter Number : "))
        Numbers.append(Number)

    start_time = time.perf_counter()
    # Create threads
    tObj1 = threading.Thread(target=MaximumThreadFunction, args=(Numbers,))
    tObj2 = threading.Thread(target=MinimumThreadFunction, args=(Numbers,))

    # Start threads
    tObj1.start()
    tObj2.start()

    # Wait for threads to complete
    tObj1.join()
    tObj2.join()

    end_time = time.perf_counter()

    # Display results
    print(f"Maximum Number is : {MaximumNumber}")
    print(f"Minimum Number is : {MinimumNumber}")
    print(f"Required Time : {end_time-start_time:.4f}")

# Program execution starts from here
if __name__ == "__main__":
    main()