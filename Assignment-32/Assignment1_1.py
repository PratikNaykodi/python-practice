# 1: Write a program that creates a new text file every minute.

# The filename should contain the current timestamp.

# Example:
# File_25_07_2026_16_30_00.txt
# Write the following information into the file:
#     Filename
#     Creation date
#     Creation time

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
# Function name : CreateFile
# Input         : None
# Output        : Creates a new text file
# Description   : Creates a new text file every minute with the
#                 current timestamp in the filename and writes
#                 the filename, creation date, and creation time.
# Date          : 22/07/2026
# Author        : Pratik Naykodi
#
#########################################################################

def CreateFile():

    CurrentTime = datetime.now()

    FileName = "File_" + CurrentTime.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

    fobj = open(FileName, "w")

    fobj.write("Filename : " + FileName + "\n")
    fobj.write("Creation Date : " + CurrentTime.strftime("%d-%m-%Y") + "\n")
    fobj.write("Creation Time : " + CurrentTime.strftime("%I:%M:%S %p"))

    fobj.close()

    print("File created successfully :", FileName)

#########################################################################
#
# Function name : main
# Input         : None
# Output        : Creates a new file every minute
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

    # Schedule the task every 1 minute
    schedule.every(1).seconds.do(CreateFile)

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