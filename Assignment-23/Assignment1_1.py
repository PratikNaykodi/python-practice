# 1. Write a Python program using multiprocessing. Pool to calculate the sum of all even numbers from 1 to N for every number from the given list.

# Input:
# Data = [1000000, 2000000, 3000000, 4000000]
# Expected Task: 
# For each number N, calculate:
# 2+4 +6 + ... +N

# Expected Output Format:
# Process ID : 1234
# Input Number : 1000000
# Sum of Even Numbers : 250000500000

import multiprocessing
import os
import time

# Function to calculate Sum of Even number 2+4+6 + ... +N
def SumEven(No):
    print("Process PID : ", os.getpid())

    Sum = 0
    
    # Calculate the sum of Even from 1 to Number
    for i in range(1,No+1):
        if(i % 2 == 0):
            Sum = Sum + i

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

    # Execute SumEven() for each number using multiprocessing
    Result = pobj.map(SumEven, Data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()
    print(f"Input Numbers : {Data}")
    print(f"Sum of Even Numbers : {Result}")
    print(f"Time required {end_time-start_time:.4f} seconds")
    
if __name__ == "__main__":
    main()