from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Temporary in-memory data storage
users = {}


@app.route("/")
def home():
    return ("Welcome to the Flask API!")


@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)

    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """ add a new user to the dict """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get('username')
    print(f"User name: {username}")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username is users:
        return jsonify({"error": "Username already exists"}), 400

    users[username] = data

    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5000)
