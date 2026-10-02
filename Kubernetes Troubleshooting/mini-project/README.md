# Kubernetes Troubleshooting Mini Project

This is the class Nginx Deployment and Service challenge. The [Session 14 example](https://github.com/Mehul01-Max/devops-heros/tree/main/session-14-kubernetes-troubleshooting/mini-project) supplied the missing image tag and selector investigation.

```text
Client -> troubleshooting-service -> matching Nginx Pods
```

## Broken Pod questions

1. **What was its status?** It first showed ErrImagePull and later ImagePullBackOff.
2. **What was the error?** The registry could not find `nginx:this-tag-does-not-exist`.
3. **Which command found the reason?** `kubectl describe pod project-broken-pod` and `kubectl events --for pod/project-broken-pod` showed the pull error.
4. **What was wrong with the image?** The image name was valid, but the requested tag did not exist.
5. **How did I fix it?** I applied `fixed-pod.yaml` with `nginx:1.28-alpine` and waited for the Pod to become ready.

The [initial error](../outputs/image-before.txt), [backoff](../outputs/image-backoff.txt) and [healthy Pod](../outputs/image-after.txt) record the result. I inspected the error before applying the fix.

## Investigation table

| Problem | What I saw | Command | Root cause | Fix |
|---|---|---|---|---|
| Broken Pod | ErrImagePull, then ImagePullBackOff | describe and events | Nonexistent image tag | Use a real tag |
| Service problem | No ready backend addresses, failed HTTP request | Pod labels, Service describe and EndpointSlice | Selector `wrong-app` did not match Pod labels | Restore `troubleshooting-app` selector |
| Image problem | Registry reported tag not found | Pod describe | Invalid image version | Apply `fixed-pod.yaml` and wait for readiness |

## Command and troubleshooting questions

1. **What does get tell us?** It lists resources and current summary fields such as readiness, status and age.
2. **Get versus describe?** Get is a summary or structured view; describe expands configuration, conditions and events for investigation.
3. **Why logs?** Container output often explains application startup errors or crashes. `--previous` helps after a restart.
4. **When exec?** When a container is running and I need to inspect a file, environment variable, DNS lookup or local HTTP response.
5. **CrashLoopBackOff?** A container has failed repeatedly and Kubernetes is waiting before another restart. The command or application error must be investigated.
6. **ImagePullBackOff?** Kubernetes could not pull the image and delays another attempt. Possible causes include a wrong tag, missing credentials or registry/network problems.
7. **Why Pending?** A Pod may be waiting for scheduling, enough resources or storage. In this exercise its CPU request exceeded node capacity.
8. **Why no Service endpoints?** Its selector may match no Pods, or matching Pods may be unready. This challenge used a wrong selector.
9. **Selector and labels?** The Service chooses Pods whose labels match the selector. A running Pod with different labels is not a backend for that Service.
10. **Kubernetes DNS?** CoreDNS resolves names such as `troubleshooting-service.troubleshooting-audit.svc.cluster.local` so clients can find Services without hard-coding IP addresses.

The complete [troubleshooting results](../README.md) include all required failure types, their fixes and screenshots.
