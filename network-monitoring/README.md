# Network Monitoring Tool

## Overview

This Python-based Network Monitoring Tool helps ensure high availability for your applications. It:
- ✅ Monitors an application endpoint.
- ✅ Sends an email alert if the application is down.
- ✅ Attempts to restart the container.
- ✅ If needed, reboots the Linode server to restore service.

## Prerequisites

Before running the script, ensure you have:

- A Linode server.
- Docker installed and an application (e.g., NGINX) running in a container.
- A valid Linode API token.
- Python 3 and required libraries installed:

```bash
pip install requests smtplib paramiko linode_api4
```
- Environment variables configured:
```angular2html
export EMAIL_ADDRESS='your-email@gmail.com'
export EMAIL_PASSWORD='your-email-password'
export RECIPIENT_EMAIL='recipient-email@gmail.com'
export SERVER_PWD='your-server-password'
export LINODE_TOKEN='your-linode-api-token'
```
## How to Use the Script
- Uncomment lines 71-74 to enable the monitoring function
```angular2html
   monitor_website("your-application-ip:8080")
```
- Replace your-application-ip with the actual IP address or domain where your application is running.

- Run the script

## Expected Behavior
- If the application is running fine, it logs a success message.
- If the application goes down:
- It sends an email alert.
- It attempts to restart the container.
- If the issue persists, it reboots the Linode server and restarts the container once the server is back up.