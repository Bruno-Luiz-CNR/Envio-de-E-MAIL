from email.mime.application import MIMEApplication

from PySide6.QtCore import QThread, Signal
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

from paramiko import file


class EmailThread(QThread):
    progress_signal = Signal(str)
    progress_signal2 = Signal(float)

    def __init__(self, parent=None):
        super(EmailThread, self).__init__(parent)
        self.meuemail = ""
        self.senha = ""
        self.row_data_list = []
        self.arquivo_anexo = ""
        self.running = True

    def set_data(self, meuemail, senha, row_data_list, arquivo_anexo):
        self.meuemail = meuemail
        self.senha = senha
        self.row_data_list = row_data_list
        self.arquivo_anexo = arquivo_anexo

    def run(self):
        total_emails = len(self.row_data_list)
        sent_emails = 0
        for row_data in self.row_data_list:
            if not self.running:
                break

            email, assunto_personalizado, corpo = row_data
            subject = str(assunto_personalizado)
            sender = str(self.meuemail)
            recipients = [email]
            password = str(self.senha)

            msg = MIMEMultipart()
            msg.attach(MIMEText(corpo))

            if self.arquivo_anexo:
                with open(self.arquivo_anexo, 'rb') as file:
                    attach = MIMEApplication(file.read(),_subtype="pdf")
                    attach.add_header('Content-Disposition','attachment',filename=str('Curriculo'))
                    msg.attach(attach)

            msg['Subject'] = subject
            msg['From'] = sender
            msg['To'] = ', '.join(recipients)

            try:
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
                    smtp_server.login(sender, password)
                    smtp_server.sendmail(sender, recipients, msg.as_string())
                    sent_emails += 1
                    progress_percentage = (sent_emails / total_emails) * 100
                    self.progress_signal2.emit(progress_percentage)
                    self.progress_signal.emit(f"{email} - E-mail enviado com sucesso\n")
            except smtplib.SMTPAuthenticationError:
                self.progress_signal.emit(f"Seu usuário/senha não são validos\n")
            except smtplib.SMTPException:
                self.progress_signal.emit(f"Erro ao enviar e-mail para {email}\n")
            except Exception:
                self.progress_signal.emit(f"Erro desconhecido ao enviar e-mail para {email}\n")

    def stop(self):
        self.running = False
        self.wait()
