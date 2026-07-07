# 4. Write a program that counts how many odd numbers exist between 1 and N.

# Input:
# Data = [1000000, 2000000, 3000000, 4000000]

# Expected Output Format:
# Process ID : 1237
# Input Number : 1000000
# Odd Number Count : 500000

import multiprocessing
import os
import time

def OddCount(Number):
    print("Process ID :", os.getpid())

    Count = 0

    for Value in range(1, Number + 1):
        if Value % 2 == 1:
            Count = Count + 1

    return Count

def main():
    Size = int(input("Enter the Size of List : "))

    # Data = [1000000,2000000,3000000,4000000]
    Data = list()
    for i in range(Size):
        Data.append(int(input("Enter number : ")))

    Result = []
    start_time = time.perf_counter()
    
    pobj = multiprocessing.Pool()

    Result = pobj.map(OddCount, Data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()
    print(f"Input Numbers : {Data}")
    print(f"Odd Number Counts : {Result}")
    print(f"Time required {end_time-start_time:.4f} seconds")
    
if __name__ == "__main__":
    main()