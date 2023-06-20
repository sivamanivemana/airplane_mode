# Copyright (c) 2023, Rohit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import string
import random
from collections import Counter
 


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
    
        
    
    
        
