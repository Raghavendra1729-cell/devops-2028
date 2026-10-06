# VPC - Networking

**Name:** Raghavendra  
**Enrollment number:** 24BCS10250

**Session:** 18

A VPC is an isolated virtual network in an AWS Region. A CIDR block defines its IP address range. Subnets divide that range and belong to individual Availability Zones.

| Component | Purpose |
|---|---|
| Route table | Chooses where traffic for a destination goes |
| Internet Gateway | Connects the VPC to the internet |
| NAT Gateway | Gives private-subnet workloads outbound connectivity without accepting unsolicited inbound traffic |
| Security group | Stateful allow rules attached to supported resources |
| Network ACL | Stateless allow and deny rules associated with subnets |

## Public and private subnets

A public subnet has a route to an Internet Gateway. An EC2 instance also needs a public address and matching security rules to communicate directly over the internet. A private subnet has no direct route to the Internet Gateway; it may use NAT for outbound internet access.

A NAT Gateway does not make a private instance publicly reachable. It has costs, so this small project uses one public subnet and does not add NAT. That is a simple class layout rather than a multi-tier production network.

## Security groups and ACLs

Security groups track connections, so allowed request traffic permits the corresponding response. They contain allow rules. Network ACLs are evaluated in rule-number order and require both directions to be allowed because they are stateless. An overly restrictive ACL can block traffic even when a security group allows it.

## Example

The Terraform VPC uses `10.20.0.0/16`; its public subnet uses `10.20.1.0/24`. The route table sends `0.0.0.0/0` to the Internet Gateway. The EC2 security group accepts port 80, while SSM is used for administration.

[VPC user guide](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html).
