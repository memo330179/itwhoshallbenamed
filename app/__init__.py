from flask import Flask

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    
    from app.auth.models import db
    db.init_app(app)
    
    # Blueprints
    
    from app.auth.auth import mod_auth
    app.register_blueprint(mod_auth, url_prefix='/api')
    
    return app