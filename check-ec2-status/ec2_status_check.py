import boto3
ec2_client = boto3.client('ec2')
ec2_resource = boto3.resource('ec2')

ec2_statuses = ec2_client.describe_instance_status()

def status_check():
    for ec2_status in ec2_statuses['InstanceStatuses']:
        instance_id = ec2_status['InstanceId']
        instance_status = ec2_status['InstanceStatus']['Status']
        system_status = ec2_status.get('SystemStatus').get('Status')

        print(f'Instance Status Check of instance {instance_id} is {instance_status}')
        print(f'System Status Check of instance {instance_id} is {system_status}')


status_check()