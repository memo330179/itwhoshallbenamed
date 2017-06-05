from app.tests.base import BaseTestCase
import json

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
  