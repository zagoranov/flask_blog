from wtforms import PasswordField, SubmitField, StringField, IntegerField, SelectField, TextAreaField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Optional, NumberRange, IPAddress, Regexp
from flask_wtf import FlaskForm
from .models import Project
from flask_login import current_user

def project_query():
    return Project.query.filter(Project.user_id == current_user.id)

class ProjectForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()], render_kw={"placeholder": "Title"})
    description = StringField('Description', validators=[DataRequired()], render_kw={"placeholder": "Description"})
    submit = SubmitField('Save')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()], render_kw={"placeholder": "Title"})
    posttext = TextAreaField('Text', render_kw={"placeholder": "Text"})
    project_id = QuerySelectField(query_factory=project_query, allow_blank=False)
    visibility = SelectField('Visibility', coerce=int, choices=[(0, 'Открытый пост'), (1, 'Только подписчики'), (2, 'Только автор')])
    submit = SubmitField('Save')

class CommentForm(FlaskForm):
    content = TextAreaField('Comment', render_kw={"placeholder": "Comment"})
    submit = SubmitField('Save')

class UserForm(FlaskForm):
    name = StringField('Name', render_kw={"placeholder": "Name"})
    submit = SubmitField('Save')