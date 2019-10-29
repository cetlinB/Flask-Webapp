from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from web_app.config import Config

app = Flask(__name__, template_folder="static")
app.config.from_object(Config)

db = SQLAlchemy(app)

from web_app import webapp
from web_app.applogic import models
