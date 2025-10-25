# This Dockerfile is expertly crafted to build a Docker image for a Python web application.
# It incorporates detailed, insightful comments for understanding each step and robust
# "logging" statements to trace the build execution process effectively.
# This setup is ideal for development, debugging, and maintaining clear build visibility.

# --- Build Stage: Application Image ---
# We use a specific version of an official Python runtime image as our base.
# 'python:3.9-slim-buster' is chosen for several key reasons:
# 1. Reproducibility: Pinning a specific version (3.9) ensures consistent build environments.
# 2. Security: Official images are maintained and regularly updated with security patches.
# 3. Size Optimization: 'slim-buster' variants are smaller than full 'buster' images,
#    as they omit many common but unnecessary packages, reducing the final image footprint.
#    This balances size efficiency with compatibility for most Python libraries (unlike 'alpine' which can cause issues).
FROM python:3.9-slim-buster

# --- Build-time Trace: Start of Dockerfile execution ---
# These echo statements act as build-time "logs," indicating the start of the build process
# and providing immediate context about the chosen base image and initial state.
RUN echo "--- Starting Docker Image Build Process ---" && \
    echo "Using base image: python:3.9-slim-buster" && \
    echo "Initial current working directory: $(pwd)" && \
    echo "Current user for this step: $(whoami)"

# Set the working directory for all subsequent instructions within the container.
# This centralizes application files and simplifies path management, ensuring commands
# are executed from a consistent, expected location. '/app' is a common and good practice.
WORKDIR /app

# --- Build-time Trace: Working directory setup ---
# Confirm the working directory has been set and display essential environment details.
RUN echo "--- Working directory set to /app ---" && \
    echo "Current working directory after WORKDIR instruction: $(pwd)" && \
    echo "Detailed environment variables (PATH, HOME, LANG, TERM, PYTHON*):" && \
    env | grep -E 'PATH|HOME|LANG|TERM|PYTHON'

# Configure Python-specific environment variables for optimized container behavior.
# 1. PYTHONDONTWRITEBYTECODE=1: Prevents Python from writing .pyc files.
#    This reduces image size, avoids potential issues on read-only filesystems, and
#    is generally unnecessary in container environments.
# 2. PYTHONUNBUFFERED=1: Ensures that Python's stdout and stderr streams are not buffered.
#    This is critical for containerized applications, as it allows application logs
#    to be immediately visible in `docker logs`, facilitating real-time monitoring and debugging.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# --- Build-time Trace: Python environment configuration ---
RUN echo "--- Python environment variables configured for container best practices ---"

# Copy the Python dependency file (requirements.txt) into the container.
# This is a crucial optimization for Docker layer caching:
# By copying only `requirements.txt` first, if this file (and thus dependencies) doesn't change
# between builds, Docker can reuse the cached layer for dependency installation,
# significantly speeding up rebuilds. The `.` signifies copying to the current WORKDIR (/app).
COPY requirements.txt .

# --- Build-time Trace: requirements.txt copied ---
# Verify that requirements.txt has been successfully copied and show its details.
RUN echo "--- requirements.txt copied to working directory ---" && \
    echo "Contents of $(pwd) before dependency installation:" && \
    ls -la requirements.txt # List the copied file to confirm its presence and permissions

# Install the Python dependencies specified in requirements.txt.
# `--no-cache-dir`: Prevents pip from storing downloaded packages in a cache directory.
# This further reduces the final image size, as build-time caches are typically not needed at runtime.
# `set -x` is temporarily enabled to provide verbose tracing of the pip command execution,
# which can be invaluable for debugging dependency installation issues. `set +x` disables it.
RUN echo "--- Installing Python dependencies from requirements.txt ---" && \
    set -x && \
    pip install --no-cache-dir -r requirements.txt && \
    set +x && \
    echo "--- Python dependencies installed successfully ---"

# Copy the rest of the application source code into the working directory.
# This step is intentionally placed after dependency installation. If only the application
# code changes, Docker will rebuild this layer and subsequent layers, but it will reuse the
# cached layers for the base image and dependency installation, maintaining build efficiency.
# The `.` means copy everything from the build context root to the current WORKDIR (/app).
COPY . .

# --- Build-time Trace: Application code copied ---
# List the contents of the application directory to confirm all files have been copied.
RUN echo "--- Application source code copied to /app ---" && \
    echo "Listing contents of /app:" && \
    ls -la /app # List all files and directories in /app to verify build context

# Declare the port on which the application inside the container will listen.
# This instruction is purely informational and serves as documentation.
# It does not actually publish the port; to make the port accessible from the host,
# it must be explicitly published using the `-p` flag with `docker run` (e.g., `-p 8000:8000`).
EXPOSE 8000

# --- Build-time Trace: Port declaration ---
RUN echo "--- Application port 8000 declared for exposure ---"

# Define the default command to execute when the container starts.
# This `CMD` uses the "exec" form (`["executable", "param1", "param2"]`), which is
# highly recommended. It runs the command directly without invoking a shell, allowing
# signals (like SIGTERM for graceful shutdown) to be properly handled by the application process.
# This example assumes a Python application that starts with `python app.py`.
# This command can be overridden by providing arguments to `docker run`.
CMD ["python", "app.py"]

# --- Build-time Trace: CMD instruction set ---
RUN echo "--- Container's default command set to: python app.py ---" && \
    echo "--- Docker Image Build Process Completed Successfully ---"

# --- General Best Practices & Security Considerations (Comments for awareness) ---
# - Multi-stage builds: For production, consider using a multi-stage build to separate
#   build-time dependencies (e.g., compilers) from runtime dependencies, resulting in a much smaller final image.
# - Non-root user: Always strive to run containers with a non-root user (`USER <username>`)
#   to mitigate potential security risks, following the principle of least privilege.
# - Pin dependencies: Ensure all dependencies (in requirements.txt) are pinned to specific versions
#   to guarantee reproducible builds and prevent unexpected breakages from upstream changes.
# - .dockerignore: Use a `.dockerignore` file to exclude unnecessary files (e.g., .git, .vscode,
#   local development files, __pycache__) from the build context to speed up builds and reduce image size.
# - Regular updates: Regularly rebuild your images to pick up security patches and updates
#   from your base image and application dependencies.