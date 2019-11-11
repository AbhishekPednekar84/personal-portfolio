from extensions import db


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    url = db.Column(db.String(100))
    description = db.Column(db.String(1000))

    def __repr__(self):
        return f"Blog({self.id}, {self.title}, {self.url}, {self.description})"
