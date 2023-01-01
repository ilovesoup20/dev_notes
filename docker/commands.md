# Docker commands

```sh
# Build image
$ docker build -t getting-started .

# Start app container
# `-d`: run in detached mode
# `-p`: map port between host and container
$ docker run -dp 3000:3000 getting-started

# See running containers
$ docker ps

# Stop container
docker stop <container id>

# Remove container
docker rm <container id>

# Stop and remove container in single command
$ docker rm -f <container id>

```