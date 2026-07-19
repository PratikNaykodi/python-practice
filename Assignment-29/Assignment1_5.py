# 5: Frequency of a String in File
# Problem Statement:
# Write a program which accepts a file name and one string from the user and returns the frequency (count of
# occurrences) of that string in the file.

# Input:
# Demo.txt Marvellous
# Expected Output:
# Count how many times "Marvellous" appears in Demo.txt.

def StringFrequency(FileName, SearchString):
    with open(FileName, "r") as file:
        data = file.read()

    words = data.split()
    count = words.count(SearchString)

    return count

def main():
    FileName = input("Enter file name: ")
    SearchString = input("Enter string to search: ")

    try:
        Frequency = StringFrequency(FileName, SearchString)

        print("Frequency of", SearchString, "in", FileName, "is:", Frequency)
    except FileNotFoundError:
        print("File does not exist.")

if __name__ == "__main__":
    main()