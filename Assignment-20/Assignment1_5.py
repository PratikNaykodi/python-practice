# 5. Design a Python application that creates two threads named Thread1 and Thread2.

# Thread1 should display numbers from 1 to 50.
# Thread2 should display numbers from 50 to 1 in reverse order.
# Ensure that:
# Thread2 starts execution only after Thread1 has completed.
# Use appropriate thread synchronizatio

# Import threading module
import threading

# Function to display numbers from 1 to N
def DisplayForward(Number):
    for Value in range(1, Number + 1):
        print(Value, end=" ")
        # print(Value)

    print()
    # print("-"*10)

# Function to display numbers from N to 1
def DisplayReverse(Number):
    for Value in range(Number, 0, -1):
        print(Value, end=" ")
        # print(Value)

    print()
    # print("-"*10)

# Main function
def main():
    # Accept number from user
    Number = int(input("Enter Number : "))

    # Create Thread1
    Thread1 = threading.Thread(target=DisplayForward, args=(Number,))

    # Create Thread2
    Thread2 = threading.Thread(target=DisplayReverse, args=(Number,))

    # Start Thread1
    Thread1.start()

    # Wait for Thread1 to complete
    Thread1.join()

    # Start Thread2
    Thread2.start()

    # Wait for Thread2 to complete
    Thread2.join()

    print("Exit from main")

# Program execution starts from here
if __name__ == "__main__":
    main()