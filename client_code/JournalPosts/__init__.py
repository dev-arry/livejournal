from ._anvil_designer import JournalPostsTemplate
from anvil import *


class JournalPosts(JournalPostsTemplate):

  def __init__(self, **properties):
    super().__init__(**properties)

    print("JOURNAL ITEM:", self.item)

    self.dom_nodes["username"].textContent = str(self.item["username"])
    self.dom_nodes["post"].textContent = str(self.item["post"])

    created = self.item["created"]

    if created:
      self.dom_nodes["created"].textContent = created.strftime("%d %B %Y, %H:%M")
    else:
      self.dom_nodes["created"].textContent = ""