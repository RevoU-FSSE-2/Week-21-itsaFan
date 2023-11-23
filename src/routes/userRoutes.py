from flask import Blueprint, jsonify
from utils.decode_jwt import get_user_id_from_token
from services.user_service import get_user_profile

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/user/me', methods=['GET'])
def user_profile():
    user_id, error, status = get_user_id_from_token()
    if error:
        return jsonify(error), status

    profile = get_user_profile(user_id)
    if not profile:
        return jsonify({"error": "User not found"}), 404

    return jsonify(profile), 200
