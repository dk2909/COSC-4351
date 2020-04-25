from ._anvil_designer import LoginFormTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class LoginForm(LoginFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    #Shows login status of user (DK)
  def update_login_status(self):
    user = anvil.users.get_user()
    if user is None:
      self.login_status.text = "You are not logged in"
    else:
      self.login_status.text = "You are logged in as %s" % user ['email']
  
  #calls login and sign up form (DK)
  def login_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    try:
      anvil.users.login_with_form()
      #open store form BS
      open_form('Store')
      return 'login_btn_clicked'
    except Exception as e:
      return e


    #continue as guest (DK)
  def guest_login_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    try:
      open_form('Store')
      return 'guest_login_clicked'
    except Exception as e:
      return e
    





