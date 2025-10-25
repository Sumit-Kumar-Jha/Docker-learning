# Import the Flask class from the flask library.
# Flask is a micro web framework for Python. It is called "micro" because it aims to keep the core simple but extensible.
# It provides essential tools, libraries, and technologies that allow web developers to build web applications.
from flask import Flask

# Create an instance of the Flask class. This 'app' object is the central application object.
# The `__name__` argument helps Flask determine the root path for the application. This is crucial
# for Flask to correctly locate resources like templates and static files relative to the application's module.
# In a simple, single-file application like this, `__name__` will resolve to "__main__".
# This 'app' instance will be used to configure routes, handle requests, and manage the application's lifecycle.
app = Flask(__name__)

# This is a decorator provided by Flask. Decorators in Python are a powerful feature that allow you to modify
# or extend a function's behavior without explicitly changing its source code.
# The `@app.route("/")` decorator registers the `home` function as the handler for the root URL ("/").
# When a web browser or client makes an HTTP GET request to the application's root URL (e.g., http://localhost:8000/),
# Flask will execute the `home` function.
# The string argument ("/") specifies the URL path that this function will respond to.
@app.route("/")
# Define the view function (also commonly referred to as a route handler or controller function) named `home`.
# This function is responsible for processing requests made to the associated URL path and generating a response.
# In Flask, view functions must return a string, a tuple (response, status, headers), a Response object, or a WSGI callable.
def home():
    # Return a simple string. Flask automatically takes this string and wraps it into an HTTP response.
    # By default, Flask will set the HTTP Content-Type header to `text/html` and the HTTP status code to `200 OK`.
    # This string will be sent back to the client and displayed in their web browser.
    return "Hello, Welcome to the course!"

# This is a standard Python idiom. It checks if the script is being run directly by the Python interpreter
# (e.g., `python your_app_file.py`) rather than being imported as a module into another script.
# This ensures that the development server `app.run()` is only started when this script is executed as the main program,
# preventing it from running if this file were merely imported into another larger application.
if __name__ == "__main__":
    # Run the Flask application development server.
    # `app.run()` starts a local HTTP server that listens for incoming web requests.
    # `host="0.0.0.0"` configures the server to listen on all available public IP addresses.
    # This makes the server accessible not only from the local machine (using `127.0.0.1` or `localhost`)
    # but also from other devices on the same network. This is particularly useful for development
    # when testing on different devices, or when running the application inside a container or virtual machine.
    # `port=8000` specifies that the server should listen on TCP port 8000. You can access the application
    # by navigating to `http://<your_server_ip>:8000/` in a web browser.
    # For production environments, `app.run()` is not recommended. Instead, a robust production-ready
    # WSGI server (like Gunicorn, uWSGI, or Waitress) would be used to serve the Flask application.
    app.run(host="0.0.0.0", port=8000)