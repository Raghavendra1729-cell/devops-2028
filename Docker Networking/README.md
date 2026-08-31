# Docker Networking and Bind Mounts

**Name:** Raghavendra

**Enrollment number:** 24BCS10250

## 1. Container networking

I used Docker Compose to start a frontend, a backend, and a database. I made three bridge networks and connected the backend to both the frontend and backend networks.

| Container | Image | Networks |
| --- | --- | --- |
| `frontend` | `nginx:alpine` | `course-frontend-net` |
| `backend` | `alpine:3.22` | `course-frontend-net`, `course-backend-net` |
| `database` | `mysql:8.4` | `course-backend-net`, `course-database-net` |

The setup is in [`three-tier/docker-compose.yml`](three-tier/docker-compose.yml).

```text
frontend <--> backend <--> database
```

I started the containers with:

```bash
cd three-tier
cp .env.example .env
docker compose up -d --wait
docker compose ps
```

I used these commands to check the networks and their containers:

```bash
docker network ls --format '{{.Name}}' | grep '^course-'

for network in course-frontend-net course-backend-net course-database-net; do
  printf '%s: ' "$network"
  docker network inspect "$network" --format '{{range .Containers}}{{.Name}} {{end}}'
done
```

The result shows all three containers and networks. It also shows the backend on `course-frontend-net` and `course-backend-net`.

![Containers and Docker networks](task1-container-network-proof.png)

### Connectivity checks

```bash
docker compose exec -T frontend ping -c 2 backend
docker compose exec -T backend ping -c 2 database
docker compose exec -T frontend ping -c 1 database
```

The frontend could reach the backend, and the backend could reach the database. Both checks had `0% packet loss`. The frontend-to-database check failed with `bad address 'database'` because those two containers do not share a network.

![Container connectivity checks](task1-connectivity-proof.png)

## 2. Apache with the host network

I pulled the Apache HTTP Server image and ran it with the host network. I did not use `-p` because the container was using the host network directly.

```bash
docker pull httpd:2.4-alpine
docker run -d --name apache-host --network host httpd:2.4-alpine
docker inspect apache-host --format 'NetworkMode={{.HostConfig.NetworkMode}} State={{.State.Status}}'
curl http://localhost:80
```

The inspect output showed `NetworkMode=host` and `State=running`.

![Apache container using the host network](task2-host-network-proof.png)

I then opened `http://localhost` in the browser. Apache was available directly on port 80.

![Apache page on localhost](task2-apache-browser-proof.png)

## 3. Nginx bind mount

I created a local `bind-mount` folder with an `index.html` file. The first version of the page contained `Hello students`.

I mounted the folder into the Nginx document root:

```bash
docker run -d \
  --name bind-nginx \
  -p 8082:80 \
  --mount type=bind,src="$PWD/bind-mount",dst=/usr/share/nginx/html,readonly \
  nginx:alpine
```

This was the page before I changed the file:

![Original bind-mounted page](task3-original-page-proof.png)

I changed the heading to `Hello students - file updated` and refreshed the browser without restarting the container.

```bash
docker inspect bind-nginx --format '{{range .Mounts}}{{.Type}} {{.Source}} -> {{.Destination}} RW={{.RW}}{{end}}'
docker inspect bind-nginx --format 'StartedAt={{.State.StartedAt}} RestartCount={{.RestartCount}}'
curl -s http://localhost:8082 | grep '<h1>'
```

The output shows a bind mount, `RestartCount=0`, and the updated heading.

![Bind mount and restart count](task3-bind-mount-proof.png)

After refreshing the same page, the new text appeared immediately:

![Updated bind-mounted page](task3-updated-page-proof.png)

## 4. Overlay networks

I read about overlay networks and how they connect containers running on different Docker hosts. The hosts first join the same Docker Swarm. When a service is attached to an overlay network, Docker carries its container traffic between the hosts through a VXLAN tunnel. Docker also provides service discovery, so services on the same overlay network can find each other by name.

Overlay networks are useful for:

- applications whose containers are spread across multiple hosts;
- replicated services in a Docker Swarm;
- keeping communication between services on a private Docker network.

An overlay network is created on a Swarm manager. A basic example is:

```bash
docker swarm init
docker network create --driver overlay --attachable multi-host-network
```

I did not create a real multi-host overlay in this exercise because that requires more than one Docker host.
