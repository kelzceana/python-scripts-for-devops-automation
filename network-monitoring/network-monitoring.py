# this script is used the monitor a website on its endpoint, send an email if the application is down
import requests
import smtplib
import os

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
RECIPIENT_EMAIL = os.environ.get('RECIPIENT_EMAIL')

def send_email(email_message):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp_gmail:
        smtp_gmail.starttls()
        smtp_gmail.ehlo()
        smtp_gmail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp_gmail.sendmail(EMAIL_ADDRESS, RECIPIENT_EMAIL, email_message)

def monitor_website(website_ip):
    try:
        response = requests.get("http://" + website_ip)
        if response.status_code == 200:
            print("Website " + "http://" + website_ip + " is up and running.")
        else:
            print("Website " + "http://" + website_ip + " is down.")
            # send email to infrastructure engineer
            msg = f'Subject: Application down. \n\n Aplication is down and returned a {response.status_code} status code. \n Investigate the issue and restart the server'
            send_email(msg)


    except Exception as error:
        print(f'connection error')
        print("Website " + "http://" + website_ip + " is down.")
        # send email to infrastructure engineer
        msg = f'Subject: Application down. \n\n Application not assesible at all'
        send_email(msg)



monitor_website("69.164.216.49:8080")