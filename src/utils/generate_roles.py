from models.permission import Permission, db

def initialize_roles():
    for role_name in ['ROLE_USER', 'ROLE_ADMIN']:
        if not Permission.query.filter_by(name=role_name).first():
            role = Permission(name=role_name)
            db.session.add(role)
    db.session.commit()
