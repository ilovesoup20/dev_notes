# Overview

Things learned in this guide - 
- Build and run an image as container
- Share images using Docker Hub
- Deploy Docker applications using multiple containers with a database
- Run applications using Docker Compose

### What is a container?
A container is a sandboxed process on your machine that is isolated from all other processes on the host machine. The **isolation** leverages [kernel namespaces and cgroups](https://medium.com/@saschagrunert/demystifying-containers-part-i-kernel-space-2c53d6979504), features that have been in Linux for a long time. Docker makes it these capabilities approachable and easy to use. In summary, a container:
- is a runnable instance of an image. You can create, start, stop, move, or delete a container using the Docker API or CLI
- can be run on local machines, virtual machines or deployed to the cloud
- is portable (can be run on any OS)
- is isolated from other containers and runs its own software, binaries, and configurations

### What is a container image?
When running a container, it uses an isolated filesystem. This custom filesystem is provided by a container image. Since the image contains the container's filesystem, it must contain everything needed to run an application - all dependencies, configurations, scripts, binaries, etc. The image also contains other configuration for the container, such as environment variables, a default command to run, and other metadata.