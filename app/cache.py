from flask_caching import Cache

cache = Cache()

def init_cache(app):
    app.config.from_object('app.config.Config')
    cache.init_app(app)
