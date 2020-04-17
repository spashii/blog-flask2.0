from flask import render_template, url_for, flash, redirect
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/home')
def index():
    user = {'username': 'Sameer'}
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
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember me{form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=form)