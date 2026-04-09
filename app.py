import logging
from flask import Flask

# Configure the logging system to capture execution flow and runtime information.
# This helps in debugging and monitoring the state of the application in real-time.
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize the Flask application instance.
# The name argument helps Flask determine the root path for resources and templates.
app = Flask(__name__)
logger.info("Flask application instance successfully initialized.")

@app.route("/")
def home():
    """
    Handle the root endpoint request.
    Returns a simple greeting message to the user.
    """
    logger.info("Handling request to the root ('/') endpoint.")
    response = "Hello, Welcome to the course!"
    logger.debug(f"Returning response: {response}")
    return response

if __name__ == "__main__":
    # Start the development server.
    # host="0.0.0.0" makes the server accessible externally.
    # port=8000 specifies the networking port.
    logger.info("Starting the Flask development server on host 0.0.0.0, port 8000.")
    try:
        app.run(host="0.0.0.0", port=8000)
    except Exception as e:
        logger.error(f"Application failed to start: {e}")
    finally:
        logger.info("Flask application process terminated.")