# This script automates data backup for EC2 instances
import boto3
import schedule

ec2_client = boto3.client('ec2')
ec2_vol = ec2_client.describe_volumes()
volume_ids = []

def create_snapshot():
    for vol in ec2_vol['Volumes']:
        new_snapshot = ec2_client.create_snapshot(
            VolumeId=vol['VolumeId']
        )
        print('Created snapshot {}'.format(new_snapshot['SnapshotId']))


schedule.every().monday.do(create_snapshot)

while True:
    schedule.run_pending()