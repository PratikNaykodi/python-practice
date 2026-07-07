# 4.Write a program that calculates
# 1^5+2^5+3^5+ ..... +N^5
# for multiple values of N simultaneously using Pool.

# Input :
# [
#     1000000,
#     2000000,
#     3000000,
#     4000000
# ]
# Output:
# multiple values of N simultaneously
# Measure total execution time.

import multiprocessing
import os
import time

# Function to calculate 1^5 + 2^5 + ... + N^5
def SumCalculate(No):
    print("Process ID : ", os.getpid())

    Sum = 0
    
    # Calculate the sum of fifth powers from 1 to Number
    for i in range(1,No+1):
        Sum = Sum + (i ** 5)

    return Sum

# Main function
def main():
    # Accept the size of the list
    Size = int(input("Enter the Size of List : "))

    # Data = [1000000,2000000,3000000,4000000]
    # Create an empty list
    Data = list()
    # Accept numbers from the user

    for i in range(Size):
        Data.append(int(input("Enter number : ")))

    Result = []
    start_time = time.perf_counter()
    
    # Create a process pool
    pobj = multiprocessing.Pool()

    # Execute SumCalculate() for each number using multiprocessing
    Result = pobj.map(SumCalculate, Data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()
    print(f"Input Numbers : {Data}")
    print(f"Result is : {Result}")
    print(f"Time required {end_time-start_time:.4f} seconds")

if __name__ == "__main__":
    main()