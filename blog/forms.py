from wtforms import PasswordField, SubmitField, StringField, IntegerField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Optional, NumberRange, IPAddress, Regexp
from flask_wtf import FlaskForm

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()], render_kw={"placeholder": "Title"})
    posttext = TextAreaField('Text', render_kw={"placeholder": "Text"})
    submit = SubmitField('Save')

class CommentForm(FlaskForm):
    content = TextAreaField('Comment', render_kw={"placeholder": "Comment"})
    submit = SubmitField('Save')