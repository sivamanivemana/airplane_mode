# Copyright (c) 2023, Rohit and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class AirplaneFlight(Document):
    
 def before_submit(self):
     self.status = 'Completed'
