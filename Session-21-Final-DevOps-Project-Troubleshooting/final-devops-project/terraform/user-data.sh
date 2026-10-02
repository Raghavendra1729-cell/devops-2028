#!/usr/bin/env bash
set -euo pipefail
apt-get update
apt-get install -y curl git openssl
curl -fsSL https://get.k3s.io -o /tmp/install-k3s.sh
INSTALL_K3S_VERSION=v1.34.1+k3s1 sh /tmp/install-k3s.sh
snap start amazon-ssm-agent
