from ._anvil_designer import ItemWindowTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ItemWindow(ItemWindowTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings
    self.init_components(**properties)

    #create new list for items in cart as you click them BS
  def button_1_click(self , **event_args):
    #app_tables.order.add_row(Column8=anvil.users.get_user())
    try:
      ProductExist = False
      
      self.new_item = {"CartProduct": self.item['Item']}
      self.new_item2 = {"ProductCost": self.item['Cost']}
          
      main_form = get_open_form()
    
      ProductExist = False
      for key in main_form.data:
        if key['CartProduct'] == self.item['Item']:        
          ProductExist = True
          pass
      for key in main_form.data2:
        if key['ProductCost'] == self.item['Cost']:
          pass
      
      if ProductExist:
        ProductExist = False
        pass
        
      else:
        main_form.data.append(self.new_item)
        main_form.data2.append(self.new_item2)
        #add items to order data table
        #self.i += 1
        row = app_tables.order.add_row(Item=str(self.item['Item']),Cost=self.item['Cost'])
    
      main_form.repeating_panel_2.items = main_form.data
      main_form.repeating_panel_3.items = main_form.data2
      
      return 'add_item_clicked'
    
    except Exception as e:
      return e
    


   
