# 1. Write a program which accepts one character and checks whether it is Vowel or Consonant.
#Input : a
#Output: Vowel

# Function to check whether character is vowel or consonant
def CheckVowel(Char):
    # Convert character to lowercase
    Char = Char.lower()

    # Check character is present in vowels
    if Char in ('a', 'e', 'i', 'o', 'u'):
        return True
    else:
        return False

# Main function to accept input and display result
def main():
    # Accept character from user
    Ch = input("Enter Character : ")

    # Check input contains only one alphabet character
    if len(Ch) != 1 or not Ch.isalpha():
        print("Enter correct character")
        return

    # Call CheckVowel function
    Ret = CheckVowel(Ch)

    # Display result
    if Ret:
        print("Vowel")
    else:
        print("Consonant")

# Program execution starts from here
if __name__ == "__main__":
    main()