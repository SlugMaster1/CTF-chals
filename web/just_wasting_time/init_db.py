from os import urandom
from app import app, db, User

def init_db():
    with app.app_context():
        db.create_all()
        if not User.query.filter_by(username='admin').first():
            test_user = User(username='admin',jwt_algorithm='HS256')
            test_user.set_password(urandom(16).hex())
            db.session.add(test_user)
            db.session.commit()

if __name__ == '__main__':
    init_db()
