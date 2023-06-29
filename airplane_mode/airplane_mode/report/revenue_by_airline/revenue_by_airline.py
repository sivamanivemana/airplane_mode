# Copyright (c) 2023, Rohit and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
  columns, data = [
   {
  	   "label": "Airline",
       "fieldname": "airline",
       "fieldtype": "link",
       "width": 230,
   },
   {
       "label": "Revenue",
       "fieldname": "revenue",
       "fieldtype": "Currency",
       "width": 230,
   },  
   ], []
  
  tickets = frappe.db.get_all("Airplane Ticket", fields=['name', 'total_amount'])
  records = []
  revenue_by_airline = { }
  
  for ticket in tickets:
      records.append(frappe._dict({"name":ticket['name'][:-33], "total_amount":ticket['total_amount']}))
      
  for record in records:
      if (record.name) in revenue_by_airline:
           revenue_by_airline[record.name] = revenue_by_airline[record.name] + record.total_amount
          
      else:
           revenue_by_airline[record.name] = record.total_amount
           
  for airline in frappe.db.get_all("Airline", fields=['name']):
      if not airline["name"] in revenue_by_airline:
          revenue_by_airline[airline["name"]] = 0
    
  revenues=[]
  for airline, revenue in revenue_by_airline.items():
      data.append(frappe._dict({"airline":airline, "revenue":revenue}))
      revenues.append(revenue)
  total_revenue = sum(revenues)
      
  chart = {
  	"data": {
  		"labels": [d.airline for d in data],
  		"datasets" : [{
  			"name": "Revenue by Month",
  			"values": [d.revenue for d in data],
  			}]
  		},
  	"type":"donut",
  }
  
  report_summary = {
			"value": total_revenue,
			"label": _("Total Revenue"),
			"datatype": "Currency",
			"indicator": "Green" if total_revenue > 0 else "Red",
			"currency": "INR",
		},
  
 
 
  return columns, data, None, chart, report_summary
