# 3. For every number in the given list, count how many prime numbers exist between 1 and N using multiprocessing Pool.
# Prime Number:
# A prime number is a number greater than 1 that has exactly two factors:
# 1 and the number itself.
# Examples: 2, 3, 5, 7, 11, 13, 17, 19
# Input:
# [
#     10000
#     20000
#     30000
#     40000
# ]
# Output: 
# Display total prime count for each number.
# Enter the Size of List : 4
# Enter Number : 10000
# Enter Number : 20000
# Enter Number : 30000
# Enter Number : 40000

# Process ID : 13240
# Process ID : 14520
# Process ID : 17368
# Process ID : 19884

# Input Numbers : [10000, 20000, 30000, 40000]
# Prime Counts : [1229, 2262, 3245, 4203]

# Time required : 0.2845 seconds

import multiprocessing
import os
import time
def PrimeCount(No):
    print("Process ID : ", os.getpid())

    Count = 0

    # Check every number from 2 to Number
    for Value in range(2, No + 1):
        IsPrime = True

        # Check whether Value is prime
        # Value ** 0.5 gives the square root of the number.
        # We check only up to the square root because checking beyond it is unnecessary.
        for Index in range(2, int(Value ** 0.5) + 1):
            if Value % Index == 0:
                IsPrime = False
                break

        if IsPrime:
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

    Result = pobj.map(PrimeCount, Data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()
    print(f"Input Numbers : {Data}")
    print(f"Prime Counts : {Result}")
    print(f"Time required {end_time-start_time:.4f} seconds")
    
if __name__ == "__main__":
    main()