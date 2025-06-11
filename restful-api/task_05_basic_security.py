from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    jwt_required,
    create_access_token,
    get_jwt_identity,
    get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# JWT Configuration
app.config['JWT_SECRET_KEY'] = 'your-secret-string'

# Initialize extensions
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# User database - EXACTLY as specified
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

# Basic Auth verification
@auth.verify_password
def verify_password(username, password):
    if username in users:
        user = users[username]
        if check_password_hash(user['password'], password):
            return username
    return False

# JWT Error handlers - ALL must return 401
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

# Routes - EXACT specification match
@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """Returns exactly: Basic Auth: Access Granted"""
    return "Basic Auth: Access Granted"

@app.route('/login', methods=['POST'])
def login():
    """Login endpoint that returns JWT token"""
    data = request.get_json()

    if not data or not data.get('username') or not data.get('password'):
        return jsonify({"error": "Username and password required"}), 400

    username = data.get('username')
    password = data.get('password')

    if username in users:
        user = users[username]
        if check_password_hash(user['password'], password):
            # Create token with user info
            additional_claims = {
                "role": user['role'],
                "username": username
            }
            access_token = create_access_token(
                identity=username,
                additional_claims=additional_claims
            )
            return jsonify({"access_token": access_token})

    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """Returns exactly: JWT Auth: Access Granted"""
    return "JWT Auth: Access Granted"

@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """Admin only route - returns exactly specified messages"""
    claims = get_jwt()
    user_role = claims.get('role')

    if user_role != 'admin':
        # EXACT error message as specified
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"

if __name__ == '__main__':
    app.run(debug=True)
