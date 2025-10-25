import logging
from flask import Flask

# Configure logging for the application.
# This setup ensures that log messages are emitted to the console.
# - level: DEBUG captures all messages (DEBUG, INFO, WARNING, ERROR, CRITICAL).
# - format: Defines the layout of log messages, including timestamp, log level,
#           the logger's name, the function where the log was made, and the message itself.
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(name)s - %(funcName)s - %(message)s')

# Get a logger instance specifically for this module.
# Using '__name__' ensures the logger is named after the current module (e.g., 'app' if the file is app.py).
# This allows for more granular control over logging output and filtering by module.
logger = logging.getLogger(__name__)

# Log the initialization process of the Flask application.
logger.info("Attempting to initialize Flask application instance.")

# Initialize the Flask application instance.
# '__name__' is a special Python variable that gets the name of the current module.
# Flask uses this to locate resources like template files and static assets relative to this module.
app = Flask(__name__)

logger.info("Flask application instance initialized successfully.")

# Define a route for the root URL ("/").
# The '@app.route("/")' decorator registers the 'home' function as the handler
# for HTTP GET requests made to the application's base URL (e.g., http://localhost:8000/).
# This is a core mechanism in Flask for mapping URLs to Python functions.
@app.route("/")
def home():
    """
    Handles requests to the root URL (/).
    This function is invoked by Flask when a client accesses the application's home page.
    It constructs and returns a simple string message, which Flask then sends back
    to the client as the HTTP response body.
    """
    logger.debug("Received GET request for the home page ('/').")

    # The content to be returned to the client.
    response_message = "Hello, Welcome to the course!"

    logger.info(f"Preparing to send response: '{response_message}'")
    return response_message

# This conditional block ensures that the Flask development server only runs when
# the script is executed directly (e.g., `python your_app.py`), not when it's
# imported as a module into another script. This is a standard Python idiom.
if __name__ == "__main__":
    logger.info("Application script is being executed directly.")

    # Configuration for the Flask development server.
    # '0.0.0.0': Makes the server accessible from any IP address on the network,
    #            not just localhost. This is crucial for development in environments
    #            like Docker containers or when accessing from other devices.
    server_host = "0.0.0.0"
    # '8000': Specifies the port number on which the server will listen for incoming requests.
    #         8000 is a common alternative to Flask's default 5000 and the standard HTTP port 80.
    server_port = 8000
    # 'debug=True': Enables Flask's debug mode. This provides several development-friendly features:
    #               1. An interactive debugger for unhandled exceptions in the browser.
    #               2. Automatic reloading of the server when code changes are detected.
    #               3. Activates Flask's internal debug logging.
    #               NOTE: Debug mode should NEVER be used in a production environment due to security risks.
    debug_mode_enabled = True

    logger.info(f"Starting Flask development server on http://{server_host}:{server_port}")
    logger.info(f"Debug mode is {'enabled' if debug_mode_enabled else 'disabled'} for this server instance.")

    # Start the Flask development server.
    # The `app.run()` call is blocking; it initiates the web server and listens indefinitely
    # for incoming HTTP requests until it's explicitly stopped (e.g., via Ctrl+C).
    app.run(host=server_host, port=server_port, debug=debug_mode_enabled)

    # This line of code will typically not be reached during normal execution,
    # as `app.run()` is a blocking call. It would only execute if the server
    # process is gracefully shut down through a signal other than a forceful termination.
    logger.info("Flask development server has shut down.")