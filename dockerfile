# Dockerfile for a Python Flask application
#
# This file defines the steps to build a Docker image for a Python application.
# A Docker image is a lightweight, standalone, executable package that includes
# everything needed to run a piece of software, including the code, a runtime,
# libraries, environment variables, and config files.
#
# The overall architecture involves:
# 1. Starting from a base operating system with Python pre-installed.
# 2. Setting up a dedicated working directory inside the container.
# 3. Copying the application source code into this directory.
# 4. Installing any required Python dependencies.
# 5. Declaring which network ports the application will listen on.
# 6. Specifying the command to run the application when the container starts.
#
# Each step builds a new layer in the Docker image, making the build process efficient
# and leveraging caching for faster subsequent builds.

# Use a lightweight base image with Python
#
# The `FROM` instruction initializes a new build stage and sets the Base Image for subsequent instructions.
# It specifies the parent image from which our image will be built.
#
# `python:3.9-slim` is chosen for several reasons:
# - `python`: Indicates that the image contains a Python runtime environment.
# - `3.9`: Specifies the exact version of Python (3.9.x) to ensure consistency and avoid compatibility issues.
# - `-slim`: This tag indicates a "slim" variant of the image. Slim images are much smaller than
#            full-featured Python images because they are based on a minimal Debian distribution
#            (like `debian:buster-slim`). This reduces the final image size, leading to faster downloads,
#            less disk usage, and a smaller attack surface, which is beneficial for production deployments.
#            It includes just enough packages to run Python and common `pip` installations.
FROM python:3.9-slim

# Set the working directory in the container
#
# The `WORKDIR` instruction sets the working directory for any `RUN`, `CMD`, `ENTRYPOINT`,
# `COPY`, and `ADD` instructions that follow it in the Dockerfile.
#
# In this case, `WORKDIR /app` means that all subsequent commands (like `COPY` and `CMD`)
# will be executed relative to the `/app` directory inside the container.
# If `/app` does not exist, Docker will create it automatically.
# This centralizes application files and simplifies file paths within the container.
WORKDIR /app

# Copy the application code to the container
#
# The `COPY` instruction copies new files or directories from <src> and adds them to
# the filesystem of the container at path <dest>.
#
# - The first argument `.` (dot) refers to the current directory on the host machine
#   where the `docker build` command is executed. This means all files and subdirectories
#   (excluding those specified in a `.dockerignore` file) from the host's current directory
#   will be copied.
# - The second argument `/app` is the destination path inside the container.
#   Since `WORKDIR` was set to `/app`, this copies all the host's application files
#   into the `/app` directory within the container.
# This step ensures that our Python application script (`app.py` in this case)
# and any other necessary files are available inside the Docker image.
COPY . /app

# Install Flask (a lightweight Python web framework)
#
# The `RUN` instruction executes any commands in a new layer on top of the current image
# and commits the results. The committed image is used for the next step in the Dockerfile.
#
# `pip install flask` uses `pip`, the standard package installer for Python,
# to download and install the Flask web framework and its dependencies.
# Flask is a micro-framework for building web applications in Python, chosen for its simplicity
# and flexibility, often used for smaller applications or APIs.
# This step ensures that the application has all the necessary Python libraries
# to run correctly within the container. It's crucial that this step comes *after*
# copying the application code if there were a `requirements.txt` file, but for a
# single direct install, order doesn't matter as much, as long as `pip` is available.
RUN pip install flask

# Expose port 8000 to the outside world
#
# The `EXPOSE` instruction informs Docker that the container listens on the specified
# network ports at runtime. It's metadata for the image, indicating the intended ports.
#
# `EXPOSE 8000` declares that the application inside the container will use port 8000.
# This instruction does *not* actually publish the port. To make the port accessible
# from the host machine or other containers, you must explicitly publish it
# when running the container, typically using the `-p` or `--publish` flag with `docker run`
# (e.g., `docker run -p 8000:8000 ...`).
# It acts as documentation and can be used by `docker run` to suggest default port mappings.
EXPOSE 8000

# Command to run the application
#
# The `CMD` instruction provides defaults for an executing container.
# These defaults can include an executable, or they can omit the executable,
# in which case you must specify an `ENTRYPOINT` instruction.
#
# `CMD ["python", "app.py"]` specifies the command to execute when a container
# is started from this image. This is the "exec" form of `CMD`, which is
# the preferred format. It's parsed as a JSON array containing the executable
# and its arguments.
# - `python`: The Python interpreter executable.
# - `app.py`: The Python script to be executed by the interpreter.
#
# This command will start our Flask application using the Python interpreter.
# If a `docker run` command specifies additional arguments, those arguments will
# override this `CMD` instruction entirely. For example, `docker run my-image /bin/bash`
# would start a bash shell instead of running `app.py`.
# If you wanted the command to always run, and allow additional arguments to be passed to it,
# you would typically use an `ENTRYPOINT` instruction.
CMD ["python", "app.py"]