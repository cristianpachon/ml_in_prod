from flask_wtf import FlaskForm
from wtforms import DecimalField, StringField, SubmitField

class InputFeatures(FlaskForm):
    username = StringField('Name')
    usersurname = StringField('Surname')
    submit = SubmitField('Submit')