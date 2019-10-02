
from my_app import app
from models import Table1, Table2
from forms import LoginForm, Form2
from flask import render_template


@app.route('/')
def index():
    return '<h1>This is HTML</h1>'


@app.route('/login')
def login():
    form = LoginForm()  # initialise forms
    return render_template('index.html', form=form)  # pass form to template
