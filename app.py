from flask import Flask
from flask_migrate import Migrate
from config import Config
from extensions import db
from api import api


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    api.init_app(app)
    migrate = Migrate(app, db)

    from views import blog
    from views import contact
    from views import main
    from views import portfolio
    from views import search

    # from api import search as search_api

    app.register_blueprint(blog.blog_blueprint)
    app.register_blueprint(contact.contact_blueprint)
    app.register_blueprint(main.main_blueprint)
    app.register_blueprint(portfolio.portfolio_blueprint)
    app.register_blueprint(search.search_blueprint)
    # app.register_blueprint(search_api.search_blueprint)

    return app


if __name__ == "__main__":  # pragma: no cover
    app = create_app()
    app.run(debug=True)
