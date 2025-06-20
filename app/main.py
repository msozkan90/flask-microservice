from flask import Flask
from app.config import Config
from app.extensions import db
from flask_cors import CORS
from app.routes.auth import auth_bp
from app.routes.album import album_bp
from app.utils.error_handlers import error_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    CORS(app)
    
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(album_bp, url_prefix="/api")
    app.register_blueprint(error_bp)

    with app.app_context():
        db.create_all()

    return app
