from ._anvil_designer import LineNoLabelTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class LineNoLabel(LineNoLabelTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.label_1.text = anvil.server.call('LineNo')

    # Any code you write here will run when the form opens.