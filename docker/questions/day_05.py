"""
7. What is Docker Compose, and how is it different from Dockerfile?
Docker Compose is a tool for defining and managing multi-container Docker 
applications using a YAML file (docker-compose.yml). It allows us to configure 
services, networks, and volumes in a single file, making it easier to manage 
complex applications.

Differences from Dockerfile:

A Dockerfile is used to build a single Docker image by defining its layers and 
dependencies. Docker Compose is used to run and orchestrate multiple containers 
that may rely on each other (e.g., a web app container and a database container).
"""

"""
8. Why do we use volumes in Docker? 
We use Docker volumes to keep data safe outside of Docker containers. They 
provide a separate location on hosts where data lives even if the container 
gets removed. Also, it's easier to manage, back up, and share the volumes among 
containers. 
"""

"""
What is the difference between docker run and docker start?

The docker run command is used to generate a new container from an image and
docker start is meant to start a container that was already created before
"""