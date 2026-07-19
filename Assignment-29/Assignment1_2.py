# 2: Display File Contents
# Problem Statement:
# Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the
# console.

# Input:
# Demo.txt
# Expected Output:
# Display contents of Demo.txt on console.

def DisplayFile(FileName):
    with open(FileName, "r") as file:
        data = file.read()
        print(data)

def main():
    FileName = input("Enter file name: ")

    try:
        DisplayFile(FileName)
    except FileNotFoundError:
        print("File does not exist.")

if __name__ == "__main__":
    main()