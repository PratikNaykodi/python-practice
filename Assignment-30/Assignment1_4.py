# 4: Create a task that executes every day at 9:00 AM and prints:

# Namskar ...
# Use:
# schedule.every().day.at ("09:00").do( ... )

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
# Output        : Namskar ...
# Description   : Displays "Namskar ..." every day at 9:00 AM
# Date          : 22/07/2026
# Author        : Pratik Naykodi
#
#########################################################################

def Display():
    print("Namskar ...")

#########################################################################
#
# Function name : main
# Input         : None
# Output        : Prints "Namskar ..." every day at 9:00 AM
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

    # Schedule the function to run every day at 9:00 AM
    schedule.every().day.at("09:00").do(Display)

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