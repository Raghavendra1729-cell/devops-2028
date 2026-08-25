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

It returned this HTML response:

```html
<h1>Hello World from Docker multi-stage build</h1>
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

## Recorded build and deployment

The [class repository](https://github.com/Mehul01-Max/devops-heros) was cloned to inspect its examples. My multi-stage application is kept here so it can be built directly. The [new build output](outputs/multi-stage.txt) shows the successful image build, running container, host port 8080 and required page text.

The three language deployment requirement is covered by the independently built [Node.js](../Docker%20Fundamentals/outputs/node.txt), [Python](../Docker%20Fundamentals/outputs/python.txt) and [Java](../Docker%20Fundamentals/outputs/java.txt) applications.

![Multi-stage application on port 8080](images/multi-stage-verified.jpg)
