# 4. Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which are even. Map function will calculate its square. Reduce will return addition of all that numbers.

# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# List after filter = [2, 4, 4, 2, 8, 10]
# List after map = [4, 16, 16, 4, 64, 100]
# Output of reduce = 204

# Import reduce function from functools module
from functools import reduce

# Filter function to keep only even numbers
def FilterData(Number):
    return Number % 2 == 0

# Map function to calculate the square of each number
def MapData(Number):
    return Number ** 2

# Reduce function to add two numbers
def ReduceData(FirstNumber, SecondNumber):
    return FirstNumber + SecondNumber

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

    # Apply filter() to get only even numbers
    FilterResult = list(filter(FilterData, Numbers))

    # Apply map() to calculate the square of each filtered number
    MapResult = list(map(MapData, FilterResult))

    # Apply reduce() to calculate the addition of all squared numbers
    ReduceResult = reduce(ReduceData, MapResult)

    # Display the results
    print(f"Input List = {Numbers}")
    print(f"List after filter = {FilterResult}")
    print(f"List after map = {MapResult}")
    print(f"Output of reduce = {ReduceResult}")

# Program execution starts from here
if __name__ == "__main__":
    main()