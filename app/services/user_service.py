from app import db
from app.models.user import User


def get_user(user_id):
    return User.query.get(user_id)


def create_user(username, email):
    new_user = User(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()
    return new_user
