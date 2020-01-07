from flask import Blueprint, render_template
from app import get_current_year

portfolio_blueprint = Blueprint(
    "portfolio", __name__, template_folder="templates"
)


@portfolio_blueprint.route("/portfolio")
def portfolio():
    """
    View method to render the portfolio.html page - https://www.abhishekpednekar.com/portfolio

    Returns
    -------
    portfolio.html: html / jinja2 template
    """
    return render_template(
        "portfolio.html", title="Portfolio", year=get_current_year()
    )
