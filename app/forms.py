from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField,
                     BooleanField, SubmitField, TextAreaField)
from wtforms.validators import (ValidationError, DataRequired,
                                Length, Email, EqualTo, Regexp)
from app.models import User


class LoginForm(FlaskForm):
    username_or_email = StringField('Username or Email', validators=[
        DataRequired(), Length(max=64)])
    password = PasswordField('Password', validators=[
        DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
        
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(), Length(min=-1, max=64),
        Regexp('^[A-Za-z0-9_.]*$',
            message='Username can contain only letters, numbers, dots or underscores.')])
    email = StringField('Email', validators=[
        DataRequired(), Length(max=128),
        Email()])
    password = PasswordField('Password', validators=[
        DataRequired(), Length(min=8, max=64)])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(), EqualTo('confirm_password',
            message='Passwords do not match.')])
    submit = SubmitField('Register')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data.lower()).first()
        if user is not None:
            raise ValidationError('This username is taken. Please choose another one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data.lower()).first()
        if user is not None:
            raise ValidationError('There is an accout associated with this email already.')

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(), Length(min=-1, max=64),
        Regexp('^[A-Za-z0-9_.]*$',
            message='Username can contain only letters, numbers, dots or underscores.')])
    bio = TextAreaField('About Me', validators=[Length(max=128)])
    submit = SubmitField('Submit')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data.lower()).first()
            if user is not None:
                raise ValidationError('This username already exists. Please choose another one.')

class PostForm(FlaskForm):
    post = TextAreaField('Say something', validators=[
        DataRequired(), Length(min=1, max=256)])
    submit = SubmitField('Submit')

                
