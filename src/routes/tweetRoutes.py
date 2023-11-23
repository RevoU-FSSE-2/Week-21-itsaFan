from flask import Blueprint, request, jsonify, current_app
from utils.decode_jwt import get_user_id_from_token
from services.tweet_service import post_tweet

tweet_bp = Blueprint('tweet_bp', __name__)

@tweet_bp.route('/tweet', methods=['POST'])
def create_tweet():
    
    user_id, error, status = get_user_id_from_token()
    if error:
        return jsonify(error), status

    data = request.get_json()
    tweet_content = data.get('tweet')

    if not tweet_content or len(tweet_content) > 150:
        return jsonify({"error": "Invalid tweet content"}), 400

    tweet = post_tweet(user_id, tweet_content)
    return jsonify({"id": tweet.id, "tweet": tweet.tweet}), 201
