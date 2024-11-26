from flask import Flask
from app.cache import init_cache

def create_app():
    app = Flask(__name__)

    init_cache(app)

    from app.routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app
