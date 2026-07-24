# 1: Write a program that accepts:
#     A message from the user
#     A time interval in seconds

# Schedule the program to display the message repeatedly after the specified interval.

# Example input:
# Enter message: Jay Ganesh
# Enter interval in seconds: 5
# Expected output:
# Jay Ganesh
# every five seconds.
# Validate that the interval is greater than zero.

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
# Description   : Prints the user message after the specified interval
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
# Output        : Displays the message repeatedly
# Description   : Accepts a message and interval from the user,
#                 validates the interval, and schedules the task.
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
    Interval = int(input("Enter interval in seconds : "))

    if(Interval <= 0):
        print("Marvellous Automation Error : Interval should be greater than zero.")
        return

    schedule.every(Interval).seconds.do(DisplayMessage, Message)

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