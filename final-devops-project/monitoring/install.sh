#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
kubectl get namespace observability >/dev/null 2>&1 || kubectl create namespace observability
if ! kubectl -n observability get secret grafana-admin >/dev/null 2>&1; then
  password=$(openssl rand -hex 24)
  kubectl -n observability create secret generic grafana-admin --from-literal=password="$password"
fi
kubectl apply -f stack.yaml
kubectl -n observability rollout status deployment/prometheus --timeout=240s
kubectl -n observability rollout status deployment/grafana --timeout=240s
