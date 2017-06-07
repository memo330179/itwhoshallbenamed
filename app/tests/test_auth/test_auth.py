from app.tests.base import BaseTestCase
import json
from app.models import User
from app import db

class TestAuthCase(BaseTestCase):
  
  def test_register_user(self):
    register = self.client.post('/auth/users', 
                              data=json.dumps(dict(
                                username = "test_user",
                                email = "test@test.com",
                                password = "test"
                                )),
                                content_type='application/json',
                              follow_redirects = True)
    response = register.json
    assert response['username'] == 'test_user'
  
  def test_get_user(self):
    user = User(username="testy", email="testy@test.com")
    user.hash_password("password")
    db.session.add(user)
    db.session.commit()
    user = self.client.get('/auth/users/1',
                      follow_redirects = True)
    response = user.json
    assert response['username'] == 'testy' 
  