from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('name', validators=[DataRequired()])
    phone = StringField('name', validators=[DataRequired()])
    message = StringField('name', validators=[DataRequired()])