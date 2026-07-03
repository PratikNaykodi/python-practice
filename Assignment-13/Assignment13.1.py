# 1. Write a program which accepts lenght and width of rectangle and prints area.
#
# Input :
# Length = 5
# Width  = 4
#
# Output:
# Area = 20

# Function to calculate area of rectangle
def RectangleArea(Length, Width):
    # Calculate area using formula: Length * Width
    return Length * Width

# Main function to accept input and display result
def main():
    # Accept length from user
    Length = int(input("Enter Length : "))

    # Accept width from user
    Width = int(input("Enter Width : "))

    # Call RectangleArea function and store returned value
    Ret = RectangleArea(Length, Width)

    # Print area of rectangle
    print("Area of Rectangle :", Ret)

# Program execution starts from here
if __name__ == "__main__":
    main()