# 2. Write a program which accept one number and display below pattern.
# Input: 5
# Output: 
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# Function to display the pattern
def Display(No):
    for i in range(No):
        for j in range(No):
            print("*", end=" ")
        print()

# Main function
def main():
    Number = int(input("Enter Number : "))

    Display(Number)

# Program execution starts from here
if __name__ == "__main__":
    main()