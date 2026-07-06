# 4. Write a program which display 5 times Marvellous on screen.
# Output :
# Marvellous
# Marvellous
# Marvellous
# Marvellous
# Marvellous

# Function to display "Marvellous" 5 times
def Display(No):
    for i in range(No):
        print("Marvellous")

# Main function
def main():
    Number = int(input("Enter Number : "))
    Display(Number)

# Program execution starts from here
if __name__ == "__main__":
    main()