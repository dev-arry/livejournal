from ._anvil_designer import JournalPostsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class JournalPosts(JournalPostsTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)

  def form_show(self, **event_args):
    print(self.item)

    self.username.text = str(self.item['username'])
    self.post.text = str(self.item['post'])
    self.created.text = str(self.item['created'])