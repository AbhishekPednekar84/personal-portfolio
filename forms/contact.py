from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email


class ContactForm(FlaskForm):
    username = StringField(
        "Your Name", validators=[DataRequired(), Length(min=2, max=25)]
    )
    email = StringField("Your Email", validators=[DataRequired(), Email()])
    subject = StringField(
        "Subject", validators=[DataRequired(), Length(min=2, max=20)]
    )
    message = TextAreaField("Your Message", validators=[DataRequired()])
    submit = SubmitField("SEND")

    def __repr__(self):
        return f"<Name: {self.username} - Email: {self.email} - Subject: {self.subject}>"
