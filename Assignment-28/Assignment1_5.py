# 5: Search a Word in File
# Problem Statement:
# Write a program which accepts a file name and a word from the user and checks whether that word is present in
# the file or not.

# Input:
# Demo.txt Marvellous

# Expected Output:
# Display whether the word Marvellous is found in Demo.txt or not.

def SearchWord(FileName, Word):
    with open(FileName, "r") as file:
        data = file.read()

    if Word in data:
        return True
    else:
        return False

def main():
    FileName = input("Enter file name: ")
    Word = input("Enter word to search: ")

    try:
        if SearchWord(FileName, Word):
            print(Word, "is present in", FileName)
        else:
            print(Word, "is not present in", FileName)
    except FileNotFoundError:
        print("File does not exist.")

if __name__ == "__main__":
    main()