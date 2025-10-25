# Import the Flask class from the flask package.
# Flask is a lightweight WSGI web application framework. It's often referred to as a "microframework"
# because it doesn't include an ORM, form validation, or other features that more extensive
# frameworks like Django might have. It provides core functionalities for web development,
# like request routing, templating, and session management, allowing developers to choose
# their preferred tools for other aspects.
from flask import Flask

# Create an instance of the Flask application.
# The first argument, `__name__`, is a special Python variable that gets the name of the current module.
# Flask uses this to determine the root path of the application so it can locate resources
# like templates and static files relative to the application's module.
# This 'app' object is the central point of the Flask application, on which all configurations,
# routes, and other application-specific elements will be registered.
app = Flask(__name__)

# This is a decorator provided by Flask that associates a URL path with a function.
# When a client requests the root URL ("/") of the application, Flask will execute
# the `home` function defined immediately after this decorator.
# The string argument "/" represents the URL path. For example, if your application
# is running on `http://127.0.0.1:8000`, then accessing `http://127.0.0.1:8000/` will
# trigger this `home` function.
@app.route("/")
# Define a view function named `home`.
# View functions are responsible for handling incoming requests to a specific URL and
# returning a response that will be sent back to the client's browser.
# This function serves as the handler for the root URL ("/").
def home():
    # This line returns a simple string. Flask automatically takes this string,
    # wraps it in an HTTP response object, sets the Content-Type header to `text/html; charset=utf-8`
    # by default, and sends it back to the client.
    # This is the simplest form of a response in Flask. In more complex applications,
    # one might return HTML templates rendered with dynamic data, JSON data for APIs,
    # or redirect responses.
    return "Hello, Welcome to the course!"

# This block ensures that the development server only runs when the script is executed directly
# (e.g., `python your_app_file.py`) and not when it's imported as a module into another script.
# `__name__` is set to "__main__" when the script is run directly.
# This is a standard Python idiom for defining code that should only be executed when the module
# is the main program.
if __name__ == "__main__":
    # Start the Flask development server.
    # `app.run()` initializes a local development server for testing the application.
    # It is not suitable for production deployment due to performance and security reasons.
    #
    # `host="0.0.0.0"`: This setting makes the server publicly available on all network interfaces.
    # If set to `127.0.0.1` (the default if omitted), the server would only be accessible from the
    # machine it's running on (localhost). Using `0.0.0.0` allows access from other devices on the
    # network or from within Docker containers, which is common for development.
    #
    # `port=8000`: This specifies the port number on which the server will listen for incoming HTTP requests.
    # The default HTTP port is 80, but 8000 is a common alternative for development to avoid
    # requiring superuser privileges to bind to privileged ports (like 80 or 443).
    #
    # When this line executes, the Flask application enters a listening state, waiting for
    # incoming web requests.
    app.run(host="0.0.0.0", port=8000)