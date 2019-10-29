from sqlalchemy import func, desc, create_engine
from sqlalchemy_utils import database_exists, create_database
from web_app.config import Config


def make_new_database():
    engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
    if not database_exists(engine.url):
        create_database(engine.url)

def create_user_table():
    engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
    print(engine.has_table('User'))


create_user_table()
