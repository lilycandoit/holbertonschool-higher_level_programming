from flask import Flask, jsonify, request

app = Flask(__name__)

# Temporary in-memory data storage
users = {
    "jane": {"username": "jane", "name": "Jane",
             "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John",
             "age": 30, "city": "New York"}
}

def format_user(user_data):
    """Helper function to ensure consistent user data ordering"""
    return {
        "username": user_data.get("username"),
        "name": user_data.get("name"),
        "age": user_data.get("age"),
        "city": user_data.get("city")
    }


@app.route("/")
def home():
    return ("Welcome to the Flask API!")


@app.route("/data")
def get_data():
    # Format all users with consistent ordering
    formatted_users = [format_user(user) for user in users.values()]
    return jsonify(formatted_users)


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)

    if user:
        formatted = format_user(user)
        print(f"Original: {user}")
        print(f"Formatted: {formatted}")
        return jsonify(formatted)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """ add a new user to the dict """
    data = request.get_json()
    print(f"Parsed JSON: {data}")

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get('username')
    print(f"User name: {username}")
    
    if not username:
        return jsonify({"error": "Username is required"}), 400

    users[username] = data

    formatted_user = format_user(data)

    return jsonify({"message": "User added", "user": formatted_user}), 201


if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5000)
