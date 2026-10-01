from ._anvil_designer import HomeScreenTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class HomeScreen(HomeScreenTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)

    # Load existing posts
    self.repeating_panel_1.items = app_tables.journal_post.search(
      tables.order_by("created", ascending=False)
    )

  @handle("timer_1", "tick")
  def timer_1_tick(self, **event_args):
    self.repeating_panel_1.items = app_tables.journal_post.search(
      tables.order_by("created", ascending=False)
    )

  @handle("post_button", "click")
  def post_button_click(self, **event_args):
    username = self.username_text.text
    post = self.post_text.text

    if username.strip() == "" or post.strip() == "":
      Notification(
        "Please enter username and a post",
        title="Alert!",
        timeout=2
      ).show()
      return

    # Add the new post FIRST
    anvil.server.call('journal_post', username, post)

    # THEN refresh the repeating panel
    self.repeating_panel_1.items = app_tables.journal_post.search(
      tables.order_by("created", ascending=False)
    )

    Notification(
      "Post successful",
      title="Notification",
      timeout=2
    ).show()

    self.clear_input()

  def clear_input(self):
    self.username_text.text = ""
    self.post_text.text = ""

  def reload_system(self):
    open_form('HomeScreen')

  @handle("headline_2", "click")
  def headline_2_click(self, **event_args):
    open_form('AboutScreen')