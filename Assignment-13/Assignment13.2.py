# 2. Write a program which accepts redius of circle and prints area of circle.
#
# Input : 5
# Output: 78.5

# Function to calculate area of circle
def CircleArea(Radius):
    # Calculate area using formula: pi * r * r
    Area = 3.14 * Radius * Radius
    # Return area of circle
    return Area

# Main function to accept input and display result
def main():
    # Accept radius from user
    Radius = int(input("Enter Radius : "))

    # Call CircleArea function and store returned value
    Ret = CircleArea(Radius)

    # Print area of circle
    print("Area of Circle :", Ret)

# Program execution starts from here
if __name__ == "__main__":
    main()