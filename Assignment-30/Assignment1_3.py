# 3: Write a program that schedules a function to print:

# Coding Kar ..!
# every 30 minutes.

#########################################################################
#
# Importing required libraries
#
#########################################################################

import schedule
import time

#########################################################################
#
# Function name : Display
# Input         : None
# Output        : Coding Kar ..!
# Description   : Displays "Coding Kar ..!" every 30 minutes
# Date          : 22/07/2026
# Author        : Pratik Naykodi
#
#########################################################################

def Display():
    print("Coding Kar ..!")

#########################################################################
#
# Function name : main
# Input         : None
# Output        : Coding Kar ..! every 30 minutes
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

    # Schedule the function every 30 minutes
    schedule.every(30).minutes.do(Display)

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