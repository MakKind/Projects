import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class NotificationManager:
    def __init__(self):
        self.my_email = "binmainak883@gmail.com"
        self.password = "lycd grgs atwc blfn"

    def send_mail(self, mssg):
        subject = 'Low Price Alert!'
        body = mssg
        msg = MIMEMultipart()
        msg['From'] = self.my_email
        msg['To'] = "binmainak813@gmail.com"
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.password)
            connection.sendmail(self.my_email, "binmainak813@gmail.com", msg.as_string())
