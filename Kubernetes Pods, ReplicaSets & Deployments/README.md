# Kubernetes Pods, ReplicaSets & Deployments

**Name:** Raghavendra
**Enrollment number:** 24BCS10250
**Class:** Lecture 10

## Aim

The aim of this session was to practise four deployment strategies and observe different Pod lifecycle states.

I ran the commands below from this folder.

Before starting, I checked the cluster:

```bash
minikube start --driver=docker
kubectl get nodes
```

## 1. Rolling update

A rolling update replaces old Pods gradually. The application can remain available while the new version is being created.

```bash
kubectl apply -f 01-rolling-update/deployment-v1.yaml
kubectl rollout status deployment/rolling-web
kubectl get pods -l app=rolling-web --show-labels

kubectl apply -f 01-rolling-update/deployment-v2.yaml
kubectl rollout status deployment/rolling-web
kubectl get pods -l app=rolling-web --show-labels
kubectl get replicasets
```

The Deployment uses `maxSurge: 1` and `maxUnavailable: 0`. Kubernetes creates a new Pod before removing an old one. After the update, all three Pods have the `version=v2` label.

![Rolling update and rollback](images/local-deployment-rolling-rollback.png)

If an update has a problem, the previous revision can be restored:

```bash
kubectl rollout history deployment/rolling-web
kubectl rollout undo deployment/rolling-web
kubectl rollout status deployment/rolling-web
```

## 2. Blue-green deployment

Blue is the current version and green is the new version. Both versions run at the same time, but the Service sends traffic to only one of them.

```bash
kubectl apply -f 02-blue-green/blue.yaml
kubectl apply -f 02-blue-green/green.yaml
kubectl apply -f 02-blue-green/service-blue.yaml
kubectl get pods -l app=strategy-app --show-labels
kubectl get service strategy-service -o jsonpath='{.spec.selector.slot}'
```

The selector first returns `blue`. I switched the Service to green with:

```bash
kubectl apply -f 02-blue-green/service-green.yaml
kubectl get service strategy-service -o jsonpath='{.spec.selector.slot}'
kubectl run blue-green-test --rm -i --restart=Never --image=curlimages/curl:8.12.1 -- curl -s http://strategy-service
```

The response changed from `BLUE v1` to `GREEN v2`.

![Blue-green Service switch](images/local-blue-green-cutover.png)

## 3. Canary deployment

A canary deployment sends a small part of the traffic to the new version. I used four stable Pods and one canary Pod behind the same Service.

```bash
kubectl apply -f 03-canary/stable.yaml
kubectl apply -f 03-canary/canary.yaml
kubectl apply -f 03-canary/service.yaml
kubectl get pods -l app=canary-app --show-labels
kubectl get endpointslice -l kubernetes.io/service-name=canary-service
```

I sent repeated requests from a temporary Pod:

```bash
kubectl run canary-test --rm -i --restart=Never --image=curlimages/curl:8.12.1 -- sh -c 'for i in 1 2 3 4 5 6 7 8 9 10; do curl -s http://canary-service; done'
```

Most responses came from `STABLE v1`, while some came from `CANARY v2`. The exact order can change because the Service distributes requests between its endpoints.

![Stable and canary responses](images/local-canary-responses.png)

## 4. Recreate deployment

The Recreate strategy stops all old Pods before creating the new Pods. This causes a short period when the application is unavailable.

```bash
kubectl apply -f 04-recreate/deployment-v1.yaml
kubectl apply -f 04-recreate/service.yaml
kubectl rollout status deployment/app-recreate
kubectl get pods -l app=app-recreate

kubectl apply -f 04-recreate/deployment-v2.yaml
kubectl get pods -l app=app-recreate -w
kubectl rollout status deployment/app-recreate
```

I verified the final version with:

```bash
kubectl run recreate-test --rm -i --restart=Never --image=curlimages/curl:8.12.1 -- curl -s http://recreate-service
```

The final response was `Application v2`.

![Recreate update](images/local-recreate-outage.png)

## Deployment strategy comparison

| Strategy | How it works | Main point |
|---|---|---|
| Rolling update | Replaces Pods gradually | Application stays available |
| Blue-green | Runs two complete versions and switches the Service | Easy to switch back |
| Canary | Runs a small number of new-version Pods | New version is tested with limited traffic |
| Recreate | Deletes old Pods before creating new ones | Simple, but has downtime |

## Pod lifecycle practice

I applied the lifecycle examples with:

```bash
kubectl apply -f pod-lifecycle/
kubectl get pods -l lab=pod-lifecycle
kubectl get pods -l lab=pod-lifecycle -w
```

These files intentionally create different states and behaviours:

| File | What I observed |
|---|---|
| `01-running.yaml` | A long-running Pod reaches `Running` |
| `02-pending.yaml` | A large CPU request keeps the Pod in `Pending` on the local cluster |
| `03-succeeded.yaml` | A successful one-time command ends in `Succeeded` |
| `04-failed.yaml` | A command with exit code 1 ends in `Failed` |
| `05-crashloopbackoff.yaml` | The container repeatedly exits and reaches `CrashLoopBackOff` |
| `06-imagepullbackoff.yaml` | An invalid image causes `ImagePullBackOff` |
| `07-readiness.yaml` | A failing readiness check keeps the Pod running but not ready |
| `08-liveness.yaml` | A failing liveness check restarts the container |
| `09-startup.yaml` | The startup probe allows time for Nginx to start |
| `10-init-container.yaml` | The init container completes before the main container starts |
| `11-multi-container.yaml` | Two containers share a file using an `emptyDir` volume |
| `12-termination.yaml` | The container handles `SIGTERM` before it exits |

I used these commands to inspect the Pods, events, and logs:

```bash
kubectl describe pod lifecycle-crashloop
kubectl logs lifecycle-crashloop --previous
kubectl describe pod lifecycle-imagepull
kubectl describe pod lifecycle-readiness
kubectl get events --sort-by=.metadata.creationTimestamp
```

![Pod lifecycle results](images/fresh-pod-lifecycle.png)

![CrashLoopBackOff details](images/local-crashloopbackoff.png)

![Readiness probe result](images/local-readiness-probe.png)

## ReplicaSet, DaemonSet and StatefulSet examples

The examples in the `controllers` folder show three different controllers:

```bash
kubectl apply -f controllers/
kubectl get replicasets
kubectl get daemonsets
kubectl get statefulsets
kubectl get pods -o wide
```

- A ReplicaSet keeps the requested number of identical Pods running.
- A DaemonSet runs one Pod on every suitable node.
- A StatefulSet gives its Pods stable names and ordered identities.

![ReplicaSet and DaemonSet](images/local-replicaset-daemonset.png)

## Cleanup

```bash
kubectl delete -f pod-lifecycle/ --ignore-not-found
kubectl delete -f controllers/ --ignore-not-found
kubectl delete -f 01-rolling-update/deployment-v2.yaml --ignore-not-found
kubectl delete -f 02-blue-green/ --ignore-not-found
kubectl delete -f 03-canary/ --ignore-not-found
kubectl delete -f 04-recreate/ --ignore-not-found
```

## Output for each lifecycle YAML

Each file was applied in the `lifecycle-audit` namespace. I saved `get`, `describe` and relevant container logs for each example. Completed and failed one-time Pods have final phases; CrashLoopBackOff and ImagePullBackOff describe container waiting states. The screenshot pages display those recorded command outputs.

### 01-running

[Commands and details](outputs/01-running.txt)

![01-running output](images/lifecycle/01-running.jpg)

### 02-pending

[Commands and details](outputs/02-pending.txt)

![02-pending output](images/lifecycle/02-pending.jpg)

### 03-succeeded

[Commands and details](outputs/03-succeeded.txt)

![03-succeeded output](images/lifecycle/03-succeeded.jpg)

### 04-failed

[Commands and details](outputs/04-failed.txt)

![04-failed output](images/lifecycle/04-failed.jpg)

### 05-crashloopbackoff

[Commands and details](outputs/05-crashloopbackoff.txt)

![05-crashloopbackoff output](images/lifecycle/05-crashloopbackoff.jpg)

### 06-imagepullbackoff

[Commands and details](outputs/06-imagepullbackoff.txt)

![06-imagepullbackoff output](images/lifecycle/06-imagepullbackoff.jpg)

### 07-readiness

[Commands and details](outputs/07-readiness.txt)

![07-readiness output](images/lifecycle/07-readiness.jpg)

### 08-liveness

[Commands and details](outputs/08-liveness.txt)

![08-liveness output](images/lifecycle/08-liveness.jpg)

### 09-startup

[Commands and details](outputs/09-startup.txt)

![09-startup output](images/lifecycle/09-startup.jpg)

### 10-init-container

[Commands and details](outputs/10-init-container.txt)

![10-init-container output](images/lifecycle/10-init-container.jpg)

### 11-multi-container

[Commands and details](outputs/11-multi-container.txt)

![11-multi-container output](images/lifecycle/11-multi-container.jpg)

### 12-termination

[Commands and details](outputs/12-termination.txt)

![12-termination output](images/lifecycle/12-termination.jpg)


All workload and controller manifests passed [Kubernetes server validation](outputs/server-validation.txt).
