# 5. Write a program which display 10 to 1 on screen.
# Output : 10 9 8 7 6 5 4 3 2 1

# Function to display numbers from 10 to 1
def Display(No):
    for i in range(No, 0, -1):
        print(i, end=" ")

# Main function
def main():
    Number = int(input("Enter Number : "))
    Display(Number)

# Program execution starts from here
if __name__ == "__main__":
    main()