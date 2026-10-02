#!/usr/bin/env bash
set -euo pipefail
apt-get update
apt-get install -y nginx
printf '<h1>Terraform cloud project</h1><p>Raghavendra - 24BCS10250</p>\n' > /var/www/html/index.html
systemctl enable --now nginx
snap start amazon-ssm-agent
