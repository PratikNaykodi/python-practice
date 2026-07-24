# 5: Write a program that deletes all empty files from a specified directory every hour.

# The program should:
#     Scan the directory recursively
#     Detect files whose size is zero bytes
#     Delete the empty files
#     Store deleted file paths in a log file
#     Handle permission errors

# Test the program only on a sample directory.

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
# Function name : DeleteEmptyFiles
# Input         : Directory path
# Output        : Deletes empty files
# Description   : Scans the specified directory recursively,
#                 deletes all empty files, stores deleted file
#                 paths in a log file, and handles permission errors.
# Date          : 22/07/2026
# Author        : Pratik Naykodi
#
#########################################################################

def DeleteEmptyFiles(DirectoryPath):
    Ret = os.path.exists(DirectoryPath)
    if(Ret == False):
        print("Marvellous Automation Error : Directory does not exist.")
        return

    Ret = os.path.isdir(DirectoryPath)

    if(Ret == False):
        print("Marvellous Automation Error : Invalid directory.")
        return

    CurrentTime = datetime.now()

    fobj = open("DeleteEmptyFilesLog.txt", "a")

    fobj.write("-" * 50 + "\n")
    fobj.write("Scan Time : ")
    fobj.write(CurrentTime.strftime("%d-%m-%Y %I:%M:%S %p"))
    fobj.write("\n")

    DeletedFiles = 0

    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryPath):

        for FileName in FileNames:
            FilePath = os.path.join(FolderName, FileName)

            try:
                if(os.path.getsize(FilePath) == 0):
                    os.remove(FilePath)
                    DeletedFiles = DeletedFiles + 1
                    print("Deleted :", FilePath)
                    fobj.write("Deleted : " + FilePath + "\n")

            except PermissionError:
                print("Permission denied :", FilePath)
                fobj.write("Permission denied : " + FilePath + "\n")

    fobj.write("Total Empty Files Deleted : " + str(DeletedFiles) + "\n")
    fobj.write("-" * 50 + "\n\n")

    fobj.close()

#########################################################################
#
# Function name : main
# Input         : None
# Output        : Deletes empty files every hour
# Description   : Accepts directory path from the user and
#                 schedules the DeleteEmptyFiles function.
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

    # Schedule the task every 1 hour
    schedule.every(1).hours.do(DeleteEmptyFiles, DirectoryPath)

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