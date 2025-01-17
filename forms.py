from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class QuestionForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired()])
    question = TextAreaField(label="Question", validators=[DataRequired()])
    submit = SubmitField(label="Submit")
