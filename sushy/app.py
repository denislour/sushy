from flask import Flask
from sushy.blueprints.page import page
from sushy.extensions import debug_toolbar


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
    app.register_blueprint(page)

    # Register extentions
    extensions(app)

    return app


def extensions(app):
    """
        Register the extentions for Flask application
    """

    debug_toolbar.init_app(app)
