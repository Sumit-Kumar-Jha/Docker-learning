"""
File: app.py
Purpose: A simple Flask web application serving a welcome message.
Usage: Run 'python app.py' to start the development server on port 8000.
Dependencies: flask
"""

import logging
from flask import Flask

# Configure logging to capture execution flow and status updates
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route("/")
def home():
    """
    Handles the root URL request.

    Returns:
        str: A welcome message for the user.
    """
    logger.info("Received request for the home route '/'")
    
    # Simple logic to return the static greeting
    # In a production environment, this could involve rendering templates or fetching DB data
    response_message = "Hello, Welcome to the course!"
    
    logger.debug(f"Returning response: {response_message}")
    return response_message

if __name__ == "__main__":
    """
    Entry point for the application.
    Configures the Flask server to run on the specified host and port.
    """
    try:
        logger.info("Starting Flask application on 0.0.0.0:8000")
        
        # Start the application server
        # host='0.0.0.0' makes the server accessible externally
        # port=8000 defines the specific listener port
        app.run(host="0.0.0.0", port=8000)
        
    except Exception as e:
        # Catch and log any initialization errors, such as port binding conflicts
        logger.error(f"Failed to start the application: {e}")