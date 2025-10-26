# Import the Flask class from the flask package.
# Flask is a lightweight WSGI web application framework. It is designed to make getting started with web development quick and easy, with the ability to scale up to complex applications.
# The `Flask` class itself is the central object that represents your web application.
from flask import Flask

# Create an instance of the Flask class. This is your WSGI application.
# The first argument, `__name__`, is a special Python variable that gets the name of the current module.
# Flask uses this to determine the root path of the application so it can find resources like templates and static files relative to the module's location.
# This `app` object will handle all incoming web requests and route them to the appropriate functions.
app = Flask(__name__)

# This is a decorator provided by Flask that associates a URL path with a specific function.
# When a web browser requests the root URL ("/") of your application, Flask will execute the function defined immediately after this decorator.
# The "/" path typically represents the main page or homepage of a website.
@app.route("/")
# Define a Python function named `home`. This is often referred to as a "view function" or "route handler".
# View functions are responsible for handling requests to a particular URL and returning the data to be displayed in the browser.
def home():
    # This line returns a simple string. In Flask, whatever a view function returns is sent back to the client
    # (e.g., a web browser) as the HTTP response body.
    # Flask automatically wraps this string in an HTTP response object with a default status code of 200 OK
    # and a 'Content-Type' header of 'text/html; charset=utf-8'.
    return "Hello, Welcome to the course!"

# This is a standard Python idiom that checks if the script is being run directly (as opposed to being imported as a module into another script).
# If the script is executed directly, `__name__` will be set to "__main__".
# This ensures that the Flask development server only starts when you explicitly run this file.
if __name__ == "__main__":
    # Start the Flask development server. This method runs the application on a local server.
    # `debug=True` is often used during development to automatically reload the server on code changes
    # and provide a debugger in the browser, though it's omitted here for simplicity.
    # `host="0.0.0.0"` makes the server publicly available on your network interface.
    # If you used "127.0.0.1" (localhost), it would only be accessible from the machine running the server.
    # "0.0.0.0" is essential for deploying in environments like Docker containers or when you want to access
    # the server from other devices on your local network.
    # `port=8000` specifies the port number on which the server will listen for incoming HTTP requests.
    # You can access the application by navigating to `http://<your-server-ip>:8000/` in a web browser.
    app.run(host="0.0.0.0", port=8000)