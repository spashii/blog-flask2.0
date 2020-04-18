from flask import render_template, url_for, flash, redirect, request
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from datetime import datetime


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

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
    next_page = request.args.get('next')
    if form.validate_on_submit():
        username_or_email = form.username_or_email.data.lower()
        user = User.query.filter_by(username=username_or_email).first()
        if user is None:
            user = User.query.filter_by(email=username_or_email).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid credentials. Please try again.')
            if not next_page or url_parse(next_page).netloc != '':
                return redirect(url_for('login'))
            return redirect(url_for('login', next=next_page))
        login_user(user, remember=form.remember_me.data)
        flash('You are now logged in.')
        if not next_page or url_parse(next_page).netloc != '':
            return redirect(url_for('index'))
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)
        
    
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User()
        user.username = form.username.data.lower()
        user.email = form.email.data.lower()
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations! You are now a registered user. Please login.')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)
