import smtplib
from email.mime.text import MIMEText

class EmailNotifier:
    def __init__(self, sender_email, receiver_email, smtp_user, smtp_pass, smtp_server, smtp_port=587):
        self.sender_email = sender_email
        self.receiver_email = receiver_email
        self.smtp_user = smtp_user
        self.smtp_pass = smtp_pass
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_email(self, subject, body):
        """Send an email using SMTP with UTF-8 encoding."""
        try:
            message = MIMEText(body, "html", "utf-8")
            message["Subject"] = subject
            message["From"] = self.sender_email
            message["To"] = self.receiver_email

            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.smtp_user, self.smtp_pass)
                server.sendmail(self.sender_email, self.receiver_email, message.as_string())
            print("✅ Email sent successfully!")
        except Exception as e:
            print(f"❌ Error sending email: {e}")