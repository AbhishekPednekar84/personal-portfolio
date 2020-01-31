from flask import Flask
from flask_migrate import Migrate
from config import Config
from extensions import db
from datetime import datetime


def create_app(config_class=Config):
    """
    Returns the flask application instance

    Parameters
    ----------
    config_class: class

    Returns
    -------
    app: object
    """
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate = Migrate(app, db)

    from views import blog
    from views import contact
    from views import main
    from views import portfolio
    from views import sitemap
    from api.search import search_blueprint

    app.register_blueprint(blog.blog_blueprint)
    app.register_blueprint(contact.contact_blueprint)
    app.register_blueprint(main.main_blueprint)
    app.register_blueprint(portfolio.portfolio_blueprint)
    app.register_blueprint(sitemap.sitemap_blueprint)
    app.register_blueprint(search_blueprint, url_prefix="/api")

    return app


def get_current_year():
    """
    Returns the current year that will be displayed on the website footer

    Returns
    -------
    current_year: int
    """
    current_year = datetime.now().year
    return current_year


if __name__ == "__main__":  # pragma: no cover
    app = create_app()
    app.run()
