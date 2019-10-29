from flask_login import UserMixin
from web_app import db


class User(UserMixin, db.Model):
    __tablename__ = "User"
    id = db.Column('id', db.Integer, primary_key=True, nullable=False)
    login = db.Column('login', db.Unicode, nullable=False)
    password = db.Column('password', db.Unicode, nullable=False)
    name = db.Column('name', db.Unicode, nullable=False)
    lastname = db.Column('lastname', db.Unicode, nullable=False)

    def __repr__(self):
        return f"User('{self.id}','{self.login}','{self.password}','{self.name}','{self.lastname}')"
