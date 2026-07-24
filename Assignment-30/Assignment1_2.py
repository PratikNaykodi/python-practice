# 2: Write a Python program that displays the current date and time
# after every one minute.
# Use the datetime module.

# Expected output:
# Current Date and Time: 25-07-2026 04:30:00 PM

#########################################################################
#
# Importing required libraries
#
#########################################################################

import schedule
import time
from datetime import datetime

#########################################################################
#
# Function name : DisplayDateTime
# Input         : None
# Output        : Displays current date and time
# Description   : Prints the current date and time every 1 minute
# Date          : 22/07/2026
# Author        : Pratik Naykodi
#
#########################################################################

def DisplayDateTime():
    CurrentTime = datetime.now()
    print("Current Date and Time :", CurrentTime.strftime("%d-%m-%Y %I:%M:%S %p"))

#########################################################################
#
# Function name : main
# Input         : None
# Output        : Current date and time after every 1 minute
# Description   : Controls the execution of the scheduler
# Date          : 22/07/2026
# Author        : Pratik Naykodi
#
#########################################################################

def main():
    Border = "-" * 50

    print(Border)
    print("Marvellous Automation Script")
    print(Border)

    # Schedule the function every 1 minute
    schedule.every(1).minutes.do(DisplayDateTime)

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