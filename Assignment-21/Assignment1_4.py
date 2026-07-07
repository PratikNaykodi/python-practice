# 4. Design a Python application that creates two threads.

# Thread 1 should compute the sum of elements from a list.
# Thread 2 should compute the product of elements from the same list.
# Return the results to the main thread and display them.

# Import threading module
import threading

# Global variables
SumResult = 0
ProductResult = 0

# Function to calculate sum of elements
def Sum(Numbers):
    Total = 0

    for Number in Numbers:
        Total = Total + Number

    return Total

# Function to calculate product of elements
def Product(Numbers):
    Result = 1

    for Number in Numbers:
        Result = Result * Number

    return Result

# Thread function for sum
def SumThread(Numbers):
    global SumResult
    SumResult = Sum(Numbers)

# Thread function for product
def ProductThread(Numbers):
    global ProductResult
    ProductResult = Product(Numbers)

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
    t1 = threading.Thread(target=SumThread, args=(Numbers,))
    t2 = threading.Thread(target=ProductThread, args=(Numbers,))

    # Start threads
    t1.start()
    t2.start()

    # Wait for both threads to complete
    t1.join()
    t2.join()

    # Display results
    print("Sum of Elements :", SumResult)
    print("Product of Elements :", ProductResult)

# Program execution starts from here
if __name__ == "__main__":
    main()