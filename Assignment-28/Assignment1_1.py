# 1: Count Lines in a File
# Problem Statement:
# Write a program which accepts a file name from the user and counts how many lines are present in the file.
# Input:
# Demo.txt
# Expected Output:
# Total number of lines in Demo. txt.

def CountLines(FileName):
    count = 0

    with open(FileName, "r") as file:
        for line in file:
            count += 1

    return count

def main():
    FileName = input("Enter file name: ")

    try:
        Lines = CountLines(FileName)
        print("Total number of lines in", FileName, ":", Lines)
    except FileNotFoundError:
        print("File does not exist.")

if __name__ == "__main__":
    main()