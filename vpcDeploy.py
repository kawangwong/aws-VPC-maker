import boto3
from namingParameters import *

client = boto3.client('ec2', region_name = regionlocation)
ec2 = boto3.resource('ec2', region_name = regionlocation)
## aws_access_key_id='AWS_ACCESS_KEY_ID', aws_secret_access_key='AWS_SECRET_ACCESS_KEY' parameters needed to run.

route_table = ec2.RouteTable("id")


vpc1 = ec2.create_vpc(CidrBlock=cidr_block)
vpc1.create_tags(
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
    CidrBlock =cidr1,
    AvailabilityZone =az1)

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
    CidrBlock= cidr2,
    AvailabilityZone =az2)

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
    CidrBlock=cidr3,
    AvailabilityZone=az3)

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
    CidrBlock=cidr4,
    AvailabilityZone=az4)

## creates 4 subnets

internet_gateway = ec2.create_internet_gateway(
    TagSpecifications = [
        {
            "ResourceType": "internet-gateway",
            "Tags": [
                {
                "Key": "Name",
                "Value": igName,
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
                igName,
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
vpc = ec2.Vpc(vpcIDcode) ##what is the id?
routetable = vpc.create_route_table()
route1 = routetable.create_route(DestinationCidrBlock='0.0.0.0/0', GatewayId=igIDcode)
##creates route table. need to add name tags to this.




print("script sucessful")
