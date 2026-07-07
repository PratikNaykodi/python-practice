# 1. Design a Python application that creates two threads named Prime and NonPrime.

# Both threads should accept a list of integers.
# The Prime thread should display all prime numbers from the list.
# The NonPrime thread should display all non-prime numbers from the list.

# Import threading module
import threading
import time

# Global variables
PrimeNumbers = []
NonPrimeNumbers = []

# Function to check whether a number is prime
def ChkPrime(Number):
    if Number <= 1:
        return False

    for Index in range(2, Number):
        if Number % Index == 0:
            return False

    return True

# Thread function to return prime numbers
def Prime(Numbers):
    PrimeList = []

    for Number in Numbers:
        if ChkPrime(Number):
            PrimeList.append(Number)

    return PrimeList

# Thread function to return non-prime numbers
def NonPrime(Numbers):
    NonPrimeList = []

    for Number in Numbers:
        if not ChkPrime(Number):
            NonPrimeList.append(Number)

    return NonPrimeList

# Wrapper function for Prime thread
def PrimeThreadFunction(Numbers):
    global PrimeNumbers
    PrimeNumbers = Prime(Numbers)

# Wrapper function for Non-Prime thread
def NonPrimeThreadFunction(Numbers):
    global NonPrimeNumbers
    NonPrimeNumbers = NonPrime(Numbers)

# Main function
def main():
    # Accept number of elements from user
    Size = int(input("Enter Number of Elements : "))

    # Create an empty list
    Numbers = []

    # Accept numbers from user
    for i in range(Size):
        Number = int(input("Enter Number : "))
        Numbers.append(Number)

    start_time = time.perf_counter()
    # Create threads
    tObj1 = threading.Thread(target=PrimeThreadFunction, args=(Numbers,))
    tObj2 = threading.Thread(target=NonPrimeThreadFunction, args=(Numbers,))

    # Start threads
    tObj1.start()
    tObj2.start()

    # Wait for threads to finish
    tObj1.join()
    tObj2.join()

    end_time = time.perf_counter()

    # Display results
    print(f"Prime Numbers are : {PrimeNumbers}")
    print(f"Non-Prime Numbers are : {NonPrimeNumbers}")
    print(f"Required time : {end_time-start_time:.4f}")

# Program execution starts from here
if __name__ == "__main__":
    main()