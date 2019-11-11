from flask import Blueprint, render_template
from extensions import db
from models.blog import Blog


blog_blueprint = Blueprint("blog", __name__, template_folder="templates")


@blog_blueprint.route("/blog")
def blog():

    blogs = db.session.query(
        Blog.id,
        Blog.title,
        Blog.url,
        Blog.description
    ).order_by(Blog.id.desc()).all()
    return render_template("blog.html", title='Blog', blogs=blogs)
