# aws-VPC-maker
A simple script to create a single VPC in two AZ with 4 subnets using boto3

<h2>Current function:</h2>
Single VPC
4 subnets attached to VPC
1 IG gateway created and attached to VPC
Creating a route table with 2 routes. private and public
Current will connect IG to all the subnets, which needs to be fixed.

I've also added a parameters file that can be edited so that the deployment can be more variable to the location and AZ the user would like to use.


<h2>Future:</h2>
Elastic IP for private subnets

Note:
There's probably a more streamline way of grabbing the ID, but documentation to do so seems difficult to read. Must research more. also ignore the redundancy in subnet. could have used some calculator and likely additional modules to do dynamic changing IP subnetting along with naming schemas for reduction in code repeats. May consider a for loop in future.

Documentation used: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_vpcs
https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcs.html

https://stackoverflow.com/questions/47329675/boto3-how-to-check-if-vpc-already-exists-before-creating-it

