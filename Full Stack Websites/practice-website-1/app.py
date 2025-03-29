import os
import smtplib

from dotenv import load_dotenv

from flask import Flask, render_template, request
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

app = Flask(__name__)

# Setting some configurations
os.environ['EMAIL_ADDRESS'] = os.getenv('EMAIL_ADDRESS')

def send_email(to_email):

    # Sender Email & Password (Use App Password for Gmail)
    EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
    EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

    # Receiver Email
    TO_EMAIL = to_email

    # Create Email Message
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_EMAIL
    msg['Subject'] = "Thank You For Submitting The Form"

    # Email Body
    body = "Hey, Thankyou for submitting your form we will make sure to process your request, Thank You From Talha."
    msg.attach(MIMEText(body, 'plain'))

    # Connect to Gmail's SMTP Server and Send Email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Use port 587 for TLS
        server.starttls()  # Secure the connection
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Login to email account
        server.sendmail(EMAIL_ADDRESS, TO_EMAIL, msg.as_string())  # Send email
        server.quit()  # Close the connection
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Error: {e}")


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit', methods=['POST'])
def form():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    send_email(email)
    # print('Email Sended Successfully')

    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)