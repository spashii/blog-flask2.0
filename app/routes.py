from flask import render_template, url_for
from app import app


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
