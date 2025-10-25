# Import the Flask class from the flask package.
# Flask is a micro web framework for Python, designed to make getting started with web development quick and easy.
# It provides tools and libraries to build web applications, including handling HTTP requests, routing URLs, and generating responses.
from flask import Flask

# Create an instance of the Flask class.
# This 'app' object will be the central object for the entire web application.
# It's used to configure routing, handle requests, and manage the application's lifecycle.
# The '__name__' argument helps Flask determine the root path for the application.
# This is crucial for Flask to locate resources like templates and static files correctly relative to the module.
app = Flask(__name__)

# The '@app.route("/")' is a decorator that associates the 'home' function with a specific URL path.
# When a web browser requests the root URL ("/") of the application, Flask will execute the 'home' function.
# This decorator defines a 'route' for the application, mapping a URL endpoint to a Python function that handles it.
# The "/" signifies the root URL of the web application (e.g., http://localhost:8000/).
@app.route("/")
def home():
    # This is a 'view function' (or 'route handler').
    # Its purpose is to handle requests coming to the "/" route and return an HTTP response.
    # In Flask, the return value of a view function is automatically converted into an HTTP response.
    # Here, a simple string is returned, which Flask will send as the body of the HTTP response.
    return "Hello, Welcome to the course!"

# This standard Python idiom ensures that the `app.run()` method is called only when the script is executed directly,
# not when it's imported as a module into another script.
# This separation is good practice for structuring applications.
if __name__ == "__main__":
    # Start the Flask development server.
    # The 'app.run()' method launches a local web server that listens for incoming HTTP requests.
    # 'host="0.0.0.0"' makes the server externally visible to any device on the network (not just localhost).
    # This is useful for testing across different machines or in containerized environments.
    # 'port=8000' specifies that the server should listen on port 8000.
    # By default, Flask runs on port 5000 and host 127.0.0.1 (localhost).
    # Note: The development server provided by Flask is not suitable for production deployment.
    # For production, a more robust WSGI server like Gunicorn or uWSGI is used.
    app.run(host="0.0.0.0", port=8000)