# Kubernetes FQDN

An FQDN is a fully qualified domain name. It gives the complete DNS path instead of relying on the search domains in a Pod's `/etc/resolv.conf`.

For a normal Service, the pattern is:

```text
<service>.<namespace>.svc.<cluster-domain>
```

The usual cluster domain is `cluster.local`, so the ClusterIP example in the `default` namespace is:

```text
web-service-clusterip.default.svc.cluster.local
```

Pods in `default` can normally use the short name `web-service-clusterip`. A Pod in another namespace can use `web-service-clusterip.default`, while the full name works regardless of the caller's namespace.

The headless StatefulSet also gives stable Pod records:

```text
web-headless-0.web-service-headless.default.svc.cluster.local
web-headless-1.web-service-headless.default.svc.cluster.local
```

## Hands-on check

```bash
kubectl apply -f ../01-clusterip.yaml
kubectl apply -f ../05-headless.yaml
kubectl run dns-client --image=busybox:1.36 --restart=Never -- sleep 3600
kubectl wait --for=condition=Ready pod/dns-client --timeout=120s

kubectl exec dns-client -- nslookup web-service-clusterip
kubectl exec dns-client -- \
  nslookup web-service-clusterip.default.svc.cluster.local
kubectl exec dns-client -- \
  nslookup web-headless-0.web-service-headless.default.svc.cluster.local
```

The first two queries resolve the Service. The StatefulSet query resolves one stable Pod identity behind the headless Service.
