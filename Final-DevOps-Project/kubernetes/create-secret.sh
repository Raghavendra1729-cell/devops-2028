#!/usr/bin/env bash
set -euo pipefail
namespace=${1:-final-project}
kubectl get namespace "$namespace" >/dev/null 2>&1 || kubectl create namespace "$namespace"
token=$(openssl rand -hex 24)
kubectl -n "$namespace" create secret generic notes-secret --from-literal=API_TOKEN="$token" --dry-run=client -o yaml | kubectl apply -f -
