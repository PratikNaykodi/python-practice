# 3: Write a program that scans a specified directory every minute.

# The task should display:
# Directory name
#     Number of files
#     Number of subdirectories

# Date and time of scanning

# Use the os module.

# Example output:
# Directory Scanned: E:/Data
# Total Files: 15
# Total Subdirectories: 4
# Scan Time: 25-07-2026 04:30:00 PM

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
# Function name : DirectoryScanner
# Input         : Directory path
# Output        : Displays directory details
# Description   : Scans the specified directory and displays the
#                 number of files, subdirectories, and scan time.
# Date          : 22/07/2026
# Author        : Pratik Naykodi
#
#########################################################################

def DirectoryScanner(DirectoryPath):

    Ret = os.path.exists(DirectoryPath)

    if(Ret == False):
        print("Marvellous Automation Error : Directory does not exist.")
        return

    Ret = os.path.isdir(DirectoryPath)

    if(Ret == False):
        print("Marvellous Automation Error : Invalid directory.")
        return

    TotalFiles = 0
    TotalSubDirectories = 0

    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryPath):
        TotalFiles = TotalFiles + len(FileNames)
        TotalSubDirectories = TotalSubDirectories + len(SubFolderNames)

    CurrentTime = datetime.now()

    print("-" * 50)
    print("Directory Scanned      :", DirectoryPath)
    print("Total Files            :", TotalFiles)
    print("Total Subdirectories   :", TotalSubDirectories)
    print("Scan Time              :", CurrentTime.strftime("%d-%m-%Y %I:%M:%S %p"))
    print("-" * 50)

#########################################################################
#
# Function name : main
# Input         : None
# Output        : Scans directory every minute
# Description   : Accepts directory path from the user and schedules
#                 the DirectoryScanner function.
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

    # Schedule the task every minute
    schedule.every(1).minutes.do(DirectoryScanner, DirectoryPath)

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