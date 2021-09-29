#file to edit parameters and import to a deployment


regionlocation = "us-east-2"
##region of where you want this VPC deployed
vpcName = "ProductionENVtest"
##name of the VPC

cidr_block = "192.168.1.0/24"
##how big you want the entire VPC to be

cidr1 = '192.168.1.0/26'
cidr2 = '192.168.1.64/26'
cidr3 = '192.168.1.128/26'
cidr4 = '192.168.1.192/26'
#this is the sizing of the subnets for each network, the code currently allows for 4 subnets, but can be modified into more or less.

az1 = "us-east-1a"
az2 = "us-east-2a"
az3 = "us-east-1a"
az4 = "us-east-2a"
##settting the availability zone. by default, we're doing an AZ with 1 public and 1 private in the same AZ and 1 and 1 in a second AZ.

igName = "ig-East"
#name of the internet gateway created