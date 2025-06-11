# Flask JWT Authentication Tutorial - Complete Implementation
# File: task_05_basic_security.py

# ============================================================================
# STEP 1: IMPORTS AND SETUP
# ============================================================================

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

# ============================================================================
# STEP 2: CREATE FLASK APP AND CONFIGURE JWT
# ============================================================================

app = Flask(__name__)

# IMPORTANT: Use a strong secret key and change it in production!
app.config['JWT_SECRET_KEY'] = 'super-secret-string'

# Create instances
auth = HTTPBasicAuth()  # For Basic Authentication
jwt = JWTManager(app)   # For JWT Authentication

# ============================================================================
# STEP 3: USER DATABASE (In-Memory Storage)
# ============================================================================

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

# ============================================================================
# STEP 4: BASIC AUTHENTICATION SETUP
# ============================================================================


@auth.verify_password
def verify_password(username, password):
    if username in users:
        user = users[username]
        if check_password_hash(user['password'], password):
            return username  # Authentication successful
    return False  # Authentication failed

# ============================================================================
# STEP 5: JWT ERROR HANDLERS (VERY IMPORTANT!)
# ============================================================================


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Called when no JWT token is provided"""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Called when JWT token is malformed or invalid"""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Called when JWT token has expired"""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Called when JWT token has been revoked"""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Called when a fresh token is required but not provided"""
    return jsonify({"error": "Fresh token required"}), 401

# ============================================================================
# STEP 6: BASIC AUTHENTICATION ROUTES
# ============================================================================


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """
    This route requires HTTP Basic Authentication

    Test with:
    curl -u user1:password http://localhost:5000/basic-protected
    """
    return "Basic Auth: Access Granted"

# ============================================================================
# STEP 7: JWT AUTHENTICATION - LOGIN ROUTE
# ============================================================================


@app.route('/login', methods=['POST'])
def login():
    """
    Login endpoint that returns a JWT token

    Expected JSON payload:
    {
        "username": "user1",
        "password": "password"
    }

    Returns:
    {
        "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
    }
    """
    # Get JSON data from request
    data = request.get_json()

    # Validate input
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({"error": "Username and password required"}), 400

    username = data.get('username')
    password = data.get('password')

    # Check if user exists and password is correct
    if username in users:
        user = users[username]
        if check_password_hash(user['password'], password):
            # Create JWT token with user info embedded
            additional_claims = {
                "role": user['role'],
                "username": username
            }
            access_token = create_access_token(
                identity=username,
                additional_claims=additional_claims
            )
            return jsonify({"access_token": access_token})

    # Authentication failed
    return jsonify({"error": "Invalid credentials"}), 401

# ============================================================================
# STEP 8: JWT PROTECTED ROUTES
# ============================================================================


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """
    This route requires a valid JWT token

    Test with:
    curl -H "Authorization: Bearer YOUR_JWT_TOKEN"
    http://localhost:5000/jwt-protected
    """
    # get_jwt_identity() returns the username from the token
    current_user = get_jwt_identity()
    return "JWT Auth: Access Granted"

# ============================================================================
# STEP 9: ROLE-BASED ACCESS CONTROL
# ============================================================================


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """
    This route requires JWT token AND admin role

    Test with admin token:
    curl -H "Authorization: Bearer ADMIN_JWT_TOKEN"
    http://localhost:5000/admin-only
    """
    # Get the current JWT claims (includes our custom role)
    claims = get_jwt()
    user_role = claims.get('role')

    # Check if user has admin role
    if user_role != 'admin':
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


# ============================================================================
# STEP 11: RUN THE APPLICATION
# ============================================================================


if __name__ == '__main__':
    app.run(debug=True)
