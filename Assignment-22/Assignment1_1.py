# 1. Write a program that accepts a list of integers and uses Pool.map() to calculate the sum of squares from 1 to N for every element in the list.

# Example Input
# [1000000,2000000,3000000,4000000]
# Expected Output
# [
#     333333833333500000,
#     2666668666667000000,
#     .....
# ]

import multiprocessing
import os
import time
def SumSquare(No):
    print("Process ID : ", os.getpid())

    Sum = 0
    
    for i in range(1,No+1):
        Sum = Sum + (i ** 2)

    return Sum

def main():
    Size = int(input("Enter the Size of List : "))

    # Data = [1000000,2000000,3000000,4000000]
    Data = list()
    for i in range(Size):
        Data.append(int(input("Enter number : ")))

    Result = []
    start_time = time.perf_counter()
    
    pobj = multiprocessing.Pool()

    Result = pobj.map(SumSquare, Data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()
    print(f"Input Numbers : {Data}")
    print(f"Sum of Square : {Result}")
    print(f"Time required {end_time-start_time:.4f} seconds")
    
if __name__ == "__main__":
    main()