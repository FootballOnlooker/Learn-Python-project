from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app.db import db
from app.headphones.models import Headphone


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(120), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(10), index=True)
   # user_choice_id = db.Column(db.Integer, db.ForeignKey('user_choices.id'))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.email)

    @property
    def is_admin(self):
        return self.role == 'admin'

    def __repr__(self):
        return '<User name={} id={}>'.format(self.username, self.id)


"""
class UserChoice(db.Model):
     __tablename__ = 'user_choices'
     
    id = db.Column(db.Integer, primary_key=True)
    headphone_id = db.Column(db.Integer, db.ForeignKey('headphones.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<User_choice {}>'.format(self.email)
"""