from extensions import db
from sqlalchemy.dialects.postgresql import TSVECTOR


class Blog(db.Model):
    __tablename__ = "blog"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    url = db.Column(db.String(100))
    description = db.Column(db.String(1000))
    description_token = db.Column(TSVECTOR)

    def __repr__(self):
        return f"Blog({self.id}, {self.title}, {self.url}, {self.description})"
