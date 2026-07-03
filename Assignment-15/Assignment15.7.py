# 7. Write a lambda function using filter() which accepts a list of strings and returns list of strings having length greater than 5.
#
# Input : ["Python", "Java", "Programming", "C"]
# Output: ["Python", "Programming"]

# Lambda function to check string length greater than 5
LengthCheck = lambda Value: len(Value) > 5

# Main function
def main():
    # Accept list of strings from user
    Strings = input("Enter Strings : ").split()

    # Apply lambda function using filter()
    Result = list(filter(LengthCheck, Strings))

    # Print strings having length greater than 5
    print("Strings with length greater than 5 :", Result)

# Program execution starts from here
if __name__ == "__main__":
    main()
