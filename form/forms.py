from flask_wtf import FlaskForm
from wtforms import SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange

class InputFeatures(FlaskForm):
    median_age = FloatField('Median Age', validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField('Submit form')
