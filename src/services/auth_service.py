from models.user import db, User
from models.permission import Permission
from extensions import bcrypt
from sqlalchemy.exc import IntegrityError
import jwt
import datetime
from flask import current_app


# Register
def register_user(username, password, bio):
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return {"error": "Username already exists"}

    pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    default_role = Permission.query.filter_by(name='ROLE_USER').first()
    new_user = User(username=username, password=pw_hash, bio=bio, permission=default_role)

    try:
        db.session.add(new_user)
        db.session.commit()
        return new_user
    except IntegrityError:
        db.session.rollback()
        return {"error": "Database error occurred"}

# Login 
def login_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=8),
            'iat': datetime.datetime.utcnow(),
            'userId': user.id,
            'username': user.username,
            'bio': user.bio,
            'role': user.permission.name
        }
        token = jwt.encode(payload, current_app.config.get('SECRET_KEY'), algorithm='HS256')
        return token
    return None