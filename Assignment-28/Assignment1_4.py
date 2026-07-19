# 4: Copy File Contents into Another File
# Problem Statement:
# Write a program which accepts two file names from the user.
#     First file is an existing file
#     Second file is a new file
# Copy all contents from the first file into the second file.

# Input:
# ABC.txt Demo.txt

# Expected Output:
# Contents of ABC.txt copied into Demo.txt.

def CopyFile(SourceFile, DestinationFile):
    with open(SourceFile, "r") as src:
        data = src.read()

    with open(DestinationFile, "w") as dest:
        dest.write(data)

    print("Contents of", SourceFile, "copied into", DestinationFile)

def main():
    SourceFile = input("Enter source file name: ")
    DestinationFile = input("Enter destination file name: ")

    try:
        CopyFile(SourceFile, DestinationFile)
    except FileNotFoundError:
        print("Source file does not exist.")

if __name__ == "__main__":
    main()