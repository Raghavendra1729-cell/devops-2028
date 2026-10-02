# IAM - Governance

**Name:** Raghavendra  
**Enrollment number:** 24BCS10250

**Session:** 18

IAM controls who can access AWS resources and which actions they can perform. Authentication checks identity; authorization checks permissions.

| Term | Meaning |
|---|---|
| User | An identity for a person or a workload; can have long-term credentials |
| Group | A collection of IAM users with shared permissions |
| Role | An identity assumed temporarily by a user or service |
| Policy | A JSON document describing allowed or denied actions and resources |
| Permission | The ability to perform an action on a resource |

Policies can be attached to users, groups and roles. A role is useful when EC2 needs to call an AWS service without storing access keys in the application. Groups cannot be assumed like roles.

## Least privilege and good practices

Give an identity only the actions and resources it needs. For example, a program that reads one bucket should not have permission to delete every bucket. Start with a limited policy and adjust it when a required operation is denied.

Use temporary credentials and IAM roles where possible. Protect the root account with MFA, avoid root access keys, and use root only for tasks that require it. Review unused identities and permissions. Keep keys out of source code, and rotate any exposed key.

## Example

The cloud project attaches an EC2 instance role with the SSM managed-instance policy. The server can register with Systems Manager, while the student uses a separately authenticated identity to open an SSM session. The role does not grant general access to S3.

Common uses include separating developer and administrator access, giving services permissions, and controlling cross-account access.

[AWS IAM security practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).
