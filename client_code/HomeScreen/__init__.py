from ._anvil_designer import HomeScreenTemplate
from anvil import *


class HomeScreen(HomeScreenTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    # Any code you write here will run before the form opens.

  @handle("post_button", "click")
  def post_button_click(self, **event_args):
    Notification("Testing", title="message title", style="sucess", timeout=2).show()
    """This method is called when the button is clicked"""
