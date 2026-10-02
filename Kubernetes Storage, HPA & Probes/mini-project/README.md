# Nginx Storage, HPA and Probes Mini Project

The class mini project runs Nginx with a 500Mi PVC, all three HTTP probes, and an HPA with two to five replicas at 50% CPU. This local exercise follows the [Session 13 example](https://github.com/Mehul01-Max/devops-heros/tree/main/session-13-storage-hpa-probes/mini-project).

```text
Client -> web-service -> Nginx Pods
                         | probes and CPU requests
                         | /data -> PVC web-data -> PV
Metrics Server -> HPA -> Deployment replica count
```

Run from this folder:

```bash
kubectl apply -f namespace.yaml
kubectl apply -f pvc.yaml -f deployment.yaml -f service.yaml -f hpa.yaml
kubectl -n production-webapp rollout status deployment/web-app
kubectl -n production-webapp get pods,pvc,hpa
kubectl -n production-webapp exec deployment/web-app -- sh -c 'echo "Raghavendra 24BCS10250" > /data/student.txt'
kubectl -n production-webapp exec deployment/web-app -- cat /data/student.txt
kubectl -n production-webapp delete pods -l app=web-app
kubectl -n production-webapp rollout status deployment/web-app
kubectl -n production-webapp exec deployment/web-app -- cat /data/student.txt
```

All old application Pods were deleted. The replacement Pods still read `Raghavendra 24BCS10250` from the claim. [Persistence output](outputs/persistence.txt) records the old and new Pod names and both reads.

![PVC persistence](../images/persistence.jpg)

The [probe and Service output](outputs/probes-and-service.txt) shows the configured checks and a successful Nginx response through the Service.

```bash
kubectl -n production-webapp port-forward service/web-service 8086:80
```

Open `http://127.0.0.1:8086`.

```bash
kubectl -n production-webapp apply -f load-generator.yaml
kubectl -n production-webapp scale deployment/load-generator --replicas=6
kubectl -n production-webapp top pods
kubectl -n production-webapp get hpa,pods -w
kubectl -n production-webapp describe hpa web-app-hpa
kubectl -n production-webapp delete deployment load-generator
```

The local scale-down stabilization window is 60 seconds. This makes recovery easier to observe during the lab. Both Pods mount the same ReadWriteOnce claim on the single Minikube node. The deployment uses the class Recreate strategy, so an image update can cause downtime.

The [load result](outputs/load-scaling.txt) shows the HPA increasing from two to three application Pods. The [recovery output](outputs/load-recovered.txt) shows two healthy application Pods after the generator was removed.

![Mini-project HPA under load](../images/mini-project-scaling.jpg)

![HPA after removing the load](../images/mini-project-recovered.jpg)
