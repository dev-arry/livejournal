from ._anvil_designer import HomeScreenTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class HomeScreen(HomeScreenTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    # Any code you write here will run before the form opens.

  @handle("post_button", "click")
  def post_button_click(self, **event_args):
    username = self.username_text.text
    post = self.post_text.text

    if username.strip() == "" or post.strip() == "":
      Notification("Please enter username and a post", title="Alert!", timeout=2).show()
      return
    
    anvil.server.call('journal_post', username, post)
    Notification("Post successful", title="Notification", timeout=2).show()
    self.clear_input()
    """This method is called when the button is clicked"""

  def clear_input(self):
    self.username_text.text = ""
    self.post_text.text = ""

    
