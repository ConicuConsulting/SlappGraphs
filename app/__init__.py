from flask import Flask
from app.routes.base import base_bp
from app.routes.agn import agn_bp
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register Blueprints
    app.register_blueprint(base_bp)
    app.register_blueprint(agn_bp)

    return app
