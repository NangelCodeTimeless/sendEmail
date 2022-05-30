import smtplib
from email.mime.text import MIMEText
import socket


class Email:
    def __init__(self, host, puerto):
        self.de = "CTORRESNAUN@CRECE.USS.EDU.PE"
        self.password = "N(N+1)/"
        self.host = host
        self.puerto = puerto

    def send_email(self, to_message, subject=" ", msg=" "):

        if self.verificar_internet() == 1:
            try:
                server = smtplib.SMTP(self.host, self.puerto)
                server.starttls()
                server.login(self.de, self.password)
                message = MIMEText(msg)
                message['Subject'] = subject
                para = message['to'] = to_message
                server.sendmail(self.de, para, message.as_string())
                print("El Email fue enviado correctamente...")
                server.quit()
            except smtplib.SMTPServerDisconnected:
                print("Error servidor desconectado")
            except smtplib.SMTPAuthenticationError:
                print("Error con las credenciales: Usuario/password incorrectos")
        else:
            print("No hay conexion a internet")

    @classmethod
    def verificar_internet(cls):
        objSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            objSocket.connect(("www.google.com", 80))
            return 1
        except socket.error:
            return 0




