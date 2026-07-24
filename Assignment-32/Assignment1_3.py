# 3: Write a program that reads and displays the contents of a specified text file every minute.

# Handle the following conditions:
#     File does not exist
#     File is empty
#     Permission is denied
#     File cannot be opened

#########################################################################
#
# Importing required libraries
#
#########################################################################

import os
import schedule
import time

#########################################################################
#
# Function name : ReadFile
# Input         : File path
# Output        : Displays file contents
# Description   : Reads and displays the contents of the specified
#                 text file every one minute.
#                 Handles file not found, empty file,
#                 permission denied and file open errors.
# Date          : 22/07/2026
# Author        : Pratik Naykodi
#
#########################################################################

def ReadFile(FilePath):

    Ret = os.path.exists(FilePath)

    if(Ret == False):
        print("Marvellous Automation Error : File does not exist.")
        return

    Ret = os.path.isfile(FilePath)

    if(Ret == False):
        print("Marvellous Automation Error : Invalid file.")
        return

    try:
        fobj = open(FilePath, "r")

        Data = fobj.read()

        if(len(Data) == 0):
            print("Marvellous Automation Error : File is empty.")
            fobj.close()
            return

        print("-" * 50)
        print("Contents of the file are :")
        print("-" * 50)
        print(Data)
        print("-" * 50)

        fobj.close()

    except PermissionError:
        print("Marvellous Automation Error : Permission denied.")

    except OSError:
        print("Marvellous Automation Error : File cannot be opened.")

#########################################################################
#
# Function name : main
# Input         : None
# Output        : Reads file every minute
# Description   : Accepts file path from the user and schedules
#                 the ReadFile function.
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

    # Schedule the task every 1 minute
    schedule.every(1).minutes.do(ReadFile, FilePath)

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