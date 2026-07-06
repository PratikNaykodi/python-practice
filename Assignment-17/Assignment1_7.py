# 7. Write a program which accept one number and display below pattern.
# Input: 5
# Output: 
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

# Function to display the pattern
def Display(No):
    for i in range(No):
        for j in range(1, No + 1):
            print(j, end=" ")
        print()

# Main function
def main():
    Number = int(input("Enter Number : "))

    Display(Number)

# Program execution starts from here
if __name__ == "__main__":
    main()