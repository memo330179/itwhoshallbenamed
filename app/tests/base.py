import os
from flask_testing import TestCase

from app import create_app
from app import db

class BaseTestCase(TestCase):
  
  def create_app(self):
    """creates the application for tests"""
    return create_app('test_config')
    
  def setUp(self):
    db.create_all()
    
  def tearDown(self):
    db.session.remove()
    db.drop_all()