from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth", __name__)

# Example hardcoded users
USERS = {
    "admin": "password123"
}

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if USERS.get(username) == password:
        token = create_access_token(identity=username)
        return jsonify(access_token=token), 200
    else:
        return jsonify(msg="Bad username or password"), 401

