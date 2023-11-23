from flask import request, jsonify, Blueprint, make_response
from services.auth_service import register_user, login_user

auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    result = register_user(data['username'], data['password'], data['bio'])

    if isinstance(result, dict) and "error" in result:
        return jsonify(result), 400 

    return jsonify({'id': result.id, 'username': result.username}), 201  


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    token = login_user(data['username'], data['password'])

    if token:
        response = make_response(jsonify({"message": "Login Success!"}), 200)
        response.set_cookie('token', token, max_age=8*60*60)
        return response
    else:
        return jsonify({"error": "Invalid username or password"}), 401