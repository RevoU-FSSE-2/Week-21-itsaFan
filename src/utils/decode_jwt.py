from flask import request, current_app
import jwt

def get_user_id_from_token():
    token = request.cookies.get('token')
    if not token:
        return None, {"error": "Authentication required"}, 401

    try:
        payload = jwt.decode(token, current_app.config.get('SECRET_KEY'), algorithms=['HS256'])
        return payload['userId'], None, 200
    except jwt.ExpiredSignatureError:
        return None, {"error": "Expired token. Please log in again."}, 401
    except jwt.InvalidTokenError:
        return None, {"error": "Invalid token. Please log in again."}, 401