# Terraform S3 Demo

**Name:** Raghavendra  
**Enrollment number:** 24BCS10250

**Session:** 18

This configuration creates a private S3 bucket with versioning and server-side encryption. The bucket name and region are variables, and the bucket name, ARN and region are outputs.

## Files

| File | Purpose |
|---|---|
| `provider.tf` | Terraform and AWS provider versions; AWS region |
| `variables.tf` | Input definitions |
| `terraform.tfvars` | Non-sensitive example settings |
| `main.tf` | Bucket, versioning, encryption and public access protection |
| `outputs.tf` | Values returned after apply |
| `.terraform.lock.hcl` | Selected provider version and checksums |

## Commands

Run from this folder. Use an authenticated AWS profile with permission to manage the bucket. Bucket names are globally unique; change `bucket_name` if the configured name is already taken.

```bash
export AWS_PROFILE=devops
aws sts get-caller-identity
terraform init
terraform fmt
terraform validate
terraform plan -out=s3.tfplan
terraform apply s3.tfplan
terraform show
terraform output
aws s3api get-bucket-versioning --bucket "$(terraform output -raw bucket_name)"
aws s3api get-public-access-block --bucket "$(terraform output -raw bucket_name)"
```

`init` downloads the provider. `fmt` formats the source. `validate` checks the configuration. `plan` previews changes and `apply` performs them. `show` displays the current state; `output` prints the declared output values.

The local state records the resources Terraform manages. State files and saved plans are excluded from Git because they can contain sensitive data.

## Cleanup

```bash
terraform plan -destroy
terraform destroy
terraform show
```

Keep the bucket empty for this exercise. If objects are uploaded, remove their versions and delete markers before destroying a versioned bucket. The configuration does not force-delete data.

## Local configuration check

```bash
terraform init -backend=false
terraform fmt -check
terraform validate
```

These checks examine the configuration without creating AWS resources.

[AWS provider S3 bucket documentation](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket).
