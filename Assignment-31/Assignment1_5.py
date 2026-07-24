# 5: Write a program that accepts a directory name from the user and
# counts the number of files inside it every five minutes.

# Write the result into:
# DirectoryCountLog.txt
# Each entry should contain:
#     Directory path
#     Number of files
#     Date and time

#########################################################################
#
# Importing required libraries
#
#########################################################################

import os
import time
import schedule
from datetime import datetime

#########################################################################
#
# Function name : DirectoryCount
# Input         : Directory path
# Output        : Writes directory details into log file
# Description   : Counts the number of files in the specified
#                 directory every five minutes and stores the
#                 result in DirectoryCountLog.txt.
# Date          : 22/07/2026
# Author        : Pratik Naykodi
#
#########################################################################

def DirectoryCount(DirectoryPath):

    Ret = os.path.exists(DirectoryPath)

    if(Ret == False):
        print("Marvellous Automation Error : Directory does not exist.")
        return

    Ret = os.path.isdir(DirectoryPath)

    if(Ret == False):
        print("Marvellous Automation Error : Invalid directory.")
        return

    TotalFiles = 0

    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryPath):
        TotalFiles = TotalFiles + len(FileNames)

    CurrentTime = datetime.now()

    fobj = open("DirectoryCountLog.txt", "a")

    fobj.write("-" * 50 + "\n")
    fobj.write("Directory Path : " + DirectoryPath + "\n")
    fobj.write("Number of Files : " + str(TotalFiles) + "\n")
    fobj.write("Date and Time : " +
               CurrentTime.strftime("%d-%m-%Y %I:%M:%S %p") + "\n")
    fobj.write("-" * 50 + "\n\n")

    fobj.close()

    print("Directory details written successfully.")

#########################################################################
#
# Function name : main
# Input         : None
# Output        : Counts files every five minutes
# Description   : Accepts directory path from the user and
#                 schedules the DirectoryCount function.
# Date          : 22/07/2026
# Author        : Pratik Naykodi
#
#########################################################################

def main():
    Border = "-" * 50

    print(Border)
    print("Marvellous Automation Script")
    print(Border)

    DirectoryPath = input("Enter directory path : ")

    # Schedule the task every 5 minutes
    schedule.every(5).minutes.do(DirectoryCount, DirectoryPath)

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