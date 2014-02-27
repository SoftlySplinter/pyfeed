class RSSv2:
  """Generates RSS feeds from data."""

  FEED_REQUIRED = ['title', 'link', 'description']
  FEED_OPTIONAL = ['language', 'copyright', 'managingEditor', 'webMaster',
                   'pubDate', 'category', 'docs', 'cloud', 'ttl', 'image',
                   'rating', 'textInput', 'skipHours', 'skipDays', 'posts']
  POST_REQUIRED = ['title', 'link', 'description']

  def generate(self, data):
    assert self.valid(data)

  def valid(self, data):
    if 'posts' not in data:
      data['posts'] = []
    return all(map(lambda req: req in data, self.FEED_REQUIRED)) and all(map(lambda elem: elem in self.FEED_OPTIONAL or elem in self.FEED_REQUIRED, data)) and self.postsValid(data['posts'])

  def postsValid(self, posts):
    return all(map(self.postValid, posts))

  def postValid(self, post):
    return all(map(lambda req: req in post, self.POST_REQUIRED))
           
