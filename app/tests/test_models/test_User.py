from app.tests.base import BaseTestCase
from app.models import User
from app import db
class UserTestCase(BaseTestCase):
  
  def setUp(self):
    super().setUp()
    user = User(username="testy", email="testy@test.com")
    user.hash_password("password")
    db.session.add(user)
    db.session.commit()
    
  def test_lookup(self):
    user_exists = db.session.query(User).filter_by(username="testy").count()
    assert(user_exists==1)
    
  
    
    