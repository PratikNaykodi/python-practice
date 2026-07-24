# 7: Write a Python program that performs a file backup every hour.

# The program should:
#   1. Accept the source file path.
#   2. Accept the destination directory path.
#   3. Copy the source file to the destination directory.
#   4. Add the current date and time to the backup filename.
#   5. Write the backup operation details into:
        # backup_log.txt
        # Example backup filename:
        # Data_25_07_2026_16_30_00.txt

        # Example log entry:    
            # Backup completed successfully at 25-07-2026 04:30:00 PM
            # Use the shutil module for file copying.

# run command : python Assignement1_7.py Demo.txt "D:\Pratik Workspace\python-practice\Assignment-30\Backup"

#########################################################################
#
# Importing required libraries
#
#########################################################################

import sys
import os
import time
import shutil
import schedule
from datetime import datetime

#########################################################################
#
# Function name : BackupFile
# Input         : Source file path, Destination directory path
# Output        : Backup file and log entry
# Description   : Creates a backup of the source file every hour
#                 with the current date and time in the filename.
#                 Writes backup details into backup_log.txt.
# Date          : 22/07/2026
# Author        : Pratik Naykodi
#
#########################################################################

def BackupFile(SourceFile, DestinationDirectory):

    Ret = os.path.exists(SourceFile)

    if(Ret == False):
        print("Marvellous Automation Error : Source file does not exist.")
        return

    Ret = os.path.isfile(SourceFile)

    if(Ret == False):
        print("Marvellous Automation Error : Invalid source file.")
        return

    Ret = os.path.exists(DestinationDirectory)

    if(Ret == False):
        print("Marvellous Automation Error : Destination directory does not exist.")
        return

    Ret = os.path.isdir(DestinationDirectory)

    if(Ret == False):
        print("Marvellous Automation Error : Invalid destination directory.")
        return

    CurrentTime = datetime.now()

    FileName = os.path.basename(SourceFile)

    Name, Extension = os.path.splitext(FileName)

    BackupFileName = Name + "_" + CurrentTime.strftime("%d_%m_%Y_%H_%M_%S") + Extension

    DestinationPath = os.path.join(DestinationDirectory, BackupFileName)

    shutil.copy2(SourceFile, DestinationPath)

    print("Backup created successfully.")
    print("Backup File :", BackupFileName)

    fobj = open("backup_log.txt", "a")

    fobj.write("Backup completed successfully at ")
    fobj.write(CurrentTime.strftime("%d-%m-%Y %I:%M:%S %p"))
    fobj.write("\n")

    fobj.close()

#########################################################################
#
# Function name : main
# Input         : Command line arguments
# Description   : Controls the automation script
# Date          : 22/07/2026
# Author        : Pratik Naykodi
#
#########################################################################

def main():
    Border = "-" * 50

    print(Border)
    print("Marvellous Automation Script")
    print(Border)

    if(len(sys.argv) == 3):
        SourceFile = sys.argv[1]
        DestinationDirectory = sys.argv[2]

        # Perform backup every hour
        schedule.every(1).hours.do(BackupFile, SourceFile, DestinationDirectory)

        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        print("Invalid number of arguments")
        print("Usage : python FileName.py SourceFile DestinationDirectory")

#########################################################################
#
# Starter of the automation script
#
#########################################################################
if __name__ == "__main__":
    main()