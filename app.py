from flask import Flask

print("[INFO] Application script started.")

app = Flask(__name__)
print(f"[INFO] Flask application initialized with name: '{__name__}'")

@app.route("/")
def home():
    print("[INFO] Entering function: 'home'")
    response_message = "Hello, Welcome to the course!"
    print(f"[INFO] 'home' function preparing to return: '{response_message}'")
    return response_message
    print("[INFO] Exiting function: 'home' (This line may not be reached if return is executed)")

if __name__ == "__main__":
    print("[INFO] Running application in main block.")
    host_address = "0.0.0.0"
    port_number = 8000
    print(f"[INFO] Starting Flask server on http://{host_address}:{port_number}")
    app.run(host=host_address, port=port_number)
    print("[INFO] Flask server stopped.")