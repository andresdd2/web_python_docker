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


@app.route("/users", methods=["POST"])
def create_user():
    try:
        data = request.json
        user = User(data['name'], data['email'])

        conn = get_connection()
        with conn.cursor() as cursor:
            sql = "INSERT INTO users(name, email) VALUES (%s, %s);"
            cursor.execute(sql, (user.name, user.email))
            conn.commit()
        return jsonify({"message": "Usuario creado con exito"}), 201
    except Exception as e:
        return jsonify({"message": str(e)})
    finally:
        conn.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)