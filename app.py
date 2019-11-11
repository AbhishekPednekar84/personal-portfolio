from flask import Flask
from config import Config
from extensions import db


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    from views import blog
    from views import contact
    from views import main
    from views import portfolio

    app.register_blueprint(blog.blog_blueprint)
    app.register_blueprint(contact.contact_blueprint)
    app.register_blueprint(main.main_blueprint)
    app.register_blueprint(portfolio.portfolio_blueprint)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
