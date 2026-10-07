output "instance_id" {
  value = aws_instance.web.id
}

output "public_ip" {
  value = aws_instance.web.public_ip
}

output "application_url" {
  value = "http://${aws_instance.web.public_ip}"
}

output "bucket_name" {
  value = aws_s3_bucket.project.id
}

output "vpc_id" {
  value = aws_vpc.main.id
}
