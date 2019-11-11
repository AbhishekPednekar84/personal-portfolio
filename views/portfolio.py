from flask import Blueprint, render_template

portfolio_blueprint = Blueprint(
    "portfolio", __name__, template_folder="templates")


@portfolio_blueprint.route("/portfolio")
def portfolio():
    return render_template("portfolio.html", title='Portfolio')
