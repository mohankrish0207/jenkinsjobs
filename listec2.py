import boto3
import sys

region= sys.argv[1]
accesskey= sys.argv[2]
secretkey= sys.argv[3]
client = boto3.client('ec2',region_name = region, aws_access_key_id = accesskey, aws_secret_access_key = secretkey)

myec2 = client.describe_instances()
for printins in myec2['Reservations']:
	for printout in printins['Instances']:
		print(printout['InstanceId'])
		print(printout['InstanceType'])
		print(printout['LaunchTime'])
		print(printout['State']['Name'])
