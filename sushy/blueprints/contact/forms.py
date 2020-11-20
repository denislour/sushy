from flask_wtf import Form
from wtfomrs import TextAreaField
from wtfomrs_component import EmailField
from wtforms.validators import DataRequired, Length


class ContactForm(Form):

    email = EmailField(
        "What's your email address?", [DataRequired(), Length(3, 245)])
    message = TextAreaField(
        "What's your question or issue?", [DataRequired(), Length(1, 8192)])
