from pyfeed.rss import RSSv2
from unittest import TestCase

class RSSv2TestCase(TestCase):
  def setUp(self):
    self.feed = RSSv2()
    self.validFeed = {
      'title': 'Liftoff News', 
      'link': 'http://liftoff.msfc.nasa.gov/',
      'description': 'Liftoff to Space Exploration.',
      'language': 'en-us'
    }

  def testValidator(self):
    assert self.feed.valid(self.validFeed)
