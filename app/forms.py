from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField,
                     BooleanField, SubmitField)
from wtforms.validators import (ValidationError, DataRequired,
                                Length, Email, EqualTo)
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
                           DataRequired(), Length(min=-1, max=64)])
    email = StringField('Email', validators=[
                        DataRequired(), Email(), Length(max=128)])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=8, max=64)])
    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(), EqualTo('confirm_password', message='Passwords do not match.')])
    submit = SubmitField('Register')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('This username is taken. Please choose another one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('There is an accout associated with this email already.')
