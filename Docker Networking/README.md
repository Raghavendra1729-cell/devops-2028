# Docker Networking

For this homework, I practised Docker networks, host networking, bind mounts, and overlay networks.

## 1. Frontend, backend, and database containers

I created three containers with three separate bridge networks.

| Container | Image | Networks |
| --- | --- | --- |
| `frontend` | Nginx | `course-frontend-net` |
| `backend` | Alpine | `course-frontend-net`, `course-backend-net` |
| `database` | MySQL | `course-backend-net`, `course-database-net` |

The backend is connected to two networks, so it can communicate with both the frontend and database. The frontend and database do not share a network.

### Run the containers

```bash
cd "Docker Networking/three-tier"
cp .env.example .env
docker compose up -d
docker compose ps
```

### Check connectivity

```bash
# This works because frontend and backend share a network.
docker compose exec -T frontend ping -c 2 backend

# This works because backend and database share a network.
docker compose exec -T backend ping -c 2 database

# This fails because frontend and database are isolated.
docker compose exec -T frontend ping -c 1 database
```

The first two commands worked. The last command returned `bad address 'database'`, which is expected and shows that the frontend cannot reach the database directly.

### Connectivity result

<img src="Screenshot 2026-08-31 at 7.41.25 PM.png" alt="Terminal showing successful frontend to backend and backend to database checks, plus the expected frontend to database failure" width="900">

## 2. Apache using the host network

I used the official Apache HTTP Server image (`httpd`) with host networking. With host networking, the container uses the host network directly, so no `-p` option is needed.

```bash
docker pull httpd:2.4-alpine
docker run -d --name apache-host --network host httpd:2.4-alpine
curl http://localhost:80
```

Before running this command, I enabled host networking in Docker Desktop and made sure port `80` was available.

### Apache result

The Apache page opened directly at `http://localhost` (port `80`).

<img src="Screenshot 2026-08-31 at 7.42.00 PM.png" alt="Apache It works page running through host networking on localhost port 80" width="850">

## 3. Nginx bind mount

I created an `index.html` file in the local `bind-mount` folder and mounted that folder into an Nginx container.

```bash
cd "Docker Networking"
docker run -d \
  --name bind-nginx \
  -p 8082:80 \
  --mount type=bind,src="$PWD/bind-mount",dst=/usr/share/nginx/html,readonly \
  nginx:alpine
```

I first opened `http://localhost:8082` and saw the original file content.

<img src="Screenshot 2026-08-31 at 7.43.06 PM.png" alt="Nginx bind mount showing the original Hello students page on localhost port 8082" width="850">

Then I changed the heading in `bind-mount/index.html` to `Hello students - file updated` and refreshed the browser. I did not restart the container.

<img src="Screenshot 2026-08-31 at 7.44.27 PM.png" alt="Nginx bind mount showing the updated file content without restarting the container" width="850">

This shows that changes in the local folder appear inside the container immediately through the bind mount.

## 4. Overlay networks

I learned that overlay networks are used when containers or services run on more than one Docker host. The hosts need to be part of the same Docker Swarm, and Docker handles communication between the hosts.

Overlay networks are useful for multi-host applications, replicated services, and communication between Swarm services. I did not run this part locally because it needs more than one Docker host.

Example command on a Swarm manager:

```bash
docker network create --driver overlay --attachable multi-host-network
```

## Clean up

```bash
docker rm -f apache-host bind-nginx
cd "Docker Networking/three-tier"
docker compose down -v
```

These commands remove only the containers, networks, and volume created for this homework.

## What I learned

- Containers can communicate by name when they are on the same Docker network.
- Connecting the backend to two networks allows it to communicate with the frontend and database while keeping the database separate from the frontend.
- Host networking lets a container use the host network directly.
- A bind mount connects a local folder to a container, so local file changes can be seen without restarting the container.
- Overlay networks connect services across multiple Docker hosts.
