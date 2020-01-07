from flask import Blueprint, render_template

main_blueprint = Blueprint("main", __name__, template_folder="templates")


@main_blueprint.route("/")
@main_blueprint.route("/main")
def main():
    """
    View method to render the home.html page - https://www.abhishekpednekar.com/

    Returns
    -------
    home.html: html / jinja2 template
    """
    return render_template("home.html")
