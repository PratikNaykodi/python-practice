# 2: Count Words in a File
# Problem Statement:
# Write a program which accepts a file name from the user and counts the total number of words in that file.
# Input:
# Demo.txt
# Expected Output:
# Total number of words in Demo.txt.

def CountWords(FileName):
    count = 0

    with open(FileName, "r") as file:
        for line in file:
            words = line.split()
            count += len(words)

    return count

def main():
    FileName = input("Enter file name: ")

    try:
        Lines = CountWords(FileName)
        print("Total number of word in", FileName, ":", Lines)
    except FileNotFoundError:
        print("File does not exist.")

if __name__ == "__main__":
    main()