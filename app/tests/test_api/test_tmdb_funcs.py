import unittest
from app.api import tmdb_funcs

class TestTMDbFuncs(unittest.TestCase):
  
  def test_guessit(self):
    
    self.assertDictContainsSubset(
      { "title": "futurama",
        "season" : 1,
        "episode" : 2 }, 
        tmdb_funcs.guess_name('futurama_s1e2'))