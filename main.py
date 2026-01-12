from flask import Flask, jsonify
from flask_cors import CORS # Import CORS
import os

app = Flask(__name__)
CORS(app) # This allows your React app to talk to this API

@app.route("/search")
def search():
    return jsonify({"status": "success", "message": "Flight search active"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
