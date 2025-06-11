"""
Docker Overview
Docker is an open-source platform for building, testing, deploying, updating, managing, 
and scaling applications. It streamlines operations by offering software packed into 
standardised and executable units called containers. These units comprise essential 
components required to run the software. Examples of components include runtime, 
libraries, system tools, and code.

Basic Docker Interview Questions
The fundamental level interview questions on Docker are as follows:

1. What is Docker, and why is it used?
Docker is an open-source platform for application development, from building to scaling. 
It is preferred for its ability to accelerate the process of building, sharing, and running 
applications without requiring environment configuration or management.

Docker integrates with existing software development tools, optimizing the workflow. The 
platform is also compatible with multiple cloud platforms.

2. What is a Docker container?
A Docker container is a standard software packaging unit that contains code and other 
dependencies such as system libraries, runtime, system tools, and settings. These speed 
up the application's running across various environments. In simple terms, Docker can be 
considered an executable, standalone, and lightweight package.

3. How do you create a Docker container?
A Docker container can be created using the ‘docker container create’ command in the 
system command. This command establishes the new container from the specified image 
without starting it immediately. The newly created container is generated in a ‘created’ 
state, writable, and open to running specific commands.

4. How does Docker differ from a virtual machine?
Docker is a software platform for creating and running Docker containers, while a Virtual 
Machine refers to the physical machine that runs an operating system.

Docker boots in a few seconds, uses an execution engine, requires less memory, and involves 
a complex usage method. VM takes a few minutes to boot, uses a hypervisor, is less memory 
efficient, and is easy to use.

5. What is a Docker image?
Docker images are read-only templates in the form of a blueprint or snapshot. They contain 
guidelines or instructions for creating a container. These images are standalone and 
executable files that comprise the dependencies, libraries, and files essential for the 
container.

Docker images are shareable and portable and can be stored in registries to track projects, 
user group access, complex software architectures, and others.

6. How do you push and pull Docker images?
Docker images are stored in Docker Hub. To obtain the image or pull it, the required command 
is
docker pull rocker/verse

To push the image to the newly created repository, the appropriate command is
docker push yourhubusername/verse_gapminder

7. What is a Dockerfile?
A Dockerfile is a text document comprising all the commands required for image assembly. 
Users call these commands. Examples of Dockerfile commands include ‘ADD’, ‘ARG’, ‘COPY’, 
‘LABEL’, and many more.

The commands aren’t case-sensitive, but being in uppercase helps easy identification of 
the arguments used in the command. Dockerfiles are used to run the instructions by Docker, 
and they must begin with a ‘FROM’ instruction.

8. What is a Docker registry?
The Docker registry is the centralized storage, management, and distribution system for 
container images. It comprises Docker repositories that contain different versions of the 
images. Images from the registry can be accessed through push and pull commands.

9. What is Docker Hub?
Docker Hub is a hosted registry solution available directly from Docker Inc. It provides 
public and private repositories and solutions like automated build and integrated source 
control.

The public repository is open for access, and the image names are as follows: 
organization/user name. Private repositories are private to the repository creator or 
organization member. The Docker Hub images are verified and secured for safe usage.

10. What is Docker Compose?
Docker Compose is a tool for defining and running multi-container applications. It allows 
projects to run with multiple containers from a single source: a YAML configuration file.

Docker Compose allows you to manage various services, data volumes, and networks easily. It 
is also compatible with working in all environments, such as production, staging, development, 
testing, and CI workflows.

Intermediate Docker Interview Questions
The Docker interview questions for the intermediate level are as follows:

11. How do you create a Docker network, and why would you need it?
A Docker network can be created through the following command:

docker network create [OPTIONS] NETWORK
The Docker network connects different services running in separate containers. Its 
functionality is essential, especially in scenarios requiring service communication 
while being decoupled. The preference can further be owed to features like flexible 
network models, automatic service discovery, security, isolation, and dynamic scaling.

12. What is the difference between Docker run and Docker start?
Docker’s run command creates and starts a new container from a specific image. Running 
here is done for an already started container that requires the command to execute the 
main process.

The start command works to start a stopped container, which requires beginning to execute 
the main process. The container may have stopped for various reasons, such as using the 
stop command, memory overconsumption, or the operating system.

13. What are Docker volumes?
Docker volumes are the container storage and management components of Docker. It can be 
easily created through the command ‘docker volume create’ or via Docker itself during 
service or container creation.

Docker volumes are preferred because they are easy to manage through Docker CLI commands 
or Docker API, secure sharing across multiple containers, and operability on both Linux and 
Windows containers.

14. How do you update an existing Docker image?
Updating the existing Docker image is possible through the following steps:

Check the current version by using the command ‘docker images’
Pull the latest Docker image by downloading the new version of the image
Use the ‘latest’  tag if unsure about the host system default
You can also update the image to a specific version using the command 
‘docker pull [image]:[version-number]’
Stop and remove the container based on the old image. It requires finding the outdated 
container with the command ‘docker ps’
Stop the container using the command ‘docker stop [container-id-or-name] ’ and 
remove it with the command ‘docker rm [container-id-or-name]’
Create a new container using the run command, which is 
‘docker run [options] [image] [commands]’
Note: You can check whether a container will run the new Docker image by listing the 
containers using the above commands.

15. What is a multi-stage build in Docker?
Multi-stage Docker optimizes the Docker files and images without compromising the ease 
of readability and maintenance. It converts the image-building process into multiple 
stages, which allows for the inclusion of the necessary dependencies per the final 
application's functionality. It offers memory and time efficiency.

16. How can you improve the performance of Docker containers?
Improving the performance of Docker containers is possible in the following ways:

Modify the frequency and size of Docker images when running a Docker container
Run containers as non-root users whenever possible to reduce attacks
Make use of multi-stage build, which is to be done by using two or more ‘FROM’ statements
Set resource containers to limit container resources by using the ‘-- cups’ and ‘-- memory’ flags
Preload the image cache and use lightweight base images
Use monitoring tools to optimize container health
17. How do you share data between containers?
Follow the mentioned steps to share data between containers:

Create an independent volume named Datavolume1 using the command ‘docker volume create --name DataVolume1’
Create a new container and attach Datavolume1 using the command ‘docker run --rm -ti -v DataVolume1:/datavolume1 ubuntu’
Verify its persistence using the command ‘cat /datavolume1/Example1.txt’
Use the command to create a new container and new volume ‘docker run -ti --name=Container2 -v DataVolume2:/datavolume2 ubuntu’
Add data to the volume with the command ‘echo ‘Example2" > /datavolume2/Example2.txt
cat /datavolume2/Example2.txt’
Exit the container and restart. Then verify the volume has mounted and data’s persistence using the command ‘cat /datavolume2/Example2.txt’
Remove the container using ‘docker rm d0d2233b668eddad4986313c7a4a1bc0d2edaf0c7e1c02a6a6256de27db17a63’
Check the persistence by listing the volumes with the command ‘docker volume ls’
Use ‘docker volume rm DataVolume2’ to remove the second volume
Add the data image with the command ‘docker run -ti --rm -v DataVolume3:/var ubuntu’ and then exit and check the volume contents
Create container4 and datavolume4 using the previous command
Now create a file with the text ‘echo "This file is shared between containers" > /datavolume4/Example4.txt’ followed by exiting the container 
Again, create container5 to mount the volume from container4 and check the data persistence
Append the text from container5 and exit the container
Restart container4 with the command ‘docker start -ai Container4’ and check the changes using ‘lcat /datavolume4/Example4.txt’ and exit
Make the volume read-only using ‘docker run -ti --name=Container6 --volumes-from Container4:ro ubuntu’
Check the status by removing the example file using the command ‘rm /datavolume4/Example4.txt’
Exit and clean the containers and volume 

18. How does Docker handle container orchestration?
In addition to other container orchestration tools, Docker can perform the function with 
its built-in tool, Docker Swarm. It is a user-friendly and simple way to orchestrate, 
requiring interactions similar to regular Docker CLI commands.

Swarm allows service discovery, replica count, declarative scaling, and rolling updates. 
Docker Compose is another widely used method of handling container orchestration.

19. What is the use of docker-compose.yml?
Docker-compose.yml is used for container orchestration. It defines the required images, 
exposed ports,  access to host filesystems, and other configurations to run multi-counter 
applications efficiently.

20. How would you manage multiple containers using Docker Compose?
Docker Compose eases the management of multiple containers by defining the entire 
multi-container application in a single YAML file named compose.yml. It allows for 
the running of containers in a specific order and the management of network connections 
easily. It also enables scaling individual services up or down based on demand.

Advanced Docker Interview Questions
The Docker interview questions for experienced professionals are as follows:

21. How does Docker handle orchestration, and what tools are available for it?
Docker can handle orchestration through both built-in tools and external tools. 
The built–in tools include Docker Swarm and Docker Compose. The commonly used external 
tool for orchestration is Kubernetes.

22. What is Docker content trust, and how is it used?
Docker content trust allows verification of the pulled or deployed images from the 
registry server. It verifies the publisher and integrity of the received data and offers 
the ability to use digital signatures for sent and received data. The digital signatures 
are added by the publishers, like organizations or individuals, and signed and stored on 
the Docker Notary server of choice.

23. Explain the concept of namespaces in Docker.
Namespaces are an important concept in Docker that provides an isolated workspace for the 
container. Dockers create a set of namespaces for the container being run. They are 
features of the Docker Linux kernel that isolate kernel resources, allowing each set 
of processes to see only their environment.

There are various types of namespaces, including user namespace, network namespace, 
process ID (PID) namespace, interprocess communication (IPC) namespace, and others.

24. How does Docker achieve container isolation?
Container isolation in Docker is possible through Linux features such as control groups (
cgroups), kernel namespaces, and secure computing mode (seccomp). For instance, Docker 
configures cgroups by creating a new cgroup hierarchy and assigns them the container’s 
processes, Kernel namespaces allow a set of processes an isolated view of resources, 
and seccomp works by allowing filtering the system calls made by a process.

25. What is the role of cgroups in Docker?
Control groups, or cgroups, are a feature of the Linux kernel used to limit resource 
availability and allocate system resources such as memory and CPU for Docker containers. 
They help avoid ‘noisy neighbour’ issues and are used by other containerization tools. 
Docker uses cgroups for container isolation, and each container is associated with its own 
cgroups.

26. How do you configure persistent storage in Docker?
Docker ensures data resilience through container volumes. It involves creating a volume 
and mounting it into the container with a command. The volume remains accessible even after 
deleting the container. The volumes for persistent storage comprise their lifecycle and can 
expand depending on the type of application and data being used.

27. What is a Docker registry mirror, and why would you use it?
Registry mirror refers to the local duplicate of the public registry, which mirrors or 
replicates its file structure.  It pulls the image from the public registry and stores 
it before providing it to the user. Then the next request involves producing the image 
from the legal registry mirror.

The Docker registry mirror protects against public registry outages, performs image 
vulnerability scanning, accelerates pod creation, and avoids limits on accessing the 
public registry.

28. What is the Docker security scan, and how does it work?
Docker security scans assess vulnerabilities in container images. Depending on the scanning 
tool, they can detect a variety of risks. The scanning evaluates the packages and other 
dependencies defined in the container image file to identify vulnerabilities.

Docker security scans alert the user if a vulnerability is found, which can be further 
handled by updating the Docker image to the latest version. Docker generally has built-in 
scanning tools inside the registry, while image scanners like Clair and Anchore can also 
be used for scanning.

29. How can Docker improve Continuous Delivery (CD)?
Docker contributes to better Continuous Delivery (CD) by streamlining and accelerating 
the deployment process. It integrates well with source control management and the integration 
tool. The feature also automatically creates an image when the user submits the code.

Docker also allows developers to build and test applications in parallel, thus reducing 
deployment time while minimizing errors. 

30. What are Docker Plugins, and how are they used?
Docker Plugins are extensions that enhance the capabilities of the Docker engine. There are 
specific types of Docker Plugins, such as volume, authorization, and network plugins. 
The volume allows volume persistence across various Docker hosts, while the network plugin 
allows network plumbing. The authorization plugin handles Docker daemon requests.
"""