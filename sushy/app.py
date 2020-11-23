from celery import Celery
from flask import Flask

from sushy.blueprints.page import page
from sushy.blueprints.contact import contact
from sushy.extensions import debug_toolbar, mail, csrf


CELERY_TASK_LIST = [
    'sushy.blueprints.contact.tasks',
]


def create_celery_app(app=None):
    """
        Create a new Celery object and tie together
        The Celery config to the app's
        config. Wrap all tasks in the context of the application.
    """

    app = app or create_app()

    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'],
                    include=CELERY_TASK_LIST)
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery


def create_app(settings_override=None):
    """
        Create a Flask application using the app factory pattern.
    """

    # Enable instance's flag to using the config files in instance directory
    app = Flask(__name__, instance_relative_config=True)

    # Get config value from sushy/config/settings file
    app.config.from_object('config.settings')

    # Override config value from sushy/instance/settings.py
    app.config.from_pyfile('settings.py', silent=True)

    if settings_override:
        app.config.update(settings_override)

    # Register blueprints
    app.register_blueprint(contact)
    app.register_blueprint(page)

    # Register extentions
    extensions(app)

    return app


def extensions(app):
    """
        Register the extentions for Flask application
    """

    debug_toolbar.init_app(app)
    mail.init_app(app)
    csrf.init_app(app)

    return None
