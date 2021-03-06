
#comminications forms.py: messages, notifications, reflections, todos

from flask import request
from flask_wtf import FlaskForm
from wtforms import Form
from wtforms.fields import *
from wtforms_components import StringField, SelectField, DateField
from wtforms.validators import ValidationError, DataRequired, Length
from flask_babel import _, lazy_gettext as _l
from app.models import User
import calendar

#This form is for entering new reflections ("posts").
class PostForm(FlaskForm):
    post = TextAreaField(_l('Write a reflection.'), validators=[DataRequired()])
    submit = SubmitField(_l('Submit'))

#This form enables users to manually create tasks for the todo list.
class TaskForm(FlaskForm):
    name = TextAreaField(_l(u'Task Name'), validators=[DataRequired()])
    priority = SelectField(_l('Priority'), choices=[('high', 'high'), ('medium', 'medium'), ('low', 'low')], validators=[DataRequired()])
    due_date = DateField(_l('Due Date', format='%Y-%m-%d'))
    description = TextAreaField(_l('Description'))
    done = SelectField(u'Complete?', choices=[('no', 'No'), ('yes', 'Yes'),])
    submit = SubmitField(_l('Submit'))

#This form is to create a message. 
class MessageForm(FlaskForm):
    message = TextAreaField(_l('Message'), validators=[DataRequired(), Length(min=1, max=140)])
    submit = SubmitField(_l('Submit'))