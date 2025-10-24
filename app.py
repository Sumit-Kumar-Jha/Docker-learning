# Import the Flask class from the flask library to create a web application.
from flask import Flask
# Import the logging module to enable logging for the application.
import logging

# Configure basic logging to output informational messages.
# This will help in debugging and monitoring the application's flow.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create an instance of the Flask class.
# __name__ is a special Python variable that gets the name of the current module.
# Flask uses this to know where to look for resources like templates and static files.
app = Flask(__name__)
logging.info("Flask application created.")

# Define a route for the root URL ("/").
# The @app.route() decorator tells Flask what URL should trigger our function.
@app.route("/")
def home():
    """
    This function handles requests to the root URL and returns a welcome message.
    """
    logging.info("Request received for the home page ('/').")
    try:
        # The response to be sent to the client.
        response_message = "Hello, Welcome to the course!"
        logging.info(f"Successfully prepared response: '{response_message}'")
        return response_message
    except Exception as e:
        # Log any unexpected errors that occur during request handling.
        logging.error(f"An error occurred while handling the request for '/': {e}", exc_info=True)
        # Return a generic error message to the client.
        return "An internal server error occurred.", 500

# This block checks if the script is being run directly (not imported).
# It's the standard entry point for running a Flask application.
if __name__ == "__main__":
    # Start the Flask development server.
    # host="0.0.0.0" makes the server publicly available on the machine's IP address.
    # port=8000 specifies the port number to run the server on.
    logging.info("Starting Flask development server on host 0.0.0.0, port 8000.")
    app.run(host="0.0.0.0", port=8000)