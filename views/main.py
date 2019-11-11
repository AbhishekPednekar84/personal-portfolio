from flask import Blueprint, render_template

main_blueprint = Blueprint("main", __name__, template_folder="templates")


@main_blueprint.route("/")
@main_blueprint.route("/main")
def main():
    return render_template("home.html")
