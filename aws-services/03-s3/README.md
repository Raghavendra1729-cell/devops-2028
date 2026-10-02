# S3 - Storage

**Name:** Raghavendra  
**Enrollment number:** 24BCS10250

**Session:** 18

S3 stores objects in buckets. It is object storage, so it does not act like an EC2 disk attached to the operating system.

| Term | Meaning |
|---|---|
| Bucket | Container for objects; names in the general-purpose namespace are globally unique |
| Object | Data with a key, metadata and an optional version ID |
| Storage class | Storage option selected for access frequency and retrieval needs |
| Versioning | Keeps multiple versions and uses delete markers for ordinary deletes |
| Lifecycle policy | Rules that transition or expire objects and old versions |
| Encryption | Protects stored object data, such as SSE-S3 or SSE-KMS |
| Bucket policy | Resource-based JSON permissions for the bucket and objects |

Standard fits frequently accessed objects. Intelligent-Tiering can adjust tiers based on usage. Standard-IA and One Zone-IA target less frequently accessed data. Glacier classes suit archive use, with different retrieval times and conditions. Choose based on access patterns rather than only storage price.

## Access and protection

Block Public Access helps prevent accidental public exposure. IAM and bucket policies still need appropriate permissions. Encryption protects stored data; it does not decide who can read it. SSE-KMS also involves KMS key permissions.

Versioning helps recover older data, but old versions consume storage. A lifecycle rule can expire old versions after a chosen retention period. Removing the current object alone does not empty a versioned bucket.

## Example and uses

`terraform-s3-demo` creates a private bucket with versioning and AES256 server-side encryption. Outputs identify the bucket and its ARN. Common uses include backups, static assets, logs, datasets and build artifacts. A private bucket cannot be used as a public website without additional serving and access configuration.

[S3 user guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html).
