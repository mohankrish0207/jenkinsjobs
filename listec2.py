import boto3
import sys

accesskey= sys.argv[1]
secretkey= sys.argv[2]
client = boto3.client('ec2',region_name = 'ap-south-1', aws_access_key_id = accesskey, aws_secret_access_key = secretkey)

myec2 = client.describe_instances()
for printins in myec2['Reservations']:
	for printout in printins['Instances']:
		for printname in printout['Tags']:
			print(printout['InstanceId'])
			print(printout['InstanceType'])
			print(printout['LaunchTime'])
			print(printout['State']['Name'])
			print(printname['Value'])
