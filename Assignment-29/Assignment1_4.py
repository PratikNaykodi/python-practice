# 4:Compare Two Files (Command Line)
# Problem Statement:
# Write a program which accepts two file names through command line arguments and compares the contents of
# both files.
#     If both files contain the same contents, display Success
#     Otherwise display Failure

# Input (Command Line):
# Demo.txt Hello.txt

# Expected Output:
# Success OR Failure

import sys

def CompareFiles(File1, File2):
    with open(File1, "r") as f1:
        Data1 = f1.read()

    with open(File2, "r") as f2:
        Data2 = f2.read()

    if Data1 == Data2:
        return True
    else:
        return False

def main():
    if len(sys.argv) != 3:
        print("Usage: python program.py <File1> <File2>")
        return

    File1 = sys.argv[1]
    File2 = sys.argv[2]

    try:
        if CompareFiles(File1, File2):
            print("Success")
        else:
            print("Failure")
    except FileNotFoundError:
        print("One or both files do not exist.")

if __name__ == "__main__":
    main()