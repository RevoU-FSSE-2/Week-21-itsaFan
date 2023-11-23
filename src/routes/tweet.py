from flask import Blueprint, request, jsonify, current_app
import jwt
from services.tweet_service import post_tweet

tweet_bp = Blueprint('tweet_bp', __name__)

@tweet_bp.route('/tweet', methods=['POST'])
def create_tweet():
    
    token = request.cookies.get('token')
    if not token:
        return jsonify({"error": "Authentication required"}), 401

    try:
        payload = jwt.decode(token, current_app.config.get('SECRET_KEY'), algorithms=['HS256'])
        user_id = payload['userId']
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Expired token. Please log in again."}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token. Please log in again."}), 401

    data = request.get_json()
    tweet_content = data.get('tweet')


    if not tweet_content or len(tweet_content) > 150:
        return jsonify({"error": "Invalid tweet content"}), 400

    tweet = post_tweet(user_id, tweet_content)
    return jsonify({"id": tweet.id, "tweet": tweet.tweet}), 201
