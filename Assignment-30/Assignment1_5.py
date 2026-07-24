# 5: Schedule a task that executes every five minutes.

# The task should write the current date and time into a file named:

# Marvellous.txt
# New entries should be appended without removing previous entries.

# Example file contents:
# Task executed at: 25-07-2026 04:30:00 PM
# Task executed at: 25-07-2026 04:35:00 PM
# Task executed at: 25-07-2026 04:40:00 PM

#########################################################################
#
# Importing required libraries
#
#########################################################################

import schedule
import time
import os
from datetime import datetime

#########################################################################
#
# Function name : WriteDateTime
# Input         : None
# Output        : Writes current date and time into Marvellous.txt
# Description   : Checks whether Marvellous.txt exists or not.
#                 If the file does not exist, displays an error
#                 and returns.
# Date          : 22/07/2026
# Author        : Pratik Naykodi
#
#########################################################################

def WriteDateTime():

    Ret = os.path.exists("Marvellous.txt")

    if(Ret == False):
        print("Marvellous Automation Error : Marvellous.txt file does not exist.")
    else:
        print("Marvellous.txt file is not present.")
        print("Creating Marvellous.txt file...")
        open("Marvellous.txt", "w").close()

    CurrentTime = datetime.now()

    fobj = open("Marvellous.txt", "a")

    fobj.write("Task executed at : ")
    fobj.write(CurrentTime.strftime("%d-%m-%Y %I:%M:%S %p"))
    fobj.write("\n")

    fobj.close()

    print("Current date and time written successfully.")

#########################################################################
#
# Function name : main
# Input         : None
# Output        : Executes the task every five minutes
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

    # Schedule the task every 5 minutes
    schedule.every(5).minutes.do(WriteDateTime)

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