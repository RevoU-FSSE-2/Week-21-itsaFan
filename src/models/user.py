from extensions import db
from models.user_follow import UserFollow

class User(db.Model):
    
    # Fields
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    bio = db.Column(db.String(200))
    
    # Asociation follow
    followed = db.relationship(
        'UserFollow',
        foreign_keys=[UserFollow.follower_id],
        backref=db.backref('follower', lazy='joined'),
        lazy='dynamic',
        cascade='all, delete-orphan'
    )
    followers = db.relationship(
        'UserFollow',
        foreign_keys=[UserFollow.followed_id],
        backref=db.backref('followed', lazy='joined'),
        lazy='dynamic',
        cascade='all, delete-orphan'
    )
    
    
    # Relationship buat role
    permission_id = db.Column(db.Integer, db.ForeignKey('permission.id'), nullable=False)
    permission = db.relationship('Permission')

    def __repr__(self):
        return f'<User {self.username}>'
