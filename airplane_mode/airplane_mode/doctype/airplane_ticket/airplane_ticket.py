# Copyright (c) 2023, Rohit and contributors
# For license information, please see license.txt

from frappe.model import delete_doc
import frappe
from frappe.model.document import Document
import string
import random

class AirplaneTicket(Document):
    
 def before_save(self):
    add_ons = self.add_ons
    
    
    total_add_ons = 0
    for add_on in add_ons:
        total_add_ons += add_on.amount 
        
        
    self.total_amount = int(self.ticket_price) + total_add_ons
            
    
 def before_submit(self):
    if self.status != 'Boarded':
        frappe.throw("Please change ticket status to 'Boarded' for ticket submission")
    
    self.seat = str(''.join(random.choices(string.digits, k=2)) + ''.join(random.choices(string.ascii_uppercase, k=1)))
    
        
 def validate(self):
     self.remove_duplicates()

 def remove_duplicates(self):
     table_field = self.add_ons
     rows_to_delete = []
     existing_rows = set()
     
     for i, row in enumerate(table_field):
         row_key = (row.item) # Use fields that make a row unique
         if row_key in existing_rows:
             rows_to_delete.append(i)
         else:
             existing_rows.add(row_key)
             
     
     # Delete rows_duplicate
     for i in reversed(rows_to_delete):
        table_field.pop(i)
        
