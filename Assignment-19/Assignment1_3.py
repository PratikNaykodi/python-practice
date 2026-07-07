# 3. Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90. Map function will increase each number by 10. Reduce will return product of all that numbers.

# Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# List after filter = [76, 89, 86, 90, 70]
# List after map = [86, 99, 96, 100, 80]
# Output of reduce = 6538752000

# Import reduce function from functools module
from functools import reduce

# Filter function to keep numbers between 70 and 90
def FilterData(Number):
    return Number >= 70 and Number <= 90

# Map function to increase each number by 10
def MapData(Number):
    return Number + 10

# Reduce function to multiply two numbers
def ReduceData(FirstNumber, SecondNumber):
    return FirstNumber * SecondNumber

# Main function
def main():
    # Accept number of elements from user
    Size = int(input("How many numbers in list : "))

    # Create an empty list
    Numbers = list()

    # Accept numbers from user and store them in the list
    for Index in range(Size):
        Number = int(input("Enter Number : "))
        Numbers.append(Number)

    # Apply filter() to get numbers between 70 and 90
    FilterResult = list(filter(FilterData, Numbers))

    # Apply map() to increase each filtered number by 10
    MapResult = list(map(MapData, FilterResult))

    # Apply reduce() to calculate the product of all mapped numbers
    ReduceResult = reduce(ReduceData, MapResult)

    # Display results
    print(f"Input List = {Numbers}")
    print(f"List after filter = {FilterResult}")
    print(f"List after map = {MapResult}")
    print(f"Output of reduce = {ReduceResult}")

# Program execution starts from here
if __name__ == "__main__":
    main()