from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from app import creator


class AddTask(FlaskForm):
    title = StringField('write your info', validators=[DataRequired()])
    submit = SubmitField('Submit')
    creator()

