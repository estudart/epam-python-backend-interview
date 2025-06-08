"""
Q1: What is Docker, and why would someone use it?

Docker is a platform that allows developers to package applications and 
their dependencies into containers. These containers are lightweight, 
portable, and run consistently across different environments — from a 
developer’s laptop to production. It's commonly used for improving CI/CD workflows, 
simplifying deployments, and ensuring environment consistency.

##############################################################################

Q2: Explain the difference between a Docker **image** and a **container**.

A Docker image is a read-only template containing the application code, 
libraries, and environment needed to run a container. A container is a running 
instance of that image — it’s a live process with its own isolated filesystem.

##############################################################################

Q3: What are some advantages of using Docker in a development or production environment?

Portability: Containers run the same way on any system that supports Docker.
Efficiency: Lightweight compared to VMs — faster start time and lower resource use.
Isolation: Each container runs in its own environment.
Consistency: Eliminates “works on my machine” problems.
CI/CD: Great for automation, testing, and deployment pipelines.

##############################################################################

Q4: What is the purpose of a `Dockerfile`? Can you describe a basic one?

A Dockerfile is a script that contains a list of instructions to build a 
Docker image. It defines the base image, working directory, dependencies to install, 
and commands to run the application.

**Q5.** What does this Dockerfile do?

```Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]

First it sets what is the image used for the build, which is in this case python3.11, then
it creates a working app in which the service is gonna be running an where we are gonna store
all dependencies files, then it copies the requiments and install all of it. Afterwards all
files are copied from the host and stored in the container, and for the last step the application
is started using teminal comand line.
```

##############################################################################

Q6: How do volumes work in Docker? Why and when would you use one?

Volumes are used in Docker to persist data outside of the container lifecycle. 
When a container is removed, its internal filesystem is also lost — but data in 
volumes is preserved.

##############################################################################

Q7: What’s the difference between `CMD` and `ENTRYPOINT` in a Dockerfile?

CMD: provides default arguments to a container.
ENTRYPOINT: defines the main command to run.

# CMD example
CMD ["python", "main.py"]

# ENTRYPOINT example
ENTRYPOINT ["python"]
CMD ["main.py"]

##############################################################################

Q8: How would you connect two containers (like a web app and a database) using Docker?

docker network create mynet
docker run -d --name db --network mynet postgres
docker run -d --name web --network mynet mywebapp

You can connect containers using a custom Docker network. This allows containers 
to communicate via container name (DNS).

##############################################################################

Q9: What is the difference between `docker run`, `docker build`, and `docker-compose up`?

docker run: to run an container from a given image
docker build: build an image from a given dockerfile
docker-compose up: to start multiple containers given a docker-compose file with various applications

##############################################################################

Q10: What are some best practices for writing Dockerfiles?

Use a small base image (python:3.11-slim)
Use .dockerignore to reduce image size
Combine commands to reduce layers
Use COPY instead of ADD (unless you need tar extraction)
Don’t run apps as root — use a non-root user
Use multi-stage builds if compiling things (e.g. Go, Node)

"""