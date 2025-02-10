#restores volume from latest backup and attaches the backup to the instance
#Call function with your required ID
import boto3
from operator import itemgetter

ec2_client = boto3.client('ec2')
ec2_resource = boto3.resource('ec2')

def restore_backup(instance_id):
    volumes = ec2_client.describe_volumes(
        Filters=[
            {
                'Name': 'attachment.instance-id',
                'Values': [instance_id]
            }
        ]
    )
    volume_id = volumes['Volumes'][0]['VolumeId']

    snapshots = ec2_client.describe_snapshots(
        OwnerIds =['self'])
    latest_snapshot = sorted(snapshots['Snapshots'], key=itemgetter('StartTime'), reverse=True)[0]


    new_volumes = ec2_client.create_volume(
        SnapshotId = latest_snapshot['SnapshotId'],
        AvailabilityZone = 'us-east-1a',
        TagSpecifications = [
            {
                'ResourceType': 'volume',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'Prod'
                    }

                ]
            }
        ]
    )
# wait until volume is available before attaching it to an instance
    while True:
        vol = ec2_resource.Volume(new_volumes['VolumeId'])
        if vol.state == 'available':
            ec2_resource.Instance(instance_id).attach_volume(
                VolumeId=new_volumes['VolumeId'],
                Device='/dev/sdh'
            )
            break


restore_backup('i-075cee131dc6025f0')




