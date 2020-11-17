from flask import Flask
from sushy.blueprints.page import page


def create_app():
    """
        Create a Flask application using the app factory pattern.

        :return: Flask app
    """

    # Enable instance's flag to using the config files in instance directory
    app = Flask(__name__, instance_relative_config=True)

    # Get config value from sushy/config/settings file
    app.config.from_object('config.settings')

    # Override config value from sushy/instance/settings.py
    app.config.from_pyfile('settings.py', silent=True)

    # Register blueprints
    app.register_blueprint(page)

    return app
