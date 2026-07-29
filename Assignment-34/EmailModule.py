import smtplib
from email.message import EmailMessage
import os


def SendMail(ToMail, FileName):

    SenderMail = "pratikpython.test@gmail.com"
    Password = "qymexgxcmpjqdopg"

    try:
        # Step 1 : Create Email object
        msg = EmailMessage()

        # Step 2 : Set mail headers
        msg["From"] = SenderMail
        msg["To"] = ToMail
        msg["Subject"] = "Process Log File"

        # Step 3 : Add mail body
        msg.set_content("Attached Process Log File.")

        fobj = open(FileName, "rb") 

        Data = fobj.read()

        Name = os.path.basename(FileName)

        msg.add_attachment(
            Data,
            maintype="application",
            subtype="octet-stream",
            filename=Name
        )

        # Step 4 : Create SMTP SSL connection manually
        smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)

        # Step 5 : Login using Gmail + App password
        smtp.login(SenderMail, Password)

        # Step 6 : Send the email
        smtp.send_message(msg)

        return True

    except Exception as e:

        file = open("ProcessLog.txt", "a")
        file.write(str(e))

        return False