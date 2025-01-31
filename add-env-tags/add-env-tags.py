import boto3

#Frankfurt Region
frankfurt_ec2_client = boto3.client('ec2', region_name='eu-central-1')
frankfurt_ec2_resource = boto3.resource('ec2', region_name='eu-central-1')
frankfurt_reservations = frankfurt_ec2_client.describe_instances()['Reservations']
frankfurt_instance_ids = []

#Paris Region
paris_ec2_client = boto3.client('ec2', region_name='eu-west-3')
paris_ec2_resource = boto3.resource('ec2', region_name='eu-west-3')
paris_reservations = paris_ec2_client.describe_instances()['Reservations']
paris_instance_ids = []

for res in frankfurt_reservations:
    frankfurt_instances = res['Instances']
    for instance in frankfurt_instances:
        frankfurt_instance_ids.append(instance['InstanceId'])


response = frankfurt_ec2_resource.create_tags(
    Resources= frankfurt_instance_ids,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'prod'
        },
    ]
)

for res in paris_reservations:
    paris_instances = res['Instances']
    for instance in paris_instances:
        paris_instance_ids.append(instance['InstanceId'])


response = paris_ec2_resource.create_tags(
    Resources= paris_instance_ids,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'dev'
        },
    ]
)