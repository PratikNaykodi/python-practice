# 3: Display File Line by Line
# Problem Statement:
# Write a program which accepts a file name from the user and displays the contents of the file line by line on the
# screen.
# Input:
# Demo.txt
# Expected Output:
# Display each line of Demo. txt one by one.

def DisplayFile(FileName):
    with open(FileName, "r") as file:
        for line in file:
            print(line, end="")

def main():
    FileName = input("Enter file name: ")

    try:
        DisplayFile(FileName)
    except FileNotFoundError:
        print("File does not exist.")

if __name__ == "__main__":
    main()