from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields
from slugify import slugify

db = SQLAlchemy()

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
  id = fields.int(dump_only=True)
  title = fields.Str()
  overview = fields.Str()
  slug = fields.Str()
  series_art = fields.Str()
