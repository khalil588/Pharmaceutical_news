import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pharmaceutical_news import get_newest_pharmaceutical_news
from bd_connection import get_users
def send_email(sender_email, sender_password, recipient_emails, subject, body):
    # Create the email headers and body
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ', '.join(recipient_emails)
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the Gmail SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        server.login(sender_email, sender_password)  # Log in to your email account
        text = msg.as_string()  # Convert the email content to a string
        server.sendmail(sender_email, recipient_emails, text)  # Send the email
        server.quit()  # Disconnect from the server

        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Example usage




def sending_email():
    news = get_newest_pharmaceutical_news()
    us = get_users()['Email'].to_list()
    for n in news : 
        send_email(
    sender_email="khalil.mekni@esen.tn",
    sender_password="07240408",
    recipient_emails=us,
    subject=n['title'],
    body=n['summarized_article']
    )


