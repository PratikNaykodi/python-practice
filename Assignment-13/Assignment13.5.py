# 5. Write a program which accepts Marks and Display grade.
# Condition Example:
# >= 75   -> Distinction
# >= 60   -> First Class
# >= 50   -> Second Class
# <  50   -> Fail
#
# Input : 80
# Output: Distinction

# Function to calculate grade based on marks
def CheckGrade(Marks):
    # Check for Distinction
    if Marks >= 75:
        return "Distinction"
    # Check for First Class
    elif Marks >= 60:
        return "First Class"
    # Check for Second Class
    elif Marks >= 50:
        return "Second Class"
    # If marks are below 50
    else:
        return "Fail"

# Main function to accept input and display result
def main():
    # Accept marks from user
    Marks = int(input("Enter Marks : "))

    # Call CheckGrade function and store returned grade
    Ret = CheckGrade(Marks)

    # Print grade
    print("Grade :", Ret)

# Program execution starts from here
if __name__ == "__main__":
    main()