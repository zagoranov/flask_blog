from wtforms import PasswordField, SubmitField, StringField, IntegerField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Optional, NumberRange, IPAddress, Regexp
from flask_wtf import FlaskForm

class PostForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()], render_kw={"placeholder": "Заголовок"})
    posttext = TextAreaField('Текст', render_kw={"placeholder": "Текст"})
    submit = SubmitField('Записать')

class CommentForm(FlaskForm):
    content = TextAreaField('Комментарий', render_kw={"placeholder": "Комментарий"})
    submit = SubmitField('Записать')