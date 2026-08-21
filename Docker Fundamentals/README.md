# Docker Fundamentals

## Homework

For this homework, I created four simple "Hello World" web applications using Docker. I kept every application in a separate folder with its own source code and Dockerfile.

| Application | Folder | Container port | Local URL |
| --- | --- | ---: | --- |
| Node.js | `nodejs-app` | 3000 | `http://localhost:3000` |
| Python | `python-app` | 8000 | `http://localhost:8000` |
| Java | `java-app` | 8080 | `http://localhost:8080` |
| Apache HTTP Server | `apache-app` | 80 | `http://localhost:8081` |

## Before running

I started Docker Desktop first and checked that Docker was ready using:

```bash
docker info
```

I ran the following commands from this `Docker Fundamentals` folder.

## 1. Node.js application

Files used: `nodejs-app/app.js` and `nodejs-app/Dockerfile`

```bash
docker build -t hello-node ./nodejs-app
docker run -d --name hello-node -p 3000:3000 hello-node
curl http://localhost:3000
```

This displays: `Hello World from Node.js + Docker!`

### Browser result

<img src="image-1.png" alt="Node.js Hello World page" width="700">

Stop this application when finished:

```bash
docker rm -f hello-node
```

## 2. Python application

Files used: `python-app/app.py` and `python-app/Dockerfile`

```bash
docker build -t hello-python ./python-app
docker run -d --name hello-python -p 8000:8000 hello-python
curl http://localhost:8000
```

This displays: `Hello World from Python + Docker!`

### Browser result

<img src="image-3.png" alt="Python Hello World page" width="700">

Stop this application when finished:

```bash
docker rm -f hello-python
```

## 3. Java application

Files used: `java-app/HelloServer.java` and `java-app/Dockerfile`

```bash
docker build -t hello-java ./java-app
docker run -d --name hello-java -p 8080:8080 hello-java
curl http://localhost:8080
```

This displays: `Hello World from Java + Docker!`

### Browser result

<img src="Screenshot 2026-08-31 at 7.19.03 PM.png" alt="Java Hello World page" width="700">

Stop this application when finished:

```bash
docker rm -f hello-java
```

## 4. Apache HTTP Server application

Files used: `apache-app/index.html` and `apache-app/Dockerfile`

```bash
docker build -t hello-apache ./apache-app
docker run -d --name hello-apache -p 8081:80 hello-apache
curl http://localhost:8081
```

This displays: `Hello World from Apache + Docker!`

### Browser result

<img src="Screenshot 2026-08-31 at 7.20.18 PM.png" alt="Apache Hello World page" width="700">

Stop this application when finished:

```bash
docker rm -f hello-apache
```

## Verification

I built all four images successfully and started each application in its own container. I also checked every localhost URL, and each one returned the correct Hello World page. The port mappings were:

```text
hello-node    3000:3000
hello-python  8000:8000
hello-java    8080:8080
hello-apache  8081:80
```

To display the running homework containers:

```bash
docker ps --filter "name=hello-"
```

## Clean up all homework containers

```bash
docker rm -f hello-node hello-python hello-java hello-apache
```

This command affects only the containers created for this assignment.

## What I learned

- I learned how to write a Dockerfile using a base image, copy my application files, expose a port, and start the application with `CMD`.
- I understood that the container port and the localhost port can be different, for example Apache uses `8081:80`.
- I learned how to build an image with `docker build`, run it with `docker run`, and check it using `curl` in the terminal or the browser.
- I also learned to stop and remove containers after testing so that the same container name and port can be used again.
