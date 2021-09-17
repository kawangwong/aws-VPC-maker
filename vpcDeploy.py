import boto3


client = boto3.client('ec2', region_name ='us-west-1')
ec2 = boto3.resource('ec2', region_name ='us-west-1')
## aws_access_key_id='AWS_ACCESS_KEY_ID', aws_secret_access_key='AWS_SECRET_ACCESS_KEY' parameters needed to run.


vpcName = "ProductionENVtest"
cidr_block = "192.168.1.0/24"
##easy way to allocate values to the VPC

vpc = ec2.create_vpc(CidrBlock=cidr_block)
vpc.create_tags(
    Tags = [
        {"Key": "Name",
        "Value": vpcName}
        ]
        )
##creates the VPC

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

##pulls the VPCID to pass variable

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

## creates 4 subnets

internet_gateway = ec2.create_internet_gateway(
    TagSpecifications = [
        {
            "ResourceType": "internet-gateway",
            "Tags": [
                {
                "Key": "Name",
                "Value": "ig-west"
                },
            ]
        }
    ]
)
## create internet gateway

igData = client.describe_internet_gateways(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': [
                'ig-west',
            ]
        },
    ],
    DryRun=False,
)
igInfos = igData["InternetGateways"]
igDict = igInfos[0]
igIDcode = igDict.get("InternetGatewayId")
print(igIDcode)

## grabs the IG id

internet_gateway.attach_to_vpc(VpcId=vpcIDcode)
## attaches ig to the newly made VPC

print("script sucessful")