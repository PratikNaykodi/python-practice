# 3. Write a program that counts how many even numbers exist between 1 and N using Pool.map().

# Input:
# Data = [1000000, 2000000, 3000000, 4000000]

# Expected Output Format:
# Process ID : 1236
# Input Number : 1000000
# Even Number Count : 500000

import multiprocessing
import os
import time

def EvenCount(Number):
    print("Process ID :", os.getpid())

    Count = 0

    for Value in range(1, Number + 1):
        if Value % 2 == 0:
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

    Result = pobj.map(EvenCount, Data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()
    print(f"Input Numbers : {Data}")
    print(f"Even Number Counts : {Result}")
    print(f"Time required {end_time-start_time:.4f} seconds")
    
if __name__ == "__main__":
    main()