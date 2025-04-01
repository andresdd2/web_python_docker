from flask import Flask, jsonify, request
from config import get_connection
from models import User

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Api Flask con Python"})

@app.route('/users', methods=["GET"])
def get_users():
    try:
        conn = get_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM users")
            user = cursor.fetchall()
            return jsonify({"users": user})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)