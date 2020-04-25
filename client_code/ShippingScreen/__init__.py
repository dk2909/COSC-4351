from ._anvil_designer import ShippingScreenTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
#BS
from ..ShippingScreen.Form1 import Form1
from anvil.tables import app_tables


class ShippingScreen(ShippingScreenTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run when the form opens.

        # assign address name to label on shipping screen form BS
        count = 0
        for r in app_tables.shipping_address.search():
            count = count + 1

        street_address = [r['Street Address'] for r in app_tables.shipping_address.search()]
        city = [r['City'] for r in app_tables.shipping_address.search()]
        state = [r['State'] for r in app_tables.shipping_address.search()]
        zip_code = [r['Zip'] for r in app_tables.shipping_address.search()]
        self.label_6.text = street_address[count - 1]
        self.label_7.text = city[count - 1]
        self.label_8.text = state[count - 1]
        self.label_9.text = zip_code[count - 1]
        
        rawstring = "https://us-street.api.smartystreets.com/street-address?auth-id=8dfbd3dc-56db-e870-1471-38d8bf8d798e&auth-token=kx3hjvxp9MdOgGi3W3n3&street={self.label_6.text}&city={self.label_7.text}&state={self.label_8.text}&zipcode={self.label_9.text}"

    # clear table and vaildate address and place order
    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        try:
            
            count = 0
            for r in app_tables.shipping_address.search():
                count = count + 1
    
            street_address = [r['Street Address'] for r in app_tables.shipping_address.search()]
            city = [r['City'] for r in app_tables.shipping_address.search()]
            state = [r['State'] for r in app_tables.shipping_address.search()]
            zip_code = [r['Zip'] for r in app_tables.shipping_address.search()]
            self.label_6.text = street_address[count - 1]
            self.label_7.text = city[count - 1]
            self.label_8.text = state[count - 1]
            self.label_9.text = zip_code[count - 1]

            rawstring = "https://us-street.api.smartystreets.com/street-address?auth-id=8dfbd3dc-56db-e870-1471-38d8bf8d798e&auth-token=kx3hjvxp9MdOgGi3W3n3&street={label6}&city={label7}&state={label8}&candidates=2".format(label6=self.label_6.text,label7=self.label_7.text,label8=self.label_8.text,label9=self.label_9.text)
     
            #url encoding
            encoded_str = anvil.server.call('urlencode', rawstring)
            
            return_value = anvil.server.call('address_api', encoded_str)
            print(return_value)
            return_value = str(return_value)
            if (return_value != '[]'):
              alert("Order was placed Successfully!")
              # clear order data table when button is click BS
              app_tables.order.delete_all_rows()
            else:
              alert("Order unsuccessful, wrong address")
              app_tables.shipping_address.delete_all_rows()
              open_form('Checkout')
            return 'place_order_clicked'
        except Exception as e:
            return e
 












