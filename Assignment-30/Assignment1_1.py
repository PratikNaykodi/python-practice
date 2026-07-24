# 1: Write a Python program that prints:

# Jay Ganesh ...
# every two seconds.

# Use:
# schedule.every(2).seconds.do( ... )
# Expected output:
# Jay Ganesh ...
# Jay Ganesh ...
# Jay Ganesh ...

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
# Output        : Jay Ganesh ...
# Description   : Displays "Jay Ganesh ..." every 2 seconds
# Date          : 22/07/2026
# Author        : Pratik Naykodi
#
#########################################################################

def Display():
    print("Jay Ganesh ...")

#########################################################################
#
# Function name : main
# Input         : None
# Output        : Jay Ganesh ... every 2 seconds
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

    # Schedule the Display function every 2 seconds
    schedule.every(2).seconds.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

    print(Border)
    print("Thank you for using Marvellous Automation Script")
    print(Border)

#########################################################################
#
# Starter of the automation script
#
#########################################################################

if __name__ == "__main__":
    main()