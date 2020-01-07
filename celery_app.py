from flask import Flask
from utilities.factory import make_celery


def create_celery_app():
    """
    Returns a celery instance

    Returns
    -------
    celery: object
    """
    app = Flask(__name__)
    celery = make_celery(app)

    return celery
