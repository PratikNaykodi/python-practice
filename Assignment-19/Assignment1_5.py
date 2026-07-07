# 5. Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all prime numbers. Map function will multiply each number by 2. Reduce will return Maximum number from that numbers. (You can also use normal functions instead of lambda functions).

# Input List = [2, 70, 11, 10, 17, 23, 31, 77]
# List after filter = [2, 11, 17, 23, 31]
# List after map = [4, 22, 34, 46, 62]
# Output of reduce = 62

# Import reduce function from functools module
from functools import reduce

# Filter function to keep only prime numbers
def FilterData(No):
    if No <= 1:
        return False

    for Index in range(2, No):
        if No % Index == 0:
            return False

    return True

# Map function to multiply each number by 2
def MapData(No):
    return No * 2

# Reduce function to return the maximum number
def ReduceData(No1, No2):
    if No1 > No2:
        return No1
    else:
        return No2

# Main function
def main():
    # Accept the number of elements from the user
    Size = int(input("How many numbers in list : "))

    # Create an empty list
    Numbers = list()

    # Accept numbers from the user and store them in the list
    for Index in range(Size):
        Number = int(input("Enter Number : "))
        Numbers.append(Number)

    # Apply filter() to get only prime numbers
    FilterResult = list(filter(FilterData, Numbers))

    # Apply map() to multiply each prime number by 2
    MapResult = list(map(MapData, FilterResult))

    # Apply reduce() to find the maximum number
    ReduceResult = reduce(ReduceData, MapResult)

    # Display the results
    print(f"Input List = {Numbers}")
    print(f"List after filter = {FilterResult}")
    print(f"List after map = {MapResult}")
    print(f"Output of reduce = {ReduceResult}")

# Program execution starts from here
if __name__ == "__main__":
    main()