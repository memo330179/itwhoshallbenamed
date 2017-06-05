from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_filename):
  app = Flask(__name__)
  app.config.from_object(config_filename)
  
  from app.models import db
  db.init_app(app)
  
  # Blueprints
  from app.auth.auth import mod_auth
  app.register_blueprint(mod_auth, url_prefix='/auth')
  from app.index.index import main
  app.register_blueprint(main)
  return app