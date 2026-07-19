# 3: Copy File Contents into a New File (Command Line)
# Problem Statement:
# Write a program which accepts an existing file name through command line arguments, creates a new file
# named Demo.txt, and copies all contents from the given file into Demo.txt.

# Input (Command Line):
# ABC.txt

# Expected Output:
# Create Demo. txt and copy contents of ABC. txt into Demo.txt.

import sys

def CopyFile(SourceFile):
    with open(SourceFile, "r") as src:
        data = src.read()

    with open("Demo.txt", "w") as dest:
        dest.write(data)

    print("Contents of", SourceFile, "copied into Demo.txt")

def main():
    if len(sys.argv) != 2:
        print("Usage: python program.py <SourceFile>")
        return

    SourceFile = sys.argv[1]

    try:
        CopyFile(SourceFile)
    except FileNotFoundError:
        print("Source file does not exist.")

if __name__ == "__main__":
    main()