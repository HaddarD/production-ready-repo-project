import os
from flask import Flask
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    return f"Hello from {os.getenv('SERVICE_NAME')}!"

if __name__ == "__main__":
    port = os.getenv("SERVICE_PORT")

    if port is None:
        raise ValueError("SERVICE_PORT is not set in the .env file")

    app.run(host="0.0.0.0", port=int(port))

