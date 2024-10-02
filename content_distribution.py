import smtplib
from email.mime.text import MIMEText

def send_email(recipient, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'your-email@example.com'
    msg['To'] = recipient

    with smtplib.SMTP('smtp.example.com') as server:
        server.login('your-email@example.com', 'your-password')
        server.sendmail('your-email@example.com', recipient, msg.as_string())

# Example usage
send_email('customer@example.com', 'Special Offer', 'Enjoy a 20% discount on your next stay!')
