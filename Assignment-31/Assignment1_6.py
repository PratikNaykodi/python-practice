# 6: Write a program that schedules the following messages:

#     Monday at 9:00 AM: Start your weekly goals
#     Wednesday at 5:00 PM: Review your weekly progress
#     Friday at 6:00 PM: Weekly work completed

# Use:
# schedule.every().monday.at( ... )
# schedule.every().wednesday.at( ... )
# schedule.every().friday.at ( ... )

#########################################################################
#
# Importing required libraries
#
#########################################################################

import schedule
import time

#########################################################################
#
# Function name : MondayMessage
# Input         : None
# Output        : Start your weekly goals
# Description   : Displays the Monday reminder at 9:00 AM
# Date          : 22/07/2026
# Author        : Pratik Naykodi
#
#########################################################################

def MondayMessage():
    print("Start your weekly goals")

#########################################################################
#
# Function name : WednesdayMessage
# Input         : None
# Output        : Review your weekly progress
# Description   : Displays the Wednesday reminder at 5:00 PM
# Date          : 22/07/2026
# Author        : Pratik Naykodi
#
#########################################################################
def WednesdayMessage():
    print("Review your weekly progress")

#########################################################################
#
# Function name : FridayMessage
# Input         : None
# Output        : Weekly work completed
# Description   : Displays the Friday reminder at 6:00 PM
# Date          : 22/07/2026
# Author        : Pratik Naykodi
#
#########################################################################
def FridayMessage():
    print("Weekly work completed")

#########################################################################
#
# Function name : main
# Input         : None
# Output        : Schedules weekly reminder messages
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

    # Schedule the weekly reminders
    schedule.every().monday.at("09:00").do(MondayMessage)
    schedule.every().wednesday.at("17:00").do(WednesdayMessage)
    schedule.every().friday.at("18:00").do(FridayMessage)

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