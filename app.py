# Import the Flask class from the flask package.
# Flask is a micro web framework for Python. It provides tools, libraries, and technologies
# to build web applications.
# The 'Flask' class itself is the central object that represents your web application.
from flask import Flask

# Create an instance of the Flask class.
# This 'app' object will be your WSGI (Web Server Gateway Interface) application.
# It's the central registry for routes, configurations, and extensions.
# The first argument, '__name__', is the name of the current Python module.
# Flask uses this to know where to look for resources like templates and static files relative to this module.
# It helps Flask correctly locate files if your application is spread across multiple files.
app = Flask(__name__)

# The '@app.route("/")' is a decorator.
# Decorators are a way to modify or enhance a function or method.
# In Flask, the '@app.route()' decorator is used to associate a URL path with a Python function.
# When a client makes an HTTP request to the root URL ("/") of the application,
# Flask will execute the 'home' function defined immediately below this decorator.
# This effectively maps the URL path to a specific view function.
@app.route("/")
def home():
    # This is a view function (also known as a route handler).
    # Its purpose is to handle requests that arrive at the '/' route.
    # It returns a simple string. Flask automatically converts this string into an HTTP response.
    # By default, Flask will set the Content-Type header to 'text/html' for string responses,
    # and the string itself becomes the body of the HTTP response.
    return "Hello, Welcome to the course!"

# This is a standard Python idiom.
# It ensures that the code inside this block only runs when the script is executed directly.
# If this script were imported as a module into another script, the code inside this block would not run.
# This is crucial for web applications, as you might want to import parts of your app
# into a production server setup without automatically starting the development server.
if __name__ == "__main__":
    # Start the Flask development server.
    # app.run() initializes a local web server to serve your application.
    # It is intended for development purposes only and is not suitable for production deployments.
    #
    # host="0.0.0.0": This tells the server to listen on all available public IPs.
    #                When set to "0.0.0.0", the server is accessible from any machine on the network
    #                (including other containers or your host machine if running in a VM/Docker),
    #                not just from the machine running the server itself (which would be '127.0.0.1' or 'localhost').
    # port=8000: This specifies the port number on which the server will listen for incoming HTTP requests.
    #            Standard HTTP usually uses port 80, but 8000 is a common alternative for development to avoid
    #            requiring root privileges to bind to lower ports.
    # debug=True (often added in dev): While not explicitly here, setting debug=True would enable Flask's debugger
    #                                  and auto-reloader, which automatically restarts the server when code changes are detected.
    app.run(host="0.0.0.0", port=8000)