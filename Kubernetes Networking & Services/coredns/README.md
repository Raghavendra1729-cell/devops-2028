# CoreDNS in Kubernetes

CoreDNS is the cluster DNS server. Kubernetes installs it as a Deployment and exposes it through the `kube-dns` Service for compatibility. Pods send DNS queries to that Service IP.

When a Service is created, Kubernetes DNS records are generated from the Service name and namespace. A normal Service name resolves to its stable ClusterIP. A headless Service returns Pod IP records instead. An `ExternalName` Service returns a CNAME for the configured external hostname.

## Configuration and checks

```bash
kubectl get deployment coredns -n kube-system
kubectl get service kube-dns -n kube-system
kubectl get configmap coredns -n kube-system -o yaml
kubectl get pods -n kube-system -l k8s-app=kube-dns
kubectl logs -n kube-system -l k8s-app=kube-dns --tail=20
kubectl exec dns-client -- cat /etc/resolv.conf
```

The Corefile inside the ConfigMap controls plugins such as `kubernetes`, `forward`, `cache`, `health`, and `ready`. The `kubernetes` plugin answers cluster-local records; `forward` sends non-cluster queries to upstream resolvers.

## Troubleshooting order

1. Check that the CoreDNS Pods are Running and Ready.
2. Check that the `kube-dns` Service and EndpointSlices exist.
3. Inspect `/etc/resolv.conf` inside the affected Pod.
4. Try both the short Service name and the full FQDN.
5. Confirm the Service name, namespace, selector, and EndpointSlices.
6. Read CoreDNS logs and the CoreDNS ConfigMap for errors.

```bash
kubectl get endpointslice -n kube-system \
  -l kubernetes.io/service-name=kube-dns
kubectl exec dns-client -- nslookup kubernetes.default.svc.cluster.local
kubectl exec dns-client -- nslookup kubernetes.io
```

If cluster names fail but external names work, I check the Service name, namespace, and CoreDNS Kubernetes plugin. If both fail, I check the Pod resolver configuration, NetworkPolicies, and CoreDNS health.
