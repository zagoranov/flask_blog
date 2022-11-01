from wtforms import PasswordField, SubmitField, StringField, IntegerField, SelectField
from wtforms.validators import DataRequired, Optional, NumberRange, IPAddress, Regexp
from flask_wtf import FlaskForm

class PostForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()], render_kw={"placeholder": "Заголовок"})
    content = StringField('Текст', validators=[DataRequired()], render_kw={"placeholder": "Текст"})
    submit = SubmitField('Записать')