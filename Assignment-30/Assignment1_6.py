# 6: Write a script that schedules the following tasks:
#     Print Lunch Time! every day at 1:00 PM.
#     Print Wrap up work every day at 6:00 PM.
# Both tasks should be handled by separate functions.

#########################################################################
#
# Importing required libraries
#
#########################################################################

import schedule
import time

#########################################################################
#
# Function name : LunchTime
# Input         : None
# Output        : Lunch Time!
# Description   : Displays lunch reminder every day at 1:00 PM
# Date          : 22/07/2026
# Author        : Pratik Naykodi
#
#########################################################################

def LunchTime():
    print("Lunch Time!")

#########################################################################
#
# Function name : WrapUpWork
# Input         : None
# Output        : Wrap up work
# Description   : Displays wrap-up reminder every day at 6:00 PM
# Date          : 22/07/2026
# Author        : Pratik Naykodi
#
#########################################################################

def WrapUpWork():
    print("Wrap up work")

#########################################################################
#
# Function name : main
# Input         : None
# Output        : Schedules both daily tasks
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

    # Schedule the tasks
    schedule.every().day.at("13:00").do(LunchTime)
    schedule.every().day.at("18:00").do(WrapUpWork)

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