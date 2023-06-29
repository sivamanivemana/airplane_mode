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
  
  tickets = frappe.db.get_all("Airplane Ticket", fields=['name', 'total_amount'])
  records = []
  revenue_by_airline = { }
  data=[]
  
  for ticket in tickets:
      records.append(frappe._dict({"name":ticket['name'][:-33], "total_amount":ticket['total_amount']}))
      
  for record in records:
      if (record.name) in revenue_by_airline:
           revenue_by_airline[record.name] = revenue_by_airline[record.name] + record.total_amount
          
      else:
           revenue_by_airline[record.name] = record.total_amount
           
  airlines = frappe.db.get_all("Airline", fields=['name'])
  
  for airline in airlines:
      if not airline["name"] in revenue_by_airline:
          revenue_by_airline[airline["name"]] = 0
          
  revenues=[]
  for airline, revenue in revenue_by_airline.items():
      data.append(frappe._dict({"airline":airline, "revenue":revenue}))
      revenues.append(revenue)
  total_revenue = sum(revenues)
  print(total_revenue)
  
  
     
                
 def before_submit(self):
    if self.status != 'Boarded':
        frappe.throw("Please change ticket status to 'Boarded' for ticket submission")
    
    # self.seat = str(''.join(random.choices(string.digits, k=2)) + ''.join(random.choices(string.ascii_uppercase, k=1)))
    
        
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
        
        
@frappe.whitelist()
def ticket_validations(flight):
    
    get_capacity = frappe.db.get_value("Airplane", filters={"name": flight[:-14]}, fieldname="capacity")
    
    get_ticket_list_count = len(frappe.db.get_list("Airplane Ticket", filters={"flight":flight}))
    
    return [get_capacity, get_ticket_list_count]
        
