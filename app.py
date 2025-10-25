# Import the Flask class from the flask package.
# Flask is a micro web framework for Python. It provides tools, libraries, and technologies
# that allow you to build a web application. This line makes the core Flask functionality available.
from flask import Flask

# Create an instance of the Flask class. This 'app' object will be our WSGI (Web Server Gateway Interface)
# application. It handles all incoming requests and outgoing responses.
# The '__name__' argument helps Flask determine the root path for resources like templates and static files.
# It typically refers to the name of the current Python module (e.g., 'main' or 'app').
# Flask uses this to locate resources relative to the module's location.
app = Flask(__name__)

# This is a decorator provided by Flask. Decorators are a powerful Python feature that
# allows you to modify or enhance a function without changing its source code.
# The `@app.route("/")` decorator registers the `home` function as the handler for the URL path "/".
# When a client's web browser requests the root URL of our application (e.g., http://localhost:8000/),
# Flask will execute the `home` function and use its return value as the response body.
# This is the core mechanism for routing incoming HTTP requests to specific Python functions (view functions).
@app.route("/")
def home():
    # This is our "view function" or "route handler." Its purpose is to process the request
    # for the "/" route and return a response.
    # In Flask, a string returned by a view function is automatically wrapped into an HTTP response
    # with a 200 OK status code and a 'Content-Type: text/html' header by default.
    # This simple example just returns a plain text message.
    return "Hello, Welcome to the course!"

# This block ensures that the development server only runs when the script is executed directly
# (e.g., `python your_app_name.py`), and not when it's imported as a module into another script.
# `__name__` is a special built-in variable that holds the name of the current module.
# When a script is run directly, `__name__` is set to `"__main__"`.
if __name__ == "__main__":
    # This line starts the Flask development web server.
    # It makes our application accessible via HTTP requests.
    #
    # `host="0.0.0.0"`: This tells the server to listen on all available public IPs.
    #   If you used `127.0.0.1` (localhost), the server would only be accessible from the machine
    #   running the code. `0.0.0.0` allows access from other machines on the network, which is
    #   useful for testing in certain environments (e.g., Docker containers, virtual machines,
    #   or when showing the app to someone else on the same network). For production, a dedicated
    #   production-ready WSGI server like Gunicorn or uWSGI is used instead of `app.run()`.
    #
    # `port=8000`: This specifies the port number on which the server will listen for incoming requests.
    #   The default HTTP port is 80, but 8000 is a common alternative for development servers
    #   to avoid requiring elevated privileges (root access) to bind to port 80.
    app.run(host="0.0.0.0", port=8000)