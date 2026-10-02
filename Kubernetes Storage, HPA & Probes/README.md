# Kubernetes Storage, HPA and Probes

**Name:** Raghavendra
**Enrollment number:** 24BCS10250
**Session:** 13

## Volumes

The [volume notes and examples](01-kubernetes-volumes/README.md) cover emptyDir, hostPath, PV, PVC, StorageClass and dynamic provisioning. The mini project checks persistent data after Pod replacement.

## HPA exercise

`02-hpa/hpa.yml` scales the Nginx Deployment using CPU metrics. The Deployment requests 100m CPU, the target is 50%, and the allowed range is one to five Pods.

Run from `02-hpa/`:

```bash
minikube addons enable metrics-server
kubectl create namespace hpa-practice
kubectl -n hpa-practice apply -f deployment.yaml -f service.yaml -f hpa.yml
kubectl -n hpa-practice rollout status deployment/hpa-demo
kubectl -n hpa-practice get hpa,pods
kubectl -n hpa-practice top pods
kubectl -n hpa-practice apply -f load-generator.yaml
kubectl -n hpa-practice scale deployment/load-generator --replicas=6
kubectl -n hpa-practice get hpa,pods -w
kubectl -n hpa-practice describe hpa hpa-demo
kubectl -n hpa-practice delete deployment load-generator
```

The load generator makes repeated HTTP requests. I increased it from three to six generator Pods. The [recorded result](02-hpa/outputs/load-scaling.txt) shows utilization above the target and scaling from one application Pod to three. HPA compares usage to CPU requests, not to the node's total CPU capacity.

![HPA scaling under load](images/hpa-scaling.jpg)

## Probes

| Probe | Purpose | Failure result |
|---|---|---|
| Startup | Gives the application time to start | Restarts it after the configured failure threshold |
| Readiness | Checks whether a Pod can receive traffic | Removes it from ready Service endpoints |
| Liveness | Checks whether the running container is healthy | Restarts the container |

Startup success permits readiness and liveness checks to proceed. A running Pod can still be unready. The [mini-project Deployment](mini-project/deployment.yaml) uses all three probes against Nginx's HTTP endpoint.

## Mini project

The class Nginx project combines a PVC, resource requests, probes, a Service and HPA. Its [instructions and results](mini-project/README.md) include persistence and scaling verification.

## Cleanup

```bash
kubectl delete namespace hpa-practice volume-practice production-webapp
minikube ssh -- 'sudo rm -rf /tmp/course-volume-demo'
```

Deleting the mini-project namespace also removes its claim. Save any needed files before cleanup. The node path above contains only this exercise's hostPath data.
