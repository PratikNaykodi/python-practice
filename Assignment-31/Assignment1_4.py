# 4: Write a program that creates a new log file after every ten minutes.

# The filename should contain the current date and time.
# Example:
# MarvellousLog_25_07_2026_16_30_00.txt
# The file should contain:

# Log file created successfully.
# Creation Time: 25-07-2026 04:30:00 PM

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
# Function name : CreateLogFile
# Input         : None
# Output        : Creates a log file
# Description   : Creates a new log file after every 10 minutes.
#                 The filename contains the current date and time.
# Date          : 22/07/2026
# Author        : Pratik Naykodi
#
#########################################################################

def CreateLogFile():

    CurrentTime = datetime.now()

    FileName = "MarvellousLog_" + CurrentTime.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

    fobj = open(FileName, "w")

    fobj.write("Log file created successfully.\n")
    fobj.write("Creation Time : ")
    fobj.write(CurrentTime.strftime("%d-%m-%Y %I:%M:%S %p"))

    fobj.close()

    print("Log file created :", FileName)

#########################################################################
#
# Function name : main
# Input         : None
# Output        : Creates a log file every 10 minutes
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

    # Schedule the task every 10 minutes
    schedule.every(10).minutes.do(CreateLogFile)

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