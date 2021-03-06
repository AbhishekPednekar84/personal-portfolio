import config
from celery import Celery

# from app import create_app


def make_celery(app):
    """
    Returns a celery instance

    Returns
    -------
    celery: object
    """
    # app = app or create_app()
    celery = Celery(app.import_name, broker=config.Config.CELERY_BROKER_URL)
    celery.conf.update(app.config)

    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery
