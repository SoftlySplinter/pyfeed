class Feed:
  def init(self, title, link, description, optional**):
    self.attr = {title: title, link: link, description: description}
    self.attr += **optional
