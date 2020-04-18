from flask import render_template, url_for, flash, redirect, request
from app import app
from app.forms import LoginForm
from app.models import User
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse


@app.route('/')
@app.route('/home')
@login_required
def index():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful say in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'I have a cool handbag.'
        }
    ]
    return render_template('index.html', title='Home', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        next_page = request.args.get('next')
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            if not next_page or url_parse(next_page).netloc != '':
                return redirect(url_for('login'))
            return redirect(url_for('login', next=next_page))
        login_user(user, remember=form.remember_me.data)
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Login', form=form)

@app.route('/logout') 
def logout():
    logout_user()
    return redirect(url_for('index'))
