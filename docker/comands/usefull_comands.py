"""
BUILD COMMANDS

cd to the folder in which Dockerfile is located
docker build -t image_name .
"""

"""
RUN COMANDS
Comands used to run a docker image

How to run an image, simple way?
docker run image_name

How to run docker detached?
docker run -d image_name

How to run docker setting the port?
docker run -p 6000:6379 image_name

How to run an image setting the container name?
docker run --name container_name image_name

How to run as image setting env_vars?
docker run --name container_name -e var=var_value image_name
"""

"""
GET COMANDS

How to list all the containers running?
docker ps

How to list all the containers running or not?
docker ps -a

How to list all images stored?
docker images
"""

"""
STOP COMANDS

docker stop container_name
docker stop container_id
"""

"""
DEBUG COMMANDS

docker logs container_name

How to open a bash terminal inside Docker?
docker exec -it container_name bash
"""

"""
DOCKER COMPOSE

docker-compose build --up
"""

"""
DOCKER REPOSITORY

docker login
docker tag
docker push 
"""