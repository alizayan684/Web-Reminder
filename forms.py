from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask import FlaskFrom


class AddTask(FlaskFrom):
    title = StringField('Title', validators=[DataRequired()])
    submit = SubmitField('Submit')
