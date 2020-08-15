from flask_wtf import FlaskForm
from wtforms import DecimalField, StringField, SubmitField
from wtforms.validators import DataRequired, Length

class InputFeatures(FlaskForm):
    username = StringField('Name', validators = [DataRequired(), Length(min=7)])
    usersurname = StringField('Surname')
    submit = SubmitField('Submit')