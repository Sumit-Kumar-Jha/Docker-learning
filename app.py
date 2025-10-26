# Imports the Flask class from the flask package.
# Flask is a lightweight WSGI (Web Server Gateway Interface) web application framework.
# It provides the core functionalities needed to build a web application,
# such as routing URL requests to Python functions, handling HTTP responses,
# and managing application context. The 'Flask' class is the primary
# entry point for creating your web application instance.
from flask import Flask

# Creates an instance of the Flask application.
# The argument '__name__' is a special Python variable that holds the name
# of the current module. Flask uses this to determine the root path of the
# application so it can find resources like templates and static files relative
# to the module. This is a standard and recommended practice for initializing Flask apps.
app = Flask(__name__)

# This is a decorator provided by Flask to associate a URL path with a Python function.
# When a user navigates to the root URL of the application (e.g., http://localhost:8000/),
# Flask will execute the 'home' function defined immediately below this decorator.
# The "/" path specifically denotes the root or index page of the website.
@app.route("/")
def home():
    # This function, known as a view function in Flask, is responsible for
    # handling requests to the "/" URL.
    # It returns a simple string. Flask automatically takes this string and
    # wraps it in an HTTP response, setting the Content-Type header to 'text/html'
    # by default, and sends it back to the client's web browser.
    # This is the most basic form of returning content from a Flask route.
    return "Hello, Welcome to the course!"

# This block ensures that the Flask development server only runs when the script
# is executed directly (e.g., via `python your_app_name.py`), not when it's
# imported as a module into another script. This is a common Python idiom.
if __name__ == "__main__":
    # Starts the Flask development web server.
    # app.run() is typically used only for development purposes, as it's not
    # designed for high-performance or production environments.
    #
    # - host="0.0.0.0": Makes the server publicly available on your network.
    #   If you used "127.0.0.1" (localhost), it would only be accessible from
    #   the machine running the server. "0.0.0.0" means listen on all public
    #   IP addresses. This is useful for testing across devices on the same network
    #   or in containerized environments (like Docker).
    # - port=8000: Specifies the port number on which the server will listen for
    #   incoming HTTP requests. The default Flask port is 5000, but 8000 is
    #   also a commonly used alternative.
    # When this line executes, the Flask application becomes active, waiting
    # for incoming HTTP requests on the specified host and port.
    app.run(host="0.0.0.0", port=8000)