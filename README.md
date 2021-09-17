# aws-VPC-maker
A simple script to create a single VPC in two AZ with 4 subnets using boto3

Current function:
Single VPC
4 subnets attached to VPC
1 IG gateway created and attached to VPC

Future:
Routing table for 2 public and 2 private in two separte AZ
Elastic IP for private subnets

Note:
There's probably a more streamline way of grabbing the ID, but documentation to do so seams difficult. Must research mroe. also ignore the redundancy in subnet. could have used some calculator and likely additional modules to do dynamic changing IP subnetting along with naming schemas for reduction in code repeats.

Documentation used: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_vpcs
https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcs.html

https://stackoverflow.com/questions/47329675/boto3-how-to-check-if-vpc-already-exists-before-creating-it

