from extensions import db

class UserFollow(db.Model):
    follower_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    followed_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

    def __repr__(self):
        return f'<UserFollow follower={self.follower_id} followed={self.followed_id}>'