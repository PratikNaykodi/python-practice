# 1: Check File Exists in Current Directory
# Problem Statement:
# Write a program which accepts a file name from the user and checks whether that file exists in the current
# directory or not.

# Input:
# Demo.txt
# Expected Output:
# Display whether Demo. txt exists or not.

import os

def CheckFile(FileName):
    if os.path.exists(FileName):
        print(FileName, "exists in the current directory.")
    else:
        print(FileName, "does not exist in the current directory.")

def main():
    FileName = input("Enter file name: ")
    CheckFile(FileName)

if __name__ == "__main__":
    main()