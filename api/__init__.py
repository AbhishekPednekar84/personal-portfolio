from flask_restplus import Api
from .search import api as ns

api = Api(
    doc="/apidoc",
    title="Code Disciples Search API",
    description="API endpoints to search posts listed on CodeDisciples.in",
)


api.add_namespace(ns, path="/api")
