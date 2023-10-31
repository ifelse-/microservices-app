import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailSender:
    SMTP_SERVER = 'smtpout.secureserver.net'  # GoDaddy SMTP server
    SMTP_PORT = 587  # GoDaddy SMTP port
    SENDER_EMAIL = 'marvin@giveme5ive.com'  # Your GoDaddy VPS email address
    SENDER_PASSWORD = 'Dutch12345%'  # Your GoDaddy VPS email password

    def send_email(self, recipient_email, subject, message):
        try:
            # Create a message
            msg = MIMEMultipart()
            msg['From'] = self.SENDER_EMAIL
            msg['To'] = recipient_email
            msg['Subject'] = subject

            # Email body
            msg.attach(MIMEText(message, 'plain'))

            # Connect to the SMTP server
            server = smtplib.SMTP(self.SMTP_SERVER, self.SMTP_PORT)
            server.starttls()  # Use TLS for a secure connection
            server.login(self.SENDER_EMAIL, self.SENDER_PASSWORD)

            # Send the email
            server.sendmail(self.SENDER_EMAIL, recipient_email, msg.as_string())

            # Close the connection
            server.quit()
            print('Email sent successfully to', recipient_email)
        except Exception as e:
            print('Error:', str(e))
