from flask import Blueprint, render_template, request
from extensions import db
from models.blog import Blog
from app import get_current_year


blog_blueprint = Blueprint("blog", __name__, template_folder="templates")


@blog_blueprint.route("/blog")
def blog():
    """
    View method to render the blog.html page - https://www.abhishekpednekar.com/blog

    Returns
    -------
    blog.html: html / jinja2 template
    """
    page = request.args.get("page", 1, type=int)
    blogs = (
        db.session.query(Blog.id, Blog.title, Blog.url, Blog.description)
        .order_by(Blog.id.desc())
        .paginate(page=page, per_page=4)
    )
    return render_template(
        "blog.html", title="Blog", blogs=blogs, year=get_current_year()
    )
