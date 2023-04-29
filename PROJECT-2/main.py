import sys
from smtplib import SMTP_SSL as SMTP
from email.mime.text import MIMEText


def send_email(sender, destination, content, subject, text_subtype):
    SMTPserver = 'smtp.att.yahoo.com'
    USERNAME = "gazal.eg.94@gmail.com"
    PASSWORD = "**************"
    try:
        msg = MIMEText(content, text_subtype)
        msg['Subject'] = subject
        msg['From'] = sender

        conn = SMTP(SMTPserver)
        conn.set_debuglevel(False)
        conn.login(USERNAME, PASSWORD)
        try:
            conn.sendmail(sender, destination, msg.as_string())
        finally:
            conn.quit()

    except:
        sys.exit("mail failed; %s" % "CUSTOM_ERROR")


if __name__ == '__main__':
    text_subtype = 'plain'
    content = """Test message"""
    subject = "Sent from Python"
    sender = 'gazal.eg.94@gmail.com'
    destination = ['gazal.eg.94@gmail.com', 'not.exists@gmail.com']
    send_email(sender, destination, content, subject, text_subtype)
