from flask import render_template, url_for, flash, redirect
from app import app
from app.forms import LoginForm
from app.models import User
from flask_login import current_user, login_user, logout_user, login_required


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
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        else:
            login_user(user, remember=form.remember_me.data)
            flash(f'Login requested for user {form.username.data}, remember me{form.remember_me.data}')
            return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=form)

@app.route('/logout') 
def logout():
    logout_user()
    return redirect(url_for('index'))