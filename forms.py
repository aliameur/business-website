from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    name = StringField('My name is', [DataRequired()], render_kw={'placeholder': 'Full Name'})
    email = StringField('My email', [Email()], render_kw={'placeholder': 'name@example.com'})
    message = TextAreaField('Your message', [DataRequired()],
                            render_kw={'placeholder': 'I want to say that...', 'rows': 5})
