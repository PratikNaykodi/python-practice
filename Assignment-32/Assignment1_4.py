# 4: Write a program that copies all .txt files from one directory to another every ten minutes.

# The program should:
#     Accept source and destination directories
#     Validate both directories
#     Copy only .txt files
#     Maintain a log of copied files
#     Avoid terminating if one file cannot be copied

#########################################################################
#
# Importing required libraries
#
#########################################################################

import os
import shutil
import schedule
import time
from datetime import datetime

#########################################################################
#
# Function name : CopyTextFiles
# Input         : Source directory, Destination directory
# Output        : Copies all .txt files
# Description   : Copies all .txt files from the source directory
#                 to the destination directory every 10 minutes.
#                 Maintains a log of copied files and continues
#                 even if one file cannot be copied.
# Date          : 22/07/2026
# Author        : Pratik Naykodi
#
#########################################################################

def CopyTextFiles(SourceDirectory, DestinationDirectory):
    Ret = os.path.exists(SourceDirectory)

    if(Ret == False):
        print("Marvellous Automation Error : Source directory does not exist.")
        return

    Ret = os.path.isdir(SourceDirectory)

    if(Ret == False):
        print("Marvellous Automation Error : Invalid source directory.")
        return

    Ret = os.path.exists(DestinationDirectory)

    if(Ret == False):
        print("Marvellous Automation Error : Destination directory does not exist.")
        return

    Ret = os.path.isdir(DestinationDirectory)

    if(Ret == False):
        print("Marvellous Automation Error : Invalid destination directory.")
        return

    fobj = open("CopyLog.txt", "a")

    fobj.write("-" * 50 + "\n")
    fobj.write("Copy Time : ")
    fobj.write(datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))
    fobj.write("\n")

    for FolderName, SubFolderNames, FileNames in os.walk(SourceDirectory):
        for FileName in FileNames:
            if(FileName.endswith(".txt")):
                SourcePath = os.path.join(FolderName, FileName)
                DestinationPath = os.path.join(DestinationDirectory, FileName)

                try:
                    shutil.copy2(SourcePath, DestinationPath)
                    print(FileName, "copied successfully.")
                    fobj.write("Copied : " + FileName + "\n")

                except Exception as e:
                    print("Unable to copy :", FileName)
                    fobj.write("Failed : " + FileName + "\n")

    fobj.write("-" * 50 + "\n\n")
    fobj.close()

#########################################################################
#
# Function name : main
# Input         : None
# Output        : Copies .txt files every 10 minutes
# Description   : Accepts source and destination directories
#                 and schedules the CopyTextFiles function.
# Date          : 22/07/2026
# Author        : Pratik Naykodi
#
#########################################################################

def main():
    Border = "-" * 50

    print(Border)
    print("Marvellous Automation Script")
    print(Border)

    SourceDirectory = input("Enter source directory : ")
    DestinationDirectory = input("Enter destination directory : ")

    # Schedule the task every 10 minutes
    schedule.every(10).minutes.do(CopyTextFiles, SourceDirectory, DestinationDirectory)

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