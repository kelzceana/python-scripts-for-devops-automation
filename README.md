# Automation Scripts

## Overview

This directory contains a collection of Python scripts designed for automating tasks within AWS using the **Boto3** library. The scripts are intended to simplify and streamline common infrastructure management tasks such as monitoring EC2 instances, scheduling tasks, and tagging resources.

## Scripts

- **Check EC2 State**:  
  This script checks the current state (running, stopped, etc.) of EC2 instances in your AWS account.

- **Check EC2 Health Status**:  
  This script retrieves and displays the health status of EC2 instances, helping to monitor their operational state and identify any potential issues.

- **Write a Scheduled Task in Python**:  
  This script demonstrates how to set up scheduled tasks using Python, which can be used to automate recurring actions like instance backups or status checks.

- **Tag EC2 Instances**:  
  This script allows you to apply custom tags to EC2 instances, helping with organization, cost tracking, or resource management.

## Requirements

- Python 3.x
- Boto3 library: Install it using `pip install boto3`
- AWS credentials configured (e.g., using AWS CLI or environment variables)

## Usage

To run any of these scripts, ensure you have the necessary AWS permissions to interact with EC2 resources and that your credentials are properly set up. Execute the scripts using Python:

```bash
python <script_name>.py
```

