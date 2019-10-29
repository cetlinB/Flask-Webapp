from sqlalchemy import func, desc, create_engine
from sqlalchemy_utils import database_exists, create_database
from web_app.applogic import models
from web_app import db


def get_all_users():
    users = models.User.query.all()
    return users


def get_all_usernames():
    users = models.User.query.all()
    usernames = []
    for user in users:
        usernames.append(user.name)
    return usernames


def get_all_logins():
    users = models.User.query.all()
    logins = []
    for user in users:
        logins.append(user.login)
    return logins


def get_user_by_login(login):
    user = models.User.query.filter_by(login=login).first()
    return user


def get_user_by_id(user_id):
    return models.User.query.get(int(user_id))


def check_username_exist(name):
    if models.User.query.filter_by(name=name).count()>0:
        return True
    else:
        return False


def check_username_exist(name):
    if models.User.query.filter_by(name=name).count() > 0:
        return True
    return False


def check_userlogin_exist(login):
    if models.User.query.filter_by(login=login).count() > 0:
        return True
    return False


def add_user(data, hashed_password):
    new_user = models.User(login=data['login'], name=data['name'], lastname=data['lastname'],
                           password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return 0
