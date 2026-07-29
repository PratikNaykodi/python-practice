# Automation Assignment
# Please follow below rules while designing automation script as
#     Accept input through command line or through file.
#     Display any message in log file instead of console.
#     For separate task define separate function.
#     For robustness handle every expected exception.
#     Perform validations before taking any action.
#     Create user defined modules to store the functionality.

# 3.Design automation script which accept directory name from user and create log file in that
# directory which contains information of running processes as its name, PID, Username.
# Usage : ProcInfoLog.py Demo
# Demo is name of Directory.

# 4. Design automation script which accept directory name and mail id from user and create log
# file in that directory which contains information of running processes as its name, PID,
# Username. After creating log file send that log file to the specified mail.

# Usage : ProcInfoLog.py Demo Marvellousinfosystem@gmail.com
# Demo is name of Directory.
# marvellousinfosystem@gmail.com is the mail id.

import sys
import ProcessModule
import EmailModule


def main():

    if len(sys.argv) == 2:

        Directory = sys.argv[1]

        FileName = ProcessModule.CreateLog(Directory)

    elif len(sys.argv) == 3:

        Directory = sys.argv[1]

        Mail = sys.argv[2]

        FileName = ProcessModule.CreateLog(Directory)

        EmailModule.SendMail(Mail, FileName)

    else:

        print("Usage")
        print("python ProcInfoLog.py Logs")
        print("python ProcInfoLog.py Logs abc@gmail.com")


if __name__ == "__main__":
    main()