import os
from flask import Flask
from flask_cors import CORS


def create_app():
    # Config of Flask App
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(os.environ.get('APP_SETTINGS', default='config.ProductionConfig'))
    
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # register blueprints
    from api.api import api
    app.register_blueprint(api, url_prefix='/api')

    return app