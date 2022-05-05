import os, smtplib, mimetypes
from email.message import EmailMessage
from zipfile import ZipFile, ZIP_DEFLATED

WORKDIR = '/opt/JSFScan.sh'


def getListOfTxtFilesToSend():
    result = list()
    for fileInDirectory in os.listdir(path=WORKDIR):
        if fileInDirectory.endswith('.txt'):
            result.append(fileInDirectory)
    return result


def buildReportArchive():
    """ Zip all the *.txt files in 1 file result.zip"""
    pathOfFile = WORKDIR + 'result.zip'
    with ZipFile(pathOfFile, mode='w', compression=ZIP_DEFLATED) as archive:
        for logFile in getListOfTxtFilesToSend():
            if logFile is not None:  # file is None when not found
                try:
                    archive.write(logFile)
                except UnicodeDecodeError:
                    print(f"(ERROR) Unicode error for file {logFile}")
    return pathOfFile


def buildMail():
    sender = os.environ['USER_EMAIL']
    recipient = os.environ['USER_EMAIL']
    message = EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = 'Analyze of target over'
    body = """Hello;
        You can find the html report in attachement."""
    message.set_content(body)
    return message


def sendMail(results=None):
    """
    use env var [USER_EMAIL&USER_PASSWORD] to connect with gmail & send a archive in attachement
    :return: succes of email transmission in Bool
    """
    mime_type, _ = mimetypes.guess_type('result.zip')
    mime_type, mime_subtype = mime_type.split('/')
    username = os.environ['USER_EMAIL']
    password = os.environ['USER_PASSWORD']
    message = buildMail()
    archive = buildReportArchive()
    with open(archive, 'rb') as file:
        message.add_attachment(file.read(), subtype=mime_subtype, maintype='octet-stream', filename='result.zip')
    try:
        mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
        mail_server.login(username, password)
        mail_server.send_message(message)
        mail_server.quit()
        print('(DEBUG) Sent result by mails: OK')
        return True
    except smtplib.SMTPException as e:
        print(e)
    print('(WARNING) Sent result by mails: FAILED')
    return False

