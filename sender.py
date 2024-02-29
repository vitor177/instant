import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Sender:

    def enviar_email(self, html):

        sender_email = "instantredalert@gmail.com"
        #sender_email = "instantredalert@gmail.com"
        #receiver_email = "r_juscelinoaraujo@jfrn.jus.br"
        receiver_email = "joovitor177@gmail.com"
        password = 'ymmh doef rovb ntvk'

        message = MIMEMultipart("alternative")
        message["Subject"] = "Instant Red Alert"
        message["From"] = sender_email
        message["To"] = receiver_email

        # HTML a ser enviado
        text = """\
        Olá,
        Tudo bem?
        Enviado via script python"""
        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        # Conexão
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )

