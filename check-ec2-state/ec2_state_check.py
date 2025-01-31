import boto3

ec2_client = boto3.client('ec2')
ec2_resource = boto3.resource('ec2')

reservations = ec2_client.describe_instances()
for reservation in reservations['Reservations']:
    instance_id = reservation.get('Instances')[0].get('InstanceId')
    instance_state = reservation.get('Instances')[0].get('State').get('Name')
    print(f' Instance with the {instance_id} ID is  {instance_state}' )
