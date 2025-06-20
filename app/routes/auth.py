
from flask import Blueprint, request, jsonify
from app.models.user import User
from werkzeug.security import check_password_hash
from app.schemas.user import (
    UserCreateSchema, UserResponseSchema
)
from app.utils.response import success_response
from app.services.auth_service import (
    create_user,
    generate_token
)

auth_bp = Blueprint("auth", __name__)
auth_schema = UserCreateSchema()
auth_response_schema = UserResponseSchema()

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(email=data.get("email")).first()
    if user and check_password_hash(user.password, data.get("password")):
        token = generate_token(user.id)
        return jsonify({"token": token})
    return jsonify({"message": "Invalid credentials"}), 401


@auth_bp.route("/register", methods=["POST"])
def register():
    user_data = auth_schema.load(request.json)
    user = create_user(user_data)
    return success_response(auth_response_schema.dump(user), "User created")
