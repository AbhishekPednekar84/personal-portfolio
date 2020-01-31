from flask import Blueprint, send_from_directory

sitemap_blueprint = Blueprint("sitemap", __name__)


@sitemap_blueprint.route("/sitemap.xml")
def sitemap_xml():
    return send_from_directory(directory="static", filename="sitemap.xml")
