from flask import Blueprint, render_template
from app import get_current_year

portfolio_blueprint = Blueprint(
    "portfolio", __name__, template_folder="templates"
)


@portfolio_blueprint.route("/portfolio")
def portfolio():
    return render_template("portfolio.html", title="Portfolio", year=get_current_year())
