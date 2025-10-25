# Use a lightweight base image with Python
# The `FROM` instruction initializes a new build stage and sets the base image for subsequent instructions.
# Choosing `python:3.9-slim` is a best practice for production-ready images.
# - `python`: Specifies the official Python Docker image.
# - `3.9`: Pinpoints a specific major.minor Python version, ensuring consistent environments and preventing unexpected breakages from future Python updates.
# - `slim`: This tag indicates a variant of the Python image that is significantly smaller. It contains only the minimum components required to run Python, without unnecessary libraries, tools, or documentation often found in the full image. This reduces image size, build time, download size, and the potential attack surface, making it ideal for deployment.
FROM python:3.9-slim

# Set the working directory in the container
# The `WORKDIR` instruction sets the working directory for any `RUN`, `CMD`, `ENTRYPOINT`, `COPY`, or `ADD` instructions that follow it in the Dockerfile.
# If the specified directory does not exist, it will be created automatically.
# - `/app`: A common and conventional directory used as the application root inside the container. This makes it easy to locate application files and ensures that subsequent commands execute in the correct context without needing to specify full paths.
WORKDIR /app

# Copy the application code to the container
# The `COPY` instruction copies new files or directories from the host machine (the build context) into the filesystem of the container at the specified path.
# - `.`: The source path on the host machine. In this context, `.` refers to the current directory where the `docker build` command is executed. This means all files and subdirectories within the build context will be copied.
# - `/app`: The destination path inside the container. Because `WORKDIR` was previously set to `/app`, this effectively copies all the application's source code into the application's root directory within the container.
# It's important to place this after `WORKDIR` and often after dependency installation (if using `requirements.txt`) to leverage Docker's build cache effectively.
COPY . /app

# Install Flask (a lightweight Python web framework)
# The `RUN` instruction executes any commands in a new layer on top of the current image and commits the results. The committed image is used for the next step in the Dockerfile.
# - `pip install flask`: This command uses `pip`, Python's package installer, to download and install the Flask web framework along with its dependencies. Flask is a popular microframework for building web applications in Python.
# In a more complex application, one would typically use `COPY requirements.txt .` followed by `RUN pip install -r requirements.txt` to manage dependencies and potentially take advantage of Docker's build cache for faster builds when only source code changes.
RUN pip install flask

# Expose port 8000 to the outside world
# The `EXPOSE` instruction informs Docker that the container listens on the specified network ports at runtime.
# - `8000`: This indicates that the application inside the container expects to receive network traffic on TCP port 8000.
# It's crucial to understand that `EXPOSE` does NOT actually publish the port to the host machine or make it accessible from outside the container. It serves as documentation and a hint to the user running the container, indicating which ports should be mapped. To actually map the port, the `-p` or `--publish` flag must be used with `docker run` (e.g., `docker run -p 8000:8000 ...`).
EXPOSE 8000

# Command to run the application
# The `CMD` instruction provides defaults for an executing container. These defaults can include an executable, or they can be additional parameters to an `ENTRYPOINT` instruction.
# When a container is run without specifying an explicit command, the `CMD` instruction is executed. If a command is provided during `docker run`, it overrides the `CMD` instruction.
# - `["python", "app.py"]`: This is the preferred "exec" form of `CMD`. It specifies that the `python` interpreter should be executed, and `app.py` should be passed as an argument to it.
# Since the `WORKDIR` is set to `/app`, the `python` interpreter will look for `app.py` directly within the `/app` directory, starting the Flask web application.
CMD ["python", "app.py"]