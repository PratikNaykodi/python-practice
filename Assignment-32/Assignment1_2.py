# 2: Write a Python program that monitors the size of a specified file every 30 seconds.

# Write the following details into:
# FileSizeLog.txt
#     File path
#     File size in bytes
#     Date and time
# Handle the situation where the file does not exist.

#########################################################################
#
# Importing required libraries
#
#########################################################################

import os
import schedule
import time
from datetime import datetime

#########################################################################
#
# Function name : FileSizeMonitor
# Input         : File path
# Output        : Writes file details into FileSizeLog.txt
# Description   : Monitors the size of the specified file every
#                 30 seconds and writes the details into a log file.
#                 Handles the situation where the file does not exist.
# Date          : 22/07/2026
# Author        : Pratik Naykodi
#
#########################################################################

def FileSizeMonitor(FilePath):

    Ret = os.path.exists(FilePath)

    if(Ret == False):
        print("Marvellous Automation Error : File does not exist.")
        return

    Ret = os.path.isfile(FilePath)

    if(Ret == False):
        print("Marvellous Automation Error : Invalid file.")
        return

    FileSize = os.path.getsize(FilePath)

    CurrentTime = datetime.now()

    fobj = open("FileSizeLog.txt", "a")

    fobj.write("-" * 50 + "\n")
    fobj.write("File Path : " + FilePath + "\n")
    fobj.write("File Size : " + str(FileSize) + " bytes\n")
    fobj.write("Date and Time : " +
               CurrentTime.strftime("%d-%m-%Y %I:%M:%S %p") + "\n")
    fobj.write("-" * 50 + "\n\n")

    fobj.close()

    print("File size logged successfully.")

#########################################################################
#
# Function name : main
# Input         : None
# Output        : Monitors file size every 30 seconds
# Description   : Accepts file path from the user and schedules
#                 the FileSizeMonitor function.
# Date          : 22/07/2026
# Author        : Pratik Naykodi
#
#########################################################################

def main():
    Border = "-" * 50

    print(Border)
    print("Marvellous Automation Script")
    print(Border)

    FilePath = input("Enter file path : ")

    # Schedule the task every 30 seconds
    schedule.every(30).seconds.do(FileSizeMonitor, FilePath)

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