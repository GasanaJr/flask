from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from marketPackage.models import User


class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError(
                'Username already exists, Please try another one')

    def validate_email(self, email_to_check):
        user = User.query.filter_by(email_address=email_to_check.data).first()
        if user:
            raise ValidationError(
                'Email address already exists, Try a different one')

    username = StringField(label='Username', validators=[
                           Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address', validators=[
                                Email(), DataRequired()])
    password1 = PasswordField(label='Password', validators=[
                              Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password',
                              validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    email_address = StringField(label="Email Address")
    password = PasswordField(label="Password")
    submit = SubmitField(label="Login")
