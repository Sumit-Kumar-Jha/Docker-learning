# Import the Flask class from the flask module.
# Flask is a micro web framework for Python, used for building web applications.
# The 'Flask' class is the core component that represents your web application.
from flask import Flask

# Create an instance of the Flask web application.
# 'app' is the standard variable name for this instance.
# '__name__' is a special Python variable that gets the name of the current module.
# Flask uses this to know where to look for resources (like templates and static files)
# and to determine the root path for the application. It's crucial for Flask to correctly
# set up paths and identify the application's starting point, especially for package management.
app = Flask(__name__)

# The '@app.route("/")' is a decorator provided by Flask.
# Decorators are a powerful feature in Python that allow you to modify or enhance a function.
# This specific decorator registers the 'home' function as the handler for the root URL ("/").
# When a web browser requests the base URL of your application (e.g., http://127.0.0.1:8000/),
# Flask will execute the function immediately following this decorator.
@app.route("/")
# Define a view function named 'home'.
# View functions (also known as route handlers) are responsible for generating responses
# to client requests for a specific URL.
def home():
    # Return a string. Flask automatically takes this string and wraps it in an
    # HTTP response. By default, it sets the 'Content-Type' header to 'text/html'.
    # This string is what the user's web browser will display when accessing the root URL.
    return "Hello, Welcome to the course!"

# This is a standard Python idiom.
# It checks if the script is being run directly (not imported as a module into another script).
# This block ensures that the development server only starts when this script is executed
# as the main program, preventing it from starting if it's merely imported by another script.
if __name__ == "__main__":
    # Start the Flask development server.
    # 'app.run()' is a method that runs the application on a local development server.
    # It should only be used for development and testing purposes, not for production.
    #
    # 'host="0.0.0.0"': This parameter tells the server to listen on all public IPs.
    # If you used '127.0.0.1' (the default for Flask), the server would only be accessible
    # from the machine where it's running (localhost). Setting it to '0.0.0.0' allows
    # external access, meaning other devices on the same network can reach your server.
    #
    # 'port=8000': This specifies the port number on which the server will listen for
    # incoming HTTP requests. '8000' is a common choice for development servers, as it's
    # typically not reserved for other services.
    #
    # For production deployments, a more robust and efficient WSGI server (like Gunicorn, uWSGI,
    # or mod_wsgi with Apache/Nginx) would be used to serve the Flask application.
    app.run(host="0.0.0.0", port=8000)