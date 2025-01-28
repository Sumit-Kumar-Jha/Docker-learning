# Use a lightweight base image with Python
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code to the container
COPY . /app

# Install Flask (a lightweight Python web framework)
RUN pip install flask

# Expose port 8000 to the outside world
EXPOSE 8000

# Command to run the application
CMD ["python", "app.py"]
