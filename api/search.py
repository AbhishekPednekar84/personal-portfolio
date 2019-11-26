import string
from flask import request, abort
from flask_restplus import Namespace, Resource, fields
from extensions import db
from models.blog import Blog
from sqlalchemy.exc import ProgrammingError, OperationalError

# search_blueprint = Blueprint("search_api",
#                              __name__,
#                              url_prefix="/api")

api = Namespace(
    "Code Disciples Blog Search - ",
    description="Search blog posts on CodeDisciples.in",
)

model = api.model(
    "SearchModel",
    {
        "title": fields.String,
        "url": fields.String,
        "description": fields.String,
    },
)

# Search blog post by id
@api.route("/search/<int:id>")
class Search(Resource):
    @api.marshal_with(model, envelope="blog_posts")
    def get(self, id):

        try:
            result = Blog.query.get(id)

            return (
                {
                    "title": result.title,
                    "url": result.url,
                    "description": result.description,
                },
                200,
            )
        except Exception:
            abort(400, "Sorry! But that article does not exist yet")


# Search all posts
@api.route("/search_all/")
class SearchAll(Resource):
    @api.marshal_with(model)
    def get(self):
        blog_results = []

        try:
            results = Blog.query.all()

            for result in results:
                blog_results.append(result)

            return blog_results, 200
        except Exception:
            abort(404)


# Search by keyword
@api.route("/search")
class SearchAll(Resource):
    @api.marshal_with(model)
    @api.param("q", "A keyword to search with (Ex: Python, Python-Docker)")
    def get(self):
        blog_results = []
        q = str(request.args.get("q", type=str))

        special_chars = set(string.punctuation.replace("&", " "))

        if not q.isalnum():
            for char_ in special_chars:
                if char_ in q:
                    q = q.replace(char_, "|")
        else:
            q = q + ":*"

        try:
            results = db.session.query(Blog).filter(
                Blog.description_token.match(q)
            )

            for result in results:
                blog_results.append(result)

            return blog_results

        except ProgrammingError:
            abort(
                400,
                "Sorry! You sent a request that the API could not understand",
            )
        except OperationalError:
            abort(
                400,
                "Sorry! You sent a request that the API could not understand",
            )
