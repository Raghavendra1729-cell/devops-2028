# Docker Images

**Name:** Raghavendra

**Enrollment number:** 24BCS10250

## Multi-stage Node.js image

I used a multi-stage Dockerfile for a small Node.js application. The application listens on port 3000 in the container, and I mapped it to port 8080 on my computer.

The files are inside `multi-stage-app`:

```text
multi-stage-app/
├── .dockerignore
├── Dockerfile
├── package-lock.json
├── package.json
└── server.js
```

## Build and run

```bash
cd "Docker Images/multi-stage-app"
docker build -t multi-stage-hello .
docker run -d --name multi-stage-hello -p 8080:3000 multi-stage-hello
```

I checked the application with:

```bash
curl http://localhost:8080
```

It returned:

```text
Hello World from Docker multi-stage build
```

The same message appeared when I opened `http://localhost:8080` in the browser.

![Application running in the browser](Screenshot%202026-08-31%20at%207.34.12%E2%80%AFPM.png)

I also checked the container and its port mapping:

```bash
docker ps --filter "name=multi-stage-hello"
```

The output showed port 8080 on my computer mapped to port 3000 in the container.

![Container and port mapping](Screenshot%202026-08-31%20at%207.30.45%E2%80%AFPM.png)

The first stage in the Dockerfile prepares the application files. The final stage copies only the files needed to run the server using `COPY --from=builder`.
