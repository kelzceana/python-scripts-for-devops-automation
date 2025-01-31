import schedule

from ec2_status_check import status_check

def schedule_ec2_status_check():
    status_check()

schedule.every(10).seconds.do(schedule_ec2_status_check)

while True:
    schedule.run_pending()