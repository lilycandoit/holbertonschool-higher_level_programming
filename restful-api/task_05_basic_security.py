#!/usr/bin/python3
""" Nameless Module for Task 5 """

from flask import Flask, jsonify, request, abort
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "i-love-anime-and-video-games"
auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# 1st endpoint - no JWT needed
@auth.verify_password
def verify_password(username, password):
    # -- Usage example --
    # curl -X GET "http://localhost:5000/basic-protected" --user user1:password

    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return user

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# 2nd endpoint - returns JWT
@app.route("/login", methods=["POST"])
def login():
    """ login """
    # -- Usage example --
    # curl -X POST localhost:5000/login -H "Content-Type: application/json" -d '{"username":"user1","password":"password"}'

    if request.get_json() is None:
        abort(400, "Not a JSON")

    data = request.get_json()

    for k in ["username", "password"]:
        if k not in data:
            abort(400, "Missing attribute {}.".format(k))

    if data["username"] not in users or not check_password_hash(users[data["username"]]["password"], data["password"]):
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=data["username"])
    return jsonify({"access_token": access_token})


# 3rd endppoint - uses JWT
@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    # -- Usage example --
    # curl -X GET "http://localhost:5000/jwt-protected" -H "Authorization: Bearer <token_goes_here>"

    return "JWT Auth: Access Granted"

# 4th endpoint - uses JWT
@app.route("/admin-only")
@jwt_required()
def admin_only():
    """ Only for admin role users """
    # -- Usage example --
    # curl -X GET "http://localhost:5000/admin-only" -H "Authorization: Bearer <token_goes_here>"
    # NOTE: the token you use must be from a logged-in 'admin' user

    current_user = get_jwt_identity()

    if current_user not in users or users[current_user]["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


# Custom error handlers for JWT errors
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == "__main__":
    # app.run(host='localhost', port=5000, debug=True)
    app.run()