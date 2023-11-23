from extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    bio = db.Column(db.String(200))
    # Relationship
    permission_id = db.Column(db.Integer, db.ForeignKey('permission.id'), nullable=False)
    permission = db.relationship('Permission')

    def __repr__(self):
        return f'<User {self.username}>'
