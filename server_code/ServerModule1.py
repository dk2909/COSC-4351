import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime
import random
import anvil.server

import anvil.server
import urllib.parse

#call for loading table BS
@anvil.server.callable
def get_item():
  return app_tables.inventory.search()

#call for loading checkout items BS
@anvil.server.callable
def get_checkout():
  return app_tables.order.search()

#search function BS
@anvil.server.callable
def search_store(query):
  result = app_tables.inventory.search()
  if query:
    result = [
      x for x in result
      if query in x['Item']
    ]
  return result

#add total for checkout BS
@anvil.server.callable
def TotalSum():
  total = 0.00
  for row in app_tables.order.search():
    price = round(float(row["Cost"]),2)
    total = price + total
  total = round(total,2)
  strtotal = str(total)
  return strtotal

#add user email to data table BS
@anvil.server.callable
def linkUser():
  user = anvil.users.get_user()
  useremail = user['email']
  for row in app_tables.order.search():
    order_row = app_tables.order.get(Item="Shirt")
    if order_row:
      order_row.update(UserEmail=useremail)
    order_row1 = app_tables.order.get(Item="Shorts")
    if order_row1:
      order_row1.update(UserEmail=useremail)
    order_row2 = app_tables.order.get(Item="Shoes")
    if order_row2:
      order_row2.update(UserEmail=useremail)
    order_row3 = app_tables.order.get(Item="Hat")
    if order_row3:
      order_row3.update(UserEmail=useremail)

#assign random order number to data table
@anvil.server.callable
def order_no():
  begin_no = random.randint(1,100)
  order_no = begin_no + 1000
  return order_no

#add shipping info to the data tables BS
@anvil.server.callable
def add_address(address_dict):
  user = anvil.users.get_user()
  useremail = user['email']
  app_tables.shipping_address.add_row(OrderNumber=order_no(), created=datetime.now(),UserEmail=useremail,**address_dict)

#refresh address
@anvil.server.callable
def get_address():
  return app_tables.shipping_address.search()
  
@anvil.server.callable
def address_api(encoded_str):
  #print(encoded_str)
  url = "{encu}".format(encu=encoded_str)
  response = anvil.http.request(url, json=True)
  return response

@anvil.server.callable
def urlencode(rawstr):
  return urllib.parse.quote_plus(rawstr,safe="/:=&?")



