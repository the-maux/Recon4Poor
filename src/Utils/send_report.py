import os, smtplib, mimetypes
from email.message import EmailMessage
from zipfile import ZipFile, ZIP_DEFLATED
from src.Utils.shell import dump_to_file

try:
    WORKDIR = os.environ['APP_PATH']
except KeyError:
    WORKDIR = os.environ['PWD']


def dump_domains_state(domains, domain_alive):
    print(f'(DEBUG) Final check to filter on alive hosts for {len(domains)} subdomains')
    nbr_alives = len(domain_alive)
    print(f'(DEBUG) We found {nbr_alives} domain still alive ! {":D" if nbr_alives > 10 else ":("}')
    dump_to_file(namefile='domains.txt', lines=domains)
    dump_to_file(namefile='domains-alive.txt', lines=domain_alive)


def getListOfTxtFilesToSend():
    result = list()
    # for fileInDirectory in os.listdir(path=WORKDIR):
    #     if fileInDirectory.endswith('.txt'):
    #         result.append(fileInDirectory)
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
    try:
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
    except KeyError:
        print('(WARNING) Result not sent, USER_MAIL & USER_PASSWORD not defined')
    exit(-1)
