# 2.Write a Python program using multiprocessing. Pool to calculate the sum of all odd numbers from 1 to N.

# Input :
# Data = [1000000, 2000000, 3000000, 4000000]

# Expected Task:
# For each number N, calculate:
# 1 + 3 + 5 + ... + N

# Expected Output Format:
# Process ID : 1235
# Input Number : 1000000
# Sum of Odd Numbers : 250000000000

import multiprocessing
import os
import time

# Function to calculate Sum of Odd number 1 + 3 + 5 + ... + N
def SumOdd(No):
    print("Process PID : ", os.getpid())

    Sum = 0
    
    # Calculate the sum of Odd from 1 to Number
    for i in range(1,No+1):
        if(i % 2 == 1):
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

    # Execute SumOdd() for each number using multiprocessing
    Result = pobj.map(SumOdd, Data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()
    print(f"Input Numbers : {Data}")
    print(f"Sum of Odd Numbers : {Result}")
    print(f"Time required {end_time-start_time:.4f} seconds")
    
if __name__ == "__main__":
    main()