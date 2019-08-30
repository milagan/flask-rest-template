import json

from flask_sqlalchemy import SQLAlchemy

from main.settings import app

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        book_object = {
            'username': self.username,
            'password': self.password
        }
        return json.dumps(book_object)

    @staticmethod
    def username_password_match(_username, _password):
        user = User.query.filter_by(username=_username).filter_by(password=_password).first()
        if user is None:
            return False
        else:
            return True

    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def create_user(_username, _password):
        new_user = User(username=_username, password=_password)
        db.session.add(new_user)
        db.session.commit()
        return True

    @staticmethod
    def delete_user(_username):
        is_successful = User.query.filter_by(username=_username).delete()
        db.session.commit()
        return bool(is_successful)
