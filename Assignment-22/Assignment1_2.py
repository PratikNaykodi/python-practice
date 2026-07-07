# 2. Write a program that calculates factorials of multiple numbers simultaneously using Pool.map().

# Input
# [10,15,20,25]
# Output:
# Display
#   Process ID
#   Input Number
#   Factorial

import multiprocessing
import os
import time
def Factorial(No):
    print("Process ID : ", os.getpid())

    Fact = 1
    
    for i in range(1,No+1):
        Fact = Fact * i

    return Fact

def main():
    Size = int(input("Enter the Size of List : "))

    # Data = [1000000,2000000,3000000,4000000]
    Data = list()
    for i in range(Size):
        Data.append(int(input("Enter number : ")))

    Result = []
    start_time = time.perf_counter()
    
    pobj = multiprocessing.Pool()

    Result = pobj.map(Factorial, Data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()
    print(f"Input Numbers : {Data}")
    print(f"Factorial is : {Result}")
    print(f"Time required {end_time-start_time:.4f} seconds")
    
if __name__ == "__main__":
    main()