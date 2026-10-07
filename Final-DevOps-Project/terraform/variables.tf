variable "aws_region" {
  type    = string
  default = "ap-south-1"
}

variable "project_name" {
  type    = string
  default = "devops-notes"
}

variable "instance_type" {
  type    = string
  default = "t3.medium"
}

variable "bucket_name" {
  type = string
}
