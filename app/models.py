from flask import current_app
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer as
                            Serializer, BadSignature, SignatureExpired)
from marshmallow import Schema, fields, ValidationError, pre_load
from slugify import slugify
from app import db




class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True)
    email = db.Column(db.String(), index=True)
    password_hash = db.Column(db.String(64))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_auth_token(self, expiration=600):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None    # valid token, but expired
        except BadSignature:
            return None    # invalid token
        user = User.query.get(data['id'])
        return user
        
class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str()
    email = fields.Str()
    
    
# API Models

class Series(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  tmdb_id = db.Column(db.Integer)
  title = db.Column(db.String(250), nullable=True)
  overview = db.Column(db.String(), nullable=True)
  slug = db.Column(db.String(250))
  
  def __init__(self, tmdb_id, title, overview, series_art):
    self.tmdb_id = tmdb_id
    self.title = title
    self.overview = overview
    self.series_art = series_art
    self.slug = self.create_slug(self.title)
    
  def create_slug(self, title):
    return slugify(title)
    
class SeriesSchema(Schema):
  id = fields.Int(dump_only=True)
  title = fields.Str()
  overview = fields.Str()
  slug = fields.Str()
  series_art = fields.Str()
  