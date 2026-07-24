# 2: Create a function named:

# DisplayMessage (message)
# Schedule the function using:
# schedule.every(5).seconds.do(DisplayMessage, message)
# The message should be accepted from the user.

#########################################################################
#
# Importing required libraries
#
#########################################################################

import schedule
import time

#########################################################################
#
# Function name : DisplayMessage
# Input         : Message
# Output        : Displays the message
# Description   : Prints the user message every 5 seconds
# Date          : 22/07/2026
# Author        : Pratik Naykodi
#
#########################################################################

def DisplayMessage(Message):
    print(Message)

#########################################################################
#
# Function name : main
# Input         : None
# Output        : Displays the message every 5 seconds
# Description   : Accepts a message from the user and schedules
#                 the DisplayMessage function.
# Date          : 22/07/2026
# Author        : Pratik Naykodi
#
#########################################################################

def main():

    Border = "-" * 50

    print(Border)
    print("Marvellous Automation Script")
    print(Border)

    Message = input("Enter message : ")

    # Schedule the function every 5 seconds
    schedule.every(5).seconds.do(DisplayMessage, Message)

    while True:
        schedule.run_pending()
        time.sleep(1)

#########################################################################
#
# Starter of the automation script
#
#########################################################################

if __name__ == "__main__":
    main()