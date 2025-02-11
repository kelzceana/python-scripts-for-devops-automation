# this script is used the monitor a website on its endpoint, send an email if the application is down and restart the container and server
import requests
import smtplib
import os
import paramiko
import linode_api4
import time

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
RECIPIENT_EMAIL = os.environ.get('RECIPIENT_EMAIL')
SERVER_PWD = os.environ.get('SERVER_PWD')
LINODE_TOKEN = os.environ.get('LINODE_TOKEN')

def send_email(email_message):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp_gmail:
        smtp_gmail.starttls()
        smtp_gmail.ehlo()
        smtp_gmail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp_gmail.sendmail(EMAIL_ADDRESS, RECIPIENT_EMAIL, email_message)


def restart_container(container_id, hostname, username):
    print('restarting Container...')
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=hostname, username=username, password=SERVER_PWD, look_for_keys=False)
    print(f"Connected to server")
    stdin, stdout, stderr = ssh_client.exec_command(f'docker start {container_id}')
    print(stdout.readlines())
    ssh_client.close()

def restart_server_and_container(server_id, container_id, hostname, username):
    linode_client = linode_api4.LinodeClient(LINODE_TOKEN)
    nginx_server = linode_client.load(linode_api4.Instance, server_id )
    print('rebooting server...')
    nginx_server.reboot()

    #restart container
    while True:
        nginx_server = linode_client.load(linode_api4.Instance, server_id)
        if nginx_server.status == 'running':
            time.sleep(5)
            restart_container(container_id, hostname, username)
            break

def monitor_website(website_ip):
    try:
        response = requests.get("http://" + website_ip)
        if response.status_code == 200:
            print("Website " + "http://" + website_ip + " is up and running.")
        else:
            print("Website " + "http://" + website_ip + " is down.")
            # send email to infrastructure engineer
            message = f'Subject: Application down. \n\n Application is down and returned a {response.status_code} status code. \n Investigate the issue and restart the server'
            send_email(message)
            # restart the docker container
            restart_container('955f0862ee63','66.228.40.95', 'root')
    except Exception as error:
            print(f'connection error')
            print("Website " + "http://" + website_ip + " is down.")
            # send email to infrastructure engineer
            msg = f'Subject: Application down. \n\n Application not accessible at all'
            send_email(msg)
            # server and container restart
            restart_server_and_container('71703369', '955f0862ee63', '66.228.40.95', 'root')


monitor_website("66.228.40.95:8080")