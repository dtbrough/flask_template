
from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField


class LoginForm(FlaskForm):
    username = TextField('username')
    password = PasswordField('password')


class Form2(FlaskForm):
    username = TextField('username')
    password = PasswordField('password')
