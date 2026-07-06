# 8. Write a program which accept number from user and print that number of "*" on screen.
# Input : 5
# Output : * * * * *

# Function to print '*' specified number of times
def Display(No):
    for i in range(No):
        print("*", end=" ")

# Main function
def main():
    Number = int(input("Enter Number : "))

    Display(Number)

# Program execution starts from here
if __name__ == "__main__":
    main()