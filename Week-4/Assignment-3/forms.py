from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.fields import EmailField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    username = StringField('UserName', validators=[DataRequired(message='Not Null')])
    email = EmailField('Email', validators=[DataRequired(message='Not Null'),Email()])
    password = PasswordField('Password', validators=[DataRequired(message='Not Null')])
    submit = SubmitField('Submit')

class RegisterForm(FlaskForm):
    username = StringField('UserName', validators=[DataRequired(message='Not Null')])
    email = EmailField('Email', validators=[DataRequired(message='Not Null'),Email()])
    password = PasswordField('Password', validators=[DataRequired(message='Not Null')])
    password_confirm = PasswordField('Confirm Password', validators=[DataRequired(message='Not Null')])
    submit = SubmitField('Submit')