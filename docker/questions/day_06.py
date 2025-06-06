"""
Question 1:
What is the difference between COPY and ADD commands on Dockerfile?

### 📚 Dockerfile: `COPY` vs `ADD`

Both `COPY` and `ADD` are instructions in a Dockerfile used to move files into a Docker image during build time. However, they have different purposes and behaviors.

---

#### ✅ `COPY` (Recommended for Most Use Cases)

`COPY` is a simple command that copies files and directories from the host (build context) into the Docker image.

**Syntax:**

```dockerfile
COPY <src> <dest>
```

**Example:**

```dockerfile
COPY requirements.txt /app/
COPY ./src/ /app/src/
```

✔️ Use `COPY` when you just need to copy files/folders into the container.

---

#### ⚠️ `ADD` (Has Additional Features)

`ADD` works similarly to `COPY`, but also supports:

* Automatically extracting local tar archives (e.g., `.tar`, `.tar.gz`)
* Downloading files from remote URLs

**Syntax:**

```dockerfile
ADD <src> <dest>
```

**Example 1 – Extracting a tar file:**

```dockerfile
ADD myapp.tar.gz /app/
```

> This will extract the contents of `myapp.tar.gz` into `/app/`.

**Example 2 – Downloading from a URL (not recommended):**

```dockerfile
ADD https://example.com/file.txt /app/file.txt
```

---

#### 🔐 Best Practices

* ✅ **Use `COPY`** for most tasks. It's predictable and secure.
* ❌ **Avoid `ADD`** for downloading files — use `curl` or `wget` inside `RUN` steps instead:

  ```dockerfile
  RUN curl -o /app/file.txt https://example.com/file.txt
  ```

"""

"""
Question 15:
What is a Docker image repository? 

A Docker image repository stores and shares multiple container images of the same name with 
the clients or the community. We can label them with tags to differentiate their different 
versions. For example, app/marketing_campaign:v1 will be the first version of a marketing app, 
and app/marketing_campaign:v2 will be the second version.

Docker Hub, the most popular Docker image repository, allows users to host, share, and pull 
container images publicly or privately. Other alternatives include Amazon ECR, Google Artifact Registry,
and GitHub Container Registry.
"""

"""
Question 7:
What is Docker Compose, and how is it different from Dockerfile?
Docker Compose is a tool for defining and managing multi-container Docker applications using a 
YAML file (docker-compose.yml). It allows us to configure services, networks, and volumes in a 
single  file, making it easier to manage complex applications.

Differences from Dockerfile:

- A Dockerfile is used to build a single Docker image by defining its layers and dependencies.
- Docker Compose is used to run and orchestrate multiple containers that may rely on each other 
(e.g., a web app container and a database container).
"""