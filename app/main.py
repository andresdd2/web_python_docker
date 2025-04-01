from flask import Flask, jsonify, request
from config import get_connection
from models import User

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Api Flask con Python"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)