# 4. Design a Python application that creates three threads named Small, Capital, and Digits.

# All threads should accept a string as input.
# The Small thread should count and display the number of lowercase characters.
# The Capital thread should count and display the number of uppercase characters.
# The Digits thread should count and display the number of numeric digits.
# Each thread must also display:
#     Thread ID
#     Thread Name

# Import threading module
import threading

# Global variables
SmallCount = 0
CapitalCount = 0
DigitCount = 0

# Function to count lowercase characters
def Small(String):
    Count = 0

    for Character in String:
        if Character.islower():
            Count = Count + 1

    return Count

# Function to count uppercase characters
def Capital(String):
    Count = 0

    for Character in String:
        if Character.isupper():
            Count = Count + 1

    return Count

# Function to count digits
def Digits(String):
    Count = 0

    for Character in String:
        if Character.isdigit():
            Count = Count + 1

    return Count

# Thread function for lowercase characters
def SmallThread(String):
    global SmallCount

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)

    SmallCount = Small(String)

# Thread function for uppercase characters
def CapitalThread(String):
    global CapitalCount

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)

    CapitalCount = Capital(String)

# Thread function for digits
def DigitsThread(String):
    global DigitCount

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)

    DigitCount = Digits(String)

# Main function
def main():
    # Accept string from user
    String = input("Enter String : ")

    # Create threads
    Thread1 = threading.Thread(target=SmallThread, args=(String,), name="Small")
    Thread2 = threading.Thread(target=CapitalThread, args=(String,), name="Capital")
    Thread3 = threading.Thread(target=DigitsThread, args=(String,), name="Digits")

    # Start threads
    Thread1.start()
    Thread2.start()
    Thread3.start()

    # Wait for threads to complete
    Thread1.join()
    Thread2.join()
    Thread3.join()

    # Display results
    print("Number of Small Characters :", SmallCount)
    print("Number of Capital Characters :", CapitalCount)
    print("Number of Digits :", DigitCount)

    print("Exit from main")

# Program execution starts from here
if __name__ == "__main__":
    main()