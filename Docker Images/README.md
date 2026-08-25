# Docker Images

- **Name:** Raghavendra
- **Enrollment number:** 24BCS10250

## Multi-stage Node.js application

For this task, I used the multi-stage Dockerfile application. After building and running the container, it displays:

```text
Hello World from Docker multi-stage build
```

The application runs on port `3000` inside the container, and I accessed it from port `8080` on my computer.

## Folder structure

```text
Docker Images/
├── README.md
└── multi-stage-app/
    ├── .dockerignore
    ├── Dockerfile
    ├── package-lock.json
    ├── package.json
    └── server.js
```

## Build the image

```bash
cd "Docker Images/multi-stage-app"
docker build -t multi-stage-hello .
```

## Run the container

```bash
docker run -d --name multi-stage-hello -p 8080:3000 multi-stage-hello
```

## Access the application

Open [http://localhost:8080](http://localhost:8080) in a browser or run:

```bash
curl http://localhost:8080
```

## Check the running container

```bash
docker ps --filter "name=multi-stage-hello"
```

The `PORTS` column should show a mapping from host port `8080` to container port `3000`.

## Stop and remove this container

```bash
docker rm -f multi-stage-hello
```

This command targets only the container created for this exercise.

## Proof of running application

### Browser result

I opened `http://localhost:8080` after starting the container. It displayed the required message.

<img src="Screenshot 2026-08-31 at 7.34.12 PM.png" alt="Browser showing the Docker multi-stage Hello World application on localhost port 8080" width="800">

### Running container

The `docker ps` screenshot below shows that the container is running. The `PORTS` column shows the `8080:3000` mapping.

<img src="Screenshot 2026-08-31 at 7.30.45 PM.png" alt="docker ps showing the multi-stage container running on port 8080" width="900">

## What I learned

- I learned that a Docker image is used to create a running container.
- I learned that a multi-stage Dockerfile has more than one `FROM` line. The first stage builds the app and the last stage runs it.
- I used `COPY --from=builder` to copy only the required files into the final image.
- I understood port mapping with `-p 8080:3000`, where `8080` is my computer's port and `3000` is the container port.
- I used `docker build`, `docker run`, and `docker ps` to build, start, and check the application.
