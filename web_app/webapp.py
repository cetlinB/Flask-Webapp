from flask import Flask, render_template, request
from flask_login import LoginManager
from web_app.applogic import database_provider
from web_app import app
import json

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


#@login_manager.user_loader
#def load_user(user_id):
#    return database_provider.get_user_by_id(user_id)


@app.route('/')
@app.route('/index', methods={'GET'})
def main_page():
    return render_template("index.html")


@app.route('/form/data', methods={'POST'})
def get_data_form():
    if request.method == 'POST':
        form_data = request.json
        database_provider.add_user({
            'login': form_data['login'],
            'name': form_data['name'],
            'lastname': form_data['lastname']
        }, form_data['passwd'])
    return "200 OK"


@app.route('/form/validate/login/<string:login>')
def validate_name(login):
    valid = not database_provider.check_userlogin_exist(login)
    if valid:
        return "valid"
    return "not"


@app.route('/register')
def register_page():
    return render_template("register.html")

@app.route('/login', methods={'GET','POST'})
def login_page():
    if request.method == 'GET':
        return render_template("login.html")
    elif request.method == 'POST':
        print(request.json)
    else:
        return "500 Not Implemented"

@app.route('/get_all_users')
def get_all_users():
    users = database_provider.get_all_users()
    json_data = json.dumps({'users':users})
    return json_data


@app.route('/get_all_users/names')
def get_all_usernames():
    users = database_provider.get_all_usernames()
    json_data = json.dumps({'names':users})
    return json_data


@app.route('/get_all_users/logins')
def get_all_logins():
    users = database_provider.get_all_logins()
    json_data = json.dumps({'logins':users})
    return json_data


if __name__ == '__main__':
    app.run()
