# Kubernetes Volumes

**Name:** Raghavendra
**Enrollment number:** 24BCS10250
**Session:** 13

| Type | What I learned | Example |
|---|---|---|
| emptyDir | Created for a Pod and shared by its containers. Survives container restarts, but is removed when the Pod is removed. | Writer and reader share `/data/message.txt` |
| hostPath | Mounts a path from the node. Data belongs to that node and may not be present if a Pod moves elsewhere. | `/tmp/course-volume-demo` mounted at `/data` |
| PersistentVolume | A cluster storage resource with capacity, access modes and a reclaim policy. | The provisioner creates a PV for `web-data` |
| PersistentVolumeClaim | A namespaced request for storage that a workload can mount. | Mini project requests 500Mi with ReadWriteOnce |
| StorageClass | Describes a provisioner and storage settings. | Minikube's `standard` class |
| Dynamic provisioning | Creates a PV when a compatible PVC is requested, without manually defining the PV first. | `web-data` becomes Bound automatically |

```bash
kubectl create namespace volume-practice
kubectl -n volume-practice apply -f emptydir.yaml -f hostpath.yaml
kubectl -n volume-practice exec emptydir-demo -c reader -- cat /data/message.txt
kubectl -n volume-practice exec hostpath-demo -- cat /data/message.txt
minikube ssh -- 'cat /tmp/course-volume-demo/message.txt'
kubectl get storageclass
kubectl get pv
kubectl -n production-webapp describe pvc web-data
```

The reader saw the writer's file through emptyDir. The hostPath file was also readable on the node. The [volume output](outputs/volumes.txt) shows these checks, the StorageClass, PV and bound PVC. The mini project verifies the PVC data after all application Pods are replaced.

ReadWriteOnce allows read/write mounting from one node; several Pods on that same node can share the claim. It does not make a shared database safe. Minikube's hostPath provisioner is useful for a local lab; it does not provide replicated storage across nodes.

[Kubernetes volumes](https://kubernetes.io/docs/concepts/storage/volumes/).
