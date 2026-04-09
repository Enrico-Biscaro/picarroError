import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import glob
import os
import datetime
import time
import subprocess

dirName = ' ' # Folder path containing CSV files.
print('The script is running')

while(True):
    # Finding last file in the selected directory
    listFile = glob.glob(dirName)
    latestFile = max(listFile, key=os.path.getmtime)
    latestFile 

    # Detecting the last time the file was modified and the actual hours
    modificationTime = os.path.getmtime(latestFile)
    modificationTime = datetime.datetime.fromtimestamp(modificationTime)
    timeNow = datetime.datetime.now()

    # Sending email if the file was not modified in the last 15 minutes
    diffMinutes = (timeNow - modificationTime).total_seconds() / 60
    print(f'Last modification: {modificationTime}')
    print(f'Actual Time Now: {timeNow}')
    print(' ')

    if diffMinutes > 15:
        message = MIMEMultipart()
        message["To"] = ' '
        message["From"] = ' '
        message["Subject"] = ' '

        email = ' ' # Email address used for the Picarro account
        password = ' ' # App-specific password for the Google account (generate this in Google Account settings for secure access)

        title = '<b>  </b>'
        messageText = MIMEText(''' ''','html')
        message.attach(messageText)

        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo('Gmail')
        server.starttls()
        server.login(email, password)
        fromaddr = ' '
        toaddrs  = []
        server.sendmail(fromaddr,toaddrs,message.as_string())
        print('End')
        TW = ' ' # File path to TeamViewer or any other remote desktop software used to control the PC
        subprocess.Popen([TW])

        break
    time.sleep(900)