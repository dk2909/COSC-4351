from ._anvil_designer import CheckoutTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..ShippingScreen.Form1 import Form1

class Checkout(CheckoutTemplate):
  def __init__(self, **properties):

    self.init_components(**properties)
    #Calls to get checkout items BS
    self.repeating_panel_2.items = anvil.server.call('get_checkout')
    self.repeating_panel_1.items = anvil.server.call('get_checkout')
    #call to add sum
    self.label_7.text = anvil.server.call('TotalSum')
    anvil.server.call('linkUser')

#go to store/homepage BS
  def home_click(self, **event_args):
    """This method is called when the button is clicked"""
    try:
        open_form('Store')
        return 'store_home_clicked'
    except Exception as e:
        return e
    #pass

#go to account BS
  def account_click(self, **event_args):
    """This method is called when the button is clicked"""
    try:
        open_form('Account')
        return 'account_clicked'
    except Exception as e:
        return e
    #pass

#go to shipping screen BS
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    #add user to data table when click next
    try:
        new_address = {}
        saved_click = alert(content = Form1(item = new_address), title= "Enter Shipping Information", large= True, buttons=[("Save", True), ("Cancel", False)])
        if saved_click:
          anvil.server.call('add_address',new_address)
        open_form('ShippingScreen')
        return 'next_clicked'
    except Exception as e:
        return e