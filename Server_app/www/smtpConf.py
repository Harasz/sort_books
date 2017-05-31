from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SMTP_conn():

    conn = None

    def __init__(self, address='localhost', port='25', login='', password=''):
        self.address = address
        self.port = port
        self.login = login
        self.password = password

        self.getConn()

    def getConn(self):
        try:
            self.conn = SMTP_SSL(self.address, self.port)
            self.conn.ehlo()
            self.conn.login(self.login, self.password)
        except Exception as e:
            print("[Error] Błąd podczas łączenia z serwerem SMTP:\n"+str(e))

    def sendEmail(self, to, subject, text):
        msg = MIMEMultipart()

        msg['From'] = self.login
        msg['To'] = to
        msg['Subject'] = subject
        msg.attach(MIMEText(text, 'html'))

        try:
            self.conn.sendmail(self.login, to, msg.as_string())
            return True
        except Exception as e:
            try:
                if e[0] == 451:
                    self.getConn()
                    return self.sendEmail(to, subject, text)
            except:
                pass
            print("[Error] Bład z wysłaniem email: \n"+str(e))
            return False
