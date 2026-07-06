# 10. Write a program which accept name from user and Display length of its name.
# Input : Marvellous
# Output : 10

# Function to calculate length of the name
def NameLength(Name):
    return len(Name)

# Main function
def main():
    Name = input("Enter Name : ")

    Ret = NameLength(Name)

    print(f"Length of Name '{Name}' is : {Ret}")

# Program execution starts from here
if __name__ == "__main__":
    main()