from flask import Flask, jsonify, request

app = Flask(__name__)

# Temporary in-memory data storage
users = {
    "jane": {"username": "jane", "name": "Jane",
             "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John",
             "age": 30, "city": "New York"}
}


@app.route("/")
def home():
    return ("Welcome to the Flask API!")


@app.route("/data")
def get_data():
    return jsonify(list(users.values()))


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
    data = request.get_json()
    username = data.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "Duplicate username"}), 400

    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run(debug=True, port=5000)
