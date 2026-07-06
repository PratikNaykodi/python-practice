# 9. Write a program which display first 10 even numbers on screen.
# Input : 10
# Output : 2 4 6 8 10 12 14 16 18 20

# Function to display first N even numbers
def Display(No):
    for i in range(1, No + 1):
        print(i * 2, end=" ")

# Main function
def main():
    Number = int(input("Enter Number : "))

    Display(Number)

# Program execution starts from here
if __name__ == "__main__":
    main()