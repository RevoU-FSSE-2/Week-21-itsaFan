from flask import Blueprint, request, jsonify
from utils.decode_jwt import get_user_id_from_token
from services.follow_service import follow_user, unfollow_user

follow_bp = Blueprint('follow_bp', __name__)

@follow_bp.route('/follow', methods=['POST'])
def follow():
    user_id, error, status = get_user_id_from_token()
    if error:
        return jsonify(error), status

    followed_id = request.json.get('followed_id')
    return jsonify(follow_user(user_id, followed_id))

@follow_bp.route('/unfollow', methods=['POST'])
def unfollow():
    user_id, error, status = get_user_id_from_token()
    if error:
        return jsonify(error), status

    followed_id = request.json.get('followed_id')
    return jsonify(unfollow_user(user_id, followed_id))