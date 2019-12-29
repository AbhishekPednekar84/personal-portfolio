from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class Search(FlaskForm):
    search_post = StringField("Search Post", validators=[DataRequired()])
    submit = SubmitField("Search")

    def __repr__(self):
        return f"Search(Search Post: {self.search_post})"
