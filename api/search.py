import string
from flask import request, abort, Blueprint
from flask_restplus import Api, Resource, fields
from extensions import db
from models.blog import Blog
from sqlalchemy.exc import ProgrammingError, OperationalError

search_blueprint = Blueprint("search_api", __name__)

api = Api(
    search_blueprint,
    doc="/apidoc",
    title="Code Disciples Search API",
    description="API endpoints to search posts listed on CodeDisciples.in",
    default="Code Disciples Blog Search - ",
    default_label="Search blog posts on CodeDisciples.in",
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
        """
        Get method to return a blog post by the id column in the blog model

        Example - https://www.abhishekpednekar.com/api/search/1

        Returns
        -------
        blog: dict

        Raises
        ------
        HTTP 400: Bad request
        """
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
        """
        Get method to return all the blog posts blog model

        URL: https://www.abhishekpednekar.com/api/search_all/

        Returns
        -------
        blog: dict

        Raises
        ------
        HTTP 404: Articles not found
        """
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
        """
        Get method to perform a full text search based on the description_token column in the blog model

        Example - https://www.abhishekpednekar.com/api/search?q=Python

        Returns
        -------
        blog: dict

        Raises
        ------
        HTTP 400: Bad request
        """
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
