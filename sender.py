import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
class Sender:

    def enviar_email(self, html):

        sender_email = "instantredalert@gmail.com"
        #sender_email = "instantredalert@gmail.com"
        #receiver_email = "r_juscelinoaraujo@jfrn.jus.br"
        receiver_email = "vitor848485@gmail.com"
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

        attachmentPath = "PDF_TESTE.pdf"
        try:
            with open(attachmentPath, "rb") as attachment:
                p = MIMEApplication(attachment.read(),_subtype="pdf")	
                p.add_header('Content-Disposition', "attachment; filename= %s" % attachmentPath.split("\\")[-1]) 
                message.attach(p)
        except Exception as e:
            print(str(e))



        # Conexão
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )

