# Troubleshooting

I ran these exercises in a separate `troubleshooting` namespace and restored the Deployment after each issue. The [outputs](outputs/) folder contains the command results.

## 1. Missing Secret

**Problem:** the Pod did not start because the Deployment referenced `notes-secret`, which was absent.

```bash
kubectl create namespace troubleshooting
kubectl -n troubleshooting apply -f ../kubernetes/application.yaml
kubectl -n troubleshooting get pods
kubectl -n troubleshooting get events --field-selector type=Warning --sort-by=.lastTimestamp
```

The events reported `secret "notes-secret" not found`. The image was present; the missing configuration caused `CreateContainerConfigError`.

```bash
../kubernetes/create-secret.sh troubleshooting
kubectl -n troubleshooting rollout status deployment/notes
```

Creating the Secret allowed the Pod to start. Evidence: [problem](outputs/02-configuration-error.txt), [fix](outputs/03-secret-fixed.txt).

## 2. Wrong readiness path

**Problem:** the container ran, but its new Pod stayed unready.

```bash
kubectl -n troubleshooting patch deployment notes --type strategic -p '{"spec":{"template":{"spec":{"containers":[{"name":"notes","readinessProbe":{"httpGet":{"path":"/missing","port":"http"}}}]}}}}'
kubectl -n troubleshooting get pods
kubectl -n troubleshooting get events --field-selector type=Warning --sort-by=.lastTimestamp
```

The readiness probe received HTTP 404 from `/missing`. This was a wrong probe path, rather than an application crash. I reapplied the manifest containing `/ready`.

```bash
kubectl -n troubleshooting apply -f ../kubernetes/application.yaml
kubectl -n troubleshooting rollout status deployment/notes
```

Evidence: [failed probe](outputs/05-probe-error.txt), [healthy rollout](outputs/06-probe-fixed.txt).

## 3. Unavailable image tag

**Problem:** an upgrade could not start a Pod with the requested image.

```bash
kubectl -n troubleshooting set image deployment/notes notes=devops-notes:missing-tag
kubectl -n troubleshooting get pods
kubectl -n troubleshooting get events --field-selector type=Warning --sort-by=.lastTimestamp
```

The tag was not loaded locally and was unavailable from the registry. The events reported an image pull error. Existing healthy Pods remained available during the rolling update.

```bash
kubectl -n troubleshooting set image deployment/notes notes=devops-notes:1.0
kubectl -n troubleshooting rollout status deployment/notes
```

Evidence: [image pull failure](outputs/08-image-error.txt), [restored image](outputs/09-image-fixed.txt).

## 4. Service selector mismatch

The monitoring exercise changed the Service selector from `app=notes` to `app=notes-wrong`. Its EndpointSlice had no backend addresses, so Prometheus could not scrape the application.

```bash
kubectl -n final-project get pods --show-labels
kubectl -n final-project get endpointslice -l kubernetes.io/service-name=notes
kubectl -n final-project patch service notes -p '{"spec":{"selector":{"app":"notes"}}}'
```

Matching the selector to the Pod labels restored connectivity and cleared the alert.

![Failure detected by monitoring](../../Monitoring%20and%20GitOps/images/alert-firing.jpg)

![Recovery after fixing the selector](../../Monitoring%20and%20GitOps/images/alert-recovered.jpg)

## Final verification

The [verification output](outputs/10-verify.txt) shows a healthy Pod and a successful `/ready` response after the fixes. I removed the troubleshooting namespace after collecting the results.

```bash
kubectl -n troubleshooting exec deployment/notes -- python -c 'import urllib.request; print(urllib.request.urlopen("http://127.0.0.1:5000/ready").read().decode())'
kubectl delete namespace troubleshooting
```
