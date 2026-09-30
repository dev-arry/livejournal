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
    self.dom_nodes["username"].textContent = str(self.item["username"])
    self.dom_nodes["post"].textContent = str(self.item["post"])
    self.dom_nodes["created"].textContent = self.item["created"].strftime("%d %B %Y, %H:%M")