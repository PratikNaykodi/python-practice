# Automation Assignment
# Please follow below rules while designing automation script as
#     Accept input through command line or through file.
#     Display any message in log file instead of console.
#     For separate task define separate function.
#     For robustness handle every expected exception.
#     Perform validations before taking any action.
#     Create user defined modules to store the functionality.

# 1. Design automation script which display information of running processes as its name, PID, Username.
# Usage : ProcInfo.py 
# 2. Design automation script which accept process name and display information of that process if it is running.
# Usage : ProcInfo.py Notepad.exe

import sys
import ProcessModule

def main():
    if len(sys.argv) == 1:
        ProcessModule.CreateLog("Logs")

    elif len(sys.argv) == 2:
        ProcessModule.SearchProcess(sys.argv[1])

    else:
        print("Usage : ")
        print("python ProcInfo.py")
        print("python ProcInfo.py notepad.exe")


if __name__ == "__main__":
    main()