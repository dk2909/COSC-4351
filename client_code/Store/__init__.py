from ._anvil_designer import StoreTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Store(StoreTemplate):
    def __init__(self, **properties):

        self.init_components(**properties)
        # server call to get item function
        self.repeating_panel_1.items = anvil.server.call('get_item')
        self.data = []
        self.data2 = []
        # self.i = 0

    # search terms after hitting enter
    def text_box_1_pressed_enter(self, **event_args):
        """This method is called when the user presses Enter in this text box"""
        try:
            self.repeating_panel_1.items = anvil.server.call('search_store', self.search_box_1.text)
            return 'text_1_pressed'
        except Exception as e:
            return e

    # search for term after clicking search button
    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        try:
            self.repeating_panel_1.items = anvil.server.call('search_store', self.search_box_1.text)
            return 'btn_1_clicked'
        except Exception as e:
            return e

    # go to checkout/ also check if logged in
    def button_3_click(self, **event_args):
        """This method is called when the button is clicked"""
        try:
            user = anvil.users.get_user()
            if user is None:
                anvil.users.login_with_form()
                open_form('Checkout')
            else:
                open_form('Checkout')
            return 'btn_3_clicked'
        except Exception as e:
            return e
        # pass

    # go to store
    def store_button_click(self, **event_args):
        """This method is called when the button is clicked"""
        try:
            open_form('Store')
            return 'store_button_clicked'
        except Exception as e:
            return e

    # open log in prompt
    def sign_in_btn_click(self, **event_args):
        """This method is called when the button is clicked"""
        try:
            anvil.users.login_with_form()
            return 'sign_in_button_clicked'
        except Exception as e:
            return e

