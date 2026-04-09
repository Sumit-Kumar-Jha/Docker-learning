import logging
from flask import Flask

# Configure the logging system to provide timestamps and severity levels
# This is crucial for tracing request lifecycles and debugging production issues
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.StreamHandler()]
)

# Initialize the Flask application instance
# The __name__ argument allows Flask to locate resources (templates/static) relative to this file
app = Flask(__name__)

@app.route("/")
def home():
    """
    Handles the root endpoint request.
    Logs the invocation and returns a welcoming string.
    """
    logging.info("Endpoint '/' was accessed.")
    response = "Hello, Welcome to the course!"
    logging.info(f"Returning response: {response}")
    return response

if __name__ == "__main__":
    # Log the application startup event
    logging.info("Starting Flask development server on http://0.0.0.0:8000")
    
    try:
        # Run the server on all available network interfaces at the specified port
        # debug=False is implied; for local development, consider setting debug=True
        app.run(host="0.0.0.0", port=8000)
    except Exception as e:
        # Capture and log any critical failures during application startup
        logging.critical(f"Application failed to start: {e}")
    finally:
        logging.info("Flask application process terminated.")