# EC2 - Compute

**Name:** Raghavendra  
**Enrollment number:** 24BCS10250

**Session:** 18

EC2 provides virtual machines called instances. I choose an AMI, instance type, storage and network settings, then start the instance.

| Term | Meaning |
|---|---|
| AMI | Image containing the operating system and initial software |
| Instance type | CPU, memory, architecture and networking capacity |
| Key pair | Public and private keys commonly used for SSH login |
| Security group | Stateful rules controlling allowed instance traffic |
| EBS | Persistent block storage used for root and data volumes |
| Public IP | Address reachable over the internet when routing and rules allow it |
| Private IP | Address used inside the VPC |

The private key stays on the client; it should never be committed. The Terraform project uses SSM instead of opening SSH. Its Ubuntu AMI is AMD64, so the instance type and application image must support that architecture.

## Instance lifecycle

An instance moves through pending, running, stopping, stopped, shutting-down and terminated states. Stopping is different from terminating. EBS data can survive a stop. The public IPv4 address can change after a stop/start unless an Elastic IP is used. Termination deletes volumes configured with delete-on-termination; other volumes can remain.

An instance type can usually be changed after stopping an EBS-backed instance, subject to compatibility. A small type is suitable for a simple web page; monitoring and Kubernetes need more memory.

## Example and uses

The Session 19 instance installs Nginx from cloud-init. Its security group allows HTTP on port 80, and its root EBS volume is encrypted. Common uses are web servers, development machines, batch jobs and self-managed services.

Check EC2, EBS and public IP resources during cleanup. Stopping the server does not remove them all.

[EC2 instance lifecycle](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-lifecycle.html).
