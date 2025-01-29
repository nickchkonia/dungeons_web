from flask import Flask
# TODO: import dungeons_logic
# from models import db  # From your external submodule
from config.config import ConfigClass


def create_app():
    app = Flask(__name__)
    app.config.from_object(ConfigClass)  # Load selected config
    # TODO: add loggin
    print(f'[DEBUG] app.config:\n{app.config}')
    app.config['DEBUG'] = ConfigClass.DEBUG
    # Initialize extensions
    # db.init_app(app)

    return app
