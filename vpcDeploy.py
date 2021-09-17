import boto3


client = boto3.client('ec2', region_name ='us-west-1')
ec2 = boto3.resource('ec2', region_name ='us-west-1')
# aws_access_key_id='AWS_ACCESS_KEY_ID', aws_secret_access_key='AWS_SECRET_ACCESS_KEY' parameters needed to run only if your CLI wasn't set already.


vpcName = "ProductionENVtest"
cidr_block = "192.168.1.0/24"
#easy way to allocate arguements to the code without retyping etc.

vpc = ec2.create_vpc(CidrBlock=cidr_block)
vpc.create_tags(
    Tags = [
        {"Key": "Name",
        "Value": vpcName}
        ]
        )
#creates the VPC

vpcData = client.describe_vpcs(
    Filters = [
        {
            # "cidr": cidr_block,
            "Name": "tag:Name",
            "Values": [vpcName],
            },
        ]
    )

vpcInfos = vpcData["Vpcs"]
vpcDict = vpcInfos[0]
vpcIDcode= (vpcDict["VpcId"])

#pulls the VPCID to pass variable

subnet1 = ec2.create_subnet(
    TagSpecifications = [
        {
            "ResourceType": "subnet",
            "Tags": [
            {
                "Key": "Name",
                "Value": "public1"
                }
            ]
        },
    ],
    VpcId = vpcIDcode,
    CidrBlock ='192.168.1.0/26',
    AvailabilityZone ='us-west-1a')

subnet2 = ec2.create_subnet(
    TagSpecifications = [
        {
            "ResourceType": "subnet",
            "Tags": [
            {
                "Key": "Name",
                "Value": "private1"
                },
            ]
        }
    ],
    VpcId = vpcIDcode,
    CidrBlock='192.168.1.64/26',
    AvailabilityZone ='us-west-1a')

subnet3 = ec2.create_subnet(
        TagSpecifications = [
        {
            "ResourceType": "subnet",
            "Tags": [
            {
                "Key": "Name",
                "Value": "public2"
                },
            ]
        }
    ],
    VpcId = vpcIDcode,
    CidrBlock='192.168.1.128/26',
    AvailabilityZone='us-west-1c')

subnet4 = ec2.create_subnet(
        TagSpecifications = [
        {
            "ResourceType": "subnet",
            "Tags": [
            {
                "Key": "Name",
                "Value": "private2"
                },
            ]
        }
    ],
    VpcId = vpcIDcode,
    CidrBlock = '192.168.1.192/26',
    AvailabilityZone = 'us-west-1c')

#creates 4 subnets

print("script sucessful")
