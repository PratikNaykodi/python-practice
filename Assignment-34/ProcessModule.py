import psutil
import os
from datetime import datetime


# Get list of all running processes
def GetProcessInfo():

    ProcessList = []

    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            ProcessList.append(proc.info)

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return ProcessList


# Create log file
def CreateLog(DirectoryName):

    if not os.path.exists(DirectoryName):
        os.mkdir(DirectoryName)

    Time = datetime.now().strftime("%Y%m%d_%H%M%S")

    FileName = os.path.join(DirectoryName, "ProcessLog_" + Time + ".log")

    ProcessList = GetProcessInfo()

    fobj = open(FileName, "w")

    fobj.write("=" * 70 + "\n")
    fobj.write("Running Process Information\n")
    fobj.write("Created : " + str(datetime.now()) + "\n")
    fobj.write("=" * 70 + "\n\n")

    for process in ProcessList:
        fobj.write(f"Process Name : {process['name']}\n")
        fobj.write(f"PID          : {process['pid']}\n")
        fobj.write(f"Username     : {process['username']}\n")
        fobj.write("-" * 60 + "\n")

    return FileName


# Search process by name
def SearchProcess(ProcessName):

    Found = False

    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            if proc.info['name']:
                if proc.info['name'].lower() == ProcessName.lower() or (proc.info['name']).replace(".exe", "").lower() == ProcessName.lower():
                    Found = True
                    fobj = open("ProcessLog.txt", "a")

                    fobj.write("\n")
                    fobj.write("=" * 70 + "\n")
                    fobj.write("Process Found\n")
                    fobj.write("=" * 70 + "\n")

                    fobj.write(f"Name : {proc.info['name']}\n")
                    fobj.write(f"PID : {proc.info['pid']}\n")
                    fobj.write(f"User : {proc.info['username']}\n")

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    if not Found:
        pobj =  open("ProcessLog.txt", "a")
        pobj.write("\nProcess Not Running\n")