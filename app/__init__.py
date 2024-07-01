from flask import Flask
from config import Config
from .routes.green_areas import green_areas

def init_app():
    app = Flask(__name__, static_folder=Config.STATIC_FOLDER, template_folder= Config.TEMPLATE_FOLDER)
    app.config.from_object(Config)

    #BLUEPRINT
    app.register_blueprint(green_areas, url_prefix="/green_areas")

    return app
