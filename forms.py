from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from app import creator


class AddTask(FlaskForm):
    title = StringField(validators=[DataRequired()])
    submit = SubmitField('Add')
    creator()


class EditTask(FlaskForm):
    title = StringField(validators=[DataRequired()])
    submit = SubmitField('Edit')
    creator()


class DeleteTask(FlaskForm):
    submit = SubmitField('Delete')


